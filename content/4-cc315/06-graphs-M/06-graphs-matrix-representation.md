---
title: "Graphs with Matrix Representation"
pre: "6. "
weight: 66
date: 2019-02-04T10:53:26-05:00
---

{{< youtube Uwd8YkQwoqM >}}

#### Resources
* [Slides]({{< relref "/4-CC315/06-graphs-M/06-graphs-matrix-representation-slides.md" >}})

#### Video Script

[Slide 1]

In this video, we will discuss the premise of the first implementation for graphs as well as work through some examples. We will refer to this implementation as the matrix representation. 

For graphs, we need to track two key features to accurately represent them. We must store both the nodes and the edges. We will store these in separate structures. 

[Slide 2]

We will store the nodes in an array with a fixed size. Now that we have started discussing implementations, we can gain a better understanding of why we need to define the graphs capacity. 

When we initialize a graph, we will declare its capacity. In this example, our graph has size 3 and has capacity 4 as shown by the nodes array. Node A is at index one, node C is at index two, and node D is at index 4. 

[Slide 3]

To characterize the edges, we have an adjacency matrix. This will store the information about which nodes are adjacent to one another. Recall that node A and node D are adjacent of there is an edge from A to D. 

We first initialize all of the entries in our adjacency matrix to be infinity. Thus to start, we illustrate that no nodes are adjacent. Then we go through our graph edge by edge and gather the source and target. 

[Slide 4]

For example, we see an edge that connects nodes A and D. In this edge, node A is the source and node D is the target. 

[Slide 5]

We determine the index of source and the index of the target. So in this case, the source is at index 1 and the target is at index 4.

[Slide 6]

We go to our adjacency matrix at the row of the source and the column of the target. For the edge that connects A to D, we would enter the value 1 in the array in row one column four. 

For unweighted graphs, recall that we treat each edge weight as one. This is the motivation for inserting the value one into that location. 

[Slide 7]

We follow the same process for each of the edges. We have an edge with source C and target A. Thus we input a one in row three column one of our adjacency matrix. 

Take a moment to pause the video to check for understanding. Where will we put a new entry for our adjacency matrix to capture the last edge? What will this value be?

[Slide 8]

The final edge has source D and target C. The entry corresponding to this edge will be in row four column three. Since this edge has no defined weight, we will enter a one in this spot. 


[Slide 9]

When we have a weighted graph, the values in our adjacency matrix will corresponds to the weights. For example, here we have the edge with weight 150 that has source D and target F. Thus we put 150 in row 4 column 6.


[Slide 10]

Another factor we need to consider is directed versus undirected edges. Recall that an undirected edge between node A and B corresponds to an edge from A to B and and edge from B to A. When we have an undirected edge, the weight will show up twice. 

Let's look at the example of the edge with weight 13 that connects A and B. Node A is at index one and B is at index 2. Thus, we insert the value thirteen in row one column 2 as well as row 2 column 1. 


[Slide 11]

An additional consideration is how we handle loops. A loop in a graph is characterized by having the same source and target. This graph has size 4 and capacity 6.

In this example, we have a loop on node F. We could say that this is an undirected edge which connects node F and node F. Thus, we have an entry in row 6 column 6 to correspond to this edge. 


[Slide 12]

In this video, we have introduced the first implementation we will use for graphs. This implementation is twofold in that we have an array for the nodes as well as an adjacency matrix to characterize the edges. We went through various scenarios and how we expect the data structure to behave. Next we will dig into the UML diagram for this implementation of graphs. 