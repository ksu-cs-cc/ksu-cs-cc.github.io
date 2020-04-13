---
title: "Doubly Linked List"
pre: "5. "
weight: 50
date: 2020-04-07T00:00:26-05:00
---

{{< youtube qMF9aPVFwNo >}}

#### Resources

* [Slides](/3-cc310/09-lists/05-doubly-linked-lists-slides.pptx)

#### Video Script

[slide 2]

In this video, we will look at some of the operations related to doubly linked
lists. Doubly linked lists are very similar to singly linked lists, except we
add an additional pointer in each node to point to the previous node in the list
as well as the next node in the list.

In our implementation, we will also add a tail pointer, which will allow us to
perform operations at the end of the list as efficiently as we performed
operations at the beginning of a singly linked list.

We will also add a built-in iterator, which will allow the user of the list to
step through the list and perform application specific operations not provided
directly by the list class.

[slide 3]

The node of the doubly linked list is just like the singly linked list node,
with the additional previous pointer.

[slide 4]

In the node class, we have three attributes. The first holds the data associated
with the node.

The second attribute in the list is the next pointer, which points to the next
node in the list.

And finally, we have the previous pointer, which points to the previous node in
the list.

[slide 5]

The constructor requires that the user provide a piece of data as input, which
can be any type of object. The input object is stored in the node data.

Then, we need to initialize the next and previous pointers. Since we don't know
where this node will be put into the list, we cannot point it at any other
nodes. Therefore, we set both pointers to null.

[slide 6]

Now that we have our node class, we can define our DoubleLinkedList class to
store a list. The DoubleLinkedList class has four attributes.

[slide 7]

Our first attribute is a pointer to the first node in the list, which we call
"head". We will use head to provide us access to the nodes in the list when we
define our operations.

[slide 8]

The second attribute is a pointer to the last node in the list, which we call
"tail". We will use tail to provide us more efficient access to the nodes at the
end of the list.

[slide 9]

Next, we define a current pointer that works with the built-in iterator
function. Current will point at the current node in the list and will be used by
certain operations to help perform operations on the list.

[slide 10]

The final attribute is the integer size, which we use to keep track of the
number of nodes in the list. As we define the list operations, we will have to
update size any time we insert or remove a node from the list.

[slide 11]

The first operation we will look at is the "prepend" operation, which allows us
to insert a node into the first location in the list. If the list is empty, it
will simply add the node to the list. If there are already nodes in the list,
the new node will be inserted between head and the first node in the list.

[slide 12]

The first line of prepend creates a new node and puts the data into the data
attribute in the node. Now we are ready to put the node into the list.

[slide 13]

Next we check to see if there is anything in the list. If not, we simply set
both the head and tail pointers to point at the new node and we are done.

[slide 14]

However, if we already have a node in the list, we need to insert the new node
prior to the first item in the list. This requires us to update the previous
pointer in the first node in the list to point at our new node.

[slide 15]

Next, we set the next pointer in our new node to point to the first node in the
list.

[slide 16]

And then we set head to point at our new node. Now the new node is fully
inserted into the list as the first node.

[slide 17]

After we increment size, we are done and can return.

[slide 18]

Now, we will take a look at the append operation. Since we have added the new
tail pointer, the append operation looks almost exactly like the prepend
operation, except instead of performing operations at the head of the list, we
do them at the tail.

[slide 19]

The first step, as in prepend, is to create the new node. Since the list is not
empty, we can skip that part and skip to the else part of the operation.

[slide 20]

Here we simply update the tail.next, node.previous, and tail pointers to add the
new node to the end of the list. As you can see instead of adding a node before
the first node in the list, append adds the node after the last node in the
list.

[slide 21]

Removing items from a list in a doubly linked list is very much like removal in
singly linked lists, we just need to update the appropriate previous pointers as
well.

[slide 22]

In this case, our precondition requires the list to actually have something in
it before we can remove it. In our example, we have three items in the list, so
we do not need to raise an exception.

[slide 23]

Next, we create a temporary data variable to hold the data of the node at the
head of the list. We will use this temporary variable to return the data at the
end of the operation.

[slide 24]

Next, we set head to point to the second node in the list.

[slide 25]

If head is now null, that means we have deleted the last node in the list. If
this is the case, we simply set tail = null as well.

Otherwise, we set the previous pointer of the first node in the list to point to
null.

[slide 26]

Next, we decrement our size variable and then

[slide 27]

return the temporary data value from the node we just removed and we are done!

[slide 28]

The removeLast operation works very much like the remove operation except we
remove the last node in the list pointed at by the tail pointer.

[slide 29]

As shown here, if the list is not empty, we save the data into a temporary data
variable, then update the tail and tail.next pointers, and then decrement size.

[slide 30]

Finally, we return the temporary data and were done. We've removed the last node
in a doubly linked list.

[slide 31]

In this video, we've looked at inserting and removing items from both the front
and end of a doubly linked list. The addition of the tail pointer makes both
inserting and removing nodes at the end of the list just as efficient as
inserting or removing them from the front of the list. Otherwise, the only
difference between inserting and removing nodes in a singly linked list versus a
doubly linked list is making sure we update the appropriate previous pointers
when inserting or removing.
