---
title: "Python File Operations"
pre: "5.P. "
weight: 51
date: 2019-09-23T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides]({{< relref "/2-cc210/9-files/05-python-file-operations-slides.md" >}})

#### Video Script

Let's look at some of the more useful operations we can perform on files using Python.

In this example code, we're using the `pathlib.Path()` method to create a Path object representing a path on our file system. It may be an existing directory or file, or it could be something that doesn't exist. We'll see how check for that later in this video.

Of course, since we are dealing with a path on the filesystem, we should check for an IOError. So, we've added an except statement here to deal with that exception.

We're also importing the pathlib library, which will give us access to some helpful methods.

Finally, all the code on the following slides can be placed where this "more code goes here" comment is in the starter code. This helps make it a little easier to read the code on the following slides.

First, we may want to know what type of thing that path is pointing at. So, we can use methods from the pathObject we created earlier, such as `exists()`, `is_dir()` and `is_file()` to answer those questions. Each of these methods returns a Boolean value, either `True` or `Talse`, depending on what the `pathObject` is referencing.

If it is a file, we can use the `stat().st_size` attribute to see how big the file is in bytes. However, if we try to do this on a path that doesn't exist, we could get an FileNotFoundError. Also, if we perform this operation on a directory, we'll get an answer, but it won't make much sense to us right now. So, it is always a good idea to check if the item exists and is a regular file before calling this method.

What if we want to copy a file or move it to a new location? Thankfully, there are methods just for that. To move an item, we can use the `rename()` method to change a file or directory's path, effectively moving it to a new location.

To copy a file, we can use the `copy2()` method from the `shutil` library. We'll need to remember to import it before we can use it. Unfortunately, the `copy2()` method only accepts strings as arguments, so we'll have to convert our Path objects to strings before we can use them.

In both cases, these methods will overwrite any existing items at the destination without warning, so they should be used with utmost care.

Of course, we can also delete an item using the `unlink()` method on a file, or the `rmdir()` method on a directory. When doing this on a directory, we'll need to make sure the directory is empty before we try to delete it, otherwise we'll get an OSError.

Finally, if needed, we can also directly create directories using the `mkdir()` method on a directory path. If that directory already exists, we could get a FileExistsError. To create a file in Python, we can simply open it using the `open()` method directly on the Path object, providing a "w" as an argument to indicate that we'd like to write to the file. Nothing special is required there!

As we can see, there are lots of ways we can use Python to explore and manipulate both files and directories on our system. On this page you'll create a quick example program to try some of these methods yourself. See if you can get it to work!
