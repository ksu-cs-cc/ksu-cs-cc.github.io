---
title: "Graph Traversal DFS"
pre: "2. "
weight: 82
date: 2019-02-04T10:53:26-05:00
---

{{< youtube 3lalaxn0yNs >}}

#### Resources
* [Slides]({{< relref "/4-cc315/08-graph-traversal/02-graph-traversals-DFS-slides.md" >}})

#### Video Script

[Slide 1]

In this video, we will introduce the first traversal for graphs, the depth first traversal. We will go over the pseudocode and go through a thorough example. With both the depth first and breadth first traversals, we can define the algorithms iteratively or recursively. For this course, we will use the iterative algorithm. 

[Slide 2]

Here we have the pseudocode for the iterative depth first traversal. We take the graph and a source node as input. 

[Slide 3]

We start by initializing a stack, which will keep track of which node to traverse next, and a set which will keep track of which nodes we have explored. We push the source node onto our stack and begin the iterative portion.

[Slide 4]

As long as the stack is not empty, we will continue to do the traversal. At the start, we just have the source node in the stack. We will pop it from the stack and check if it has been discovered yet. In this case, it has not, so we add it to discovered. We continue by pushing the indexes of the nodes neighbors to the stack. This process will repeat until the stack is empty. 

On its own, this algorithm will traverse all of the nodes. We will modify this algorithm in a future video to act as more of a search. We want to have a good understanding of the process before adding an extra complexity. Let's go through an example to help build this understanding. 

[Slide 5]

We will walk through this example graph on the left. We will track the stack and the set of discovered nodes on the right side. The current node and neighbors will be between the graph and stack. For this graph, suppose call the traversal function on node 1. 

[Slide 6]

We start by pushing one onto the stack. We would then enter the while loop. 

[Slide 7]

We pop the top element of the stack, then add it to the discovered set as it is not already in there. 

[Slide 8]

We get the neighbors the current node. 

[Slide 9]

Then we push the indexes of the neighbors onto the stack. This is a point in which some variation can happen. If someone were to create this same graph but add the nodes in a different order, these indexes could be different. 

[Slide 10]

Once we have added all of the neighbors, we will back to the top of our while loop. 

[Slide 11]

We pop the top of the stack, add it to discovered since it is not there already, then get its neighbors. 

[Slide 12]

We push the neighbors indexes onto the stack. At this point we can note that while we have already discovered node 1, we will still add it to the stack. The depth first approach checks if the node has been discovered when we pop the value, not push it. 

[Slide 13]

Once we have added all of the neighbors, we will back to the top of our while loop. 

[Slide 14]

We pop the top of the stack, add it to discovered since it is not there already, then get its neighbors. 

[Slide 15]

We push the neighbors indexes onto the stack. At this point we can note that multiple entries of the same node appear in our stack. Similar to pushing a node that we have already discovered, we will deal with this when we pop the values from the stack. 

[Slide 16]

Here is a good place to pause the video. We are back at the top of the while loop. What is the next node we will look at? What will we have once we complete this loop? How will the stack look when we complete this loop? Will the set of discovered nodes change? Take a moment to pause the video and work it out for yourself! 

[Slide 17]

Our next node will be 9 which we will add to discovered since we haven't discovered it yet. 

[Slide 18]

Then we push the neighbors onto the stack. Again, some variation can appear in the ordering of the nodes on the stack. 

[Slide 19]

That completes that loop. How did you do? We pushed five, six, and eight onto our stack as they were neighbors of nine and we added nine to the set of discovered nodes. 

We now come to a different scenario. 

[Slide 20]

The next element that we pop is 8. We have already discovered node 8, so we can move on down the stack. The next value we pop is 6

[Slide 21]

We have not discovered 6 yet, so we add it to the set of discovered nodes and push its neighbors onto the stack. To add some explanation of the visual stack, at this point our stack ran out of room so we doubled the capacity. The top of the stack is 9 followed by 3 then 2 and so on. 

[Slide 22]

We are back at the top of the while loop and will proceed by popping the top element of the stack.


[Slide 23]

This value is 9, which have already discovered.  So we will be back at the top of the while loop and pop the next element. 

[Slide 24]

Now we are at node 3, we add it to the set of discovered nodes and get its neighbors. 

[Slide 25]

Then we push the neighbors onto the stack. 

[Slide 26]

We are back at the top of the while loop. 


[Slide 27]

This is another good point to pause and try to complete the traversal for yourself. I have included the pseudocode at this point for reference again. 

[Slide 28]

We pop the value 6 but we have already discovered it. We move to the next node. 

[Slide 29]

We pop the value 2, and add it to the set of discovered nodes.

[Slide 30]

We get its neighbors and push them onto the stack. We pop the next value which is 6.

[Slide 31]

We have discovered 6 so we will pop the next value, 3.

[Slide 32]

We run into the same situation for value 3 as well as the next two elements on the stack.//
We pop one which we have discovered, //
then we pop two which we have discovered. //
We finally get to the value five which we will pop. 

[Slide 35]

We have not discovered five, so we continue with the same procedure. Add it to the set of discovered //
then push its neighbors //
We pop the top value of the stack which has already been discovered. Then we pop again//
We have node one which we have already discovered so we will pop the next value, 7. 

[Slide 39]

We have not discovered node seven yet. So we add it to the set of discovered //
then push its neighbors. At this point, we have visited all of the nodes. We can visually account for the values one through nine in the set of discovered nodes but our stack is not empty yet. We must still continue through our stack until it is empty. 

[Slide 41-48] (popping all of the values off the stack)

Now we have an empty stack and we can verify as before that we have discovered all of the nodes. In a future video, we will discuss how this doesn't always find all of the nodes. 

[Slide 49]

While this walk through was longer than previous examples, it is an important tool for us. We have seen many scenarios that can happen and how we handle them. If you want to work through this example, I have included the slides below so you can go through it at your own pace. 