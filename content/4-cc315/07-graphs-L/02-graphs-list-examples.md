---
title: "List Graphs Examples"
pre: "2. "
weight: 72
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-CC315/07-graphs-L/02-graphs-list-examples-slides.md" >}})

#### Video Script

[Slide 1]

In this video, we will formally introduce the list representation and look at some examples. In this implementation, we will have a new graph node object and a list of those objects. 

[Slide 2]

Conceptually, we will have an array of node objects. Previously in the matrix representation, we had an array where each entry was the item of the node. In this implementation, each entry will entirely encapsulate the node and its edges.

[Slide 3]

The graph node object will contain the item, index, and a list of the edges. 

The item will be what was contained in the node. 

The index will track the position of the node in the array. 

The edges attribute for a node will capture all of the edges for which this node is the source. Entries in the edges attribute will contain ordered pairs where the first entry will be the index of the target node and the second entry will be the weight. Let's work through an example to gain a better understanding.


[Slide 4]

Suppose we have this small graph which has capacity 4 and size 3.

[Slide 5]

In this set up, lets say that node A will correspond ot the first entry, node C will correspond to the third, and node D will be the fourth. 

[Slide 8]

Inside of the graph node object for the first entry, we have all of the information corresponding to node A. We have that the item is 'A' and the index is one. For the edges, node A is the source node for a single edge. This edge goes from node A to node D with weight one. So we have a single ordered pair in our edges attribute where the first element is the target node, D with index 4, and the second entry is the weight, 1. 

[Slide 9]

Our completed list representation would be the following. Each node object has its corresponding item and index along with the edges for which the node is the source. 


[Slide 10]

Now lets look at an example of a weighted graph. As with the matrix implementation, instead of just inserting ones, we will insert the actual weights of the edges. 

[Slide 11]

Let's look at the edge from node D to node E for an example. This edge has weight nine with source node D and target node E. Node E has index five so we have the ordered pair 5 comma 9 in the edges of Node D. 

[Slide 12]

Another interesting node to look at is node E. This node has no outgoing edges and thus it has no entries in its edges attribute. 

[Slide 13]

Another example to look at is undirected edges. Here we have an undirected graph as none of the edges have directions. Recall that this means we can traverse either direction between the nodes. 

[Slide 14]

Let's examine the edge that connects node A and node B with weight 12. We see that the edge is present in both node A with the edge entry 2 comma 12 and in node B with the edge entry 1 comma 12. 

[Slide 15]

The last feature of graphs to cover is loops. Recall that a loop is and edge where the source and target node are the same. In this case, we have a loop on node D with weight one. Thus in the edges for node D, we have the ordered pair 4 comma 1.

[Slide 16]

In this video, we have introduced the second implementation we will use for graphs. We saw that this implementation will still have a list of nodes but rather than having a matrix for the edges, each node will track its own edges. We went through various scenarios and how we expect the data structure to behave. Now that we have the basics of this implementation, we will next compare the two. 