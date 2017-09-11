"""
title: Debugging build scripts in rust
date: 2017-08-31 14:00:00
published: true
type: post
"""
 
emit directives to cargo BY PRINTLN!-ing them!!! this puts them in some file that cargo checks later


Currently cargo (Rust's build tool) doesn't print output from a build script unless it fails.  There has been discussion about possibly adding this feature.  OR YOU ADD --v FOR VERBOSE

I wanted a way to do this because I was trying to better understand a crate that I was using in a build script - I wanted to be able to use print statements :)

# How can you see the output of a non failing build script?  
Make it fail at the end :)

# How can you make a build script fail?
Use `panic()`

This is how I added it to the `build.rs` file:

```rust
fn main() {
    // call external crate
    panic!();
}
```

# What does `panic()` do?
`panic()` works by unwinding the stack. 
