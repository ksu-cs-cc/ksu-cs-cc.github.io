---
title: "Graph Features and Examples"
pre: "3. "
weight: 63
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-CC315/06-graphs-M/03-graphs-features-examples-slides.md" >}})

#### Video Script

[Slide 1]

In this video, we will discuss two new features of graphs. These two features give graphs more functionality again compared to trees. The first we will discuss are loops 


[Slide 2]

A loop is depicted as an edge that starts at a node and ends at that same node. Here is an example of a graph with a single node that has a loop. 

Loops can help us depict real world processes, such as the control flow in a program. However, not all processes will be appropriate for loops.  


[Slide 3]

For example, a graph with loops can be used to represent a rudimentary security system. Suppose we start in the 'unlocked' node. Edge A would represent no action on the users part and the device will remain unlocked until the user takes action. Edge B would represent if the user indicated that they wanted the system lock the device and C would represent unlocking. Edge D would represent no action on the users part and the device would remain locked until the user or adversary took action. Edge E would be if an adversary attempted to access the device and we would be in the Alert node. 


[Slide 4]

Another functionality of graphs is that they do not have to be connected. Here we have a graph with 5 nodes where three of them are connected and two of them are not. Graphs can have nodes and clusters of nodes that are not connected to the whole. 

This feature of graphs is especially useful when we are depicting person to person relationships, travel routes, and much more. 


[Slide 5]

Lets look at an example of a graph that is disconnected and represents travel routes. Suppose we have this graph where each node is a state and each edge represents a land border between the states. 

You may notice here that our edges do not have arrowheads. We will discuss this style of graph more in a future video. In the context of this graph, the edge shows that Washington has a border with Idaho and Idaho has a border with Washington.

There is no state in the US that shares a land border with Hawaii or Alaska. This is considered a single graph which show a particular relationship between nodes. 



[Slide 6]

In this video, we have covered two additional features of graphs. Graphs can have any number of loops and any number of disconnected portions. In the next section of the module, we will discuss two specific types of graphs that we may utilize as well as their applications. 