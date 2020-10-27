---
title: "Dijkstra's Algorithm: Shortest Path"
pre: "5. "
weight: 105
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/10-PQ/05-PQ-dijkstra-alg-slides.md" >}})

#### Video Script

[Slide 1]

A classic implementation of priority queues is Dijkstra's algorithm. This function will find the shortest path from a given source node to any other node in a graph. This is a Greedy algorithm as we are trying to get the locally smallest edge to eventually get the globally shortest path.


[Slide 2]

Here we have outlined the algorithm for Dijkstra. We take as input the graph in which we are trying to find the shortest path and the node that we will be starting at. Let's go through it piece by piece. 

[Slide 3]

We start with initializations. We have two arrays, one called dists and the other called previous. This will both have length equal to the number of nodes in our graph. For dists, we set each entry to a really high number, infinity. For previous, we initialize each entry to be none. 

The dists array will keep track of the current shortest distance from the starting node to every other node. The previous array will keep track of the node we visited before we got to that node. 

We set dists equal to zero at the index of the start node. It takes us 0 units to get from the start node to the start node. 

Then we initialize an empty min-priority queue. 


[Slide 4]

Inside the loop, we insert values into our queue where the priority is equal to the edge weights from dists and the element is the index. In the pseudocode, we have used the insert function for clarity and to avoid any functions specific to a particular langue. That being said, in both Python and Java, we could use the heapify function with some clever coding! 

[Slide 5]

Once we have all of the initializing done, we proceed into the while loop. This loop will continue until our priority queue is empty. 

We extract the lowest priority element from our priority queue. In this application, this is the node which is the shortest distance away at the moment. 

Then we loop through the neighbors of that node. We get the weight of the edge between the neighbor and node. We calculate the new weight by adding together the weight up until the point of the minimum node plus the edge weight.  

[Slide 6]

If that newly calculated weight is less than the weight that is currently stored, then we update the weight in the dists array, update the entry in previous such that for node the previous was min and then we decrease the key in our priority queue for node to match the newly calculated weight. 

[Slide 7]

Once we our priority queue is empty, we return dists and previous. These together give us the shortest path weight as well as the actual path itself. 

Describing this algorithm may seem like a lot of moving parts. As always, we will work through an example to help our understanding. 


[Slide 8]

In this example, suppose that we are given this graph and want to find the shortest paths from node 1 to every other node. 

[Slide 9]

We do all of the initialization. To begin with, node 1 is the only node with a defined weight because that is where we are starting. 

[Slide 10]

We extract the minimum from our priority queue\\
and begin looping through the neighbors of node 1. First we get node 2 whose calculated distance is zero plus 6. This is because we take the weight required to get to node 1 and then add the weight required to get from node one to node 2. \\
This is an improvement compared to infinity, so we update twos distance, its previous node, as well as its entry in the priority queue. 

[Slide 13]

Now we go to the next neighbor, node 3. Its calculated weight is 4. \\
Again, this is less than infinity so we update the distance entry, the previous node for node three and then the priority queue entry. \\
Then to the next neighbor which is node 4. Its calculated weight is 2 \\
And we do the updates as two is less than infinity.\\
Then the next neighbor, node 5, which has a calculated weight of 7 \\
and the same thing, we update the entries with the weight and the previous node for node 5. 

[Slide 19]

Once we made it through all of the neighbors, we are back at the top of the while loop and remove the minimum from our priority queue. This is weight 2 for node 4. 

[Slide 20]

We then start looping through the neighbors. we start with node one. This will have a calculated weight of 4 because from the distances entry, it cost 2 to get to four and then the cost between four and one is 2. This is not less than zero, so we move on to the next neighbor. 

[Slide 21]

This is node 2 which will have a calculated weight of 5. Again, because so far it has cost us 2 to get to four and then another three to get from four to two. \\
This value is less than the recorded six, so we update the distance for two to be 5 and the previous for two to be four. 

[Slide 23]

And we continue in this style. For the sake of not being pedantic, we will skip ahead. I have linked the slides below this video which will walk through every step. You can walk through these to check for understanding. 

[Slide 36]

Once our priority queue is empty, we return the distances and the previous nodes. We can piece this information together to get all of the shortest paths. 

[Slide 37]

Here I have put together those paths based on the output from Dijkstra's algorithm. In this small of an example, we could potentially determine these paths by hand. However, once we start adding more nodes and edges, it gets much more complicated. Thus, the need for such a methodical approach. This is a very classic example of how we can use priority queues and is very beneficial in real world applications from determining the shortest path from city to city to more theoretic problems such as network routing. Again, I have linked the slides below so you can walk through this example at your own pace. 