---
title: "Graph Traversal BFS"
pre: "3. "
weight: 83
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/08-graph-traversal/03-graph-traversals-BFS-slides.md" >}})

#### Video Script

[Slide 1]

In this video, we will introduce the second traversal for graphs, the breadth first traversal. We will go over the pseudocode and go through a thorough example. With both the depth first and breadth first traversals, we can define the algorithms iteratively or recursively. For this course, we will use the iterative algorithm. 

[Slide 2]

Here we have the pseudocode for the iterative breadth first traversal. We take the graph and a source node as input. 

[Slide 3]

In the breadth first traversal, we use a queue to track which node we will visit next. We will still have a set called discovered to track which nodes we have already traversed. We start by adding the source node to discovered and enqueue the value. 