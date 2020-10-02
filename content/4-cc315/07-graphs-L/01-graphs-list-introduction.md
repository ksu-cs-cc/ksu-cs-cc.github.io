---
title: "List Graphs Introduction"
pre: "1. "
weight: 71
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-CC315/07-graphs-L/01-graphs-list-introduction-slides.md" >}})

#### Video Script

[Slide 1]

In this module, we will continue working with the graph data structure. In the last module, we introduced graphs and how we would implement them using matrices. 

We will now introduce a second way to represent the graphs. The basis of this method will be lists.

[Slide 2] 

As we saw in the previous module, graphs can have many shapes, sizes, and attributes. Graphs can be any combination of weighted and directed with many or few nodes as well as any number of edges. With such a great degree of variability the performance of a representation can vary wildly! Lets look at a small motivating example.

[Slide 3]

Suppose we have this graph which has one thousand nodes. Each node has two outgoing edges which go to the next two nodes. So node one has an edge going to node 2 and node 3. Node two has an edge going to node 3 and node 4, and so on. In total, our graph would have about two thousand edges. This graph could represent a control flow where node one is the first step and node one thousand is the last step. In some cases, we can skip a step when moving forward. 

[Slide 4]

If we look at the matrix representation of this graph, we would have a matrix that is one thousand by one thousand. This means that our matrix will have entries for one million potential edges. If our graph will not need to use those edges, then we have wasted a lot of space! In instances like the control flow graph, it is not likely we will add more edges and this will be a fixed structure. Cases like these are not well suited for the matrix representation. Thus we have a need for a new way!

[Slide 5]

This module will discuss the new representation and how it works, why we may use lists over matrices and vice versa, then we will conclude with formal UML and a project. 

