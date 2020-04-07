---
title: "Singly Linked Insert Remove"
pre: "3. "
weight: 30
date: 2020-04-07T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/09-lists/03-single-insert-remove-slides.pptx)

#### Video Script

[slide 2]

One of the most complex operations with linked lists is inserting and deleting
items from the middle of the list. In this video, we'll take a line by line look
at the general insert and remove operations that can add or remove nodes
anywhere in the list.

[slide 3]

In both operations, there are four main steps: checking the precondition,
initializing our temporary pointers, finding the right location in the list, and
then either inserting or removing the appropriate node.

[slide 4]

We'll start with the insertAt operation.

[slide 5]

There are two input parameters to the operation: the data we want to insert and
the index, or the location in the list where we want to store the data.

In this example, our data is the character “d” and the index is 2.

[slide 6]

Our first step in the operation is to ensure our precondition holds. With the
insertAt operation, the precondition is that the index provided must be valid.
That is, the index must fall between 0 and the size of the list.

This range allows us to add the data anywhere in the list, even at the end of
the list. Since size equals the number of nodes in the list and the current
index runs from 0 to size -1, adding a piece of data when the index equals size
allows us to add items at the end of the list as well.

[slide 7]

Once we are sure we have a valid index, the next step is to check to see if the
index is 0. In this case, it is simpler and more efficient to actually call our
prepend operation. It will also make the rest of the operation easier to write
since we don't need to worry about being at the beginning of the list.

[slide 8]

To keep track of where we are in the list, we need to set up some temporary
pointers and create the new data node. First, we set up the pointer curr to
point at the second node in the list, where index is equal to 1. We can skip the
first node since we have already taken care of the index equals 0 case.

[slide 9]

Next, since we will have to update the pointer in the previous node to insert a
new node, we create the variable prev and point it at the same node pointed at
by head, which is the first node in the list.

[slide 10]

And finally, we create our new node to hold data.

[slide 11]

Next, we get to the heart of the algorithm where we walk through the list using
a for loop starting at i = 1 and ending at index – 1, which is the location we
want to insert our new node at.

In our example, we start at i = 1.

[slide 12]

Within the loop, we simply update the values of prev, which we point at the curr
node. In the example, we update prev to point at node "m".

[slide 13]

and curr, which we update to point at the next node in the list. Eventually,
when we get to the end of the for loop, we will insert our new node between the
two nodes pointed at by prev and curr in the list.

In our example, we update curr to point to node "x".

[slide 14]

Since index is 2, when we loop back up to the top of the for loop, we increment
i to 2, which is now greater than index – 1, so we exit the loop.

[slide 15]

Having exited the loop, we are ready to insert our new node. So, the first thing
we do is to update prev.next to point to our new node.

[slide 16]

And then we update node.next to point at curr. We have now inserted the new node
into the list.

[slide 17]

The last thing we have to do is increment size and we are done.

insertAt is a general purpose insert operation that allows us to insert new data
anywhere in the list, which will be useful in a number of more complex linked
list operations.

[slide 18]

The next operation we will discuss is removeAt. The goal of the removeAt
operation is much like the insertAt operation, to provide a general purpose
remove operation. As with other remove operations, it will return the data in
the node removed from the list.

The only input parameter to removeAt is the index of the node we want to remove
from the list. In our example, we will assume the value of this index is 2.

[slide 19]

Again we need to check our precondition. For removeAt, the precondition is
simply that the index provided is a valid index. However, unlike the insertAt
operation, we only allow the index to range from 0 to size -1, since we can only
remove nodes that are currently in the list. Remember, that the insertAt
operation allowed the index to range up to size, since that allowed us to insert
data at the end of the list.

In this example, our index is valid, so we continue.

[slide 20]

Like the insertAt operation, we also check to see if the index is 0 and use the
remove operation if it is.

In this example, index is 2, so we move on to the else part.

[slide 21]

Here we set up our curr …

[slide 22]

… and prev pointers to point to the first two nodes in the list, just like we
did in insertAt.

[slide 23]

Now, we enter the for loop, initializing our iterator variable i to 1.

[slide 24]

We then update our prev pointer to point to the current node …

[slide 25]

… and our curr pointer to point to curr.next, the next node in the list.

[slide 26]

Now, we loop back and since i is now 2, we exit the loop since index – 1 is 1.

[slide 27]

Finally, we are ready to remove the current node from the list. As you recall,
all we have to do to accomplish this is to update the prev.next pointer to point
at the next node, curr.next, and thus remove node "x" from the list.

[slide 28]

We then update size …

[slide 29]

… and then return the data in the node we just removed, and we are finished.

[slide 30]

As we have seen, inserting and removing nodes in the middle of the list takes a
little more effort than simply inserting and removing at the beginning of the
list. In both operations, there are four main parts: checking the precondition,
initializing our temporary pointers, walking the list using a for loop to get to
the right node, and then either inserting or removing the appropriate node. If
you can master these operations, you will have a good grasp on how linked lists
work.
