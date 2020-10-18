---
title: "Introduction"
pre: "1. "
weight: 91
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/09-MST/01-MST-introduction-slides.md" >}})

#### Video Script

[Slide 1]

For this module, we will continue working with graphs, specifically minimum spanning trees. Finding a minimum spanning tree of an undirected weighted graph will allow us to extract even more information from graphs. There are many applications in which we can benefit from knowing the minimum spanning tree of a graph. Most of those deal with logistics where we are trying to efficiently transfer commodities from one point to others. These commodities include things such as power, water, information, packages, and much more. 

[Slide 2]

As a motivating example, suppose that a telecommunication company wanted to lay fiber optic lines throughout Kansas, such that most town and cities were junctures. They would like to offer fiber internet connections to most Kansans but would like to do it as efficiently as possible. In this setup, the company can lay the line from city to city in a straight-path. In the real world, they would be more methodical about this, laying it in paths which were clear from obstacles. 

[Slide 3]

In this graph, we have about 640 towns and each edge represents the direct path from town to town. This is about two hundred thousand paths to consider for the company! By finding the minimum spanning tree, the company can find the best way to lay the least amount of line while still reaching all of the towns. 

[Slide 4]

Here is an example of what that would look like! If they were to lay the cable according to these connections, then they would minimize the amount of line required and thus lower costs and line maintenance. This minimum spanning tree was generated using the matrix graph implementation from this course and Kruskals algorithm, which we will introduce in this module. 


[Slide 5]
To build up to the definition of a minimum spanning tree, we will start by defining a spanning tree. We will start with a formal definition. 
A spanning tree T of graph G is a graph in which the nodes of T are same as the nodes in T and the edges of T are a subset of the edges of G. 

The edges of T must connect all of the nodes and create no cycles. We can use the term spanning tree as its own mnemonic. 


[Slide 6]

First we have spanning, which means we will visit all of the nodes. Then we have tree, which means that there will be no cycles and each node will only be visited once. Lets look at an example with and undirected and unweighted graph. 

[Slide 7]

Suppose that we have this undirected weighted graph. 

[Slide 8] 

The figure on the right shows four spanning trees of the graph. We see that in each example, each node is visited and there are no cycles. We can go another step to understand why we call these trees. 

[Slide 9]

On the left we have the spanning trees from the previous slide. On the right, we have chosen a node for each of them to be the root. We let gravity take effect and let the nodes fall. We can see visually that each of them are a tree. In each case, we have chosen node C to be the root. We could select any node and we would still see a tree. 

[Slide 10]

Along with seeing examples of spanning trees, it is good to see counterexamples. In the top two counterexamples, we have disconnected components. 

In the top left, we have a component that contains nodes A and B and a component that contains nodes C D and E. 

In the top right, just node E is disconnected from the whole. 

In the bottom two counter examples, we have cycles. For example, in the bottom left, we have the cycle A B C A and in the bottom right, we have the cycle A B E C D A. 


[Slide 11]

In this video, we have introduced spanning trees as a building block to introduce minimum spanning trees. As we move on to minimum spanning trees, it will be important to remember that a spanning tree of a graph contains all of the nodes from the graph and it spans all of the nodes with edges of the original graph. These edges cannot create cycles and must connect all of the components. In the next video, we will introduce minimum spanning trees and how they vary from plain spanning trees. 