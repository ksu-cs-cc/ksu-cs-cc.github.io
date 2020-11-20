---
title: "Graphs"
pre: "3. "
weight: 123
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/12-Performance/03-Performance-graphs-slides.md" >}})

#### Video Script

[Slide 1]

In this video we will discuss the performance of graphs. For the basic operations we will look at the four operations on nodes and edges for both list graphs and matrix graphs. 

[Slide 2A]

To insert a node, we can do this in constant time. We can just add the node right to the array of nodes for either implementation. 

[Slide 2B]

Inserting a node will be linear with respect to the number of nodes. In our algorithm for inserting, in both cases, we looped through the nodes array and put the node in the first empty place. At most, we would have to loop to the end of the array to be able to insert it or find out that we have run out of space in our array. 


[Slide 3]

If we are given the index of the node, then we can access the node in constant time in both implementations. Our nodes are tracked in an array which allows us to access by index quite easily

[Slide 4]

Finding a node will take linear time withe respect to the number of nodes. We would iterate through our nodes array in either implementation and check the item of each nodes. 


[Slide 5]

Deleting a node will also run in linear time with respect to the number of nodes. Given the index, we can overwrite the node. However, we must then remove all of the possible incoming edges as well. For both implementations, we would check each node and remove the edge if it was there. 

[Slide 6]

Once we start working with the edges, we start to see some differences between the two implementations. Inserting an edge in a list graph will run in linear time with respect to the number of nodes. We would go to the node object and then check if the edge already exists. If it did we would remove it then add the new edge. If not, we would just add the edge. 

For the matrix implementation, inserting an edge can happen in constant time. Given the two indexes, we would go straight to the entry in our matrix and update it. 

[Slide 7]

Similarly with inserting an edge, accessing an edge in the list graph will be linear with respect the number of nodes and in the matrix graph will be done in constant time. 

[Slide 8]

Again, we have the same principal with removing an edge. It will be linear with respect to the number of nodes for the list graph and constant for the matrix graph. 

[Slide 9]

Rather than finding an edge, we will look at finding neighbors. Finding the neighbors in a list graph happens in constant time. We can simply return the edges attribute for that particular node. For the matrix graph, we would have to iterate through the row in our matrix that corresponds to the node. This would take linear time with respect to the number of nodes. 

[Slide 10]

Throughout our discussions of list graph versus matrix graph, we have often talked about the space requirements. The rule of thumb was that for sparse graphs, the list graph was better and for dense graphs, the matrix graph was better. The required space for the list graph is on the order of the sum of the number of nodes and the number of edges. The required space for the matrix graph will always be n squared, regardless of how many edges we have. 
