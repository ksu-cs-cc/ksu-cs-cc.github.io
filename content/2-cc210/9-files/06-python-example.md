---
title: "Python Example"
pre: "6.P. "
weight: 61
date: 2019-09-23T00:00:26-05:00
---

{{< youtube vZhGJEJs_ck >}}

#### Resources

* [Slides]({{< relref "/2-cc210/9-files/06-python-example-slides.md" >}})

#### Video Script

Now let's see if we can write our own program that deals with files and directories. For starters, let's take a look at the problem statement.

Whaaaa? That looks pretty complex. Just like we do with all of these examples, let's break it down into smaller parts and see if we can build it one step at a time.

For starter, we need to build a program that accepts 3 files as command-line arguments. We also need to remember that there will always be an additional argument included that is the program's name. So, if there aren't exactly 4 arguments, we should print an error and exit the program. So, we can use a simple If-Then statement to handle this part of the problem.

Next, we know that the first two files are input files that we need to read, and the third file is an output file that we should write to. So, we'll need to try and open these files for reading and writing. To do that, we'll use a Try-Exception statement that contains a With statement, and open each of the files as part of that With statement. In the video, I have split these lines of code to make it easier to read, but the With statement should actually be on the same line in your code.

Now we can think about the possible exceptions. We'll have to consider a FileNotFoundError if we try to open a file for reading that doesn't exist, as well as an IOError if we run into any issues reading or writing to any of these files. In each case, we'll just print out the message "Invalid Arguments" and use the `sys.exit()` function to exit the program.

That's all we need for our starter code. So, let's dive in deeper. We'll place the following code where this "more code goes here" comment is in our starter code.

Once we've opened the files, we'll need to read the contents of the two input files. According to the problem statement, each one contains a list of whole numbers, one per line. So, we'll create two For loops, one for each file, and inside of the loop we'll read lines of input from the file until we run out.

Next, we can convert that input to an integer. However, this could cause an exception to occur if the input cannot be converted to an integer, so we'll need to go back to our starter code and add an additional catch statement to handle a ValueError. In that case, we'll print the "Invalid Input" message.

So, back to our inner code. The program should keep track of the sum and count of both the even and odd inputs from each file. So, we'll use a simple If-Then statement to determine if the input is even or odd. Then, inside of those If-Then statements, we'll update the variables for the count and sum of each type of number. It seems like quite a bit of code, but it should hopefully be pretty straightforward to see how it works.

Finally, we'll need to write some output to the output file. To make it easier to read, we'll place that code where the "more code goes here" comment is in this code.

The output is also pretty simple. The problem statement gives us an example of what it should look like. We'll just print the four numbers, each on a separate line, in the order given. In this example, I'm using a short formatted string to convert the output to a string, and also to include the newline character `/n` at the end of each line.

Lastly, we should make sure we remember to print "Complete" to the terminal before exiting. In this case, we'll need to use the `print()` function to make sure it appears on the terminal and not in our input file.

The problem statement also helpfully reminds us to make sure we close any open files when we are done with them. Thankfully since we are using a With statement, that part is automatically handled for us!

There we go! That's all it takes to build this simple program in Python to explore reading and writing with files. See if you can get it to work yourself!