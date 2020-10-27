---
title: "Node Relationships"
pre: "2. "
weight: 102
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/10-PQ/02-PQ-node-relations-slides.md" >}})

#### Video Script


[Slide 1]

In this video we will discuss how we represent heaps in code. While they are a type of tree and further a type of graph, we will not implement heaps using a tree or a graph. 

[Slide 2]

The actual structure of heaps is much more strict than the structure of graphs and even trees, including binary trees. There is a large variety of ways that we can build even a binary tree with just five nodes. 

[Slide 3]

For a heap however, for any number of nodes five or five hundred, there is exactly one way that the nodes will be positioned. The nodes will fill each level before starting a new level and they will fill from left to right. In this example, we have 18 nodes. Any heap with 18 nodes will have this layout. 

[Slide 4]

With this in mind, we will use an array to represent the heap. To do so, we map the nodes in a specific manner into the heap. We work through the heap similar to the pattern for writing in the English language, left to right and top to bottom. Here we have matched the indexes of nodes one through eighteen to their locations in the array. 


[Slide 5]

In the implementation it is important that we are still able to determine a nodes children or parent. In our graph and tree implementations, we typically had pointers for these. Since we have just the array of nodes, we don't have an equivalent pointer. So we may ask ourselves how can we access these? For example, how could we determine which node is the parent of the ninth node? What about its children?


[Slide 6]

Since heaps are constructed in a a very regimented way, we can formulate a mathematical way to determine a nodes parent and children. 

To get the parent, we take the floor of the node index divided by 2. The floor function rounds numbers down to the nearest whole number. 

To get the children, we take the index of the node times two for the left child and two times the index plus one to get the right child. 

[Slide 7]

Suppose we wanted to determine the parent and the children of the node at index seven. Using the formulas, we would get that the parent is node 3, and the children are 14 and 15. Let's do another, then we will double check with the tree. Pause the video and try node 9 for yourself! 

[Slide 8]

For node 9, the parent node would be 4 and the children would be 18 and 19. Let's check this against the tree structure. 

[Slide 9]

Looking that the tree, we can see that this is in fact true. The parent of 7 is 3 and the parent of 9 is 4. We also got the children correct with a slight caveat. The largest node index that we have is 18, thus, node 9 won't actually have a right child. 

[Slide 10]

As an aside, which will prove helpful in the functionality of our heap, we will also discuss this extra fact of heaps. For any heap with n nodes, the nodes with indexes starting at floor of n divided by two plus one through node n, will all be leaves. 

In this example, we have a heap with 18 nodes. By this formulation, it would imply that nodes 10 through 18 are leaves. We can confirm this to ourselves but looking at the tree structure. In the video about functionality, we will discuss where this can really be useful. 

[Slide 11]

For this video, we introduced how we will represent the nodes as an array and how we map the tree structure of the heap into the array. Again, this translation relies on the fact that the heap structure is very regimented, left to right then top to bottom. We also discussed how we would find the parent and children of a particular node. In a future video, we will discuss how we can use that when inserting or removing elements from our heap. In the next video, we will introduce priority queues, which are a specific application of heaps. 