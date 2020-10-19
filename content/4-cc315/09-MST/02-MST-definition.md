---
title: "MST Definition"
pre: "2. "
weight: 92
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/09-MST/02-MST-definition-slides.md" >}})

#### Video Script

[Slide 1]

In the previous video, we outlined spanning trees of a graph. As a quick recap, these were trees which had the same nodes as the graph and the edges of the tree were a subset of the edges of the graph. To be a tree, these edges could not create cycles and all components had to be connected. 

[Slide 2]

We will now add to the definition to define a minimum spanning tree. A minimum spanning tree of a graph is a spanning tree in which the cost of the tree is smallest that is possible. In order to understand what this means, we must define the cost of a spanning tree.

[Slide 3]

The cost of a spanning tree, and more generally any graph, is the sum of it edge weights. For example, consider these spanning trees from the previous video. We can calculate their weights by adding up the edges. 

For example in the top left, we have 2 plus 3 plus 6 plus 7 to give us 18.

Again, these were the examples of spanning trees from the last video and do not represent all of the possible spanning trees. As such, the actual minimum spanning tree for this graph is not present in these examples. 

[Slide 4]

Here we have the actual minimum spanning tree for our graph. This spanning tree has cost 12. We will introduce two formal methods for finding a minimum spanning tree in a future video. For now, we can build intuition on how we might go about it. 

[Slide 5]

We have the graph on the left and the start of the minimum spanning tree on the right. We will start with just the nodes. 

[Slide 6]

Since we want a minimum spanning tree, we can select the smallest edge, which has weight one. We will put it in our minimum spanning tree. Then we find the next smallest edge. 

[Slide 7]

The next smallest is the edge with weight two and we can add it to our minimum spanning tree. Using the coloring scheme, we see that we have three separate components at this point, so we definitely aren't finished yet. We find the next smallest edge.

[Slide 8]

This is the edge with weight 3. We will add it to our minimum spanning tree. 

[Slide 9]

By adding that edge, we merge the light purple and dark purple and we now just have two components left. Then we get the next smallest edge. 

[Slide 10]

The next smallest is the edge with weight 5 that connects nodes A and B. However, nodes A and B are already in the same component, the dark purple component. Thus, we do not add this edge as it would create a cycle in our minimum spanning tree. 

[Slide 11]

The next smallest edge has weight 6 and connects nodes C and E. We will add it to our minimum spanning tree and we have finished!

[Slide 12]

We have visited all of the nodes and avoided cycles as well as disconnected components. 

[Slide 13]

The intention of this video is to help us build intuition on how we might go about finding a minimum spanning tree as well as formally defining them. To recap, a minimum spanning tree is a spanning tree with the smallest possible cost. In the next videos, we will introduce algorithms to formally find a minimum spanning tree for a graph. 