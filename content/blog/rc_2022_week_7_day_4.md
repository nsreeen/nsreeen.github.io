+++
title = "RC 2022 week 7 day 4 - clojure loop and recur"
date = 2022-09-29
+++

Today I pair programmed with Anthony.  We wrote a few small functions in both Clojure (new to me) and Haskell (new to Anthony).  Anthony showed me `loop` and `recur` as a way to avoid passing an accumulator when calling a function, and still making tail optimised recursive calls.

Here's an example in a function that sums a list of numbers:
```clojure
(defn sumList [list]
    (loop [list list acc 0]
        (if (empty? list)
            acc
            (recur (rest list) (+ acc (first list))))))
```

The function (`sumList`) gets called with one argument: `list`.  The `loop` makes two variables available: `list` gets mapped to itself, and the accumulator `acc` gets mapped (initially) to 0.  

These variables are mutable and will hold their state in subsequent tail optimised recursive calls - so `acc` will act as an accumulator here.  Tail optimised recursive calls in Clojure have to be made with the `recur` keyword.  

I found the idea of `loop` and `recur` a bit confusing initially, but then I realised that they exist because Clojure runs on the JVM: the JVM doesn't have tail call optimisation, so this code is actually implemented as a Java loop!  I think this is a pretty neat!

Also, `recur`'s syntax rules mean it must be called in a valid position to allow tail optimisation (it must be the last expression).  I quite like how explicit this makes things.
