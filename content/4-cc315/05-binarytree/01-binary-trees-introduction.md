---
title: "Binary Trees Introduction"
pre: "1. "
weight: 51
date: 2019-02-04T10:53:26-05:00
---

{{< youtube En7FDq5XrsA >}}

#### Resources
* [Slides]({{< relref "/4-CC315/05-binarytree/01-binary-trees-introduction-slides.md" >}})

#### Video Script

[Slide 1]

For this module, we will look at another special type of tree: binary trees. These types of trees have more constraints on their format and structure. Along with the regular criteria pf being a tree, binary trees must maintain this additional criteria. 

Each node can have at most 2 children. This means that nodes can have zero, one, or two children.

All of the descendants in the left branch of the tree must have items less than the item of the parent. All of the descendants in the right branch of the tree must have items greater than the item of the parent. 

Let's look at some examples. 

[Slide 2]

Here we have a binary tree where the root's item is equal to thirty. The items down the left branch of the root must be less than thirty and those down the right branch must be greater than thirty. 

[Slide 3]

Here we have shaded all of those down the left branch of the root. As mentioned, all of these items should be less than thirty. The non-shaded nodes down the right branch of the root must be greater than 30. Feel free to pause the video and verify this. 


[Slide 4]

These restrictions are not limited to just the root, the criteria must be met for each node. For example, all of the nodes to the left of the node with item 15 must be less than fifteen. 

[Slide 5]

Similarly, all of the nodes down the right of the branch of node 15 must be greater than 15. We have shaded those here. 