+++
title = "RC 2022 - wikidegrees and runtimes"
date = 2022-10-20
+++

Inspired by [sixdegreesofwikipedia](https://www.sixdegreesofwikipedia.com/), which finds the shortest path between two wikipedia articles, I made [wikidegrees](https://nsreeen.github.io/wikidegrees/).  Wikidegrees finds a random wikipedia article that is 6 degrees removed from the link provided to it.  I liked the idea of being able to explore in both directions (finding the connections between two points, or finding a new connected direction).

### How I wrote wikiedgrees
I wrote it as a static web page which calls an API.  I wrote the server in Rust, using the [axum framework](https://github.com/tokio-rs/axum).

The server takes a wikipedia URL, gets the page contents, parses it for URLs, chooses a random URL, and repeats that 6 times before returning the final URL. My code is just [one page](https://github.com/nsreeen/wikidegrees/blob/main/src/main.rs) - which is partly because the service doesn't have to do much, but mostly because I wrote it with Rust and axum.   


### Reflections on using Rust, axum, and static pages
I found using Rust and axum a joy.  The axum framework minimises boilerplate, and Rust is succinct and robust.  The only thing I didn't find immediately intuitive with Rust and axum was handling async code.  But once I got my head about it, I found it straightforward to do with axum.

I really like writing small web apps as static pages that call a microservice - it's straightforward, fast, and minimises complexity.  Wikidegrees doesn't need user authenticaion, or any navigation, which made it an ideal project to write like this.  

### Tokio, axum, and runtimes
If a function in a web server has to wait for anything to happen before it can return (eg. it's calling another web server, or a database server) it's best for the function to be async.  That's so the server can handle other requests in the meantime, instead of just waiting around.  

To run async functions we need a runtime: that's code that will run async functions and coordinate them (by polling the result to see if it's still waiting for something else, ready to continue it's work, or finished and ready to return).  

Rust *doesn't* have an inbuilt runtime, unlike Javascript and some other languages.  axum doesn't have a built in runtime either, but it can be used with Tokio - which is a popular Rust runtime library.  

To create a Tokio runtime we mark a function as `async` and with `#[tokio::main]`.  This runtime function can then call other `async` functions.
