+++
title = "Forth implemented in Python - An experiment with literate programming"
date = 2017-08-24
+++

I've been thinking about what makes code more or less easy to navigate and understand and I recently learnt about literate programming, so I decided to try writing my own literate program!


I chose to start with the code I wrote for [Pyforth](https://github.com/Nasreen123/Pyforth), my Python implementation of Forth.  Why Pyforth?  I've been wanting to revisit the code, to understand how Forth works a little better and to reason with some of the design decisions I made.  Writing the code for Pyforth was a challenge for me, so I think it will be a good challenge to try and explain it well.  Also, when I was working on it, most of the resources I found were about writing a Forth interpreter in assembly or written with language I found difficult to follow.  I want to write something that would have helped me if I'd found it a few months ago.


This is the first part of the literate program.  In this part I will cover the data structures of the interpreter.


## Contents

The data structures of a Forth implementation are:

- the parameter stack
- the return stack
- the dictionary and it's pointers
- the input stream


## The stack

The stack (or parameter stack) is used to pass parameters and return values: all functions interact with the same stack.

The stack is implemented as a Python list.  Instead of a separate top-of-stack pointer, Pyforth utilizes Python's list features by using ```stack[-1]``` to get the top-of-stack.

```python
stack = []
```

The stack could have been an object with PUSH and POP methods; I did it this way for the neatness of writing ```PUSH()``` rather than `stack.PUSH()`

```python
def PUSH(item):
    stack.append(item)

def POP():
    return stack.pop()
```


## The return stack

The return stack is mostly used to keep track of loop iterations and threads (if you're executing function B in the middle of function A: after you finish executing function B, you look at the top of the return stack to find out that you should return to function A).

The return stack is implemented the same way as the parameter stack.

```python
Rstack = []

def RPUSH(item):
    Rstack.append(item)

def RPOP():
    return Rstack.pop()
```


## The dictionary

A Forth dictionary is a block of memory, with items written to it sequentially.  It's like a dynamic array. It stores all function definitions (built-in and user defined) and variables.


Pyforth uses a Python list for the dictionary:

```python
dictionary = []
```  


The big difference in how we interact with a Forth dictionary structure compared to a Python list is that we can't access a Python list item by it's memory address.  We can access list items by index though, and Pyforth uses dictionary indexes as a stand in for memory addresses.


A Forth word takes up several dictionary cells.  Each word's entry includes:
- name of the word
- immediate flag (if true the word will be executed immediately, even in compile mode)
- link address (leads to the previous entry in the dictionary)
- code pointer (or execution token)
- the parameter field (which is optional)

In Pyforth each word has a word header, which is an instance of the `WordHeader`
class.  Each word header is one item in the dictionary, and it might have a parameter field.  The parameter field can be several items long.

```python
class WordHeader():
    def __init__(self, name, link_address, code_pointer, immediate_flag=0):
        self.name = name
        self.immediate_flag = immediate_flag
        self.link_address = link_address
        self.code_pointer = code_pointer

```


# The dictionary's pointers

There are a few places in the dictionary we need to know the location of: the end (so we know where to add to next), the word header of the last word added (so we can step through all the words in the dictionary using the link address), and the location of the code we want to execute next.

Usually a word called `HERE`, keeps track of the end of the dictionary and pushes it onto the stack.  With Python we don't have to keep track of the end of the dictionary, we can easily find out what the last index is with `len(dictionary) - 1`.


So instead we have a function that pushes that index to the stack:

```python
def HERE():
    PUSH(len(dictionary) - 1)

```

`LATEST` stores the index of the last word added to the dictionary.
When a new word is added, the index LATEST points to becomes the new word's link address.  So the new words link address points to the header of the word added directly before it.  This way
the dictionary has a linked list which starts at the last word added, and leaps back through the dictionary linking word header to word header.  We will use this later to search the dictionary for a particular word.

`PC` is short for 'program counter'.  It keeps track of the next word to execute.

`W` is short for 'working register'.  It's used to keep track of what to execute in threaded code.

Each of these pointers will store the index of a word header in the dictionary.  They are all initialized to `None`:

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

## The input stream

The input stream stores the input:

```python
input_stream = ""
```

Traditional Forth interpreters parse input in the following steps:
- `ACCEPT` takes input a line at a time, into the input buffer
- `WORD` takes character by character from the input buffer, until it reaches a delimiter (usually whitespace).  `WORD` leaves the word it made this way on the stack.  

After implementing a mostly traditional version, I decided in a later iteration to write a more Pythonic version.  

My `ACCEPT` splits the input stream at whitespace into a list of words.

```python
def ACCEPT():
    global input_stream
    input_stream = input_stream.split()
```

`WORD` removes the first word in the list and puts it onto the stack.

```python
def WORD():
    global input_stream
    PUSH(input_stream[0])
    input_stream = input_stream[1:]
```
