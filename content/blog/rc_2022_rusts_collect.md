+++
title = "RC 2022 - rust's collect"
date = 2022-10-19
+++

I learnt about Rust's `collect` method, and think it's pretty cool.  It transforms an interator into a collection, and allows some interesting transformations on the shape of data.

## type annotations determine the collection type
What type of collection the iterator is transformed into can be determined by the type annotation alone:

```rust
let array = [1, 2, 3];  
let iterator = array.into_iter();  
let vector: Vec<i32>=  iterator.collect();
```

## `collect` with `Result`
Collect can be used to transform an iterator containing `Result`s into a single `Result`.

If all the `Result`s contained in the interator are success values, collect will return a success value containing an iterator of those values:
```rust
let results: Vec<Result<i32, &str>> = vec![Ok(1), Ok(3)];  
let iterator = results.into_iter();
let collected: Result<Vec<i32>, &str> = iterator.collect();  
println!("{:?}", collected);
```
```
Ok([1, 3])
```

If there is an error value in the iterator, an error will be returned.  If there are multiple errors, the first one is returned.
```rust
let results: Vec<Result<i32, &str>> = vec![Ok(1), Err("nope"), Err("oops"), Ok(3)];  
let iterator = results.into_iter();
let collected: Result<Vec<i32>, &str> = iterator.collect();  
println!("{:?}", collected);
```
```
Err("nope")
```

I can see this being very useful: a lot of the time when one thing fails, we treat the whole thing as being a failure.  Though, in cases where computing each result is costly we may want to fail early rather than compute them all and then collect before failing.


## Collect and category theory
What I like about Rust's collect is that it allows us to transform an object by changing its container.  Instead of data in an iterator, we can have the same data in a vector.

With a `Result` error case, the data changes.

With a `Result` success case, the data stays the same and the container changes.  While the data was each wrapped in a `Result`, and then altogether in an iterator, it becomes wrapped altogether in a vector (or whatever container is specified), and then wrapped again in a `Result`.  In a way, the data is lifted from one context to another.  
