+++
title = "Validating Emails"
date = 2021-08-29
+++

Recently I had to validate email addresses and it was a lot more interesting than I expected!  The solution was a lot simpler than I expected as well, which was pretty neat!  

### The rules are more complicated than I expected!

When I started googling email address validation rules, I was expecting there to be a a few rules that I could turn into a regex but it turns out that is not the case!  

The specification is [multi-part](https://datatracker.ietf.org/doc/html/rfc5322#section-3.4.1)
[and](https://datatracker.ietf.org/doc/html/rfc1034) [long](http://www.faqs.org/rfcs/rfc822.html).  It seems like a lot of email validation is [too strict](https://haacked.com/archive/2007/08/21/i-knew-how-to-validate-an-email-address-until-i.aspx/), with attempts at precise validation being somewhat [arbitrary](https://stackoverflow.com/questions/201323/how-can-i-validate-an-email-address-using-a-regular-expression/51332395#51332395).

The [local part](https://datatracker.ietf.org/doc/html/rfc2822#section-3.4.1) can have special characters, and can have pretty much any character if wrapped in quotation marks!   

### Valid and allowed are not necessarily the same thing!

Apparently a lot of email providers don't allow some of the special characters in the local part, though they are valid (and are often excluded from validators).  

The other thing that surprised me about the local part is that it is only parsed by the email provider ... so it's possible that an email provider would allow characters that are not allowed in the specification, so an email address could be invalid but still work!  So validating against the specification could exclude some possibly functioning email addresses!

### Valid could still be wrong!

The other big issue is that even if an email is valid and possible, that doesn't tell us that it is the email address we want.  Most of the typos that could be made when entering an email address would not invalidate it.  

### What are we trying to achieve?

So is there any point in validating?  I think it can be useful, to make sure the email address was submitted in the correct field.  I think the most minimal check possible suffices for this: check there is an '@'.  

If we need to confirm that we have the correct address we should send a link to the owner to confirm.  If we just want to be sure that the user typed the address as they intended to we could ask them to input it twice.  It depends on what our goal is.

### Why I enjoyed this

What I enjoyed about this problem is that the answer is to step back and understand what we are doing and why.  And then to do the most minimal solution possible, while making peace with the fact that the solution is imperfect and it's also the best one.  

I notice a tendency in myself sometimes, to want to work in certainties.  That can be useful when working with closed systems and modelling risks, but it's also not how the world works.  Software systems have to meet the real world at some point and those edges may be imperfect.
