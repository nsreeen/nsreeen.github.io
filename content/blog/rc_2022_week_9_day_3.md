+++
title = "RC 2022: week 9 day 3 - making HTTP requests in Haskell"
date = 2022-10-05
+++

Today I spent some time trying to make HTTP requests in Haskell, so I decided to write a post about how I did that.  

The easiest to use library I came across is [wreq](https://hackage.haskell.org/package/wreq), and there is an [excellent tutorial](http://www.serpentine.com/wreq/tutorial.html) about how to use it.  

This is the code I wrote:
```
{-# LANGUAGE OverloadedStrings #-}

module Main (main) where

import Control.Lens
import Data.Aeson.Lens (_String, key)
import Network.Wreq                                                                          

main :: IO ()
main = do
  print "Input url to GET"
  url <- getLine
  response <- get url                                         
  print $ response ^. responseStatus ^. statusMessage
  print $ response ^. responseBody . key "name" . _String
```

This code gets a user inputted url and makes a get request to that url.  It then prints the response status message and the value of the "name" attribute in the response body.  There are a couple of interesting things here:

### The OverloadedStrings pragma

There are a few different string types in Haskell - String, Text, ByteString.  The `{-# LANGUAGE OverloadedStrings #-}` pragma allows the different types be operated on interchangeably via the `IsString` typeclass.  This is similar to how the `Num` typeclass allows different number types to be operated.  Overloaded strings are useful when working with strings from different places (http requests and user input).

### Lenses

`response ^. responseStatus` is lens syntax allowing data type fields to be accessed.  In an imperative language, responseStatus would be an attribute of response, and we'd access it like: `response.responseStatus`.  

In Haskell response is a data type, and unpacking the fields is usually done with pattern matching.  Using lenses allows it to be done more succinctly.
