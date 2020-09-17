---
title: "Graph Terms"
pre: "2. "
weight: 62
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-CC315/06-graphs-M/02-graphs-terms-slides.md" >}})

#### Video Script

[Slide 1]

Since trees are a type of graph, much of the vocabulary will be the same. For example, nodes will still be depicted a circles and edges will be depicted as lines connecting the nodes. Like trees, nodes can contain virtually anything, numbers, letters, and other data structures. Edges are not limited to just showing parent to child relationships in graphs. 


[Slide 2]

The edges are a key part of graphs which make them more versatile. Edges can show a wide variety of relationships like the connections between computer components, cities, and even people. So we can't simply classify the relationships as parents and children.


[Slide 3]

In a graph, node A is adjacent to node B if there is an edge from node A to node B. The neighbors of a node are all of the nodes which are adjacent to it. 


[Slide 4]

Lets look at an example. Here we have a graph that shows arbitrary connections between some nodes. We would say that node A is adjacent to node C. Note that we cannot say node C is adjacent to node A. There is not an edge that goes from C to A. Nodes B and F have no adjacent nodes as they have no outgoing edges. 


[Slide 5]

The table shown on the right shows the sets of neighbors corresponding to each node.
The neighbors of a node is the set of nodes that are adjacent to that node. Since B and F had no adjacent nodes, their neighbor is the empty set. 


[Slide 6]

When we talk about graphs, there are two terms that we can use to refer to the number of nodes: size and capacity.

The size of the graph refers to the number of nodes currently instantiated in our graph. 

The capacity of a graph is the maximum number of nodes. When we create a new graph, we will initialize it with respect to the maximum number of nodes. This will be a value which is predefined by the user. We will discuss this idea in more detail when we introduce the implementations. 


[Slide 7]

Formally, a cycle is a path in our graph that starts and ends at the same node. In a future module we will discuss how we can detect cycles programmatically. For this module, we will get familiar with the term and how we can identify cycles visually. Recall that to be a tree, we could not have cycles present. Graphs are more flexible in this regard as they do allow for cycles.

[Slide 8]

In this graph, we have two cycles present. The first cycle is A to C to D to A. The second cycle is similar but includes node E, it goes A to C to E to D to A. 

[Slide 9]

In this graph there are no cycles present. We can verify this by brute force at this point. We would go through each node and see if there is a way to start and end at it. For example, if we start at node B, there is no edge that leads out of B. Thus, there won't be a cycle starting at B. We can say the same about node E.

Now if we look at node A, we have three initial options, we can traverse to E, B or C. Nodes B and E have no outgoing edges, so that is the end of those potential paths. After traversing A then C, we now have 4 options, B, D, E, and F. We can continue searching our graph exhaustively in this way. We would also want to check paths starting at nodes C, F, and D. 

As I mentioned, we won't address how to do this programmatically until a later module. It is important to remember that cycles can be present in a graph, unlike in a tree. 


[Slide 10]

In this video, we introduced these key concepts related to graphs. In the next video we will discuss some additional features of graphs that make them distinct from trees. 