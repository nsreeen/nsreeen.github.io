+++
title = "RC 2022 Days 14 & 15 - Monoids"
date = 2022-08-29
+++

## Reflections on the last couple of days

On Thursday and Friday I pair programmed with Isaac on his Rust project and studied some category theory.  Pair programming was really fun!  Rust seems like a really cool language and set up was surprisingly easy.  It's also just really fun to program in a new language with someone who already knows it.  

Also, I decided to drop my one post a day commitment - from now on I'll combine posts when I'm working on the same things or I don't feel like writing.


## Monoids

One of the things I learnt about category theory is monoids.  Monoids are a special kind of category.  A category is a set of objects and transformations (called morphisms) that map between members of the set.  

So, for example, natural numbers (1,2,3,...) with the morphism `+` is a category.  


A monoid is a category that meets special conditions:

- there has to be a binary operation transformation (ie. it takes two operands/ arguments) eg. `+`

- there has to be an 'identity' transformation.  This means there has to be a value that can be combined with the binary operation and applied to every member of the set without changing it.  So in our example that would be `+ 0` eg. if we apply `+ 0` to 1, the result is 1 (1 is unchanged).


This pattern comes up a lot in programming.  Some examples:

- the set of `{True,False}`, the morphism `all`, and the identity value `True`

- `{True,False}`,  `any`, `False`

- any set of strings,  `concat`, and `""`

- any set of integers,  `MIN`, and `INFINITY`

- reduce
