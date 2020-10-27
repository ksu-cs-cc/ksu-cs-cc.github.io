---
title: "Priority Queues"
pre: "3. "
weight: 103
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/10-PQ/03-PQ-priority-queues-slides.md" >}})

#### Video Script

[Slide 1]

A natural application of heaps is a priority queue. This is a set of elements that have an associated key. The key corresponds to the priority of the element as defined by the user for the data. Again, these priorities could be based on money, time, edge weight for graphs, and much more.

[Slide 2]

We can use a priority queue to order tasks that need to be done throughout the day. In this example, the higher the priority, the more urgently the job needs done. We can transfer this into a heap. 

[Slide 3]

Based on the previous set of tasks, we have created this heap. 

[Slide 4]

And from the tree structure, we can examine the array that would result. Note that this will not give us a list order to do the tasks. Once we extract the maximum, we will need to reorganize the heap to get the new maximum at the top. 

[Slide 5] 

In applications like work tasks, it is natural to order them from higher priority to lower priority. However, for tasks such as Prim's algorithm it is useful to implement ordering from lower priority to higher priority. Recall that in Prim's, we were repeatedly getting the edge with the smallest weight.

[Slide 6]

Since the root of a min-heap will always be the smallest item, we can easily access it. Again, in code we will be using the array representation. This means that the first element of our array will always be the smallest element. 


[Slide 7]

In this video, we have given an introduction to an application of heaps: priority queues. In the next video, we will look at how we will actually implement priority queues in code. 