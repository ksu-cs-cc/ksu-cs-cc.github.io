---
title: "Binary Trees UML"
pre: "5. "
weight: 55
date: 2019-02-04T10:53:26-05:00
---

{{< youtube En7FDq5XrsA >}}

#### Resources
* [Slides]({{< relref "/4-CC315/05-binarytree/05-binary-trees-uml-slides.md" >}})

#### Video Script

[Slide 1]

Now we will go through the UML diagram for our binary tree implementation. MyBinaryTree will inherit from our MyTree implementation as binary trees are special trees.

Our binary tree will have two attributes, leftChild and rightChild. Each of these will instances of binary trees.


[Slide 2]

Upon initialization, we use the inherited MyTree constructor and initialize the left and right to none. At this moment, we have an empty binary tree. 


[Slide 3]

The is empty function allows us to determine just that, if our binary tree is empty. This checks if the root has a value or not. For example, after initialization, we would return true. 


[Slide 4]

The get size function will override the inherited MyTree get size function. If the tree is empty, we will return zero, otherwise, we will call the MyTree get size function. We modify the get size function in this way as the base case for MyTree was a single node with size one. In the case for binary trees, we can have empty trees so we return zero. 


[Slide 5]

The final function we will cover in this video is to sorted list function. Again, this function will do as it describes: it will return a sorted list. We will do this process recursively by calling the to sorted list function on the left child (the smaller child) then records the roots item and finishes by called the to sorted list function on the right child (the greater child). 

[Slide 6]

That completes the new functions we wil introduce for now. In future videos, you will see how to insert values and remove values along with some supplementary functions. 