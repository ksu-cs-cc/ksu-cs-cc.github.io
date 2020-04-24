---
title: "Linked List Performance"
pre: "4. "
weight: 40
date: 2020-04-24T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/12-performance/04-lists-slides.pptx)

#### Video Script

[slide 2]

Linked Lists are another commonly used data structure, and from the surface it looks like they can do just about anything an array can do. However, arrays and linked lists have vastly different performance characteristics. 

When dealing with an unsorted linked list, the biggest difference between lists and arrays is the speed of accessing a particular element. In an array, we can just use the array index to jump directly to that element in memory. A linked list, however, requires us to iterate from the start or end of the list until we find the element we are searching for. So, instead of that being a constant time access, it runs in the order of N time. 

Thankfully, inserting elements in a linked list is a constant time operation, finding a specific element requires a linear search. 

Finally, finding and removing an element also requires linear search and runs on the order of N time. However, if we use a list iterator, we can eliminate the need for us to iterate through the list twice if we've already found the element, and the removal itself happens in constant time. So, if we are careful about how we use the list's iterator functions, we can perform removals very efficiently. 

[slide 3]

We didn't really discuss sorted linked lists in this course, but let's analyze them just to see what happens. In this case, we now have to be careful to insert any new elements in sorted order, so the insert opeation now runs in the order of N time. 

Unfortunately, we don't see any performance gains from sorting a linked list, because we cannot use binary search effectively. This is because the access time of a linked list is still on the order of N time, so jumping around just isn't possible. 

Overall, sorting a linked list really doesn't make sense from a performance standpoint.

[slide 4]

We also explored how we can use linked lists to implement stacks and queues. Once again, because we are limiting ourselves to adding and removing elements from the ends of the structure, we find that we can do all operations except for searching in constant time! This is a great result, because it means that we can use linked lists effectively to create stacks and queues in our programs. 

In fact, in most programming language libraries, we'll see that the linked list implementation for stacks and queues is preferred since it can have even better performance than an array implementation. 

