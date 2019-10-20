"""
title: Understanding something from the perspective of something else
date: 2019-10-20 14:00:00
published: true
type: post
"""

Kotlin's extension functions are pretty cool.  I used them at work recently, for something that I think exemplifies why they are so powerful and is an example of a good time to use them.

-----

### The context

I was working in a monolithic codebase, and needed to call several methods on a class that was owned by another team.  

An analogy is that I needed to call methods on a class representing a `Freezer` to decide if I should offer customers the option to buy ice cream.  

In the (view presenter) class my team owned I wanted to do something like:

```
if (freezer.isIcecreamAvailable()) {
  showIceCreamOptions()
} else {
  hideIceCreamOptions()
}
```

I needed to call several already existing methods on `Freezer` to know if ice cream was available.

```
class FreezerService {

  fun getTemperature(): FreezerTemperature

  fun isInStock(item: Item): Boolean

  // other methods

}
```

-----

### The problem

I wanted a method like:

```
fun isIceCreamAvailable(freezer: Freezer): Boolean {
  return freezer.isInStock(Item.ICE_CREAM) &&
         freezer.getTemperature() == FreezerTemperature.VALID
}

```

I thought about adding to the `Freezer` class but it was already over bloated, shared by lots of teams, and only my team was interested in selling ice cream.  

I wanted this method to allow me to understand the `Freezer` from the perspective of selling ice cream.  But I didn't want to add it to my class as it shouldn't know about the details of the `Freezer`.

I thought about adding a new class, but it would basically be an adapter for the `Freezer`, and didn't make sense when the other option was to add extension functions.

-----

### The solution
I added some extension functions for the `Freezer`:

```
fun Freezer.isIceCreamAvailable(): Boolean {
  return freezer.isInStock(Item.ICE_CREAM) &&
         freezer.getTemperature() == FreezerTemperature.VALID
}
```

Which I can call like any other method of the `Freezer` class:

```
freezer.isIceCreamAvailable()
```

-----
<br>

Although I think it would be easy to overuse extension functions, there are a few reasons I think this is appropriate usage:
<br> - They are not changing any state, only checking conditions
<br> - The extension functions depend on the state of the `Freezer` only + allow us to understand it's state

<br>

When I told my friend Federico what I was doing, he said "ah, you're understanding the freezer from the perspective of the ice cream seller".  I really like this way of phrasing it - thanks Federico for this blog title!
