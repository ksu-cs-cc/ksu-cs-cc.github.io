---
title: "Linear Data Structures"
pre: "1. "
weight: 10
date: 2020-02-11T00:00:26-05:00
---

{{< youtube akOjfTCel1o >}}

#### Resources

* [Slides](/3-cc310/04-data-structures-algorithms/01-linear-data-structures-slides.pptx)

#### Video Script

[Slide 2]

All computer programs are used to manipulate data. In fact, that is all they
really can do. That’s why a course on data structures in programming is so
important. Your choice of the structure of your data can either make your
program very easy or very difficult to write. It can also make your program very
efficient, or dreadfully slow.

[Slide 3]

We will start with what we call “linear” data structures. As you might guess,
linear data structures have something to do with a line. We have already seen
the most basic linear data structure, an array or list.

Actually, an array is a finite size structure that is the basis for more
specific linear data structures such as lists, stacks, queues, and sets.

However, we can also create infinite size data structures using linked lists.
While they are actually limited by the physical capabilities of the computer we
are working on, infinite sized data structures can grow and shrink and are not
limited by a predefined “size” parameter. We can also create lists, stacks,
queues, and sets.

[Slide 4]

Lists are the simplest form of linear data structures, whether they are created
from arrays or linked lists. One of the key concepts of a list is that the items
in the list have a specific order. This order is captured in an *index* of each
item. A good example of a list is a string.

There are several useful operations that we use on lists. Like any data
structure, we need to be able to insert items into a list and remove items from
a list. This insertion and removal can take place at the front, back, or middle
of the list.

We also need to be able to find items in the list. In our example here, if I do
a *find* on the list for the letter **s**, the find operation will return
**s’**s index, in this case 2. We also typically have an operation to *get* the
item at a specific index in the list as well as an operation to return the
*size* of the list.

Lists are useful in applications where you need to keep data in order, but you
also need to be able to insert and remove data from any point in the list.

[Slide 5]

A stack is a version of a list that restricts where you can insert and remove
items to and from, in this case the end of the list. By inserting and removing
items from the same end, it implements what we call a last in, first out – or
LIFO - data structure.

We call the insertion operation *push*, while the removal operation is called
*pop*. As shown in the diagram, when we push a number onto the stack, it is
placed on top of the previous number that was pushed onto the stack. Then, as
shown in the bottom half of the diagram, when we pop numbers off the stack, they
all come off the same end of the stack, which we call the top.

There are several other useful operations on stacks, one in particular called
*peek*, that lets you look at the contents of the item on the top of the stack
without having to pop it off the stack.

Stacks are very useful when we want to keep a list of items in the order that
they were put on the list, while ensuring that we cannot manipulate the list
from the bottom or the middle.

[Slide 6]

Queues are similar to stacks except we always put data onto the list at one end
and take data off of the list at the other end. In this way, a queue is much
more like standing in line to get tickets at a box office. Instead of being last
in, first out, a queue is first in, first out – or FIFO. You can also think of
FIFO as being first come, first served.

The name of the insertion and removal operations for a queue are easy to
remember – enqueue and dequeue. The *enqueue* operation put data onto the queue
at the beginning of the list, while the *dequeue* operation takes data off the
list at the end.

The choice between using a stack or a queue really comes down to how you intend
to use your data structure. If you want first in, first out , you use a queue.
If you need last in, first out, you use a stack.

[Slide 7]

Sets are a linear data structure that is very similar to a list, with a couple
of differences. First, a set cannot contain duplicate items. Each item must be
unique. Second, a set is generally unordered, that is we do not need to keep
track of the order in the data structure.

Sets are based on the mathematical concept of sets and we therefore use many of
the same basic math operators. Besides a simple insert and remove for the set
items, we can also perform set union, intersection, difference, and subset.

[Slide 8]

Set union is simply the combining of all the elements in two sets into a new
larger set. The only tricky part to this operation is ensuring that there are no
duplicates in the union of the sets.

[Slide 9]

The intersection creates a new set from only those items found in both sets.

[Slide 10]

The set difference operation removes all the elements of one set from a second
set.

[Slide 11]

Finally, the subset operation determines of all the items in one set are in the
other set. As we see in our example the subset operation would return false for
these two sets.

Sets are useful if we want to make sure we do not have duplicate items in our
data structure. It is also useful if we need to use some of the set specific
operations we’ve discussed here.

[Slide 12]

We have looked at four different linear data structures, each with their own
specific strengths. The key to finding and using the best data structure for
your application is knowing how you will be using the data. While lists are very
general, we can use them to build more specific types of data structures that
enforce certain characteristics that allow us to optimize the insertion, storage
and retrieval of the data.
