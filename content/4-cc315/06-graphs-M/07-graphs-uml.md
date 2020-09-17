---
title: "Graphs UML"
pre: "7. "
weight: 67
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-CC315/06-graphs-M/07-graphs-uml-slides.md" >}})

#### Video Script

[Slide 1]

Now that we understand how the matrix representation should work, we will work through the UML diagram. 

[Slide 2]

First we will discuss the attributes of the MyMatrixGraph class. We have nodes, edges, and size. 

For our graph, we want to leave type of data to be stored open for our user. We see this in the nodes attribute where we have an array of objects. 

For the edges, we will use a two dimensional array of doubles to track the weights. 

We will keep track of the size of the graph using an integer. Recall that the size is the number of instantiated nodes. 


[Slide 3]

When we initialize our matrix graph, we will input the capacity. This will be the maximum number of nodes that our graph can contain. 

Initially, the size of our graph will be zero as we don't have any nodes to begin with. 

We will initialize an empty array with the dimension equal to the capacity that the user defined. 

We will initialize a two dimensional array for the edges. This will be a square matrix with the number of rows and columns equal to the capacity. 


[Slide 4]

We will now discuss the getters for this implementation. 

[Slide 5]

The first getter is get nodes. The purpose of this function is to get all of the nodes that currently make up our graph. To do this, we will loop through the nodes attribute and append the value index pair to a list. We will return that list. 

For example, if we called the get nodes function on a graph with these nodes, we would expect the following. As we looped through the nodes, we checked if it had a value. Starting at index one, we have no value, so we continue to the second index and we have a value. Thus we append the pair B comma two to our list. We would continue in that style. 

[Slide 6]

Next is getting all of the edges. The goal for this function is to return triples which have the source node index, the target node index, and the weight of the edge. We loop through the rows and columns of the edges attribute of the graph if the entry is not infinity then we add to our list. Our list will have all of the triples that correspond to edges. 

For example, if we start in the first row, the first column has infinity so we would move to the next column. Column two has the value 13, so we append one comma two comma thirteen to our list. We would continue to work through the edges attribute in that way.

[Slide 7]

The next getter is to get a single node. For this function, we will call get node with an index value. We would then access the nodes attribute at that index and return the node value that is present. 

[Slide 8]

The converse getter function is find node. Here, the input is a node. We would loop through the nodes attribute of the graph and return the index where the node occurs. If the node is not present in our nodes attribute then we would return negative one. 


[Slide 9]

Next we have the get edge function. The input for this will be the index of the source node and the index of the target node. If these indexes are not within the range of our capacity, we will return infinity. If they are both within the bounds of our capacity, then we will access the edges attribute at spot source comma target. We will return the value that is present in that location. 

[Slide 10]

We have two getters related to the number of nodes: get size and get capacity. For get size, we will simply return the size attribute. For get capacity, we can return the dimension of the nodes attribute. As a reminder, the size is the number of nodes currently in the graph and the capacity is the maximum number of nodes we can have in our graph. 

[Slide 11]

The next getter is get number of edges. In this function, similar to the get edges function, we will iterate through the edges attribute. Rather than appending the triples to a list though, we will simply count how many edges appear. For example, we would expect this function to return 10 for this graphs edges attribute. 

[Slide 12]

The last getter is get neighbors. Recall that neighbors of a source node are nodes in which there is an edge from the source to them. For this function, we will input the index of the node for which we want to get the neighbors. We will return a list of ordered pairs with the target node and the weight of the edge. 

To do this, we will go to the row that corresponds to the index from the user input. We will go through that row column by column and when we find entire that are not infinity, we will append the column index and the value. 

For this graphs edges attribute, if we called get neighbors for index 2, we would expect it to return one comma thirteen and three comma four. 


[Slide 13]

In this video, we have discussed the various attributes and getter functions of the matrix representation of graphs. In the next video, we will discuss the remaining functions. 