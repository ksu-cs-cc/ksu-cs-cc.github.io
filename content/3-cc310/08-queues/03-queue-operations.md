---
title: "Queue Operations"
pre: "3. "
weight: 30
date: 2020-03-27T00:00:26-05:00
---

{{< youtube htP3pacx1fI >}}

#### Resources

* [Slides](/3-cc310/08-queues/03-queue-operations-slides.pptx)

#### Video Script

[slide 2]

Now that you have a conceptual notion of how queues work, we will investigate
the details of the queue class. Specifically, we want to take a look at the main
operations for a queue. In this video, we will look at each operation
individually by walking through the code.

[slide 3]

The first operation we need to discuss is the class constructor. For a queue,
there are three main attributes that the class is responsible for. The queue,
which we will implement using an array called myQueue, and the start and end
attributes, which keep track of the array indexes for the beginning and end of
the queue.

Since our queue is empty when it is created, the queue constructor should
allocate the array in memory and then initialize the start attribute to -1,
which indicates that the queue is empty, and the end attribute to 0, which is
the first location we will store new items in the queue.

[slide 4]

The pseudocode for the queue constructor is shown here. Notice that we require
the calling method to explicitly provide a capacity value, which will be the
initial size of the array.

[slide 5]

The first thing we need to do in our operations is to check our preconditions.
In this case, capacity must be an integer greater than 0. As you see in our
code, we explicitly check to see if the value is an integer value. While this
may be necessary in dynamically typed languages such as Python, in typed
languages such as Java, C, or C\#, we can explicitly define capacity to be an
integer type, effectively ensuring that the value passed in will be an integer.

In either case, we must also check to ensure that the capacity value is greater
than 0. If either one of the precondition checks fail, we will raise an
exception and let the calling method handle it.

[slide 6]

If we pass the precondition checks, we then move on to the heart of the method.
There are basically three lines. One creates the myQueue array of the
appropriate capacity while the second initializes the start attribute to -1 and
the third initializes the end attribute to 0.

Since there are no loops in the Constructor operation, the constructor will run
in constant time.

[slide 7]

It is important to note that the myQueue, start, and end variables are all
defined as attributes at the class level. Thus, whenever we refer to these
attributes in any queue operation, we are referring to the same attributes.

[slide 8]

Next, we will look at the enqueue operation, which allows us to put new items
into the queue. In our example here, we have an empty queue, presumably just
created by our constructor method.

[slide 9]

When a method calls the enqueue operation, we store the value at in the array at
the index in the end attribute. Here we store "a" in array location 0.

[slide 10]

Then we increment the value in end. In this case we increment end to 1.

[slide 11]

And finally, since start was initialized to -1 to indicate an empty queue, we
must change the value in start to 0 to point it at the beginning of our queue.

Now, if start was not equal to -1, then there is no need to change the value of
start since we are only enqueuing items at the end of the queue.

[slide 12]

When we look at the enqueue code, you'll notice that the first thing it does is
to check its preconditions. In this case, the enqueue operation must ensure
there is space in the array to store the item. If the queue is full, then we
again throw an exception.

[slide 13]

If we pass the precondition check, there are two parts to the rest of the
function.

First, we copy the item into our queue array at location end. Then, we increment
end and use the modulo operator to ensure we wrap around the array if necessary.

[slide 14]

Finally, we check to see if we have inserted an item into an empty array. If so,
the start attribute is in its initial configuration and is equal to -1. Thus, we
reset start to point to 0, the first item in the queue and we are done.

Like the constructor, there are no loops so enqueue runs in constant time.

[slide 15]

Next, we will talk about the dequeue operation. There are actually four parts to
the dequeue operation. First, we check our precondition – this time it is that
the queue is not empty. Second, we copy the item at start and then increment
start. Third, we check to see if the queue is empty and reset start and end to
the initial configuration if it is. And finally, we return the item we copied
from the queue.

[slide 16]

So, in this example, after checking our precondition, we copy the item "a" so we
can return it at the end. Then we increment start by 1 to point to the new
beginning of the queue and finish up by returning the value "a" to the calling
function.

[slide 17]

The dequeue method is straightforward and structured similarly to the enqueue
operation.

We first check the preconditions, which in the case of dequeue is that the queue
is not empty. If it is, we again throw an exception.

[slide 18]

Then, if the queue is not empty, we perform the two actions I just described. We
copy the item from the start location in myQueue and then increment start by 1.
Again, we use the modulo operator to ensure we can wrap start to the beginning
of the array if needed.

[slide 19]

We then perform our check to see if we have an empty queue and, if we do, we
simply reset start and end to their initial configuration as we did in the
constructor, where start equals -1 and end = 0.

[slide 20]

And, last but not least, we return the item that was previously at the beginning
of the queue.

Like its cousin the enqueue operation, the de-queue operation runs in constant
time.

[slide 21]

Next we will look at the isFull operation, which is a really simple function.
Basically, it just returns the Boolean value of whether start equals end. If it
does, then isFull returns true, otherwise, it returns false.

So, in the example shown, since start and end are both equal to 1, a call to
isFull will return true.

[slide 22]

The isEmpty operation is structured exactly like the isFull operation. The only
difference is that we return the value of whether start is equal to -1. If it
is, then the queue is empty.

In this case, since we are in our initial configuration with start equal to -1,
the isEmpty operation will return true.

[slide 23]

However, if we look at our previous example, start is equal to 1 and so a call
to isFull will return false. As expected, isFull and isEmpty both run in
constant time.

[slide 24]

Next, we'll look at the peek operation. Peek is a simple operation that just
returns the value in the array at index start. In this way, Peek is similar to
dequeue. However, it is different in that it does not have to worry about
incrementing any indices. The only requirement is that before it returns the
value at start, peek must check to ensure that it's precondition, that the queue
is not empty, is satisfied.

Again, because of its simple structure without any loops, peek runs in constant
time.

[slide 25]

Next, we will look at the size operation. While you might think that the size
operation should be pretty simple, it actually has several cases that we must
consider to get the correct value.

The first two cases, if the queue is empty or if the queue is full, are simple.
If the queue is empty, we return 0. And, if the queue is full, we just return
the capacity of the array.

[slide 26]

The third case is rather straightforward as well. This is the case where the
queue is stored in the array with the start of the queue being less than the end
of the queue. In other words, the queue is stored linearly in the array and does
not wrap around the end of the array. In this case, size is simply the value of
the end index minus the value of the start index.

Our example shows this case, where end = 5 and start = 0. In this case, the size
of the queue is 5 - 0, or 5.

[slide 27]

The fourth case requires a little more thought. In this case, the front part of
the queue is stored at the end of the array from location start to the end of
the array, while the end part of the queue is stored in the front part of the
array, from 0 to the end -1 location.

To get the size of the queue, we simply add the size of the two parts of the
array. The size of the front part of the array is the capacity of the array
minus the value of the start index, while the size of the end part of the array
is simply the value of end.

When you add those together, you get the grand total.

In our example, we can see that the queue starts at location 4, ends at location
2, and that the capacity of the array is 6. Thus, the front part of the array is
6 – 4, or 2 elements long, while the end part of the array is 2 elements long.
We add these together to determine that the size of the queue is 4.

[slide 28]

The code for size, while it has four cases, is really quite simple. We have one
statement for each case, a return statement that matches the cases we described
in the last couple of slides.

Again, the size function will run in constant time.

[slide 29]

In many languages, such as Python, you can add space directly to an array or
list. In these languages, the doubleCapacity operation is very simple and we
won't cover it here.

However, in most traditional languages such as Java or C\# you cannot simply add
space to an array. Therefore, we have to follow a four-step process.

First, we must create a new array with double the capacity of our current array.
Next, we will copy the contents from the current array into the new array. And
then, we will point our myQueue attribute to point at the new array. Finally, we
update the value of start and end to correspond to the appropriate locations in
the new array.

[slide 30]

For the doubleCapacity operation, we have no preconditions since it doesn't
really matter if the array is empty or full. We are just changing the amount of
storage available in the array.

So, the first step is to create a new array, which we will call newQueue, which
is double the size of the myQueue array.

[slide 31]

Next, we need to copy the values from myQueue to newQueue. The example shows the
situation before we start the loop.

To simplify the copy process, we assume that we will copy items from myQueue,
one by one, into newQueue starting at element 0. Then, to ensure we copy items
out of myQueue in the correct order without having to worry about wrapping
around the end of the array, we will just use the dequeue operation to take care
of these details for us. Thus, we will loop through each item in myQueue,
dequeue it, and copy into the front of the newQueue array. Notice that we have
to store the size of myQueue into the length variable before we start the loop
since we are using the dequeue operation and the value returned by the size
operation will decrease each time we dequeue an item.

[slide 32]

Once we complete the loop, we will have copied each item from myQueue and stored
into the newQueue array.

As shown in the example, however, we still need to update the class attributes,
start, end, and myQueue.

[slide 33]

Once we update the attributes, we are done and myQueue now points to an array of
length 8 instead of length 4. And, although the location of the values in the
array changed, the new myQueue will work exactly like the old one except it will
have twice as much space.

Because doubleCapacity uses a loop to go through each element in the array in
the worst case, it should be obvious by now that it will run in order N time.

[slide 34]

The halveCapacity operation is actually the exact same as the doubleCapacity
operation, with two modifications. First, we now have a precondition. Since we
don't want to lose any items from the queue, we need to make sure that all the
items can actually fit into the new queue. And second, the new array is created
with only one half of the capacity of the old array.

[slide 35]

The differences between the doubleCapacity operation and the halveCapacity
operation are highlighted here in green. First, we have to check to ensure that
the size of the current queue will fit into a smaller queue, and, if it does, we
then create a newQueue array half the size of the existing myQueue array.

Then, the rest of the operation is exactly the same as the double capacity
operation. We simply copy the elements from myQueue into newQueue, update the
start, end, and myQueue attributes, and we're done.

Thus, if we were to perform the halveCapacity operation on the example show,

[slide 36]

it would end up looking like this new myQueue array, with half the space and the
elements of the original queue copied into the front part of the new array.

Since halveCapacity has almost the same code as doubleCapacity, it should come
as no surprise that halveCapacity runs in order N time as well.

[slide 37]

All objects are generally required to implement a toString operation to override
the default toString operation provided by the base Object class. This is
especially important if you want your output formatted in a specific manner.

In our case, we want our output to list the items in the queue from start to
end. The overall process is straightforward.

First, we create an empty output string. Next, we loop through the queue from
start to end appending the string version of each item onto the output string.
And finally, we return the output string.

[slide 38]

Next, we will take a look at the toString code. The toString operation does not
have a precondition, since if the queue is empty, we should simply return an
empty string, which represents the queue perfectly.

The operation first creates an empty output string and then enters a loop that
walks through each element of our queue. Notice that we compute the next element
in the queue by adding the loop index I to the start location of the queue.
Since the queue can wrap around the end of the array, we use the modulo operator
to ensure we end up with the appropriate array index. We then perform the
elements toString operation on it and append that to the end of our current
output string.

Once the loop is done, we simply return the output string and we are done.

Now, if we perform the toString operation on the example shown,

[slide 39]

we will get the output shown here – the string "dwkko".

Since we have a loop that potentially looks at each element in myQueue array,
toString runs in order N time.

[slide 40]

In this video, we have looked at several basic queue operations and at the
pseudocode required to implement them. Almost all the operations are
straightforward. However, there were several cases where we are required to
carefully check the preconditions so the operations worked as advertised.
Finally, we saw that many of the operations run in constant time, while more
complex operations such as double and halveCapacity and toString run in N time.
