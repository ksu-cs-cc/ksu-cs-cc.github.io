---
title: "Binary Trees Traversals"
pre: "3. "
weight: 53
date: 2019-02-04T10:53:26-05:00
---

{{< youtube En7FDq5XrsA >}}

#### Resources
* [Slides]({{< relref "/4-CC315/05-binarytree/03-binary-trees-traversal-slides.md" >}})

#### Video Script

[Slide 1]

As we talked about in the basic trees module, we want to be able to transfer trees into a linear representation. In that module, we introduced two types of traversal, the preorder traversal and postorder traversal. We stressed the point that since the children of the nodes have no defined order, these traversals can result in different strings. Since binary trees have a defined order, this is no longer the case! 


[Slide 2]

For binary trees, we can be more specific about the definitions. For the preorder traversal, we will access the root then call the preorder traversal on the left child and then call the preorder traversal on the right child. 


[Slide 3]

For the postorder traversal, we will call the postorder traversal on the left child, then call the postorder traversal on the right child and then access the root. We will look at some examples now. 


[Slide 4]

For this binary tree, these will be the unique traversals. For generic trees, these traversals could result in many different strings. 


[Slide 5]

For binary trees, the principle of the traversals is the same. The prefix of the traversal always refers to the root. So for the preorder traversal, the root comes first then the left child followed by the right child. For the postorder traversal, the root comes after the left and right children. In the next video, we will discuss a new type of traversal that we can apply to binary trees. 