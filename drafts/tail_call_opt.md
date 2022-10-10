+++
title = "RC 2022: week 9 day 3 - everything is a thunk or why tail call optimisation isn't a thing in Haskell"
date = 2022-10-07
+++

In most functional languages, [tail call](https://en.wikipedia.org/wiki/Tail_call) optimisation  (TCO) is an important feature.  TCO allows functions to be written recursively, without building up too many frames on the call stack.  

TCO doesn't really make sense in Haskell, as it's a lazily evaluated language.  

https://stackoverflow.com/questions/13042353/does-haskell-have-tail-recursive-optimization

https://wiki.haskell.org/Tail_recursion

https://mail.haskell.org/pipermail/haskell-cafe/2009-March/058607.html

https://stackoverflow.com/questions/3429634/foldl-is-tail-recursive-so-how-come-foldr-runs-faster-than-foldl
