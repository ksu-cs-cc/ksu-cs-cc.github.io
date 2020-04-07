---
title: "List-Based Stack"
pre: "4. "
weight: 40
date: 2020-04-07T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/09-lists/04-list-based-stack-slides.pptx)

#### Video Script

[slide 2]

Now that we understand how lists work, we are going to build a stack data
structure on top of our list implementation. As you've probably already noticed,
there are many similarities between lists and stacks, so we won't really have to
work too hard at it.

[slide 3]

You remember that a stack is a sequential set of items stored starting at the
bottom of the stack that grows upwards as we put items into the stack.

We use the push operation to put items onto the top of the stack and the pop
operation to take items off the top of the stack.

[slide 4]

Lists work similar to stacks. With lists we enqueue items at the head of the
list and dequeue items at the tail of the list.

However, there are also other operations that will help us create an efficient
list-based stack. Chief among those is the removeFirst operation, which removes
items off the front of the list.

[slide 5]

So when we implement our stacks with a list, the key concept to keep in mind is
that we will equate the top of the stack to the head of the list and the bottom
of the stack to the tail of the list.

[slide 6]

In our original stack implementation, we created several operations besides push
and pop. These include peek to see the data at the top of the stack and two
Boolean operations isEmpty and isFull. And because we implemented our stack with
a predetermined capacity, we had to create double and halve capacity operations
to modify the length of the stack if needed.

[slide 7]

The good news is that with a list-based implementation, there are no
predetermined capacities. A list can grow until we run out of memory. What this
does is to effectively remove the need for three operations: isFull,
doubleCapacity, and halveCapacity.

Next, we will take a look at each of the remaining operations and see how we can
implement them with list operations.

[slide 8]

Our first operation we will look at is the push operation. The stack push
operation works by calling the list prepend operation, which provides the exact
functionality we need.

If we call the push operation with the parameter "q'

[slide 9]

we'll get the results we see here. A node with "q" in it will be added to the
head of the list.

[slide 10]

The pop operation is also very straightforward. However, we first need to check
to see if the list is empty. If it is, we raise an exception. If not, we call
the list removeFirst operation and return the data from removeFirst. Again, the
removeFirst operation provides the precise functionality we need.

So, if we call pop on the stack shown …

[slide 11]

the removeFirst operation will remove the "q" node from the list and return the
value of "q", which gets passed on to the original calling function.

[slide 12]

Next we have our isEmpty operation. Once again, the list isEmpty operation
provides the same functionality we need for stacks.

[slide 13]

So, if we call isEmpty on the stack shown, we will get a "false" value returned.

[slide 14]

Finally, the stack peek operation is implemented using the list peek operation.
Since the list peek operation returns the data from the last node inserted into
the list, it is exactly what we need to implement the stack peek operation.

In this example, if we call the peek operation, it will return "z" without
making any changes to the stack.

[slide 15]

In this video, we've looked at how we could implement a stack using an existing
linked list implementation. We found that due to the similarities between lists
and stacks, the implementation was not only easy from a coding perspective, but
it is also very efficient. This efficiency comes from the fact that the list
operations we used all run in constant time. Simple and efficient, what could be
better than that!
