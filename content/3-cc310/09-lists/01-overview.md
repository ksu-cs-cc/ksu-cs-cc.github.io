---
title: "Lists Overview"
pre: "1. "
weight: 10
date: 2020-04-07T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/09-lists/01-overview-slides.pptx)

#### Video Script

[slide 2]

Most people use lists for a variety of reasons. You may use lists to keep track
of the tasks you need to do, or the goods you need to buy. But lists are also
useful in programming. In fact, a list is a very general data structure that
holds a sequence of data that is typically all related to each other.

Actually, we have already seen a wide variety of lists in programming. Some of
these lists include arrays, stacks, and queues. However, lists are very flexible
and can be used to implement stacks and queues very efficiently.

[slide 3]

A common use of lists in software is the history section of your web browser. As
you see here, we can move both forward and backward in our history to view any
of the recent web pages you have visited. Your history is really nothing more
than a list of web pages that your browser keeps track of. When you right click
the forward button, you see a list of web pages that you originally visited
after your current webpage.

[slide 4]

And, if you right click the backward arrow, you get a list of the web pages you
visited prior to the current page you are at.

[slide 5]

Another good example of a software list is your playlist in your favorite music
player. As you know, playlists have an order and can be almost any size, from 1
song, to hundreds of songs. Like your web browser, you can click the forward and
next buttons to move to the previous song in the list as well as the last song
in the list.

[slide 6]

So, what does a list look like in a computer. As shown here, lists consist of a
sequence of data, where each data is linked to the next piece of data in the
list. The head of the list points to the first item in the list, while the tail
points to the last item in the list. We call these kinds of lists "linked
lists".

Nodes are used to store both the data and pointers for each item in the list.
For example, the data "a" is stored in a node along with the pointer from "a" to
"b".

If we need to find a specific node in the list, we need to "walk" the tree,
starting at the head and moving from node to node until we find the node
containing the data we are looking for.

[slide 7]

Inserting an item into the middle of the list is also fairly straightforward. As
you recall, when we wanted to insert a piece of data into a sorted array, we had
to move the contents of the array down by 1 to make room for the new item.

In a linked list, we simply need to create a new node and then rearrange some of
the pointers.

For example, if we want to insert the node "c" into the list, ...

[slide 8]

we change the pointer in node "b" to point to the new node "c", ...

[slide 9]

and then set the pointer in "c" to point to the node "d". We have inserted the
new node "c" into the list in just a few steps.

[slide 10]

So, what if we want to delete an item in the list? Let's say we want to remove
node "d" from the list.

[slide 11]

All we need to do is to change the pointer in node "b" to point to node "e"
instead of node "d" and we are done. Its that easy.

You might wonder about the pointer from node "d" to node "e". Do we need to
change or remove that? Well, no. If we start at the head of the list and "walk"
through our list to the tail, there is no way to reach node "d". It is no longer
part of the list.

[slide 12]

Eventually, the garbage collector will come along and find node "d" with nothing
pointing to it and return its memory locations to free memory.

[slide 13]

A doubly linked list is very similar to a standard singly linked list, with one
exception. Instead of having a single pointer from a node to the next node in
the list, the doubly linked list has 2 pointers. The first points to the next
node in the list like in the singly linked list. But the change lies in the
second pointer, which points to the previous node in the list. We will call
these the previous and next pointers.

Adding this second pointer to the previous node makes many operations easier to
perform. For example, when removing a node from the list, we can refer to the
previous node and the next node.

We can also walk the list in reverse, from the tail to the head just as easily
as walking from the head to the tail.

The only drawback is that we now have to make sure we keep track of both the
previous and next pointers when inserting and deleting nodes.

[slide 14]

So, let's look at inserting a new node "c" into a doubly linked list. Again, the
procedure is basically the same as before, we just need to make sure we update
the previous pointers in the nodes as well.

[slide 15]

The first step is to change the next pointer in node "b" to point to node "c".

[slide 16]

Now, we change the previous pointer from the node "d" to point at the new node.

[slide 17]

Then we set the pointers in "c". We set the previous pointer in "c" to point to
"b" ...

[slide 18]

and the next pointer to point to "d". And, we are done. Conceptually its very
easy and adding an additional pointer only takes a tiny amount of time.

[slide 19]

Removing nodes from a doubly linked list is also basically the same as doing it
in a singly linked list.

[slide 20]

We first change the next pointer in node "b" to point to node "e" ...

[slide 21]

and the previous pointer in node "e" to point to "b". That's really all there
is.

[slide 22]

And just like in the singly linked case, the garbage collector will eventually
come and free the memory space taken by the removed node.

[slide 23]

Linked lists are a very flexible and efficient data structure that has uses in a
wide variety of applications. Not only can lists be used directly, but they can
also be used as the basis of other types of data structures such as stacks and
queues as well. We looked at both singly and doubly linked lists and showed some
simple examples of how we insert and remove nodes for the list.
