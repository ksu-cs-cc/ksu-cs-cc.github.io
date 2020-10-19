---
title: "Prims Algorithm "
pre: "4. "
weight: 94
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/09-MST/04-MST-prim-slides.md" >}})

#### Video Script

[Slide 1]

In this video, we will look at Prims algorithm for finding a minimum spanning tree. This algorithm takes the graph and a starting node as input. 

[Slide 2]

We start similarly to Kruskals by initializing the minimum spanning tree to be the nodes of the graph. We have a set to track the visited nodes and we add the starting node to it. Then, rather than taking all of the edges, we just get the edges where the starting node is the source. We sort this list then begin the iterative portion. 

[Slide 3]

While we have not visited all of the nodes, we get the smallest edge. If the target of the edge is not yet discovered then we will take the if block. In this block, we add the edge to our minimum spanning tree and add the target node to the set of visited nodes. We get the outgoing edges of the target node and add them to the list of available edges. Once we are done with that, we remove the edge from the list of available edges and then sort it again. We repeat this until all of the nodes have been visited. Let's work through an example. 

[Slide 4]

We will use the same graph that we used in the Kruskal walk through. For Prim's algorithm, we need to input a start node and in this walk through, we will pick node zero. 

[Slide 5]

We initialize our minimum spanning tree to just have the nodes of our input graph. 

[Slide 6]

We initialize the set that will track which nodes we have visited\\
and add the starting node to it. \\
Then we get the available edges. These are the edges for which the start node is the source. \\
Then we sort the list smallest to largest in terms of edge weight.  

[Slide 10]

Then we start the iteration and get the first edge.\\
Since the target, node 2 has not yet been visited, we will take the if block. So we add the edge to our minimum spanning tree, we add the outgoing edges of node 2 to the list of available edges,\\
and then we sort the list. 

[Slide 13]

Now we are back at the top of our loop, and we get the next edge. \\
The target node, node zero has already been visited so we remove it from the list of available edges and move to the next edge.

[Slide 15]

The next edge connects node two to node three. Node three has not been visited yet so we will take the if block. \\
We add the edge to our minimum spanning tree and add node three to the set of visited nodes. We get the outgoing edges of node three and add them to the list of available edges. Finally, we remove the edge from the list of available edges and then sort the edges. 

[Slide 17]

We get the next edge which has source three and target two. Node two is already in our set of visited nodes, so we remove the edge form the list and move on to the next smallest edge. \\
That is the edge which connects node zero and node one. Node one has not been visited yet. \\
We add the edge to our minimum spanning tree and we add node one to the set of visited nodes. Then we get the nodes where node one is the source and add them to the list of available edges. We remove the edge from the list of available edges and then sort the list. 

[Slide 20]

We get the next smallest edge which connects nodes one and zero. Node zero has already been visited, so we move to the next smallest edge. This is a good place to pause and try a few steps for yourself. We are back at the top of the while loop, what will the next edge be, will our set of visited nodes change, will we add edges to our list of available edges?

[Slide 21]

The next edge connects node zero to node three. Node three has already been visited so we remove that edge from the list of available edges and move on to the next edge. In this iteration, the set of visited nodes did not change and we did not add any additional edges. 

[Slide 22]

The next edge connects node three to node zero. Again, zero has already been visited, so we will move on after removing the edge from the list of available edges. This is another good spot to check for understanding. We are at the top of the while loop and we just finished with the edge that connects node three to node zero. What will the next edge be, will we add a node to the set of visited nodes, will we add edges to the list of available edges, will our minimum spanning tree get a new edge? 

[Slide 23]

The next edge connects node three to node five. We have not yet visited node five so we will take the if block. \\
We add the edge to our minimum spanning tree and add node five to the set of visited nodes. Then we add the outgoing edges of node five to the list of available edges, we remove the edge from the list of available edges, and then sort the list. And that finishes that iteration.

[Slide 25]

The next edge connects node five to node three. Node three has already been visited, so we remove the edge from the list and move to the next edge. 

[Slide 26]

The next edge connects node five to node four. We have not yet visited node four, so we take the if block. 

[Slide 27]

We add the node to the set of visited nodes and we add the edge to our minimum spanning tree. Then we add the outgoing edges of node four to the list of available edges. We remove the edge from the list of available edges and then sort the list. We are then at the top of the while loop. 

[Slide 28]

At this point, the set of visited nodes is all of the nodes, and thus we are done so we return our minimum spanning tree. 

[Slide 29]

To conclude this video we will give the informal intuition behind Prims algorithm. 

We choose a random node to start with, and then grow our minimum spanning tree edge by edge. We will pick the smallest edge that can connect a new node to our tree. We repeat that process until we have connected all of the nodes. 

In this video, we have introduced the pseudocode and gone through an example for Prims algorithm as we did in Kruskals algorithm. We will implement both of these in the project for this module. 