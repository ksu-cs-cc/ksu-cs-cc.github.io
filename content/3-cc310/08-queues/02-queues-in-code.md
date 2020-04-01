---
title: "Queues in Code"
pre: "2. "
weight: 20
date: 2020-03-27T00:00:26-05:00
---

{{< youtube J0wMfzsq42c >}}

#### Resources

* [Slides](/3-cc310/08-queues/02-queues-in-code-slides.pptx)

#### Video Script

[slide 2]

Like stacks, there are several ways to store queues in a computer. In this
module we will focus on queues that store their data in arrays. There are also
other, more dynamic methods such as linked-lists that we can use as well.

[slide 3]

Using an array to store a queue requires us to keep track of both the start and
end of the queue, since the array has a limited size and we will want to "wrap"
our queue around the end of the array when required. To do this, we use a start
variable to hold the index to the beginning of our queue. When the queue is
empty, we typically set start equal to -1.

To keep track of the index for the end of our queue, we use a variable called
end. The end variable points to the element in the array where we will store our
next item. Therefore, we initialize end to 0. And, if start ever equals end, we
know the queue is full.

To encapsulate the functionality of our queue, we typically put everything in a
class, where the queue array and the start and end variables are protected. We
then provide a few basic methods that allow a user to effectively use the queue.
In this video, we will discuss the two main operations on queues, enqueue and
dequeue.

[slide 4]

The nice thing about queues is the simplicity of its code. Here is code for the
enqueue function. Since we are adding an item to the queue and we are using an
array for storage, we must always check to make sure the queue is not full. If
it is, we throw an exception in line 2.

Assuming we have space in the queue, the rest of the code is straightforward.
First, in line 3 we store the item in the array at the index held by the
variable end. Then we increment end in line 4, using the modulo operator to wrap
the index end back to the front of the array if it runs out of room. If you
don't recall the details of the modulo operator, now would be a really good time
to review it.

Finally, lines 5 and 6 capture the situation where we are enqueueing an item
into an empty queue, where start was initialized to -1. In this case, we set
start equal to 0 to point to the newly added item in the queue.

Now, let's assume we call enqueue with the parameter "d".

[slide 5]

The result of that operation is seen here. Notice that "d" was stored into index
0 of the array and end was incremented from 0 to 1. Also, since start was equal
to -1 the value of start was reset to 0.

[slide 6]

Now we look at the situation where we have enqueued four additional items: "c",
"k", "j", and "s". Here, the variable end has been incremented 4 times and now
has the value of 5, which points to the last empty element in the array.

Notice, however, that start has not changed at all. This is what we expect since
the beginning of the queue is still in index 0 of our array.

[slide 7]

Now, finally, let's go ahead and enqueue one more item to fill the array. In
this case, we enqueue "w", which is stored in element 5 of the array. The
variable end is incremented by 1 to 6 and then the modulo operator is used to
convert its final value to 0.

Notice that the values of variables start and end are now equal, which indicates
that the queue is full.

[slide 8]

Let's take a look at the dequeue operator, which takes an item off the queue and
returns it to the calling function. Since we are taking items off the queue, we
must ensure that there are actually items in the queue before we begin. This is
our precondition, which is implemented by lines 1 and 2.

If we pass that test, we copy the item from the array at index start in line 3
and then increment start by 1 in line 4, using the modulo operator to wrap
around the end of the array if needed.

Notice that we can also get into the situation where the variables start and end
are equal due to the effect of the dequeue operation. However, instead of
signifying the fact that the queue is full, it now indicates the fact that the
queue is empty. To make sure we can differentiate between the queue being full
and the queue being empty, we reset the queue to its initial configuration with
start equal to -1 and end equal to 0 in lines 6 and 7.

Later, when we check to see if the queue is empty, we will use the condition
"start == -1", while to check and see if the queue is full we will use the
condition "start == end".

Finally, we return the item to the calling function in line 8.

So, now lets look at an example of performing a dequeue operation.

[slide 9]

The effects of a dequeue operation are shown here. After copying the "d" from
index 0, we increment start to 1 and then return the copied item "d".

[slide 10]

If we do another dequeue operation, we see a similar result. We copy "c" from
index 1, increment start to 2, and then return "c" to the calling function.

[slide 11]

Now, what will happen if we enqueue a "z"? In this case, end equals 0, so we
store "z" into index 0.

[slide 12]

Then, we increment end from 0 to 1 and we are done. We now have a queue that
starts at index 2 and wraps itself around the array, ending up at index 0.

[slide 13]

In this video, we have looked at how we can use an array to implement a queue.
Besides the array, we use the variable start to keep track of the beginning of
the queue and the variable end to keep track of the end of the queue. There are
several other operations that can make using queues much easier such as isFull
and isEmpty as well as the peek function, which allows us to look at the item on
top of the queue without actually dequeuing it from the queue. We will look at
these operations later.
