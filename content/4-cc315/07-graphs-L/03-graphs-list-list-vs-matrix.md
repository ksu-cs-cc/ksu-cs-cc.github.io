---
title: "List VS Matrix"
pre: "3. "
weight: 73
date: 2019-02-04T10:53:26-05:00
---

{{< youtube y4bCalShe_Y >}}

#### Resources
* [Slides]({{< relref "/4-CC315/07-graphs-L/03-graphs-list-list-vs-matrix-slides.md" >}})

#### Video Script

[Slide 1]

At this point, we have seen the two implementations in action. This video will offer an analysis on when it may be better to use one over the other. 

In the matrix representation, we have a nodes array and an adjacency matrix. For the list representation, we have a list of node objects where the node objects contain their index, item, and outgoing edges. Let's start by looking at space requirements. 

[Slide 2]

For a graph with N nodes and E edges, the matrix implementation will have an N dimensional array for the nodes and an N by N array for the edges. The list representation will also have an N dimensional array for the nodes however, all of the graph nodes will only take the number of edges times 8 bytes of space. 

This means that the matrix will always have entries for N squared edges and the list will have a variable number of entries. Let's look at where this can impact our performance. 

[Slide 3]

There are two cases we should look at to get an idea of the impacts. Those are sparse and dense graphs. In a graph, the maximum number of possible edges is N squared. 

A sparse graph is a graph in which the number of edges is much lower than the maximum and a dense graph is a graph in which the number of edges is close to the maximum number of edges. 

Here we have an example of each. These graphs have the same number of nodes but vastly different amounts of edges. Recall that an undirected edge counts as two edges. The sparse graph has nine edges and the dense graph has forty edges. For these graphs, the maximum would be sixty four. 

For the sparse graph, the matrix implementation would waste a lot of space, assuming we won't be adding more edges. The list representation will be much more succinct.

For the dense graph, the matrix implementation will have a sufficient amount of space. The list representation, will take more space than the matrix as it is tracking every edge as an ordered pair. 

[Slide 4]

For a rule of thumb with graphs if the proportion edges to the maximum number of edges is greater than one sixty fourth, then it is preferable to use the matrix representation. Space is not the only concern we have when are comparing the two implementations. We also want to consider how often we will be accessing edges. 

[Slide 5]

If we need to quickly access or update edges, then the matrix method is preferred. We can directly access an edge by going to the entry in the matrix. In the list implementation, we would go to the source node and see if the edge was in its edges attribute. If that node has many edges, which are in no particular order, it could take a while to determine if the edge exists. We will discuss further in the UML videos the precise procedure we will use when accessing edges. 

[Slide 6]

In short, the matrix representation is good for dense graphs, meaning there are a lot of edges, as well as graphs where we will be frequently accessing edges. It is important to remember that regardless of how many edges we have, the  matrix implementation will always take up space for the maximum number of edges. The list representation is good for situations where we have sparse graphs in terms of space. However, if we are needing to access and update edges frequently, then the list implementation may not be a good choice. In the next videos, we will see why this is the case as we look at the UML diagram for the list representation.