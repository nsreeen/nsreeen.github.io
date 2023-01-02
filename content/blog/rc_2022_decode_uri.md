+++
title = "RC 2022 - decoding URIs"
date = 2022-10-14
+++

I was working with wikipedia URLs recently, and wanted to display URLs which were encoded with escaped characters (eg. "https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life").  

At first I thought this would be tricky, but then I found out this is really easy to do in JavaScript.  Which makes sense, since it's the kind of thing that's probably needed quite often in frontend work.  

It's called ['percent encoding'](https://en.wikipedia.org/wiki/Percent-encoding) or 'URL encoding'.  

### What is percent encoding?
URLs must use ASCII characters.  There are some characters that have special meaning, and therefore cannot be used as part of the URL.  For example, the `#` is used to navigate to sections within a page - if it was also used as part of the URL the browser wouldn't know how to interpret it.  

So if we want to use a reserved character as part of the URL, we have to encode it.  Instead of `#`, we use `%23`: a percent sign to flag the encoding and the ASCII value of the character.  `%27` encodes `'`.

For example:
```
decodeURIComponent("https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life")
=> "https://en.wikipedia.org/wiki/Conway's_Game_of_Life"
```

### What are the reserved characters?
The following characters are reserved:
`! 	# 	$ 	& 	' 	( 	) 	* 	+ 	, 	/ 	: 	; 	= 	? 	@ 	[ 	]`

### Use in non English URLs
Percent encoding is also used for non English URLs: the non English characters are converted to their UTF-8 values, which makes them valid ASCII.  As with reserved character encoding, the `%` is used to flag that they are encoded characters.  

For example:
```
decodeURI("https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D9%84%D8%BA%D8%A9_%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9")
=> "https://ar.wikipedia.org/wiki/اللغة_العربية"
```

The first few characters in the encoded URL are `%D8%A7`.  `D8A7` is the UTF-8 value of the Arabic letter `ا`.  This is the first letter of the Arabic words `اللغة_العربية`(Arabic is read right to left, but when encoded the letter order is reversed).  

```
encodeURIComponent("ا")
=> "%D8%A7"
```

-----

I find these very specific JavaScript features really neat: I like that it's a generic modern programming language but also has a bunch of functionality that's very specific to the browser.
