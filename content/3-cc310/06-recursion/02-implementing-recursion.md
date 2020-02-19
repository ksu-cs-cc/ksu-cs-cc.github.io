---
title: "Implementing Recursion"
pre: "2. "
weight: 20
date: 2020-02-18T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/06-recursion/02-implementing-recursion-slides.pptx)

#### Video Script

[slide 2]

In this video, we will look at how recursion works internally on the computer.
Specifically, we’ll look at how the operating system handles function calls and
what that looks like when the function is a recursive function.

[slide 3]

For our example, we will use a simple function, MAIN, that calls a recursive
function, OUTPUT. The OUTPUT function uses head recursion to take in an integer,
N, and then write out the sequence of numbers from 0 to N in reverse order.

As you can see in our example, the base case for OUTPUT is when N equals 0. In
this case, we write out the current value of N in line 2 and then jump to the
return statement in line 7.

If the parameter N is not equal to 0, then the function calls itself recursively
with the parameter N-1. Once the recursive call returns, the function writes the
number N in line 5 and returns in line 7.

Notice that for this function to work correctly, N should be greater or equal to 0.
If not, line 4 will continually call the OUTPUT function with N-1 forever or
until we get an error for running out of memory. This is a case of not correctly
handling the function’s precondition. I leave it to you as an exercise to figure
out how to correct this.

[slide 4]

So, how does the operating system handle function calls. The operating system
has its own stack data structure it uses to keep track of the order of function
calls. We call this stack the *activation stack*. When a program is run or a
function is called, all the important information about that program or function
is saved in an *activation record* that is pushed onto the activation stack.

A typical activation record has space allocated for a function instance’s
parameters, local data or variables, temporary data, and its current status. As
we see in our figure, the activation record for the MAIN program has been pushed
onto the stack.

[slide 5]

Then, when MAIN calls OUTPUT, the first instance of an OUTPUT activation record
is pushed onto the stack. While there are many other data in the activation
record, we will be concerned about the *return address* and the parameter N. The
return address actually refers to the next statement to execute in the function
that called OUTPUT, which allows execution to begin where it left off after the
function call.

In this case, the parameter N is 3 and the return address in the MAIN program is
line 2. Execution starts in line 1 of OUTPUT and since N is not equal to 0, we
jump to line 4 and call OUTPUT with parameter N-1, or 2.

[slide 6]

We push a second OUTPUT activation record. This time the return address is line
5 of function OUTPUT and the parameter N = 2.

We again start executing at line 1 and end up calling OUTPUT in line 4. This
time N-1 will be equal to 1.

[slide 7]

Once again, we create a new OUTPUT activation record and push it on the stack.
The return address is line 5 in OUTPUT and the parameter N = 1.

We once again jump to line 4 to call OUTPUT with the new parameter of 0.

[slide 8]

Finally, we push the final activation record for OUTPUT with a return address of
5 and a parameter of N = 0, which results in executing our base case.

In this case, we write out the current value of parameter N, which is 0, and
jump to line 7 to return.

Now, when we execute the return, we save the return address from the current
activation record and then pop the current activation record off of the stack.
We begin executing in the next activation record at the saved return address.

[slide 9]

Thus, in this case, we start execution at line 5 of OUTPUT, which writes out the
value of N, which is now 1. By popping off the previous activation record, the
context of our execution automatically changes from N = 0 to N = 1.

When we perform the return in line 7, we again save the return address and pop
the activation record.

[slide 10]

Here again, we perform the same execution steps as we did for the last
activation record, but this time N = 2, so we write out 2 and return.

[slide 11]

Finally, we get down to the last OUTPUT activation record, which again starts at
line 5 which was saved from the previous activation record. We write the current
value of N, which is now 3, and then return to the MAIN activation record,
starting at return address 2.

[slide 12]

Here, we continue execution of the MAIN program at line 2 and write “Done”. We
are finally done with our program and the MAIN program exits.

[slide 13]

We have seen how function calls work within the computer. The key to the whole
process is using a stack to store data specific to each function. This data is
stored in an activation record, which consists of data such as function
parameters, local data, and return addresses. Using a stack of activation
records allows the operating system to work on one function at a time without
losing track of the data associated with all the function calls that have
preceded the current function, even in the case of recursive function calls.
