---
title: "Binary Trees Insert Elements"
pre: "6. "
weight: 56
date: 2019-02-04T10:53:26-05:00
---

{{< youtube En7FDq5XrsA >}}

#### Resources
* [Slides]({{< relref "/4-CC315/05-binarytree/06-binary-trees-insert-slides.md" >}})

#### Video Script

[Slide 1]

We will now look at how to insert values into our binary tree. When inserting elements, we must make sure we maintain the order in our tree. Remember, left descendants must be less than the node and right descendants must be greater. 

For example, suppose we have this tree and we want to insert the value 45. We would start at the root. 45 is less than 80, so we traverse left. 


[Slide 2]

45 is greater than 40 so we traverse right from node 40


[Slide 3]

45 is less than 60 so we traverse left from node 60


[Slide 4]

45 is less than 50 so we would traverse left from node 50. There is no child to traverse to so we would create the node and build the connection.


[Slide 5]

We would get the following tree. We have created a node with item 45, made its parent node 50 and made it a child of node 50. And that completes inserting a value. 


[Slide 6]

Here is the pseudocode for inserting a value. As with other algorithms, we will walk through this bit by bit. 


[Slide 7]

The first case that we have is if the current nodes item is equal to the value that we are trying to insert. In this case, we would simply return false as this means the value was already in our binary tree. 

[Slide 8]

Next is the case that the current nodes item is greater than the value we are trying to insert. We get the left child of the current node. If it is none, then we call the insert function from that node on value. If the left child is none, then we are at the end of our traversal and can insert the value. We create a node with its item equal to value, add it as a child using the MyTree method, and finally set the left child of the current node equal to the new node we created. 


[Slide 9]

Finally, we have the case that the current nodes item is less than the value we are trying to insert. We follow the same procedure as with the greater than case but with respect to the right child. 