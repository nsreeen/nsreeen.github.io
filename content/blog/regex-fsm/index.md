+++
title = "Regex and finite state machines"
date = 2017-08-22
+++


Regular expressions patterns are implemented as finite state machines! I find this pretty cool, and finding this out has helped me to understand both things a bit better.

## Why is this cool?
This means that we can:
- find substrings on just one pass through a string
- without looking ahead (only knowing about one character at a time)
- while only keeping track of a few extra  variables (or states)


## What is a finite state machine?
A finite state machine is just a model for understanding something.  It models something that has different states, and that can only be in one of those states at one time.

For example, a door can either be locked or not locked:

![Image of two circles: one has 'locked' written inside, and the other has 'unlocked' written inside.  There are two arrows, each pointing from one circle to the other.](door_states.png "A door as a finite state machine")


We can add the conditions that cause the state to change:

![The same image as above, but with the arrow leading to 'unlocked' labeled 'turn key right', and the arrow leading to 'locked' labeled 'turn key left'.](door_states_with_conditions.png "A door as a finite state machine, with conditions")

A finite state machine is defined by:
- possible states
- conditions that cause transitions between states to occur
- the starting state (if appropriate - the door is always either locked or unlocked, so the diagrams above don't have a separate starting state)

## A regular expression as a finite state machine
If I wanted to search a string for substrings that:
- start with `a`
- have one or more `b`'s in the middle
- and end with `c`

I could search for the regex pattern `ab+c` (where `+` means the previous character can occur one or more times).

So:
- `abc`, `abbbc`, and `abbbbbbbbc` would all match,
- but `ac` and `acb` wouldn't match.

We can draw this as a finite state machine:

![Image of a finite state machine with circles representing the states 0, 1, 2, 3, and 'not a match'.  'a' can move us from state 0 to 1, 'b' from state 1 to 2, and 'c' from state 2 to 3.  State 3 is double circled.](regex_machine.png "A regex pattern as a finite state machine")


Notes:
- the double circle shows that state 3 is an end state (ie. if we get to state 3, we have found a match)
- some inputs do not cause a change in state (eg. in state 0, any input that is not `a` causes the state to remain 0)

## Keeping track of states
If we want to find out if a string (say: `aabc`) contains our pattern, we will iterate through the string and keep track of our possible states. We'll start out with only one possible states: state 0.  At each character in the string, we will update all possible states with the new input, removing states that `do not match`

We will iterate through each character like this:

<table>
<tr>
<th>Current possible States  </th>
<th>Input character  </th>
<th>Update possible states  </th>
</tr>

<tr>
<td> 0 </td><td>  `a`  </td><td> 1 </td>
</tr>
<tr>
<td>  0, 1  </td><td> `a`  </td><td> 1  </td>
</tr>

<tr>
<td>  0, 1   </td><td> `b`  </td><td> 0, 2</td>
</tr>

<tr>
<td> 0, 2  </td><td> `c`  </td><td> 0, 3 </td>
</tr>

</table>


State 3 is one of our current states, so we know that the string contains our pattern!

If we wanted to find the matching substrings (ie. return the index of each match), we'd have to also keep track of those too.
