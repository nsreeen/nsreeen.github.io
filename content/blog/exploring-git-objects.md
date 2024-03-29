+++
title = "Exploring git objects"
date = 2018-09-16
+++

Running the `git commit` command in a directory creates inside it a `.git` directory.  In other words, initializing a directory as a git repository means creating a `.git` folder in it.  All of the magic that happens in projects using git will be wrapped up and hidden away in that folder.

The `.git` directory has a bunch of interesting things inside it:
```
branches        config       HEAD   index  logs     packed-refs
  COMMIT_EDITMSG  description  hooks  info   objects  refs
```

This post is about the `.git/objects` directory, one of the most interesting parts. It stores the state of your work at specific points in the past (when you added or commited work) by writing changes to files in the `.git/objects` directory.  Each object file represents a snapshot of changes.

Here's an example of how it looks inside:
```
├── objects
│   ├── 05
│   │   └── 63f77d884e4f79ce95117e2d686d7d6e282887
│   ├── 83
│   │   └── 3f294e32d36a5016344f6db69e727c48b51ad6
│   ├── af
│   │   └── 5626b4a114abcb82d63db7c8082c3c4756e51b
│   ├── info
│   └── pack
```


The files in there are hard to see as they are not in an easily readable format.  Luckily git has some built in commands for viewing the contents of these files!


### Hash paths
The really cool thing about this is that the path for an object is generated by hashing the changes it contains.  The first two characters of the hash become the directory in the `.git/objects` directory, and the rest becomes the filename of the object.  This is really neat because it means that git creates an immutable record of changes.

I create a file called 'hello' containing the text "Hello, world!" and add it to git.  I can find the hash of this change by running:
`git hash-object hello`
=> af5626b4a114abcb82d63db7c8082c3c4756e51b

The path for the object represting the change I made will be:
.git/objects/af/5626b4a114abcb82d63db7c8082c3c4756e51b

If I look at the contents of my `.git/objects`, I can see it:
```
├── objects
│   ├── af
│   │   └── 5626b4a114abcb82d63db7c8082c3c4756e51b
│   ├── info
│   └── pack
```


### Viewing objects contents

To see an objects contents we have to first find out its type.

An objects type is the type of change it represents: blob, tree, or commit.  the different types of objects are created in the following cases:
blob: the changes to each file in your working directory when you `add`
tree: each directory that has changes when you `commit`
commit: each `commit` itself gets its own object too

To find out the type of an objects file given its hash we can run:
`cat-file -t <hash>`

Then we can use the type to see the contents of the object:
`cat-file <type> <hash>`

For example:
`git cat-file -t 5626b4a114abcb82d63db7c8082c3c4756e51b`
=> blob
`git cat-file blob 5626b4a114abcb82d63db7c8082c3c4756e51b`
=> Hello, world!
