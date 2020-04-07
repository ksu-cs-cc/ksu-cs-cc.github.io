---
title: "List Iterator"
pre: "6. "
weight: 60
date: 2020-04-07T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/09-lists/06-list-iterator-slides.pptx)

#### Video Script

[slide 2]

Linked lists are a general purpose structure that can be used in a wide variety
of applications. However, there is no way we can predict everything that a user
might want to do with a list. It would be nice if users could implement that
functionality by themselves. So what we want to do is to allow users the ability
to actually access the data in the list without having to understand how the
list works internally. To that end, we can provide users with basic operations
they can use to add the functions they need.

The most important functionality we can add for a user is the ability to walk
through their lists and manipulate the data in them. So, in this video, we will
introduce the concept of a list iterator that will allow the user to do just
that.

[slide 3]

The first thing we need to modify in our list class is to add a new pointer,
current, that points to the iterator's current node in the list. By having a
pointer at the class level, the user can call the iterator operation over and
over while the attribute current keeps track of where the iterator is in the
list.

[slide 4]

The first operation we need to provide is the iterator reset operation. Reset
basically sets, or resets, the current pointer to null, indicating that the
iterator is not pointing at any node in the list. Users need to use this
operation to make sure that the iterator is starting at the beginning of the
list.

[slide 5]

The key function in the iterator is the getNext operation. This is where the
user gets access to the next piece of data in the list.

First we check to see if the list is empty. If it is, we return the null value,
which indicates that we have reached the end of the list.

In our example shown, our list is not empty, so we continue on.

[slide 6]

Next, we check to see if current is equal to null. If it is, we have either just
used the reset operation, or our last call to getNext reached the end of the
list and returned null.

In either case, we reset current to point to the first node of the list.

In our example, we have set current to point to node "c", the first node in the
list.

[slide 7]

If current is not null, we simply set current to current.next, or the next node
in the list. If we get to the end of the list, current.next will point to null
and thus the calling function will know that we've reach the end of the list
when the null value is returned.

In the example, if current is pointing at node "x" as shown, if we executed this
statement …

[slide 8]

we would update current to point to node "a".

[slide 9]

Once we have updated current, we need to return the data at the node where
current is pointing. However, if current does have a null value, we simply
return null indicating that we are at the end of the list.

[slide 10]

However, under normal circumstances, when current is pointing at a node in the
list, we return the data from the node to the calling function.

In the example shown where current is pointing at node "a", we would return the
value "a" to the calling function.

[slide 11]

The iterator itself provides the user access to the data in the list. However,
in order for users to manipulate the list, we also need to provide them
additional basic operations. These operations mirror the basic list operations
such as getPrevious, removeCurrent, replaceCurrent, and insertCurrent.

In this video, we will look at the removeCurrent, where we want to remove the
current node from the list. Other operations will be similar.

[slide 12]

The first thing we do is to check our precondition, which ensures that the list
is not empty.

[slide 13]

If we've satisfied our precondition, the first step in the removeCurrent process
is to actually remove the current node from the list. There are two cases to
consider based on whether the current node is the first node in the list or not.
If it's not the first node, meaning that current.previous is not null, then we
set previous node's next pointer to point at the next node. Of course, if
current is the first node in the list, then we simply set head to point at the
next node after current.

[slide 14]

In our example, since current is not the first node in the list, we set
current.previous.next to current.next as shown.

[slide 15]

Next, we set the previous pointer of the next node in the list to point to the
previous node in the list. Of course, if current.next is null, that means we are
at the end of the list and we just need to update the tail pointer.

[slide 16]

In our example, since we are not at the end of the list, we set
current.next.previous to current.previous, which effectively removes current
from the list.

[slide 17]

Finally, we do a little cleanup by setting current to point at the next node in
the list and decrementing the size variable.

[slide 18]

So now that we have an iterator and at least one operation that works
hand-in-hand with the iterator operations, let's see what a user could do with
that. Suppose the user needed to remove all data of a specific value from the
list. Using the iterator and the removeCurrent operations, we could use the
deleteAll operation to accomplish our needs without making any changes to the
linked list class.

[slide 19]

Let's assume we call deleteAll with the list shown and the data value "x". The
first line resets current to null while the second line updates current to point
at the first node in the list and returns the data there, "c", which is stored
in listData.

[slide 20]

Then, we enter our while loop where we search for data matching "x". We stay in
the while loop until we reach the end of the list.

[slide 21]

For each node in the list, we check to see if listData matches the data we are
seeking to remove, in this case "x". If it does, we call removeCurrent to delete
that node from the list. We then call getNext to retrieve the data from the next
node in the list.

[slide 22]

In the first trip through the loop in our example, the value of listData is not
equal to "x", so we call getNext, which modifies current to point to node "x"
and returns the data "x" to be stored in listData.

[slide 23]

The next time through the loop, listData is "x" and it matches the data we're
looking to remove, so we call removeCurrrent.

[slide 24]

The removeCurrent operation removes node "x" from the list as we described above
and sets current back to node "a".

[slide 25]

We then call getNext, which updates current to point at node "w".

In all, we must go through the loop three more times, although we won’t have to
remove any more nodes. The loop ends when we reach the end of the list and the
getNext operation returns null. At this point we are done with the deleteAll
function.

[slide 26]

In this video, we introduced a list iterator for our doubly linked list class.
While we did not include all the useful operations that we might need, we did
present the basic functions reset and getNext, which allows users of our list to
iterate over it without having to know the list’s internal structure. We also
showed how to create operations such as removeCurrent that work hand-in-hand
with the iterator. These additional operations allow users to write application
specific functions such as deleteAll. On the whole, iterators are extremely
useful and provide handy mechanisms that let users extend our list's
functionality.
