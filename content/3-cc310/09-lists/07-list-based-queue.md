---
title: "List-Based Queue"
pre: "7. "
weight: 70
date: 2020-04-07T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/09-lists/07-list-based-queue-slides.pptx)

#### Video Script

[slide 2]

Now we are going to take a quick look at a really great use of linked lists

[slide 3]

Queues are data structure that have sequential data storage locations. These
locations begin at the start of the queue and, as we store data in the queue,
the queue grows. We put new data into the queue using an enqueue operation and
remove data from the end of the queue using a dequeue operation.

[slide 4]

Queues have a striking similarity to linked lists, which have a head at the
start of the list and the tail at the end of the list. However, lists are much
more flexible and are able to insert and remove data from any location in the
list. In a stroke of good fortune, lists are extremely efficient in adding and
removing items from the head and tail of the list.

[slide 5]

To implement a list-based queue, all we need to do is implement the following
operations using list operations. As you recall, there are list operations that
perform each of the top 5 operations listed almost perfectly.

[slide 6]

And, the last 3 operations are not even needed by a list-based queue. Since we
are not using arrays to implement our queue, we never have to worry about the
list being full or having to increase or decrease the storage available to the
queue.

Next, we will quickly step through the top 5 operations listed to show how
easily a queue can be implemented on top of a list structure.

[slide 7]

The first operation is the enqueue operation, which simply inserts a new piece
of data at the end of the queue. This is exactly the list append operation and
thus we simply call append to implement enqueue.

As we know, append runs in constant time, and now so does enqueue.

[slide 8]

Likewise, the dequeue operation removes data from the front of the queue. In
this case, that translates directly to the list removeFirst operation. The first
node is removed from the list and its data is returned.

The dequeue operation runs in constant time as well.

[slide 9]

The peek function just returns the data at the front of the queue. Luckily, this
is the exact same operation as the list peek operation, which runs in constant
time. So we simply return the data returned by the list peek function and we are
done.

[slide 10]

The size operation, as you might imagine, is also exactly the same as the list
size operation. The list size operation just returns the value of the list size
attribute, which we return directly in the queue size operation as well. It
shouldn't surprise you that this is a constant time operation.

[slide 11]

Finally, our last operation is the toString operation. Once again, the queue
toString operation can be implemented directly using the list toString
operation. toString is the only operation we need that does not run in constant
time. Since it steps through each node in the list, it runs in order N time.

[slide 12]

In this video, we looked at how we can easily implement a queue on top of a list
data structure. All the operations required for a proper queue can be built
directly from the appropriate list operations. This is an example of where one
data structure "limits" the interface to a second data structure that it is
built on. Using the queue data structure limits the user to interacting with the
list in very specific ways, namely by inserting new data at the end and removing
it from the front of the list. This will not be the last time we see lists being
used to implement other data structures.
