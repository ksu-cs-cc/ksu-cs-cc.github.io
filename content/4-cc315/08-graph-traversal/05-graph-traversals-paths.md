---
title: "Graph Traversal Paths"
pre: "5. "
weight: 85
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/08-graph-traversal/05-graph-traversals-paths-slides.md" >}})

#### Video Script

[Slide 1]

Up to this point, we have seen the basis of breadth first and depth first traversals. In this video, we will modify the traversals to act as searches for paths. For two nodes, a source and a target node, we want to be able to find a path that connects the source to the target. 

It is important to note that there are three possibilities. First there is no path that connects the course to the target. Second there is exactly one path that connects the source to the target. Third, there are multiple paths from the source to the target. 

In the first case, we will just return nothing. In the second case, we will return the path. In the third case, we will return a path. This will just be the first path that we find, so there are no guarantees that it will be the shortest or most direct. The only thing we can be sure of is that it will connect the source with the target. 

[Slide 2]

We will start with the depth first search or D F S. The way in which we modify the traversals to do the path creation will be similar across breadth and depth first. 

[Slide 3]

Let's look at what we haven't changed in the depth first approach. We still have a stack to track which node is next and a set of nodes we have discovered. We will still perform a loop while our stack is not empty. In that loop, we push the neighbors of the current node onto the stack. 

[Slide 4]

Now let's look at what we have added to the depth first approach. First, we have added a dictionary which will map parents and children. While we use the terms parent and children, these are not exclusive to trees. We will discuss this further when we do the example. 

Then I would like to skip to lines 23 through 25. If we haven't already found a parent child relationship for the neighbor, then we will add it where the key is the neighbor and the value is the current node. Line 25 has been added to address case that there is no path. If we get through all of the elements in the stack, meaning we have discovered all of the nodes, and we never returned, then we will return nothing at this point. 

The next addition is lines 9 through 17. This block of code handles building the path which occurs when we have popped the target node off of the stack. We set up a path and work backwards through our parent map. We would start by getting the parent of the target and appending it to the path, then the parent of that parent, and so on until we reach the source. We then append the source to the path, reverse the path and then return it. 

[Slide 5]

Let's walk through an example. We have the graph that we want to find the path in on the left and the other variables on the right. As with the traversal, we have the stack, the set of discovered, the current node, and its neighbors. We have added the parent map, the path and the trace. 

Suppose we call the depth first search on this graph to find a path from node one to node six. 

[Slide 6]

We start with the source node and push it on the stack. //
Then we start the while loop. We pop node 1 and it becomes the current node.//
It has not been discovered, so we insert it in our discovered set and we get its neighbors.//
We will push two and four onto the stack, as we did in the traversal. Now we check if there was an entry for node 2 or 4 in the parent map. Since there was not, we add key 2 with value 1 and key 4 with value 1. We interpret this as we got to node 2 through node 1 and we got to node 4 through node 1. 

[Slide 10]

We are back at the top of the loop again. We will pop the top element of the stack.//
That value is 4. We add it to the set of discovered and get its neighbors. //
We push the neighbors, 1, 2, 3, and 5 onto the stack. In the parent map, we see if there is an entry with key one. There is not so we add key one value four to our dictionary. 

We check if there is an entry with key 2. We already have key 2 value one, so we do not add a second entry. 

We check if there is a key of 3 yet and since there is not, we add key 3 value 4. Again, this is saying that we got to node three through node four. And the same thing with node 5. It is has not been entered into our dictionary so we add key 5 value 4. 

[Slide 13]

We are back at the top of our while loop now. Here is a good place to pause to check for understanding. What will the next node be? What will we add to the parent map? 

[Slide 14]

The next node is 5. We haven't discovered 5 yet so we add it to the set. We get the neighbors of 5 which are 3, 4, and 6. We push those onto the stack. Nodes three and four are already keys in our parent map, so we just need to add key 6 with value 5. 

[Slide 15]

And we are back at the top of our while loop. //
We pop six from our stack, and this is the node we are trying to connect to. So now we start the process of building our path. 

[Slide 17]

We set trace to be 6//
and add it to our path. We go to our parent dictionary for key 6 which has value 5. Trace is now equal to 5.//
We append trace, which was 5, to our path and get the value for key 5 in our parent map. Trace will now be equal to that value, 4. and we repeat this process until we get back to the source//

[Slide 20]

We append trace, which was 4 to the path and go to the dictionary to get the value for key 4. This value is one, which was our source! 

[Slide 21]

So we append the source to the path//
reverse the path since it is currently target to source and we would return it. And that completes the depth first search. 

[Slide 23]

Next we have the breadth first search. As I mentioned at the beginning, the modifications will be quite similar. 

[Slide 24]

Let's look at what is the same as the breadth first traversal. We still have the queue to track the next node and the set to track the discovered nodes. We loop while the queue still has entries and in that loop, we enqueue neighbors which haven't been discovered yet. 

[Slide 25]

Looking at the modifications, we can see that we have added the same logic. We have a dictionary to track how we got from one node to another, we add to that dictionary if the key isn't already there, and once we get to the target node, we unwind the path. At the end, if we have complete the while loop this means that we have traversed all of the nodes in this graph and there is no path from the source to the target node. Let's walk through this algorithm. 

[Slide 26]

We will use the same graph as before as well as trying to connect the same nodes. 

[Slide 27]

We enqueue the source node and add it to the set of discovered nodes as per the breadth first traversal algorithm. 

[Slide 28]

We dequeue one //
then get its neighbors. Since the neighbors have not been discovered, we add them to the set of discovered and enqueue them according to the breadth first traversal algorithm. We then add key two value one to the parent map and key four value one to the parent map. 

[Slide 30]

And we are back at the top of the while loop.//
We dequeue 2 and get its neighbors. Since node one has already been discovered, we do not enqueue it and we do not add it to the parent map. 

Recall that this was a key distinction of breadth first over depth first. We first check if it was discovered then enqueue whereas in the depth first, we pushed it then when we popped it we would check if it was discovered. As with node one, node four has already been discovered, so we do not enqueue it and we do not attempt to add it to the parent map. 

[Slide 32]

We are back at the top of our loop. As in the other example, now would be a good time to pause the video and try the next loop for yourself! What will our next node be? What will we add to the parent map and the set of discovered nodes?

[Slide 33]

Our next node is 4, which has neighbors 1, 2, 3, and 5. We have already discovered nodes one and two, so we do nothing with them. We enqueue nodes three and five as well as add entries to the parent map for them. We insert key three value four and key five value four. 

[Slide 34]

We are back to the top of our loop again.//
We dequeue 3, and get its neighbors. All of its neighbors have been discovered, so we do nothing and go to the next loop.//
We will dequeue five now.

[Slide 37]

We get fives neighbors and six is the only neighbor we haven't discovered. So we enqueue six and add key six value five to our parent map. //
Then we are back at the top of the loop.//
We dequeue six now. 

[Slide 40]

Since this is our target node, we set trace equal to six. This process will now be the same as with the depth first traversal. 

[Slide 41]

We append 6 to the path and we get the value for key 6 to be the new trace. //

We append 5 to the path and get the value for key five, so four will be our new trace. //

We append 4 to the path and get the value for key 4, so 1 will be our new trace. 

[Slide 44]

Node one was our source, so we append it to the path as we have reached the beginning. //
Again, since we have built the path in the opposite direction, we must reverse the path.//

[Slide 45]

We will close this video with some points of interest. 

While in this example the searches found the same path, this is not always going to happen. It is also worth noting that the same search on the same graph may not always return the same path. This can happen when there are multiple paths from the source to the target. 

In the case that there is not a path from the source to the target, it is important that we return nothing. In both searches, the lack of a path was signified by making it all the way through the traversal without returning prior to the end. 

With that, we conclude our discussion on depth first and breadth first searches. The slides to this video will be linked below for your reference. 