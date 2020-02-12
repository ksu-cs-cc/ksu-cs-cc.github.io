---
title: "Stacks in Code"
pre: "2. "
weight: 20
date: 2020-02-11T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/05-stacks/02-stacks-in-code-slides.pptx)

#### Video Script

Slide 2

There are several ways to implement stacks on a computer. In this module we will
focus on stacks that store their data in arrays. There are also other, more
dynamic methods such as linked-lists that we can use as well.

Slide 3

Using an array to store a stack requires us to keep track of the top of the
stack. To do this, we use a *top* variable to hold the index of the current top
of the array. When the stack is empty, we typically set *top* equal to -1.

To encapsulate the functionality of our stack, we put everything in a class,
where the stack and *top* variable are protected. We then provide a few basic
methods that allow a user to effectively use the stack. In this video, we will
discuss the two main operations on stacks, *push* and *pop*.

Slide 4

Since we are using an array to store our stack, we will show our stack
horizontally, similar to how we show an array. In this case, the stack grows
from left to right. **[advance]** However, this is easily translated to a more
common view of stack as a vertical structure. In this case, the stack grows from
bottom to top. You should really be familiar with either of these views of
stacks.

Slide 5

The nice thing about stacks is the simplicity of its code. Here is code for the
*push* operation. Since we are adding an item to the stack and we are using an
array – meaning our storage in the array is limited – we must always check to
make sure the stack is not full. If it is, we throw an exception.

Assuming we have space on the stack, the rest of the code is straightforward.
First, we increment *top* by one to point to the next unused location in the
stack and then store the item in that spot in the array.

Slide 6

An example of pushing an **a** onto the stack is shown here. First, we increment
*top* to 0, which is the first location in the array.

Slide 7

We then store the **a** into the array location indexed by *top*. Pretty simple.

Slide 8

If we continue on and push **b**, **c**, **d**, and **e** onto the stack, our
array will look like this. Notice that each item is stored in the order it is
pushed onto the stack, and that *top* has been incremented to 4, which points at
the **e** on top of the stack.

Slide 9

Of course, the question you have now is how do we get the data out of the stack?

Slide 10

Once again, the code for the *pop* operation is also nice and simple. We first
check to see if the stack is empty, which is denoted by the *if top == -1*
statement at the beginning of the function.

Slide 11

Assuming there is something on the stack to pop off, we continue, this time
decrementing *top*.

Slide 12

Finally, we return the item stored where the previous top of the stack was – at
location *top + 1* in the array and we are done.

Slide 13

Now, if we perform two more *pop* operations the stack would end up looking like
this. Again, *top* has been decremented by 2 – once for each *pop* operation.

Slide 14

In this video, we have looked at how we can use an array to implement a stack.
Besides the array, the only other variable we need is a *top* variable to keep
track of where the current top of the stack is. There are several other
operations that can make using stacks much easier such as *isFull* and *isEmpty*
as well as the *peek* function, which allows us to look at the item on top of
the stack without actually popping it off the stack.
