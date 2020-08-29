---
title: "Binary Trees Remove Elements"
pre: "7. "
weight: 57
date: 2019-02-04T10:53:26-05:00
---

{{< youtube En7FDq5XrsA >}}

#### Resources
* [Slides]({{< relref "/4-CC315/05-binarytree/07-binary-trees-remove-slides.md" >}})

#### Video Script

[Slide 1]

In this video we will discuss how we remove nodes from a binary tree. Since binary trees have a strict order imposed on them, we need to be cautious when eliminating nodes. However, we want to make it as simple as possible. The way that we accomplish this is to replace the node with its smallest right branch descendant.


[Slide 2]

We aren't able to do this for all situations though. We have three distinct types of value removal. First, the simplest is removing a leaf. Next is the case when the node doesn't have a right child. Lastly, when the node dose have a right child. We will go through one of each type to help build our intuition and end with the pseudocode. 


Leaf
---

[Slide 3]

First, we have the case when we are trying to remove a leaf. Let's say we want to remove the value 80 from our binary tree. We would start by calling the remove function from the root and traverse down the tree until we find the value.


[Slide 4]

We are looking for the value 80, which is larger than 70, so we go down the right branch to 100.


[Slide 5]

We go down the left branch of 100 as 80 is less than 100. 


[Slide 6]

Then down the left branch of 90 as 80 is less than 90. Now, we can start the removal process. 


[Slide 7]

Since 80 is a leaf, we change its value to None.


[Slide 8]

From its parent node, we would want to prune its children. Meaning we want to eliminate the reference to the empty node. 


[Slide 9]

So severe the parent to child connection between the node that was formerly 80 and 90.


[Slide 10/11]

And we continue back up the tree checking that the tree is pruned. 

No Right Child
---

[Slide 12]

The next case we want to look at is removing a node with no right child. Recall that the method we are doing the removal with takes the smallest right descendant and replaces the node. So what happens if the node has no right child and only a left child. 

Suppose we wanted to removed node 120 from our binary tree. 


[Slide 13]

We call the remove function from the root for value 120 and traverse down the tree until we find it. 120 is greater than 80, so we traverse right. 


[Slide 14]

120 is less than 130 so we traverse left and we have found it! The node with value 120 only has a left child. So we traverse to the left child.

[Slide 15]

This node is not the smallest as it too has a left child, so we traverse to the left child.

[Slide 16]

Grab its value and hold on to it for later. 


[Slide 17]

Remove 90 from its former node and prune to clean up the old connection.


[Slide 18]

We traverse back up the node with 120.


[Slide 19]

We replace 120 with 90. But we are not finished at this point. Take a moment to check for yourself why we are not done. 

The node with value 90 has a left child with value 100. In binary trees, the left child must be smaller than the node and the right child greater than. 


[Slide 20]

To fix this, we simply shift node 90's left child to its right child. It is worth noting that since we are in this case, node 90 will never have a right child. Recall that we are in the case where the node we are removing only has a left child. 
 

[Slide 21/22]

Then we work our way back up the tree to the root. 


Has Right Child
---

[Slide 23]

Now suppose that we want to remove value 40 from our binary tree. Again, we want to take the smallest value from the right descendants and replace 40 with that value. This will ensure that we are maintaining proper binary tree structure. 


[Slide 24]

We traverse to the node and see that it has two children. This process is the same if the node only had a right child. 


[Slide 25]

Now we traverse down the right to remove the smallest node for our replacement. In essence, we first go down the right branch then go as far left as possible. 


[Slide 26]

We reach a leaf with value 50. 


[Slide 27]

We hold on to the value 50 as that will be our replacement. 


[Slide 28]

We prune old node 50. 


[Slide 29]

And return to the node with value 40. 


[Slide 30]

We replace value 40 with value 50.


[Slide 31]

Then return to the root. 


[Slide 32]

While the premise of this video is to introduce the remove function, we have some intermediate utility functions to introduce. In our last example, we saw the need to remove the smallest value from the tree. We also saw that we needed to prune our tree periodically. 


[Slide 33]

We have two prune functions, one for the right and one for the left. Depending on what child we may have removed, we would call one of these functions. These functions are nearly identical except for that fact that one is for the left child and the other is for the right child. 

Using the prune right child as an example, if the right child has no value, then we remove the right child using the `MyTree` remove child function. This was the function which removed the child from the parents children and the parent from the childs parent attribute. While we have severed the parent to child relationship from the MyTree perspective, the parent node still has the rightchild attribute set to the old node. We set the right childs value to be equal to the former right childs right child. In essence, we are shifting the children up one. 


[Slide 34]

Next we have remove smallest. We utilized this when the node with the value we were removing had a right child. 


[Slide 35]

Once we are in this function, we try to traverse as far left as possible to find the replacement value. So as long as our node has a left child, we continue trying to remove the smallest from that node. Once we have found the smallest, we make sure to clean up after ourselves by pruning. 


[Slide 36]

If our node has no left child, then we have found the smallest value on the right hand side of the node with the value we are removing. We save the item of the smallest node as this will be our replacement. 

If the node with the smallest value has a right child, then we need to repeat the process. This is like finding a replacement for the replacement. 

Otherwise, we eliminate the value from the smallest node and return. The previous function calls either to remove smallest or remove will clean up by pruning. 


[Slide 37]

Now that we have built up the supplementary functions we can get to the main remove function. We will work through this piece by piece.


[Slide 38]

In the else block, we are traversing through the tree to get to the node with the value. If we ever get to a point where say the value is less than our node but the node has no left child then we return false because the value is not in our tree then. 


[Slide 39]

Once we find the value, we break into the three cases we explored. First, if the node is a leaf, we set the items value to none and then the previous recursive calls manage the pruning. 


[Slide 40]

If the node does not have a right child, then we find the smallest value to be a replacement for the value. Then we clean up by pruning the left side. Finally, as we saw in our second example, we have to switch the nodes left child to the right child.


[Slide 41]

Then the last case was that we do have a right child. This could be the case that we have two children or just the right children. We find the smallest value of the left child and have that replace our value. Finally we clean up by pruning the right side. 