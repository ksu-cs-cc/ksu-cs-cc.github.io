---
title: "Binary Tree Examples"
pre: "2. "
weight: 52
date: 2019-02-04T10:53:26-05:00
---

{{< youtube En7FDq5XrsA >}}

#### Resources
* [Slides]({{< relref "/4-CC315/05-binarytree/02-binary-trees-examples-slides.md" >}})

#### Video Script

[Slide 1]

In the last video we defined binary trees and now we will look at more examples to reinforce this new concept. Recall that binary trees are special instances of trees where each node has at most two children. They also have the property that all of the descendants to the left of a node must be less than itself and all of the descendants to the right of a node must be greater than itself. 


[Slide 2]

Here is our first example. Feel free to pause the video to determine if this is a binary tree or not. When determining if a structure is a binary tree we need to check the criteria on the right. We ask ourselves, is this a tree? Does each node have two or less children? Are all of the left descendants of a node less than the nodes item? Are all of the right descendants of a node greater than the nodes item? 


[Slide 3]

This is in fact a tree. We have a single root, there are no cycles, it is fully connected, and each node has a single parent. This is not a binary tree however. The node with item 45 has three children. In a binary tree, nodes can have at most two children. The other criteria about descendants holds true for almost all of the nodes. Node 45 is a special case as it has three children and for a binary tree there is no 'rule' for a middle child. 


[Slide 4]

Now we have our second example. Again, you can pause here to make the determination for yourself!


[Slide 5]

Like our previous example, this is a tree and unlike our last example, each of the nodes have less than two children. All of the left descendants of each of the nodes are less than the node itself. Most but not all of the right descendants of each node are all greater than the node itself. The node that breaks this is the node with item equal to 31. This node should be down the left branch of the root. 


[Slide 6]

Now we have a third example. Again, you can pause here to make the determination for yourself!


[Slide 7]

While this one looks very different from all of our examples, it is in fact a binary tree. Let's go through each of the criteria. It is a tree and each node has at most two children. The left descendants of each node are less than the nodes item and all of the right descendants of each node are greater than the nodes item. 


[Slide 8]

At this point, we have used the following criteria to verify if structures are binary trees. When we implement our own binary tree, we will use these criteria to create the trees as well, making sure that they preserve these properties. 