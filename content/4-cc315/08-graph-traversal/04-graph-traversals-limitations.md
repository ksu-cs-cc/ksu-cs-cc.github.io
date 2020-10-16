---
title: "Graph Traversal Limitations"
pre: "4. "
weight: 84
date: 2019-02-04T10:53:26-05:00
---

{{< youtube sSz7UDs0cH8 >}}

#### Resources
* [Slides]({{< relref "/4-cc315/08-graph-traversal/04-graph-traversals-limitations-slides.md" >}})

#### Video Script

[Slide 1]

In the breadth first and depth first traversal videos, we worked through a graph where all of the components were connected. Recall that when we first introduced graphs, we noted that they were not required to be this way. 

For example, in this graph we have two separate components. The one with A B E and F and the component with C D G and H. 

If we were to call either traversal on this graph from node A, what nodes will we discover? Here it will be just A B E and F. 

What if we called either traversal on C? Then C would be the only node we discover. 

[Slide 2]

Let's look at all the possible starting nodes and which nodes the traversals will discover. 

As we mentioned earlier, starting at node A would result in A, B, E and F. As would B, E and F, since that component is a cycle. 

In the other component, if we started at C, we would only discover C. This is because it has no neighbors. 

If we started at D, we would only find C and D. 

To discover all of the nodes in right component, we would have to start at G. 


[Slide 3]

For general traversals where the goal is to visit all of the nodes, we would need to call the traversal from each node. This will account for nodes with no incoming edges as well as disconnected components. 


[Slide 4]

You may be asking yourself, how does this help us? On their own, the traversals can detect when the graph has nodes that are not connected to the whole. 

The other benefit is that modifying the plain traversals can give us solutions to many problems. We can modify this slightly to solve the maximum flow problem, finding the shortest path, solving mazes and much more. 

In the next video, we will modify the traversals to find paths between two nodes. 