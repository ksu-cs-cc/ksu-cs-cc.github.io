---
title: "Kruskals Algorithm"
pre: "3. "
weight: 93
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/09-MST/03-MST-kruskal-slides.md" >}})

#### Video Script

[Slide 1]

In this video, we will walk through Kruskals algorithm. The premise of this algorithm is that we will have sets of nodes which will be contained in the list ALLSETS. Then we go through all of the edges, smallest to largest, and if the source and target are not already in the same set, then we will add the edge to our minimum spanning tree and take the union of their sets. Let's work through a thorough example. 

[Slide 2]

Kruskals algorithm takes just the graph as input. 

[Slide 3]

We start by initializing our minimum spanning tree to be the nodes of the input graph. 

[Slide 4]

We initialize the empty list to hold the sets. \\
Then one by one, we create a set with one node and add them to the list ALLSETS. We do this for each node in our graph. 

[Slide 6]

Then we get all of the edges for the input graph.\\
and we sort them smallest to largest with respect to edge weight. 

[Slide 8]

Now we are prepared to start the actual loop to add edges to our minimum spanning tree. We go through the edges one by one. First we have the edge from node zero to node two with weight one. The source set will be the set that contains zero and the target set will be the set that contains two. 

[Slide 9] 

Since the sets are not equal, we will perform the code in the if block. We create the union set, which will have the elements zero and two. \\
We add it to the list of all sets and remove the source set and target set. Then we add the edge to our minimum spanning tree. 

[Slide 11]

Then we move to the next edge which connects nodes two and zero again with weight 1. Since the target and source set are the same, we don't take the if block. 

[Slide 12]

We continue to the next edge which connects nodes two and three with weight three. The source set is the set which contains zero and two and the target set is the set which contains three. 

[Slide 13]

Since they are different, we take the if block and create the union of the two, which is the set zero, two, and three. \\
We add it to the list of all sets, and remove the source set and target set. Then we add the edge to our minimum spanning tree. 

[Slide 15]

Then we are onto the next edge, which connects three and two with weight three. The source and target sets are the same so we go to the next edge. 

As always, it is good practice to pause the video and take a couple steps for yourself! We are at the next edge and this is a good place to pause. After this iteration, what sets will be in all sets, will we add an edge to our minimum spanning tree? 

[Slide 16]

The next edge connects nodes zero and one which are not in the same set yet. So we will get the union, which is the set zero, two, three, and one and add it to the list of all sets. We will remove the set that contained one and the set that contained zero, two, and three. Then we add the edge to our minimum spanning tree and we are onto the next edge. 

[Slide 17]

This edge connects nodes zero and one, which are already in the same set. So we do nothing and move to the next edge. 

[Slide 18]

The next edge connects zero and three, which are already in the same set. Again, we do nothing and move to the next edge\\
This edge connects three and zero, again, we move to the next edge since these are already in the same set. 

[Slide 20]

The next edge connects three and five which are not in the same set yet. \\
So we get the union of the two sets, which is one, two, three, one, and five. We add it to the list of all sets and remove the target and source sets. We add the edge to our minimum spanning tree. 

[Slide 22]

The next edge connects node five and three. These are already in the same set, so we move to the next edge. 

[Slide 23]

The next edge connects nodes four and five with weight seven. These nodes are not yet in the same set, so we take the if block. 

[Slide 24]

The union set is zero, two, three, one, five, and four. We add it to the list of all sets and remove the source and target sets. Then we would move to the next edge. 

[Slide 25]

While we have completed the minimum spanning tree, our algorithm will continue going through edges until we reach the end of the list. \\


[Slide 27]

Skipping ahead to the end of the loop, the algorithm will return the minimum spanning tree and we are finished! 

[Slide 28]

To conclude this video we will give the informal intuition behind Kruskals algorithm. 

We start by initializing the minimum spanning tree to have the same nodes as the graph. Then we sort all of the graph edges and create the initial sets which contain the single nodes. Then we loop through the edges and if the source and target are in separate sets, we join them and add the edge to our minimum spanning tree. 

In this video, we have introduced the pseudocode and gone through an example for Kruskals algorithm. In the next video, we will do the same for Prims algorithm. 