---
title: "Sets In Code"
pre: "2. "
weight: 20
date: 2020-04-13T00:00:26-05:00
---

{{< youtube qaO4iLtGo4o >}}

#### Resources

* [Slides](/3-cc310/10-sets/02-sets-in-code-slides.pptx)

#### Video Script

[slide 2]

In this video, I want to talk about what it takes to implement basic sets and
set operations in code. There are several different approaches to implementing
sets in code, including arrays and linked lists.

We can use arrays much like we did with stacks or queues, keeping track of the
starting and ending locations in the array of the set elements. Of course,
arrays also have their drawbacks in that they have a limited capacity and we
must explicitly manage that capacity.

[slide 3]

However, in this video, we will implement our set operations on top of a doubly
linked list. Linked lists have several efficient operations that we can use to
implement our set operations, such as append, list iterator, and remove current.

A linked list, as we have seen, is very general and provides much of what we
need.

[slide 4]

The first operation we will look at is the contains operation, which we will use
to define many of the following set operations. The contains operation
determines whether a given object already exists in our set. So, for instance,
to ensure we do not have duplicates in our set, we must first check to see if
the set already contains an object before we can add it to the set.

So, in our set class, we will define an attribute mySet as a linked list.

[slide 5]

We will use a list iterator – as we will in several of the remaining operations
– to walk through the set to find objects of interest.

To start us off, we call the list reset operation to ensure the iterator is
ready, and then call the getNext operation to get the first item in the set.

[slide 6]

The heart of the operation is a while loop. We will stay in the loop until we
reach the end of the set, or in other words, until the object we get from the
getNext operation returns null.

In the contains operation, since we are simply searching for a particular
object, if we find that object, then we return true and the operation ends.
Otherwise we get the next object from the set via the getNext operation and loop
back up to the top.

[slide 7]

Eventually, if we don't find the object, we will walk through the entire loop
and exit when we reach the end. At that point, we declare failure by returning
false.

Obviously, since we have to walk through the set using a while loop, the time
complexity of contains is order N.

[slide 8]

Next, we will look at the add operation. But before we go about adding the
object to our set, we need to enforce the no duplicates rule since our
underlying list data structure does not. Therefore, we first check to see if the
object to be added already exists in the set. If it does, we return false,
indicating that the object was not added to the set.

[slide 9]

If the object does not exist in the set, we then call append to add it to the
set and then return true, indicating that we did in fact add the object to the
set.

You may ask why we use the append operation instead of the prepend operation.
Well, since order doesn't matter in a set, we can actually use either operation
and it will work. I just chose append.

Although we have no loops, and the list append operation runs in constant time,
the use of the contains operation increases our runtime. Since contains runs in
order N time, the add operation will run in order N time as well, since it can’t
run any faster than the operations it calls.

[slide 10]

Next, we need to implement the remove operation, which is designed to remove a
given object from the set. Like the contains operation, we will have to use the
list iterator operations to walk through the list to find the object. So, we
call reset and getNext to retrieve the first object in the list.

[slide 11]

Next, we enter our while loop, which will walk through each object in the set.
The only difference between the contains operation and the remove operation is
what we do when we find the object. In the contains operation we merely returned
true, indicating that we had found the object.

[slide 12]

However, in the remove operation, we add a call to the removeCurrent operation,
which actually removes the object from the list. We then return true indicating
that we found the object and removed it from the list.

The rest of the loop is the same as contains. We get the next object and return
to the top of the loop.

[slide 13]

If we do not find the object, we will again return false indicating that we did
not find the object requested.

Again, since we have a loop that walks through each element in the set, the
remove operation runs in order N time.

[slide 14]

Our next operation is the intersection operation, which takes a set as input,
 and returns the intersection of that set and our current set as a set.

The first thing we need to do is create a new set, result, to hold the elements
in the intersection of mySet and set2. Then, since we will need to walk through
set1, we will use the reset and getNext operations to retrieve the first object,
just like we did in the first two operations.

[slide 15]

Next, we have a loop to walk through each object in mySet. Our strategy will be
to walk through mySet and see if each object in mySet is also in set2. If it is,
we'll add the object to our result set. Once we are done walking through mySet,
we will be done. Thus, the interior of the loop looks much like contains and
remove, except this time, if set2 contains the object from mySet, we add the
object to the result set.

[slide 16]

After the loop ends, we are guaranteed to have found all the objects in the
intersection, so we just return the results set.

Since we loop through each object in mySet, we know we run in at least order N
time. However, we also call set2's contains and add operations, which also run
in order N time. Therefore, each time we go through the loop, the intersection
operation ends up running in N \* 2N, or approximately N squared time.

[slide 17]

When we perform the union operation, we have two sets, mySet and set2, and we
have to include each element from both sets in the union. Here, the obvious
solution is to walk through each set and add each object we find into a new set
called result.

So, like we've done before, we use the list iterator function to walk through
the loop and call the add operation to add each object we find into result. Now
you might be asking, don't we need to check to see if the object already exists
in the result set before we add it. The answer is no because, as you recall, the
add operation already checks to make sure the object is not already in the list.
If we checked before calling add, we would simply be duplicating the call to
contains.

You might also notice that while the add operation returns true or false to
indicate whether the object was actually added or not, we don't look at the
return value. Since the only way it returns false is if the object already
existed in the set, we really don't care, since we just need to make sure the
object is in the set.

[slide 18]

When we complete the loop for mySet, we use the exact same loop structure to walk
through set2 and add all its elements into the result set. Again, we don't care
if the object is already in the list or not.

[slide 19]

Once we get through the second loop, we have added all the elements from mySet
and set2 into our results set and all that is left to do is to return it to the
calling function.

Now, we have two loops, so we run in at least 2N time. However, since we call
set2's add operation each time we go through the loop, which also runs in order
N time, the union operation ends up running in 2N \* N, or approximately N
squared time.

[slide 20]

The final operation we will look at is the isSubset operation. The isSubset
operation checks to see if each object in set2 is also contained in mySet. If it
is, then set2 is a subset of mySet.

Computing the appropriate value is straightforward and follows the same
structure as we've seen in most of the operations. We use a list iterator to
walk through each object in set2. This time, however, we check to see if the
current object is *not* in mySet. If it is not, then we return false to indicate
that set2 is not a subset of mySet.

If we get to the end of the list and fall out of the loop, we then know that
set2 is a subset of mySet and we should return true. Again, since we call the
contains operation, which runs in order N time, within a loop that walks through
each element in a set, the isSubset operation runs in order N time.

[slide 21]

In this video, we showed how we could build a set data structure on top of a
doubly linked list. We found that due to the constraint the we have no
duplicates within a set, the efficiency of our set was not as good, basically
increasing the time for insertion from constant time to order N time. However,
the list iterator operations were extremely useful when implementing operations
like union, intersection, and isSubset operations.
