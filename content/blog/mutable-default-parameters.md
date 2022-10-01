+++
title = "Mutable Default Parameters in Python"
date = 2017-03-03

+++

This week I learnt about the mutable default parameter trick, and it's pretty neat. I came across it reading (rather than while trying to fix something), but I guess it's one of those programming things that make you feel like a wizard when you use it knowingly, and a muggle while you're trying to figure out why something doesn't work.


If we do this:

```python
def suprise(some_list=[1,2,3]):

	some_list.append(4)

	print some_list

suprise()
```
We get:
```python
[1, 2, 3, 4]
```
If we call the function again:
```python
suprise()
```
We might expect the same result, but what we would actually get is:
```python
[1, 2, 3, 4, 4]
```
This is because the default list is created when the function is first defined, and the same default list is used each time.  

This happens because functions in python are objects.  When python executes a function statment it creates a new function object (using the namespace and the function code).  The default is evaluated, and then the same default is used each time the function is called.  If it's a mutable default parameter it can be changed, and whenever we use it while calling the function we will get the most up to date version of it.

Another example:

```python
suprise([1])
[1, 4]

suprise()
[1, 2, 3, 4, 4, 4]
```

A way to avoid this if necessary, is to use a place holder instead of a default that can be changed.  For example:

```python
def a_func(some_list=None):
	if some_list == None:
		some_list = []
```
