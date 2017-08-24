"""
title: Forth implemented in Python - An experiment with literate programming
date: 2017-08-24 12:00:00
published: true
type: post
"""

<br>
I've been thinking about what makes code more or less easy to navigate and understand for a few months.  More recently I've been thinking and learning about literate programming, so I decided to try writing my own literate program! 

I chose to start with the code I wrote for [Pyforth](https://github.com/Nasreen123/Pyforth), my Python implementation of Forth.  Why Pyforth?  I want to think deeply about the code again, to understand how Forth works a little better and to reason with some of the design decisions I made.  Also, I want to write something that would have helped me if I'd found it a few months ago.

This is the first part of the literate program.  In this parts I will cover most of the parts of the interpreter (all except the input stream)

<br>
## Overview Forth

The main parts of a Forth implementation are:

- the parameter stack
- the return stack
- the dictionary and it's pointers
- the input stream

<br>
I find the following break down of the things a Forth interpreter should do useful:

- interpret simple code (the outer interpretation loop) eg: ```3 DUP *```
- add to the dictionary (compile code) eg: ```: SQUARED DUP * ;``` and ```: CUBED DUP SQUARED * ;```
- interpret threaded code (the inner interpretation loop) eg: ```5 CUBED```
- deal with branching and loops

<br>
There are also built-in functions (called words).  These mostly act on the paramter stack.

<br>
## The stack

The stack (or parameter stack) is used to temporarily store data.  This is how Forth words pass receive parameters and return values: all functions interact with the same stack.

The stack is implemented as a Python list.  Instead of a separate top-of-stack pointer, Pyforth utilizes Python's list features by using ```stack[-1]``` to get the top-of-stack.

```python
stack = []
```

The stack could have been an with PUSH and POP methods; I did it this way for the neatness of writing ```PUSH()``` rather than `stack.PUSH()`

```python
def PUSH(item):
    stack.append(item)

def POP():
    tos = stack.pop()
    return tos
```


## The return stack

The return stack is used to keep track of threads (if you're executing function B in the middle of function A: after you finish executing function B, you look at the top of the return stack to find out that you should return to function A). 

The return stack is implemented the same as the parameter stack. 

```python
Rstack = []

def RPUSH(item):
    Rstack.append(item)

def RPOP():
    tos = Rstack.pop()
    return tos
```


## The dictionary

A Forth dictionary is a block of memory, with items written to it sequentially.  Each cell in the dictionary is a fixed width, so items longer than one cell's width take up multiple cells.  It's like a grow-able array.
<br>
Pyforth uses a Python list for the dictionary.  Lists behave how we want our Forth dictionary structure to: we can keep adding things in order,  appending to the end.  The actual implementation of Python lists doesn't use sequential memory blocks, but we can ignore that.  List items can be of any size, unlike dictionary cells, but that means less details to worry about in our implementation. 
<br>
The big difference in how we interact with a Forth dictionary structure compared to a Python list is that we can't directly access the memory address of a Python list item.  We can access list items by index though, and Pyforth uses dictionary indexes as a stand in for memory addresses.
<br>
The dictionary is initialized here:

```python
dictionary = []
```
<br>
A Forth word takes up several dictionary cells.  Each word's entry includes:
- name of the word
- immediate flag (if true the word will be executed immediately, even in compile mode)
- link address (leads to the previous entry in the dictionary)
- code pointer (or execution token)
- the parameter field (which is optional)

In Pyforth each word has a word header, which is an instance of the `WordHeader`
class.  Each word has a word header at one index in the dictionary, and it might have a parameter field.  The parameter field can be several items long. 

```python
class WordHeader():
    def __init__(self, name, link_address, code_pointer, immediate_flag=0):
        self.name = name
        self.immediate_flag = immediate_flag
        self.link_address = link_address
        self.code_pointer = code_pointer

```

<br>
# The dictionary's pointer

Forth usually has a pointer `HERE`, which stores the address of the end of the dictionary and pushes it onto the stack.  With Python we don't have to keep track of the end of the dictionary, we can easily find out what the last index is with `len(dictionary) - 1`.
<br>

So instead we have a function that pushes that index to the stack:

```python
def HERE():
    PUSH(len(dictionary) - 1)

```
<br>
`LATEST` stores the index of the last word added to the dictionary. 
When a new word is added, the index LATEST points to becomes the new word's link address.  This way
the dictionary has a linked list which starts at the last defined word, and leaps back through the dictionary linking word header to word header.  We will use this later to search the dictionary for a particular word.

`PC` is short for 'program counter'.  It keeps track of the next word to execute.

`W` is short for 'working register'.  It's used to keep track in threaded code.

Each of these pointers will store the index of a word header in the dictionary.

They are all initialized to `None`:

```python
LATEST = None
PC = None
W = None
```

To make the rest of the code cleaner, I use dedicated functions to change these pointers:

```python
def incrementLATEST():
    global LATEST
    HERE()
    LATEST = POP()

def update_PC(new_PC):
    global PC
    PC = new_PC

def update_W(new_W):
    global W
    W = new_W
```
<br><br><br>
