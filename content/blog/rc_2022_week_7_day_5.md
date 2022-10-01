+++
title = "RC 2022 week 7 day 4 - footer css trick"
date = 2022-09-30
+++

Today I learnt a cool CSS trick to make the footer of my blog stay at the bottom of the page!

It's to use the view ports height (`vh`) to force the rest of the page to take up almost all of the height.  I have a container div that wraps the rest of the content, and that takes up all the height except the amount of space the footer needs.  Here's the CSS of the container div:

```CSS
.container {
  min-height: calc(100vh - 100px);
}
```

My footer is around 100px high including padding, so this pushes it to the bottom of the page.

Also, I moved my blog to [Zola](https://www.getzola.org) - and it's been a joy to use!  I had to edit some markdown and template files, so took the opportunity to update the styling too.
