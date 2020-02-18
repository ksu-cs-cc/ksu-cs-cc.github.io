---
title: "Stacks Overview"
pre: "1. "
weight: 10
date: 2020-02-11T00:00:26-05:00
---

{{< youtube QgA-q4kOgjk >}}

#### Resources

* [Slides](/3-cc310/05-stacks/01-overview-slides.pptx)

#### Video Script

[slide 2]

When you think about a stack, you probably think about things such as a stack of
boxes – as we see here – or a stack of coins, or poker chips, or chairs. But
today we are going to look at stacks as data structures that are very useful in
computer science.

Now, there are several similarities between stacks in the real world and stacks
in programming.

For example, look at our stack of boxes. If you've worked with a stack of boxes,
you know that in general we only put boxes onto the top of the stack and we only
take them off from the top as well. And, if you've ever tried to pull a box out
of the middle of stack, you'll understand why we do it that way.

Whether we are talking about a stack of boxes or a stack of chairs, the fact
that we only put items on and take items off of the top of the stack means that
stacks are a first in first out structure. The last box we put onto the top of
the stack will be the first box we pull off of the stack.

[slide 3]

In programming, we think of a stack as a data structure made up of a set of
sequential data storage locations. These locations start at a specific location
that we will call the *bottom* of the stack. As we store data in the stack, we
grow the stack upwards, putting one piece of data on top of another. We keep
track of the top of the stack with a variable called *top*. Before we store
anything in the stack, we initialize *top* to point one location below the
bottom of the stack.

[slide 4]

For example, if we store a **W** on the stack, we increment *top* and store the
**W** at that location. We call the operation used to store data on a stack as
the *push* operation. You can think of the operation as pushing at item onto the
stack.

[slide 5]

We can continue to push items onto the stack as long as we do not run out of
room in the stack. So, if we *push* the value **1** onto the stack, we simply
increment *top* and then store the **1** at that location.

[slide 6]

Next, we will push a piano onto the stack using the *push(piano)* operation.
Once again, we increment *top* and store the **piano** there.

[slide 7]

So what do we do to get data off of the stack? To do that, we have a similar
operation to *push* called *pop*. When we call the *pop* operation
**[advance]**, we decrement *top* and then return the item at the old *top*
location to the calling function.

[slide 8]

By pushing and popping, we can use the same stack locations over and over. Here
we have performed another *push* operation, this time pushing an **A** onto the
stack.

[slide 9]

Now, we can do another *pop* by decrementing *top* and returning the value **A**
to the calling function.

[slide 10]

If we do yet another *pop*, we only have one value left on the stack, **W**.
Now, *top* equals *bottom*.

[slide 11]

And if we *pop* the stack again, the stack becomes empty and we are back where
we started.

[slide 12]

But what if we try to do a pop on an empty stack? **[advance]** In this case, we
will get an error because the stack is empty.

The error can be signified to the calling function in a number of ways, but for
this module, we assume we will raise an exception any time an error occurs.

The other important error we will have to handle with a stack is if we try to
push an element onto a full stack. We will talk about how to deal with this
situation in more detail in future videos.

[slide 13]

In this video, we have discussed the concept of a stack and how it works in
general. We also talked about the two main operations we perform on stacks,
*push* and *pop*. We use *push* to put items into a stack, while we use *pop* to
remove items from the stack. Finally, we talked about potential error conditions
in stacks, such as when we try to push items onto a full stack or remove items
from an empty stack.
