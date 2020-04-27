---
title: "Using Hash Tables"
pre: "3. "
weight: 30
date: 2020-04-21T00:00:26-05:00
---

{{< youtube j5TWEWJgJkk >}}

#### Resources

* [Slides](/3-cc310/11-hash-tables/03-using-hash-tables-slides.pptx)

#### Video Script

[slide 2]

Let's look at one interesting use of a hash table - implementing a set! It may sound a bit strange, but it turns out that hash tables are uniquely well suited to handling sets, and are even more efficient than our earlier implementation using linked lists.

[slide 3]

First, we know that hash tables require the keys to be unique anyway. So, if we simply use the keys of the hash table to represent the elements in the set, we've already covered one major requirement!

The second major improvement is that the `containsKey` operation of a hash table runs in constant time in the best case. This is much faster than the order N time that our linked list implementation required. So, many of our set operations are much faster when implemented using a hash table instead of a linked list.

Finally, most of the set operations directly correspond to operations we've already built for our hash table, so the implementation is very straightforward.

In this video, we'll explore some of the code needed to implement a set using a hash table. In that code, we'll use the variable `mySet` to refer to our hash table object.

[slide 4]

First, the contains operation of the set class can be implemented using the `containsKey` operation of our hash table class. This operation runs in constant time in the best case, which is already a vast improvement over our preivous set class. 

[slide 5]

Next, let's look at the `add` operation. Here, we'll simply check to see if the hash table already contains the given element as a key. If so, we can just return `false` since we don't have to add anything to the set. If not, we'll add that element to the hash table and return true. Notice that we are using the object as both the key and the value in our tuple, but we can really use any value as we are only concerned with the keys. 

Once again, this operation runs in constant time in the best case.

[slide 6]

The remove operation is even simpler! All we have to do is call the remove operation of our hash table and provide the element as the key. Then, we can check to see if the hash table's remove operation returned null. If so, that element was not in the table and null was returned, and we should return false. Otherwise, we should return true since the element was removed. This operation also runs in constant time in the best case.

[slide 7]

With those two operations covered, it is very easy to implement other operations such as `intersection` using pretty much the same code we used earlier. Here we are assuming that our hash table implementations have iterator methods, which we didn't discuss but should be easy to visualize. For `intersection`, we just loop through one set's elements, and check to see if they are contained in the other set. If so, we add that element to our output set. 

The biggest difference comes when analyzing this method. When we are using linked lists, this method runs in N * M time, where N is the size of set1 and M is the size of set2. Put another way, for each element in set1, we must look at all elements in set2 to determine if the elements match and should be included in the result.

However, using a hash table to implement our set, the contains method runs in constant time, so the best case performance is on the order of N. This is much faster than before!

[slide 8]

In this video, we looked at how we could use our hash table class to implement a set. By doing so, we discovered that most of the core set operations could be improved to run in constant time. So, by adding a bit more complexity to our implementation, we end up with a much faster and more efficient data structure.

Hopefully this example helps show the performance boost that hash tables can provide when used properly.

