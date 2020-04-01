---
title: "Queues Overview"
pre: "1. "
weight: 10
date: 2020-03-27T00:00:26-05:00
---

{{< youtube mkXpzkxGjz4 >}}

#### Resources

* [Slides](/3-cc310/08-queues/01-overview-slides.pptx)

#### Video Script

[slide 2]

When you think of a queue, if we think about the British meaning of the term, we
think about a line. Not the mathematical concept, but more like a line of people
waiting to purchase their coffee, get on an airplane, or get in to see a movie.
However, today, will present queues as a data structure with many uses in
computer science applications.

A queue of people works much like a queue in a program. If the people using the
queue are well-behaved, they get in the queue at the end and wait until everyone
ahead of them in the queue is served before they move to the head of the queue
and get their chance. In most situations, cutting in line, or entering the line
in the middle instead of at the end, is not allowed or at least frowned upon.

Queues work best when you enter at the end and wait your turn.

[slide 3]

In programming, we think of a queue as a data structure made up of a set of
sequential data storage locations. These locations begin at a specific place
that we will call the start of the queue. As we store data in the queue, we grow
the queue, putting one piece of data immediately after the previous one. We keep
track of the end of the queue with a variable called end, which points to the
next location to store data. Before we store anything in the queue, we
initialize start to -1 to indicate that the queue is empty.

[slide 4]

For example, if we store a W on the queue, we store W at end. Since start is -1,
we set start to equal end and then increment end by 1. We call the operation
used to store data on a queue as the enqueue operation. You can think of the
operation as putting at item into the queue.

[slide 5]

We can continue to enqueue items on the queue as long as we do not run out of
room in the queue. So, if we enqueue the value 1 onto the queue, we simply store
the value of 1 at end and then increment end by 1.

Notice that we do not change the value of start. Once start is no longer -1 and
is pointing to a value in the queue, we do not change the value of start unless
we take an item from the queue.

[slide 6]

Next, we will enqueue a piano onto the queue using the enqueue(piano) operation.
Once again, we store piano at end and then increment end.

[slide 7]

So what do we do to get data off of the queue? To do that, we have a similar
operation to enqueue called dequeue. When we call the dequeue operation

[slide 8]

we increment start and then return the item at the old start location. In this
case the value of W is returned to the function that called dequeue.

[slide 9]

Here we have performed another enqueue operation, this time pushing an A onto
the queue.

[slide 10]

Next, we do a dequeue, which increments start and returns the value 1.

[slide 11]

If we do yet another dequeue, we only have one value left on the queue, A.

[slide 12]

Now, if we do a dequeue operation, we will return the last item in the queue, A,
and increment start. Notice now that start equals end, which indicates that we
do not have anything left in the queue.

[slide 13]

To ensure consistency, each time we do a dequeue operation, we check to see if
“start == end” after incrementing start. If “start == end” is true, we reset the
queue back to its initial state.

[slide 14]

But what if we try to do a dequeue on an empty queue? [advance] In this case, we
will get an error because the queue is empty. The error should be signified to
the calling function, and for this module, we assume we will raise an exception
any time an error occurs.

The other important error we will have to handle with a queue is if we try to
enqueue an element onto a full queue. We will talk about how to deal with this
situation in future videos.

[slide 15]

In this video, we talked about queues and how they work in general. We also
talked about the two main operations we perform on queues, enqueue and dequeue.
We use enqueue to put items into a queue, while we use dequeue to remove items
from the queue. Finally, we talked about potential error conditions that occur
when we try to enqueue items onto a full queue or dequeue items from an empty
queue.
