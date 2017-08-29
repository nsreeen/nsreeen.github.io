<br>
I find the following break down of the things a Forth interpreter should do useful:

- interpret simple code (the outer interpretation loop) eg: ```3 DUP *```
- add to the dictionary (compile code) eg: ```: SQUARED DUP * ;``` and ```: CUBED DUP SQUARED * ;```
- interpret threaded code (the inner interpretation loop) eg: ```5 CUBED```
- deal with branching and loops

<br>
There are also built-in functions (called words).  These mostly act on the paramter stack.

<br>
