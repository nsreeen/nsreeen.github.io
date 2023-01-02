+++
title = "RC 2022 - understanding the State monad"
date = 2022-10-27
+++

The State monad is a bit different than more concrete monads like Maybe and Either, and I found it harder to get my head around.  Now I understand it better, I think it's really cool - it allows us to get the benefits of mutation, while maintaining the benefits of a pure function.

I'm going to try to explain it in a way that would have helped me understand it more easily.  

## The State monad encapsulates a computation
Unlike monads like Maybe and Either, the State monad encapsulates both data and the computations that act on it.  

The State monad provides a context with a state and some code to run: the code can access and update the state.

The State monad is initialised with the function to run and the initial state.  The State monad will call the function with the initial state, and keep track of the state.  Once the function has returned, the State monad will return the function's return value and the final state.


## A trivial example
In this example a starting value of 0 is incremented until it is 5, and then the string "computation finished" is returned.  
The full file, with imports, is available [here](https://gist.github.com/nsreeen/6278ad66deaee034b82d148ec7133423)).

```haskell
main :: IO ()
main = do
    let initialState = 1
    let (result, finalState) = runState myComputation initialState
    putStrLn "result: " + result
    putStrLn "finalState: " + finalState

myComputation :: State Int String
myComputation = do
    state <- get
    if state == 5
    then return "computation finished"
    else do
      modify (+1)
      myComputation
```
Running this code prints the following:
```
result: computation finished
finalState: 5
```


### What is the State monad doing in this example?
1. The State monad is initialised with `myComputation` and an initial state value (0).
2. The State monad calls `myComputation` with the initial value.
3. The State monad keeps track of the value of the state, which can be accessed or updated inside `myComputation` (eg. using `get` and `modify`).
4. `myComputation` returns the string "computation finished" - this is the result of the computation.
5. The State monad now returns the result of the computation ("computation finished") and the final value of the state (5).
