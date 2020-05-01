---
title: "Comparing Data Structure Performance"
pre: "2. "
weight: 20
date: 2020-04-24T00:00:26-05:00
---

{{< youtube Zxn0f78fH0w >}}

#### Resources

* [Slides](/3-cc310/12-performance/02-comparing-slides.pptx)

#### Video Script

[slide 2]

Data structures can be analyzed in terms of two performance characteristics: the amount of processing time each operation requires, and the amount of memory required to store the information in the data structure, as well as excess information required for the operations. 

For the data structures we've reviewed in this course, we won't worry about the memory useage for now. In most cases, the memory useage is on the order of N space, where N is the number of elements in the structure. That is pretty consistent for each of these structures. 

So, we are most concerned with the processing time required to perform various operations using the data structure. 

[slide 3]

That performance can be measured in one of two ways. First, we can empirically test it by using the data structure in a variety of ways and measuring how much real-world time is required to perform these operations. That will give us a good idea of how a particular data structure will perform when given a specific task or set of data, but it doesn't tell us much about how the data structure would perform in other instances, nor how it compares to other data structures.

Instead, we can use some mathematical modeling to give us a description of how the data structure performs, usually expressed as a function in terms of N, the number of elements stored in the structure. We've seen this description for most of the data structures in this course, but in this module we want to bring them all together and compare them directly.

[slide 4]

This table shows the performance characteristics for several of the data structures we've looked at in this class. We've chosen four of the most common operations: inserting an element, accessing a single element using the index of that element, finding a specific element in the structure, and then finding and deleting a specific element. We've also shown both the best and worst case performance that can be expected from each of these data structures. In general, these are the same for most operations and most structures, but there are a few unique situations that we'll discuss in more detail. 

[slide 5]

Of course, a mathematical description doesn't help that much if we can't visualize how they relate to one another. This graph shows the commonly used functions to describe the performance of an operation. The x axis across the bottom shows the size of the data structure, and the y axis on the side shows the relative amount of time required to perform the action.

So, for example, an operation that runs on the order of N time would be much slower than an operation that runs on the order of lg (N) time, and that difference becomes greater as the data structure grows in size.

While it is not shown on this graph, we use the function 1 to denote constant time. That means that, as the data structure gets larger, the operation itself should not take any more time to complete. So, the x axis itself is a great reference for a constant time function - it never increases!

The next few videos will discuss the performance characteristics of the data structures we've covered in this class in more detail. 