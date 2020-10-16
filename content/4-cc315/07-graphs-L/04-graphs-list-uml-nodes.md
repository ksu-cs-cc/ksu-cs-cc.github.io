---
title: "List Graph Node UML"
pre: "4. "
weight: 74
date: 2019-02-04T10:53:26-05:00
---

{{< youtube BVgbAW7NZY8 >}}

#### Resources
* [Slides]({{< relref "/4-CC315/07-graphs-L/04-graphs-list-uml-nodes-slides.md" >}})

#### Video Script

[Slide 1]

As we saw in the examples video, this implementation has an array of node objects. This video will go over the UML diagram for the graph node class. We will start with the attributes. 


[Slide 2]

We have three attributes for our graph node class: Item, Index, and Edges. The Item will be an object which stores whatever the node contains. The Index will be the nodes position in the array. The edges will be a list of ordered pairs such that the node is the source, the first entry is the target node index and the second entry is the weight of the edge as a double. 


[Slide 3]

Next we will discuss the getters. First, we have the basic getters which will return the various attributes of a graph node. These are get item, get index, and get edges. 


[Slide 4]

A slightly more complicated getter is get edge. From the source node, we will call the get edge function with the index of the target node as input. This will return the edge weight.

Since the edges have no guaranteed order, we must loop through each of the entries in the edges attribute. For each edge, we check if the first entry is equal to target index we are looking for. If it is, then we return the weight, which is the second element in the ordered pair. 

[Slide 5]

The last two functions deal with adding and removing edges. 

First we have add edge. This will take the target node and edge weight as input. This method will only be called by the add edge function within the list graph where we will verify that the input parameters are appropriate. 

Once we are in the method, we first call the remove edge function so we eliminate the edge if it already existed. If we skip this step, we could potentially have multiple edges going from the same source and target. 

Then we append the ordered pair with the target index and the edge weight to the edges attribute. 


[Slide 6]

Lastly, we have the remove edge function which takes the target node index as input. As with the add edge function, this will only be called by the remove edge function of the list graph where we will verify that our index is within the appropriate range. 

Once we are in the method, we loop through each of the edges. If we come across an edge ordered pair where the first entry is equal to the target index, then we will remove that edge and return true. If we loop through all of the edges and never come across the target index, we will return false. 

[Slide 7]

That concludes the UML walk through for the Graph Node object. In the next video, we will cover the UML diagram for the list graph object. 