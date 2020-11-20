---
title: "Algorithms"
pre: "5. "
weight: 125
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/12-Performance/05-Performance-algs-slides.md" >}})

#### Video Script

[Slide 1]

In this video we will do an analysis of the time and space required for the algorithms that we covered in this course. For the time complexity, we will calculate the expected number of executions. For the space complexity, we will look at the space required for each variable in the algorithm. 

[Slide 2]

First we will look at the tree traversals. In terms of time complexity, this will be linear with respect to the number of nodes. We can reason through this as we will visit each node exactly once. 

The worst case for the amount of space required would be the number of nodes. In any given iteration, we need to keep track of child and nodes children. Child will take constant space and the children will take space equal to the number of children. Thus, the worst case would be that we have a root node and the rest of the nodes are children of that node. 

[Slide 3]

The postorder traversal is the same as the preorder traversal. We visit all of the nodes, so our time complexity is linear with respect to the number of nodes. Again, we just track the children for any given node. Thus, the worst case for the space complexity is also linear with respect to the number of nodes. 

[Slide 4]

If we run either traversal on a binary tree then we can expect our space complexity to be constant. We no longer have to track the variable number of children as we know we will have at most 2 children. 

[Slide 5]

The inorder traversal was only defined on binary trees. The time complexity will be the same as we still have to visit every node. Again, our space complexity will be constant as we don't have to worry about tracking the children. 

[Slide 6]

Now we will move on the the graph algorithms. First is the depth first search time analysis. In green quotations on the right is the number of executions we expect. Lines with no notation are assumed to execute once and in constant time. We expect the while loop at line 6 to execute n times where n is the number of nodes. Similarly, the while loop at 12 and the for loop at 20 will execute n times. In any given iteration only one of these will occur. Thus, for every iteration of the while loop on 6, we will do n more executions. Therefore the time complexity will be n squared. 

[Slide 7]

Now we will look at the space requirements for depth first search. In green quotations on the right is the amount of space we expect the variable to take. The stack, discovered, parent map, path and neighbors will all have linear space requirements with respect to the number of nodes. Curr, trace, edge and node will have constant space requirements. Taking all of those into consideration, we will expect the space requirement to be linear with respect to the number of nodes. Meaning if the number of nodes doubles then the space requirement will roughly double. 

[Slide 8]

The time requirement for the breadth first search will be the same as the depth first search. We do the for loop on 19 or the while loop on 12 a total of n times. Each of those loops execute n times. Thus the space requirement for breadth first search will be n squared. 


[Slide 9]

Again, similar to depth first search we expect the space requirement to be roughly linear with respect to the number of nodes.

[Slide 10]

In total Kruskals algorithm will take the number of edges time log base two of the number of nodes. This is because getting the sourceset and target set takes log base 2 of n time. We need to get those e times in total. Thus, e times log base two of n. 


[Slide 11]

The space requirements are dependant on our choice of graph implementation. If we chose a matrix graph, it will be n squared. If we select a list graph then it will be n plus e. The better way to go for the MST is a list graph because we expect our MST to be quite sparse. 

[Slide 12]

The time required for Prims algorithm will be dependant on our use of a priority queue. If we use a priority queue then the sorting of the available edges will be logarithmic. If we use a list, then the sort could take e times log base to of e where e is the number of edges. Thus, if we use a priority queue, the time will be e times log base two of n.

[Slide 13]

Similar to Kruskals algorithm, the space required will depend on our graph implementation. Again, the smart choice is to use a list graph as our MST will be rather sparse. Thus, we would require n plus e space where n is the number of nodes and e is the number of edges. 


[Slide 14]

The time required for Dijkstra's algorithm will be n squared in the worst case. We expect the while loop to do n iterations and the for loop will do at most n iterations. Thus, we will do n iterations, n times. Therefore, we have n squared for the worst case. This occurs when the graph is very dense. If the graph is sparse, then we can expect a much better.  

[Slide 15]

The space required for Dijkstra's algorithm will be linear with respect to the number of nodes. We have 4 variables which will take space equal to the number of nodes. Thus if our number of nodes doubles, we can expect the space required to roughly double. 

[Slide 16]

That concludes the time and space analysis for the various algorithms. Here we have the summary for the tree algorithms. When directly comparing them, it is easy to see that binary trees will again offer us some added benefits beyond the four operations. 

[Slide 17]

Then we have the comparisons for the graph algorithms sectioned as they would be appropriate to compare. For example, conceptually it doesn't make sense to draw comparisons between Dijkstra's algorithm and the breadth first search. Again, for the minimum spanning tree algorithms, it would make the most sense to use a list graph as we expect our MST to be quite sparse. 