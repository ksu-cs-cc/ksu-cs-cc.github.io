---
title: "Introduction"
pre: "1. "
weight: 121
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/12-Performance/01-Performance-introduction-slides.md" >}})

#### Video Script

[Slide 1]

In this module, we will discuss the performance characteristics of the structures and algorithms that we covered in this course. We will follow as closely as possible to the type of performance analysis we did in CC310. If you recall, we looked at four basic points of functionality of the data structures: Insert, Access, Find, and Delete. We will give a brief overview in this video as to what the goal is for each of these operations. 

[Slide 2]

The first operation was insert. When we talk about inserting an element into the structure, we must take into consideration the structure properties. These can include things like order of children for a tree or maintaining the heap property for a priority queue. 

[SLide 3]

The next operation was access. This can often be data structure specific. For example, in stacks and queues in 310, we needed to access only the top of the stack or front of the queue. Similarly, in the priority queue, we will look at accessing the minimum.


[Slide 4]

The next operation was find. Again, this can be dependant on the data structure as to what the ultimate goal is. This can include finding the neighbors in a graph or finding an element in a priority queue. 

[Slide 5]

Finally, we had the delete operation. Here, we are removing an element from the structure. This encompasses removing the element as well as the clean up that may follow. In a priority queue, this would include restructuring such that the heap property is satisfied. 

[Slide 6]

To analyze the algorithms that we introduced in this course, we will look at the time and space required to complete the algorithm. We will look at the number of operations and the number of executions to analyze the time and we will look at the size of algorithm specific variables to analyze the space. 

Let's get started with the data structure analysis. 