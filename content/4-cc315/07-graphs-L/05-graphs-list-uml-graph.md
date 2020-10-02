---
title: "List Graph UML"
pre: "5. "
weight: 75
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-CC315/07-graphs-L/05-graphs-list-uml-graph-slides.md" >}})

#### Video Script

[Slide 1]

In this video, we will discuss the list graph class. Previously we have outlined the graph node class which our list graph will utilize. We will start with the attributes.  

[Slide 2]

The first attribute is nodes. This will be an array of graph nodes with a fixed length. The second attribute is size, which represents the number of nodes currently in our graph. 

[Slide 3]

Upon initialization, nodes will be set to an empty array of length capacity and size will be set to zero. 


[Slide 4]

For the next portion of the video, we will discuss the getters.


[Slide 5]

First we have get nodes. This will return a list of the nodes with their respective indexes. Here we will use the same logic as we did with the matrix graph. The difference is that instead of the items being stored directly in the index, the item will be stored in the graph node in the index. 

[Slide 6]

Next we have get edges. The functionality will be the same but we will need to implement it differently. We still want to return a list of the edges in the format (source, target, weight).

We initialize an empty list then loop through the nodes attribute. If the entry is not empty, then we will go through each edge in edges. The source for each of these edges will be the index of the node that we are currently accessing. The target will be the first entry in the edge and the weight will be the second entry in the edge. 


[Slide 7]

Next we have get node and find node. Again, these are comparable to the methods that we had in the matrix graph. 

Get node returns the node with the given index. If the index is within the possible range, then we return the value of that node. 

Find node returns the index of the given node. We iterate through our nodes and if we find that value, then we return the index. Otherwise, return `-1`. 


[Slide 8]

Now we have get edge which takes a source node index and a target node index as input. We will return the weight of the edge between the given nodes. If one or both of the indexes are out of range, then we should return infinity. From the source node object, we will call the graph node get edge function on the target index. 


[Slide 9]

Similar to our matrix graph implementation, we will have get capacity and get size. 

Get capacity will return the number of nodes we are allowed to have. Upon initialization, we will have a fixed number of possible nodes in our node array. We can simply return the size of this array. 

Get size will return the size attribute, which corresponds to the number of nodes actively in our graph.


[Slide 10]

Next we have the get number of edges function which will return the number of edges currently in the graph. To do this, we loop through each of our nodes. If our node is not empty, we access the edges attribute of our node and for each edge, we increment the counter.

[Slide 11]

The get neighbors function will return the list of ordered pairs that corresponds to target indexes and weights, for a given source node. The list representation has a slight advantage here as we already are storing our nodes neighbors in this way! If the node is not empty, then we will simply return the edges attribute. 


[Slide 12]

The remaining functions we will talk about in this video cover adding and removing nodes and edges. 

[Slide 13]

First, we have add node. This will add a node to the graph with the given value if our graph still has room. 

Finding a location for the node will be the same procedure as the matrix graph. If we find an open spot to add the node, we will instantiate a new graph node and insert it into the `nodes` attribute. 

We increment the size if we in the case that we add the node. We will return the index as an indicator of success or failure. 

[Slide 14]

To remove a node, we will take the nodes index as input. We access that node in our nodes array and proceed, assuming it is not already empty. We will set the node to be empty and this will clear all of the outgoing edges. 

To clear the potential incoming edges,  we must loop through the other nodes removing any possible incoming edges. To do this, we can utilize the graph node remove edge function.


[Slide 15]

To add an edge, we will take the index of the source and target as well as the weight. This function will add an edge with the given weight which goes from the source node to the target node. 

To do so, we check that both the source and target index are within the proper range and then access the source node. If the source node is not empty, we will call the graph node add edge function with the target index and weight as input. 


[Slide 16]

Removing and edge will follow the same procedure as adding an edge. First, we check the input values and check that the node is not empty. Then we will call the  graph node remove edge function from the source node with the target node as input. 

[Slide 17]

Finally, we have the add and remove undirected edge functions. As with the matrix implementation, the add undirected edge function will add two edges, one from node one to node two and the other from node two to node one. If adding either of these edges return false, we want the entire function to return false. 

We have a similar procedure for the remove undirected edge function. We call the remove edge function in both directions and return false if either of them fail. 


[Slide 18]

That concludes the UML diagram for the list implementation for graphs. One of the big differences for the list graph is how we access edges. It is important to remember that each node keeps track of its own outgoing edges. We will finish this module with a project then continue working with graphs and their algorithms in the next module. 