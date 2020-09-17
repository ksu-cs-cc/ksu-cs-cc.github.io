---
title: "Node and Edge Functions"
pre: "8. "
weight: 68
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-CC315/06-graphs-M/08-graphs-node-edge-functions-slides.md" >}})

#### Video Script

[Slide 1]

In the previous video, we covered the attributes and getters of our graph implementation. This video will address the remaining functions of adding and removing nodes and edges. 

[Slide 2]

First we have add node. This function will take the node value as input and try to add the node if we have not already filled to our capacity. 

We start by initializing the index to negative one. Then we loop through the nodes attribute of our graph. If the node is already in the nodes attribute, then we return its index. As we are looping, once we encounter an empty space, we will use that as the spot for our new node. We save the index of that spot. 

In this algorithm, we are trying to put the node in the first empty spot. By adding the check that node is empty and the index is still negative one, we can ensure this. For example, if we had two open spots in nodes, we would save the index of the first and keep looping through nodes. Then when we come across the second opening, we will continue since we previously found an index. 

After we go through each of the nodes, we check if we ever found an open spot. If we did, we insert value at that position and we increment the size. Regardless of if we found an opening or not, we will return the index to the user. 

[Slide 3]

Opposite of adding a node, we will now look at removing a node. We now have an added complexity in which we must account for the possible edges connected to the node. 

The user will input the index of the node they want to remove. If that index is within the bounds of our capacity and the nodes attribute at that spot is not empty then we can proceed. We will set that entry in the nodes attribute to be empty and decrement the size by one. 

Next we will go through each of the possible edges and overwrite their entries with infinity. We go through all of the edges where the node could have been the source and all of the edges where the node could have been the target.  Upon completion of that, we return true. 

In the case that the index is out of bounds or the nodes attribute is already empty at that index, we will return false. This will notify the user that we didn't actually remove the node. 


[Slide 4]

Next we will discuss the add edge function. For input, we need the index of the source node, the index of the target node, and the weight of the edge. If both indices are within the range of our capacity, we will go to the entry in the edges attribute that corresponds to source comma target. We will set that equal to the weight and return true. 

If either of the indices are out of bounds, we will return false. 


[Slide 5]

Now we will discuss removing an edge. It is a similar process to adding an edge as we are essentially adding an edge with weight infinity. The user inputs the source node index and the target node index. If both of those are within the bounds of our capacity. We will find the entry in our edges attribute that corresponds to source comma target. If that value is not already infinity, we will set it to infinity and return true.

We will return false in the case that the entry was already infinity or if either of the indices were out of range. 

[Slide 6]

The last two functions we will cover involving adding and removing undirected edges. Recall that an undirected edge is an edge in which we can travel both directions. 

For adding an undirected edge, we will have the user input the index of both of the nodes and the weight of the edge. We will then call add edge twice. First we will add the edge going one direction and then add the edge going in the opposite direction. 

We track the success of the calls with the variable RES because if either add edge fails, we must notify the user. 

[Slide 7]

Finally, we have the remove undirected edge. This is virtually the same as adding an undirected edge. The two differences are that to remove the edge, we don't need the weight and we utilize the remove edge function. 

Again, we make sure that we notify the user if one or both of these fail. 

That concludes the UML for the matrix representation for graphs. In the next module, we will introduce another representation for graphs and discuss some pros and cons of the matrix representation. 