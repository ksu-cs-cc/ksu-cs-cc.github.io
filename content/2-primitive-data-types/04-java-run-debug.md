---
title: "Java Run & Debug Project"
pre: "4.J. "
weight: 40
date: 2019-02-12T00:53:26-05:00
---

{{< youtube  >}}

#### Resources

#### Video Script

In this video, I'm going to briefly demonstrate how to provide input to your programs in Codio. In addition, I'll show you the basics of using the Codio debugger to help find errors in your code.

For starters, this project contains some sample code to allow your program to read input from the user. We'll learn about how this code works in a later chapter, but for now we can just use it in our programs to read input as needed.

Specifically, this code reads 4 inputs - 2 integers, stored as `x` and `y`, and 2 floating-point numbers, stored as `a` and `b`. Right now, the code just prints those 4 numbers to the screen. So, we can go ahead and run this program, just to see what it does.

Our program can accept inputs in one of two ways. First, we can run our program using the **Java - Run (Terminal Input)** option to provide input via the terminal. So, let's click that option and see what happens.

When we run our program, we are presented with this blinking cursor. This means that our program is waiting to accept input. On a program made specifically for users, we might print some sort of prompt that says what input is needed here. However, since we wrote this program, we'll just assume that we know what inputs we should provide. So, first, our program expects two integers. Let's enter two integers, one per line.

Then, our program expects two floating-point numbers, so we can enter those as well.

As soon as we've provided all inputs expected by our program, it moves on to the next phase and prints out the four numbers we entered. Right now that's all it does, so our program worked as expected.

Let's run it again and see what happens when we provide incorrect input. Let's enter a floating-point number first. As soon as we do, we get this error. This means that we accidentally provided an input that wasn't expected by our program. So, we'll have to restart our program and provide the correct inputs. Of course, we'll learn how to handle these unexpected inputs later in this course, but for now we'll just have to be careful.

Our program can also read input from a file. If we look at the file tree to the far left, we'll see a file named `input.txt`. If we open that file, we'll see that it has inputs already populated inside of it, which we can use in our program. So, on the Run menu, we can choose the **Java - Run (File Input)** option to run our program with that input. This time, the program will read the input from the file instead of the terminal, so it will immediately print out the results. If we want to change the inputs, we can just edit the `input.txt` file and run the program again.

Most of the projects in this course will grade your project using both terminal input and file input, so you'll want to make sure that your program handles both cases appropriately. Again, the starter code in this project will handle that just fine, so you don't have to worry about that for now.

Finally, let's take a look at the Codio debugger, just to see how it works. To start the debugger, use the **Java - Debug (File Input)** option from the debug menu, which is to the right of the run menu. Notice that it only has the ability to accept file input. This is one of the limitations of Codio at this point - it can only accept file input when using the debugger. So, make sure you have provided the correct inputs in `input.txt` before running the debugger.

Once the debugger starts, it will pause your program on the first line of code, highlighted in red to the left. Once there, we can use the buttons at the top to go through the program one step at a time, or we can press the **Resume Program** button to continue to run our program. Let's just press play for now, to see what it does.

As you can see, it allows your program to execute and terminate, and we can see the output in the panel on the right.

Let's run it again, but this time we can step through the program one step at a time. Once we have started the program, we can click the **Step Over** button to go to the next line of code. As we do so, we can see how it runs each line of code in the program individually.

In addition, we can see that it populates a list of variables in the program as we read input from the user. So, we can always see what is stored in any of our variables using the debugger.

Once we get to the end, the program will terminate.

We can also use the debugger to examine the state of our program at a specific point. To do this, we need to create a **breakpoint**. To create a breakpoint, click in the area directly to the right of the line numbers in our text editor, just like this. As you can see, it adds a small red dot to that line.

When we restart the debugger, we'll see that line listed as one of the **Breakpoints** that is loaded into the debugger. So, when we press **Resume Program** this time, we'll see that it stops when it reaches the line we marked. In this way, we can quickly see what the state of our program is when it reaches a particular line, without having to step through the program one step at a time to reach that line. So, here we can see the values of all 4 of our input variables, and make sure that those values are correct before continuing.

Finally, we can add a **Watch** to the debugger, which is an expression we'd like to see the value of as the program executes. So, for example, I could enter `x + y` as a watch. Be warned that your watch expressions won't appear until you continue executing your program. So, if I press the **Step Over** button, I can see the value of that expression. This is really handy if you are tracking a particular value or result in your code and wondering what values it has during the program's execution.

That covers all of the basic features available in Codio's debugger. Of course, there are a variety of interesting ways you can use those tools to help resolve errors in your programs. Feel free to refer to Codio's official documentation, linked from this page, to learn more about how their debugger works. 
