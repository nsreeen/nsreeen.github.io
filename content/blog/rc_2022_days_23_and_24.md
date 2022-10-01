+++
title = "RC 2022 Days 23 and 24 - Functors and Monads"
date = 2022-09-09
+++

I spent today and yesterday mostly thinking about Functors and Monads - I did some of the [Monad challenges](https://mightybyte.github.io/monad-challenges/), did some reading, and wrote some code.  I think I understand a bit more than I did, and I'm going to try and summarise what I learnt - with the disclaimer that I'm still trying to understand these concepts, so there could be mistakes (please let me know if you spot any!).

My biggest take away is that Functors and Monads are actually *not* special functional programming tricks - they are patterns that we can use in any language.  I think we do use them in non functional programming languages quite often, though perhaps less precisely sometimes.  

More specifically, they are ways of wrapping values, or putting them in context, in a way that makes doing operations on them more convenient.  

In Haskell, both are typeclasses (ie. interfaces, or behaviour that types can implement).  I'll give an example of each.

## Maybe is an example of a monad

A monad allows us to chain operations on values in a context.  

Maybe is an example of a monad (and Maybe in Haskell implements the Monad interface).  Maybe in Haskell is equivalent to Optional in some other languages like Kotlin.  It allows us to pass around either a value or no value, and it's very useful when we don't know what the outcome of a step will be.  We also have this concept in languages which require null checks, though we have to handle it differently.

This is the definition of Maybe:
```haskell
data Maybe a = Just a | Nothing
```  

Monad is a typeclass (ie. interface) in Haskell.  This is it's definition, with the function declarations that members (including Maybe) must implement:
```haskell
class Monad m where
  (>>=)  :: m a -> (  a -> m b) -> m b
  (>>)   :: m a ->  m b         -> m b
  return ::   a                 -> m a
```

The most important part of that for us is: `(>>=)  :: m a -> (  a -> m b) -> m b`.  This means that Monads must implement the `>>=` function, which takes:

1. a monad with value type a (eg. `Just 1` - a Maybe Integer)

2. a function that takes type a and returns a monad of value type b (eg. `\x -> Just (show x)`, which takes an Integer and returns a Maybe String)

And then it returns:

1. a monad of value type b (eg. `Just "1"` - a maybe String)

This is really cool because it means we can chain together a bunch of operations that may return Nothing, for example:

```haskell
Just 1 >>= functionThatMightFail >>= anotherFunctionThatMightFail
```


## List is an example of a functor

A functor allows us to transform a value that's wrapped in a context.  

This is the definition of Haskell's Functor:
```haskell
class Functor f where
    fmap :: (a -> b) -> f a -> f b
```

 An instance of Functor must implement fmap, which takes:

1. a function that transforms an a to a b

2.  a value of type a, wrapped in the context of the functor

 And it returns:

1. a value of type b, wrapped in the functors context.

 A list is an example of a functor - its fmap implementation is called map.  
```haskell
map show [1,2,3]
```
outputs:
```haskell
["1","2","3"]
```
Each value is mapped using the function `show`, and the values are within the context of the list.
