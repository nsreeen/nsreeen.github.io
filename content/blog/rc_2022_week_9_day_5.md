+++
title = "RC 2022 week 9 day 5 - foldl vs foldr vs foldl'"
date = 2022-10-07
+++

I wanted to understand the difference between Haskell's foldr and foldl a bit better, so I wrote some code to try to understand what each was doing.  Note: my rationale below is based on my current understanding, please let me know if there are any errors!

This is the code:
```Haskell
import Debug.Trace
fr f acc xs = foldr (\x y -> trace ((show x) ++ " " ++ (show y)) (f x y)) acc xs
fl f acc xs = foldl (\x y -> trace ((show x) ++ " " ++ (show y)) (f x y)) acc xs
```
`fr` and `fl` are basically wrappers around foldr and foldl, using `trace` to print the arguments passed to the function when it is evaluated.


## foldl
I called my wrapper in ghci like this: `fl (-) 0 [1..5]`, and the following printed to the terminal:
```
0 1
-1 2
-3 3
-6 4
-10 5
-15
```
So the output is -15, and (-) is applied to each item in the list starting with the accumulator (`acc`) and the first item in the list.  

The evaluation happens something like this:

(((((0 - 1) - 2) - 3) - 4) - 5)

Because Haskell is lazy, the first expression ('(0-1)') will not be evaluated until the whole thing is ready to be evaluated.  First, a thunk will be built up on the heap.  Then when the whole expression is ready to be evaluated, it will be evluated starting with the first sub expression ('(0-1)').

## foldr
I called my wrapper in ghci like this: `fr (-) 0 [1..5]`, and the following printed to the terminal:
```
5 0
4 5
3 -1
2 4
1 -2
3
```
The first expression to be evaluated here is the accumulator and the last element in the list, but we know that folds start with the first element in a list.  This is because the evaluation happens like this:

(1 - (2 - (3 - (4 - (5 - 0)))))

The first item is still the first to be processed by foldr, but to know what the second argument to (-) is the following subexpressions must be evaluated first.  So the thunk is built up, and then evaluated starting with the innermost expression ('5-0').

A way of thinking about foldr that I like, is that it just returns the list with the accumulator as the base case and the function passed replacing cons (`:`) (I can't find the  page I read this on - I'll update if I do).

## foldl'

If I pass a very long list to either `fl` or `fr` (eg. `[1..500000]`), there's a few seconds delay before the trace debug output is printed to the terminal.  This is because the whole thunk is built up before it is evaluated, which takes time if the list is very long.  

For even longer lists, there's a stack overflow and the expression cannot be calculated.  This is because once evaluation of the expression begins, the subexpressions are evaluated starting with the outermost.  The half of each subexpression that's known gets pushed to the stack.   

In the case of foldr, this build up is necessary - as we need to know the base case before we can evaluate the rest of the expression.  In the case of foldl, the build up is not necessary.  We could evaluate the subexpressions immediately, as we first process them, instead of building up the thunk on the heap and then building up the subexpression results on the stack.  

foldl' is a version of foldl that evaluates subexpressions immediately.  It does this by evaluating the left argument strictly.  In most cases, foldl' is a better choice than foldl.


-----
I found [this wiki page](https://wiki.haskell.org/Foldr_Foldl_Foldl') very helpful in understanding this.  
