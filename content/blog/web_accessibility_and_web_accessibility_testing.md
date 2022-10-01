+++
title = "Web accessibility and web accessibility testing"
date = 2017-03-24
+++

## What is web accessibility?

Web accessibility is about removing barriers which prevent people accessing the web.  Usually when people talk about web accessibility they’re talking about disability, and making sure that websites are usable in the different ways people use the internet.  However, web accessibility can be understood more broadly; issues like language (Is content available in a language you know? Do you always have to use a second or third language? Is the writing style unnecessarily academic and confusing? ) and internet connection speed are also about web accessibility.  Taken even more broadly, internet safety is also about accessibility, particularly the safety of groups who are marginalized. It’s part of a wider conversation about who the internet is for, and who benefits from it.

But ensuring websites are accessible is also just part of user experience design and good development.  Just like different people move through the world differently, people use the Internet in lots of different ways, using different tools (eg. keyboard, mouse + keyboard, monitor, smart phone, tablet, screen reader, speakers or no speakers), and experiencing it in different ways (What level of contrast between words and background is clear? How big and what font would you rather read?  Do you listen to the podcast or read a transcript?).  Good web design and development is making websites people can use with ease, even if they don’t use the web the way you and people you know do.

## What are some ways websites can be more accessible?

### Text alternative

Text can be easily rendered in different formats (text on the screen, read by a screen reader), any other format should also have a text alternative.
- All images should have [alt attributes](http://webaim.org/techniques/alttext/)
- Use [aria attributes](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) to make pages easier to navigate by keyboard
- If possible, video should have captions and a transcript.  Audio should have a transcript

### Navigation

The site should be navigable using only a keyboard.
- The [document structure](http://webaim.org/techniques/semanticstructure/) should be [well organized](http://webaim.org/techniques/tables/)
- [Forms should be navigable](http://www.afb.org/info/living-with-vision-loss/using-technology/creating-accessible-websites/accessible-forms/1235)
- All elements should be focusable - [use css focus, not just hover](https://msdn.microsoft.com/en-us/library/ms971307.aspx)
- Include a [skip link](http://webaim.org/techniques/skipnav/) for navigation and other repetitive parts of the page (so if you want to get straight to the main content you don’t have to tab through/ listen to all the links in the header

### Appearance/Clarity

- Fonts should be clear, text size should not be too small
- Color alone should not be alone to convey meaning
- Color scheme and background images should ensure contrast between text and backgrounds

## What is accessibility testing and how is it done?

Accessibility testing means checking the website meets accessibility criteria.  It can include:
- deciding on your accessibility goals during the design stage
- developing the website with these goals in mind
- using an automated testing framework
- human-verifying the results of the automated testing
- Navigating through the site using only a keyboard, and using a screen reader (or screen reader emulator)
- user testing

It’s easier and more effective to plan for it from the start, and let your accessibility guide guide development (like all good testing?).

Some parts of testing can be automated – the following can be checked automatically:
- document structure and hierarchy
- aria and alt tags
- possible color contrast issues

But automated testing has it’s limits:
- a program can judge a website’s code against a list of criteria, but it cannot navigate through the site as a human would and judge the experience for ease or frustration
- automated testing frameworks can only make suggestions on things like color contrast and clarity - they cannot be definitively judged by a program
- all the findings (even those mentioned above) have to be verified by a human

User testing is important, and should include a diverse group of user who use the web in different ways.    Having a developer or tester navigate through the website using their keyboard or a screen reader is a good way to check.  But if they don’t usually use these tools to use the web, they are inexperienced users and so will not have the same experience as a more experienced user of the tool.
