---
title: "Relationships"
pre: "8. "
weight: 38
date: 2019-02-04T10:53:26-05:00
---

{{< youtube En7FDq5XrsA >}}

#### Resources
* [Slides]({{< relref "/4-CC315/03-treetraversal/08-treetraversal-relationships-slides.md" >}})

#### Video Script

[Slide 1]

In this video, we will introduce some new functions that will determine the relationship between trees. The relationship will be ancestor, descendant, sibling, lowest common ancestor, and path from root. 

[Slide 2]

The first function is is Ancestor. This function takes `TREE` as input and we are asking is `TREE` an ancestor of this instance. In this function we work down through the tree from the instance until we find `TREE` or we hit a leaf. 

The is ancestor function has two base cases. One is if we are at `TREE` then return true. The other is if we are at a leaf that is not `TREE` then return false. 

Nodes can have many children and just because `TREE` was not down one branch of the instance doesn't mean it is not an ancestor. In the recursive case, we go through all of the children and call the is ancestor function from them with `TREE` as input. If any of those return true, then the function as a whole can return true. If none of them return true, then the function returns false. 


[Slide 3]

We also have the is descendant function which is very similar to the is ancestor function. Now we are asking is `TREE` a descendant of this instance. To implement this, we will work our way up through the tree. 

We have two base cases. The first is if we are at `TREE` then return true as we have found what we are looking for and the other is if we are at the root, then we return false. 

For the recursive case, we call the is descendant function from the parent of our instance with `TREE` as input and return that result. 

[Slide 4]

A sibling is defined as a node that shares a parent node. For this function, we get the parent of our current instance and see if the variable `TREE`is in the parent's children. If it is, then we return true, otherwise return false. 


[Slide 5]

Next we have the lowest common ancestor function. The goal of this function is to find the first ancestor that the two nodes share. This gives us the ability to determine the common ancestry. It is worth noting that all nodes within the same tree will share the root as a common ancestor however this will not always be the lowest. 

This function will take a tree, called `TREE` here, as input and determine the lowest common ancestor of th current instance and `TREE`

This function has three base cases. First, if we are at `TREE` then we return `TREE`. The next base case is if we are at an ancestor of `TREE` then we return the instance. The third base case is if we are at the root. In this case we return None because the root is the first place the nodes' lineages meet. 

For the recursive case, we work up through the instance. So we from the parent node, we call the lowest common ancestor function with `TREE` as input. 


[Slide 6]

Our last new relational function is path from root. This function will do as the name implies and will do it recursively. It will find a path from the root to the node from the bottom up. This function takes a string builder called path as input which we will build incrementally. 

If we are not at the root, then we will call the path from root function on the parent, passing our path variable and essentially going up the tree. Once we reach the root, then we append the items of the nodes which we visited.