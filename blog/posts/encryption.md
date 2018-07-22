"""
title: What is public - private key encryption?
date: 2018-07-22 14:00:00
published: true
type: post
"""

I was curious about how public private key encryption works and wanted understand it better.  So I did some research and a simple [implementation in python](https://github.com/Nasreen123/public-private-key-encryption), and it's pretty neat!  This post is a write up of what I learned. It's not complete - I only scratched the surface with this. 

There are some ideas behind the maths: 'hard' equations, computational difficulty, and trapdoors for solving hard problems.

There are two main hard math equations used: modular exponentiation to encrypt and decrypt, and euler's theorem for calculating the keys. 

## Contents
1) How it works: the ideas behind the maths

 - how easy or 'hard' a function and it's opposite are

 - computational difficulty of 'hard' functions (ie how long they take computers to do)

 - trapdoors for solving the 'hard' functions


2) How are messages encrypted? (with an  example)

- A message to encrypt

- Modular exponentiation 

- Trap door and decryption

3) How are keys calculated?

- Calculating N and phi N

- Calculating d

- Euler's theorem


## 1) How does it work?

### Easy/ hard functions

An example of a function that is easy both ways is addition/ subtraction:
<br>`x + 4 --easy--> ?`
<br>`? <--easy-- x - 4`

<br>
It's easy both ways because in both directions there are steps you take, and you know you will get to the right answer in x steps. 

<br>
An example of a function that is harder in one direction is squaring vs finding a square root:

`17 2 --easy--> ?`

`? <--harder--  √289 `

<br>
Functions that are hard in one direction are hard because you have to use trial and error to get to the answer. With big numbers, this takes a long time. 

<br>
Another example is prime factorization: What prime numbers multiplied together produce a number?
<br>`17 * 13 --easy--> ?`
<br>`? * ? --hard--> 289`


### Computational difficulty (or how long it takes to calculate)

When we say something is [computationally hard](https://en.wikipedia.org/wiki/Computational_complexity) we mean it takes a computer a prohibitively long time to do the calculation.  The 'hard' examples above wouldnt take a computer very long to compute, but the same examples with much bigger numbers would.  Encryption algorithms that are used today, with the size of numbers that are used, would take computers years to break.


### Trapdoors

Hard functions can have trapdoors that make solving them faster.  The prime factorization example above would be a lot easier if I told you that one of the prime factors of 289 is 17; it would become a straightforward division. 

The functions chosen for encryption also have trapdoors.  These make the hard equation easy to solve if you have a secret key, but difficult for everyone else.


##2) How are message encrypted?

### Let's encrypt a message

Say my friend wants to send me an encrypted message.

* I will use my private key, which only I know (`e` = 23)
* My friend will use my public key, which everyone knows (`d` = 47)
* We will both use the shared modulus, which everyone knows (`n` = 91)

Say the message my friend wants to send me is `hi`, which gets mapped to 89 (h = 8, i = 9)


### Modular exponentiation + encryption

The equation used to encrypt is [modular exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation):
<br>`message ^ e mod n`
<br>1) take the message
<br>2) raise it to be
<br>3) divide it by `N`
<br>4) the remainder is the encrypted message

So my friend encrypts:
```
89 ^ 23 mod 91 = 44
encrypted message = 44
```

Python has a built in method for modular exponentiation:
```
encrypted_message = pow(message, e, n)
```

Modular exponentiation is a good equation for encryption because it is easy one way, but hard the other way. 

```
89 ^ 23 mod 91 --easy--> ?
? ^ 23 mod 91 --hard--> 44
```


### Trap door and decryption

This example wouldn't take a computer so long to work out, but the numbers used in real encryption are much longer - tens of digits long.  It would take a computer decades to calculate the original message with such long numbers.

It's easy if you have a trapdoor though, and we do: `d`! `d` is the number that 'cancels out' the modular exponentiation of `e`.  We calculate `d` using another trapdoor which we will talk about later

To decrypt the message we use the same equation, with `d` instead of `e`.
`44 ^ d mod 91 = 89`

In python we could encrypt and decrypt like this:
```
encrypted_message = pow(message, e, N)
decrypted_message = pow(encrypted_message, d, N)
```


##3) How are the keys calculated?

We calculate `e` by generating a random prime number.  How can we calculate `d` - the trap door to decrypt?  

The answer is in how we calculate `N`: we do it in a way that leaves us another trap door to calculate `d`

### Calculating n and phi n
The way we generate `N` is by randomly choosing two large prime numbers and multiplying them together.  The two primes cannot be the same number.  This can be written in python:
```
def getN():
  prime1 = getLargePrimeNumber()
  prime2 = getLargePrimeNumber()

  if prime1 == prime2:
    return getN()

  return prime1 * prime2
```

We share `N` with everyone (along with the public key), but we don't share the prime numbers we used to make it.  So only we know the prime factorization on `N`: this let's us make another trap door: `phi of N`. 

`phi of N` is the number of numbers there are that are:
<br>- smaller than N
<br>- do not share a common factor with N (other than 1)

<br>
The phi of 7 is 6, because the only factors of 7 (a prime number) are 1 and itself, and 1 isn't counted as a factor when calculating phi.  So all positive numbers less than 7 count towards it's phi.

<br>
The phi of 8 is 4, because 1, 3, 5, and 7 don't share factors with 8.  2 is a factor of 8, so it has a common factor with 8: 2 itself.  4 and 6 also have 2 as common factors with 8

<br>
phi is multiplicative.  We can work out a numbers phi from it's factors:
`phi(a*b) = phi(a) * phi(b)`

<br>
So we can easily work out the `phi of N` from it's prime factors, as the phi of a prime number is all the numbers smaller than it
<br>`phi(N) = phi(prime1) * phi(prime2)`
<br>`phi(N) = (prime1 - 1) * (prime2 - 1)`

### Calculating `d`
To encrypt:
<br>`m ^ e mod N = c` 
<br>To decrypt:
<br>`c ^ d mod N = m`

<br>If we combine these two equations, by replacing `c` with in the lower one with it's definition in the top one, we can say :
<br>`m ^ ed mod N = m`

How can we work out `d`, so we have a trap door to decrypt?  We can use Euler's theorem.

### Eulers theorem: connecting modular exponentiation and prime factorization

[Euler's theorem](https://en.wikipedia.org/wiki/Euler%27s_theorem):
<br>`m ^ phi(N) mod N = 1 mod N`

<br>
We can change it with two small rules:
<br>1) `1 ^ k = 1`
<br>2) `1 * m = m`

<br>
To get:
<br>`m ^ k*phi(n)+1 mod N = m mod N` 

<br>
This is like the equation we used to relate `d` and `e`:
<br>`m ^ ed mod N = m` 

<br>
So we can say that
<br>`ed = k*phi(n)+1`
<br>and
<br>`d = (k*phi(n)+1) / e`

<br>
Notes:
<br> * k can be any integer - we use it to make sure we are working with an integer result
<br> * `mod N` on one side is the same as`mod N` on both sides






