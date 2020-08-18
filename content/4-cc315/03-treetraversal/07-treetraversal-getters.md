---
title: "Getters"
pre: "7. "
weight: 37
date: 2019-02-04T10:53:26-05:00
---

{{< youtube 3mFKHgv6bhk >}}

#### Resources
* [Slides]({{< relref "/4-CC315/03-treetraversal/07-treetraversal-getters-slides.md" >}})

#### Video Script

[Slide 1]

For the next step of our implementation of trees, we will add in some recursive functions. This video will cover the new getter functions for the tree. We have getters for the depth and height of a node as well as getters to retrieve the root and the size of the tree. 


[Slide 2]

First we will discuss the get depth function. Recall that the depth of the root is always zero and as we move away from the root, the depth increases. The base case for this function is if we are at the root, then we return zero. The recursive case returns one plus the depth of the parent. 


[Slide 3]

Next is the get height function. For any node, the height is the longest path to a leaf descendant. Recall that the height of a leaf will always be zero. This will be our base case. Our recursive case will capture the other nodes. 

For the recursive case, we start by setting a maximum tracker equal to zero then get the height for each child of the node. We check if their height is higher than our current maximum and if it is then set the maximum equal to their height. Once we are done with all of the children, we return one plus the maximum. 


[Slide 4]

The next getter function will get the root. The base case will be if we are at the root, then we return the tree. For the recursive case, meaning we are not at the root, we call the get root function on the node's parent. 


[Slide 5]

Our last getter function will get the size of the tree. We define the size of the tree as the number of nodes in our tree. In this case, we are recursively accumulating. We set the size equal to one as we are currently at a node. Then we loop through the children and add their size to our accumulator. 

This concludes the new getter functions for our tree. Next, we will discuss the new functions to determine node relationships. 