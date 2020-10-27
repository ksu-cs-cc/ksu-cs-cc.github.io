---
title: "Introduction"
pre: "1. "
weight: 101
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/10-PQ/01-PQ-introduction-slides.md" >}})

#### Video Script

[Slide 1]

The next data structure that we will introduce is heaps. Heaps are a versatile structure that can be utilized when we are frequently needing to reference the highest or lowest priority item. The term priority can have a variety of interpretations that are up to us to define. Based on the data set, the priority could be time traveled, urgency of tasks, cost, and much more. Specifically in this class, we will focus on graph edge weight. Then we will discuss priority queues which are an application of heaps. 

[Slide 2]

Based on the data and what its respective measure of priority is, we might try to minimize or maximize some value. We can try to minimize time or distance traveled or we could maximize our productivity by ordering a to do list based on how important it is that a task gets done. 

As I mentioned, we will be using heaps primarily on graphs and their edge weights. Most graph algorithms are greedy in nature as they typically want the shortest path, lowest cost, least number of nodes visited, and so on. 

To get a better idea of how this will come into play, let's formally define heaps. 

[Slide 3]

The underlying representation of heaps is a tree such that each node has at most two children with some extra stipulations. The structures must fulfill two additional requirements. 

The first requirement is that nodes will be on a level only if the level above is full. We can also say this as the tree must be as shallow as possible. 

The second requirement is that the nodes are as far left as possible. This means that we won't have any nodes which have right children but not left children as well as the right tree of any given node is not longer than the left tree. 

Let's look at some examples as well as counter-examples. 

[Slide 4]

Here is an example for the first requirement, which was that the tree was as shallow as possible. We can also interpret this as, before we start putting nodes on the next level, we need to fill the current level

[Slide 5]

Here we have another with the intention of stressing that fact that we can have trees with many levels. Again, the key is that we must fill a level before adding nodes to the next. Let's look at a counter example.

[Slide 6]

In this example, we have a tree similar to the one from the previous slide. However, in this example we have nodes on the fifth level even though the fourth level is not full. For this to be a valid heap, we would need for the node with value 89 to have two children. 

[Slide 7]

The second requirement was that the nodes of the tree are as far left as possible. Here is an example of what this can look like. Again, another way to remember this is that a node must have a left child if it has a right child and the right tree of any given node cannot be longer than the left tree. 

[Slide 8]

Again, we will look at a counterexample. In this counterexample, the right tree of node 91 has nodes on the third level. To be a valid heap, with this number of nodes, we would need to restructure it such that node 70 had two children. 

[Slide 9]

Another counterexample is this tree. Here node 32 has a right child but no left child. To be a valid heap, the right child would need to be on the left. 

Up to this point, we have described the structure of heaps but not necessarily how the nodes are ordered. 

[Slide 10]

Between siblings, there is no defined order, unlike in binary trees. For heaps, the only stipulation is on the parent to child relationship. This will depend on the type of heap we are looking at. 

There are two types of heaps that we can utilize. We have a max heap and a min heap. For this course, we will primarily work with a min heap. In a max heap, the parent has greater or equal priority compared to the children. We would use these for tasks which we are trying to maximize an aspect of our data. This implies that the root will always be the greatest value in the tree.

The second type is a min heap, where the parent has a smaller or equal priority compared to the children. We would use these for tasks which we are trying to minimize an aspect of our data. This implies that the root will always be the smallest value in the tree.

[Slide 11]

Let's look at a conceptual example for a max heap. Suppose we work at help desk where we earn commission based on how difficult the bug is to solve. So the harder the problem, the more money we can make! 

We can represent this as a max heap where the value of the nodes represent the commission made for a particular job. To make the most money, we would want to do the most profitable job first. We would access the root element, since it will be the most profitable. 

[Slide 12]

Once completed, we would adjust our heap so we have removed that element and replaced it with the second most profitable job, \\
and so on. Again, there is no defined order for the children like there was in a binary tree. 

[Slide 14]

To finish this video, let's look at a conceptual example for a min heap. Suppose again, we work at a help desk where the priority is to get the fastest jobs done first. Now our nodes can represent the amount of time in minutes that it is estimated to take to solve the problem. Since we are using a min-heap, the smallest element will always be the root. So we would access the root and then do that job. 

[Slide 15]

Then we move on to the next quickest job,\\
and so on. 

[Slide 17]

While these examples are immensely oversimplifying the applications of heaps, they can help us to understand more difficult concepts that we will see. 

In this video we looked at some examples of valid heaps as well as ways heaps can be invalid as well as the two types of heaps that we may encounter. In the next video, we will start discussing how we will represent heaps in code. 

