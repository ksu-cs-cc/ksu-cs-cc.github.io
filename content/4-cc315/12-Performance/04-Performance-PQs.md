---
title: "Priority Queues"
pre: "4. "
weight: 124
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/12-Performance/04-Performance-PQs-slides.md" >}})

#### Video Script

[Slide 1]

In this video we will discuss the performance of priority queues. For the basic operations we will look at insert, access minimum, find, delete minimum, and heapify. In the context of a priority queue, it does not make sense to access or remove an element other than the minimum element. An equivalent analysis can be done for a maximum priority queue where we remove the max and access the max. The running times will be the same. 

[Slide 2]

Inserting into a priority queue will run in logarithmic time with respect to the number of nodes. This was done in code by putting the element at the end and then pushing it up through the priority queue. The largest number of recursive calls that we may have to make is equal to the height of the priority queue. Since the priority queue is built in a very regimented way, this is guaranteed to be logarithmic with respect to the number of nodes. 

[Slide 3]

Since the minimum will always be the first element of our priority queue, we can access it in constant time. Similarly in a maximum priority queue, accessing the maximum will be constant time. 

[Slide 4]

To find an element in our priority queue will take linear time with respect to the number of elements. This is the case where we are looking for a particular element to see if it is even in the queue. Since the priority queue is sorted based on priority, not element, we will have to look at all of the elements. 

[Slide 5]

To remove the minimum, we remove the first element of our priority queue. Then we need to restructure to maintain the heap property. While the removal is in constant time, the restructure will be logarithmic with respect to the number of elements. 

[Slide 6]

We want to look at heapify as it is quite efficient since we are using the push down method. Doing some mathematical analysis, we can prove that this will run in linear time with respect to the number of elements. The actual proving of this fact is beyond the expectations of this course. 


[Slide 7]

The memory required for a priority queue is linear with respect to the number of elements, very much like the memory required for trees. Each ordered pair takes up constant space and we have n elements, thus it is linear with respect to the number of elements.