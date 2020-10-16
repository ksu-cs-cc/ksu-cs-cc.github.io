---
title: "Graph Traversal BFS"
pre: "3. "
weight: 83
date: 2019-02-04T10:53:26-05:00
---

{{< youtube FViSRGbGn54 >}}

#### Resources
* [Slides]({{< relref "/4-cc315/08-graph-traversal/03-graph-traversals-BFS-slides.md" >}})

#### Video Script

[Slide 1]

In this video, we will introduce the second traversal for graphs, the breadth first traversal. We will go over the pseudocode and go through a thorough example. With both the depth first and breadth first traversals, we can define the algorithms iteratively or recursively. For this course, we will use the iterative algorithm. 

[Slide 2]

Here we have the pseudocode for the iterative breadth first traversal. We take the graph and a source node as input. 

[Slide 3]

In the breadth first traversal, we use a queue to track which node we will visit next. We will still have a set called discovered to track which nodes we have already traversed. We start by adding the source node to discovered and enqueue the value. 

[Slide 4]

While the queue still has elements, we will dequeue the first element and get its neighbors. We loop through each of the neighbors and if it hasn't been discovered, then we will add it to discovered and enqueue it. 

[Slide 5]

This is a point which differs from the depth first search. Before enqueuing the neighbor, we check that it has already not been discovered. In the depth first traversal, we pushed the neighbors and then checked if they had been discovered after we pop them. Let's walk through an example. 

[Slide 6]

We will use the same graph that we used for the depth first search. We have the graph on the left and on the right is the queue, the set of discovered nodes, the current node, and its neighbors. 

With both traversals, the user must select a node to start at. As with the depth first search we will start at node 1. 

[Slide 7]

Node 1 is our source node, so we enqueue it and add it to the set of discovered nodes. Then we start the while loop to go through the queue

[Slide 8]

We dequeue one//
and get its neighbors. 

[Slide 10]

Since none of the neighbors have been discovered yet, we enqueue each of the values and add the to the set of discovered nodes. 


[Slide 11]

Then we are back at the start of our while loop. We will dequeue the first element for our next iteration. 

[Slide 12]

The next value is 2//
and we get its neighbors, which are one, three, and six.

[Slide 14]

Node one has already been discovered so we won't enqueue it. Nodes three and six will be enqueued and added to the set of discovered nodes. 

[Slide 15]

Then we are back at the top of the while loop. Here is a good place to pause and try to work out the next loop yourself. What will the next current node be? What are its neighbors? What will we enqueue and what will we discover? 

[Slide 16]

The next node we visit is four. Its neighbors are nodes one, seven and eight. 

[Slide 17]

Since we have already discovered node one, we will do nothing with it. We will enqueue nodes seven and eight as well as put them in the discovered set. 

[Slide 18]

We are back at the top of our while loop.//
I have included the pseudocode here as a reminder.  Again, it would be good to pause the video and try to complete the traversal on your own. 

[Slide 20]

The next node we visit is 5 which has neighbors one and nine. //
Node one has already been discovered so we don't enqueue it. We enqueue node nine and add it to the set of discovered nodes. 

[Slide 22]

At this point, we can visually confirm have discovered all of the nodes. Based on the algorithm, we will continue until the queue is empty. 

[Slide 23]

We dequeue three which has neighbors two and six. These have already been discovered so we continue. //
We dequeue 6 and all of its neighbors have been discovered, so we continue. //
We dequeue 7 and all of its neighbors have been discovered//
We dequeue 8 and all of its neighbors have been discovered //

[Slide 27]

Then we dequeue 9 and again all of its neighbors have been discovered//
and our queue is empty signalling the end of the traversal. 

[Slide 29]

Again, these walk-throughs are longer than previous examples, but they are an important tool for us. We have seen many scenarios that can happen and how we handle them. If you want to work through this example, I have included the slides below so you can go through it at your own pace. 
