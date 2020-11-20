---
title: "Trees"
pre: "2. "
weight: 122
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/12-Performance/02-Performance-trees-slides.md" >}})

#### Video Script

[Slide 1]

In this video, we will look at the four basic operations on each of the tree structures as well as discuss the memory required to store each structure. We will start with a general tree. 

[Slide 2]

To give an overview, we expect insert and access to take either constant time or linear time with respect to the number of nodes. We expect find and delete to take linear time with respect to the number of nodes. 

[Slide 3]

The running time for insert is a situational case. In the case that we are inserting an element and we have the parent already, then this will happen in constant time. For example, if we were at node H and wanted to insert node L, this would happen in constant time. 

However, if we were not already at the parent, then we must first find the parent and then do the insert. For example, if we were at the root and we wanted to insert node M as a child of node K, we may have to look at each node to see if it is K. Thus, the worst case running time is linear with respect to the number of nodes for inserting in a tree. 

[Slide 4]

Similar to inserting, accessing depends on where we are in the tree and what we are accessing. If we are at the nodes parent and are trying to access the node, then this will happen in constant time. For example, if we were at node F and wanted to access node I. 

However, if we are not at the parent then we have the same situation as with insert. If we wanted to access node K, then we would potentially have to visit every node until we find it. Thus, the worst case running time is also linear with respect to the number of nodes for accessing. 

[Slide 5]

The worst case scenario for finding an element in a tree is that we have to visit every node until we find it. Thus, the running time will linear with respect to the number of nodes. 

[Slide 6]

If we already have the parent of the node then deleting an element in a tree would be linear with respect to the number of children for the nodes parent. If we weren't at the parent already, finding the parent node will be linear with respect to the number of nodes. Then once we found it, deleting the child would be linear with respect to the number of children. So we can say in this case that removing a node is linear with respect to the number of nodes. 

[Slide 7]

The memory required to store a generic tree will be linear with respect to the number of nodes. 

[Slide 8]

Next, we will look at tries. Tries are rather straightforward in their analysis. Each operation will take linear time with respect to the length of the word. 


[Slide 9]

Any of the four operations on a trie, will be linear with respect to the length of the word. We would start at the root and work our way through the trie. In general, we would start at the root, then traverse our way down the trie from character to character. 

[Slide 10]

The memory required for a trie is slightly more complicated, it will be m times n where m is the length of the longest word and n is the number of words. In the worst case, we have n words that are all length m and they have no prefixes in common. In that case, it may be better to consider another structure. 

[Slide 11]

Like tries, all of the operations will run in the same time. For binary trees they will run logarithmically with respect to the number of nodes or linearly with respect to the number of nodes. This is dependant on if our tree is well balanced or not. 

[Slide 12]

If the tree is balanced then the height of the tree would be approximately log of n. Since binary tree nodes have a strict order imposed, anything that requires searching would take at most log n. However, if the tree is not well balanced, then this could be more like n. 

[Slide 13]

Like generic trees, the memory required for binary trees will be linear with respect to the number of nodes. 


[Slide 14]

That concludes the performance analysis of trees and here we have summarized all of the discussion. It is important when thinking about the requirements of a project or task to also consider these factors and how frequently this tasks will be done. 