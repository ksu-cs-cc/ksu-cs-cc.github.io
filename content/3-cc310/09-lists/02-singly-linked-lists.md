---
title: "Singly Linked Lists"
pre: "2. "
weight: 20
date: 2020-04-07T00:00:26-05:00
---

{{< youtube U-abMlixblw >}}

#### Resources

* [Slides](/3-cc310/09-lists/02-singly-linked-lists-slides.pptx)

#### Video Script

[slide 2]

Now we are going to look into the code required to create a singly linked list.
First we'll look at the code to create a node, and then we'll take a look at the
singly linked list class and some of its basic operations.

While there are literally dozens of useful operations you could write for a
linked list, we will restrict our operations to only those minimally required
for a list. We will look at the more complicated operations of inserting and
removing items from the middle of a list later.

[slide 3]

The first thing we need to look at when building lists is the definition of a
node. Lists are built on nodes and thus their definition is really important.

[slide 4]

In the node class, we have two attributes. The first holds the data associated
with a node. In our node, we will try to be as general as possible, so we will
allow any type of object to be stored in the data attribute of the node.

[slide 5]

The next attribute is the next pointer. While we call it a pointer, the next
attribute is really a variable that holds the reference to, or the address of,
another node in memory. When we say we are setting the next pointer to point at
node X, what we really mean is that we are storing the address of node X into
the variable next.

[slide 6]

The next thing we'll look at is the constructor. Notice that our constructor
requires that the user provide a piece of data as input. This data can be any
type of object. The input object is stored in the data attribute of the node.

[slide 7]

Then, we need to initialize the next pointer. Since we don't know where this
node will be put into a list, we cannot point it at another node. Therefore, we
set the next pointer to null. When we set a pointer to null, what we really mean
is that a special address is stored in the pointer variable so that the system
knows that the pointer in question is not actually pointing at a memory
location. Often, this value is 0.

[slide 8]

The node class also provides a toString operation as required for all classes.
In this case, we simply call the toString operation of the data in the node.
This allows the list toString operator to produce a string of data that will be
useful.

[slide 9]

Now that we have our node class, we can defined our SingleLinkedList class to
store a list.

[slide 10]

Our first attribute is a pointer to the first node in the list, which we call
"head". We will use head to provide us access to the nodes in the list when we
define our operations.

[slide 11]

Our second attribute is the integer size, which we use to keep track of the
number of nodes in the list. As we go through the list operations, we will have
to update size any time we insert or remove a node from the list.

[slide 12]

The first operation we will look at is the "prepend" operation, which allows us
to insert a node into the first location in the list. If the list is empty, it
will simply add the node to the list. If there are already nodes in the list,
the new node will be inserted between head and the first node in the list.

[slide 13]

So, how does prepend work? The first line creates a new node and puts the input
data into the data attribute in the node. Now we are ready to put the node into
the list.

[slide 14]

The first step is to set the next pointer in our new node to point to the node
where head is currently pointing. If the list is empty, head is null and the
next pointer in the new node will be null. However, if the list is not empty,
the new node's next pointer will point at what was the first node in the list.

[slide 15]

Next, we change head to point at the new node instead of the node it was
pointing to previously. And that's it. Head now points to our new node, which
points to the next node in the list. We have inserted the new node into our
list.

[slide 16]

Before we exit, we need to update size and we are done.

[slide 17]

Removal is also fairly straightforward. Notice that the remove operation returns
the data stored in the first node of the list. This is important in many
applications where we store data in a list to be reused at a later time.

[slide 18]

First, we need to check our precondition, namely that our list is not empty. If
size = 0, then our list is empty, and we raise an exception since we can't
remove a node from an empty list.

[slide 19]

However, assuming we have at least one node in the list, our next step is to
store the data in the first node into a temporary variable. We will then use
this temporary variable to return the data at the end of the operation.

[slide 20]

Next, we update head to point at the first node's next pointer, which points at
the second node in the list. That's really all that is required to remove the
first node from the list.

[slide 21]

Next, we update size by decrementing it by 1.

[slide 22]

And finally, we return the data in temp to complete our operation.

[slide 23]

The isEmpty operation is extremely simple. All we need to do is return the truth
of the expression, size = 0. There are no preconditions or other attributes to
update.

[slide 24]

The peek operation is also simple. In fact, all we need to do is return the data
held in the first node of the list. However, we must first be careful to check
if the list is empty before we try to return the data. Since we are not
inserting or removing any nodes from the list, we do not have to update size.

[slide 25]

So, there you have it. A brief introduction to the code required to implement a
singly linked list. Most of the operations shown are straightforward and easy to
code. Since there are no loops in any of these operations, they all run in
constant time.
