+++
title = "RC 2022: week 9 days 1 and 2 - Monad transformers"
date = 2022-10-04
+++

I've been learning about monad transformers in Haskell.  Monad transformers are a way of combining monads.  This is useful because you might need to use more than one monad at a time - say if you were using a monad to log stuff, and you were also using the Maybe monad to deal with values that may or may not be present.  Using transformers allows us to compose monadic behaviour out of the steps we are interesting in, and keep the behaviour organised in separate monads.  
