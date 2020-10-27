---
title: "Functionality"
pre: "4. "
weight: 104
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/10-PQ/04-PQ-functionality-slides.md" >}})

#### Video Script

[Slide 1]

We will now define the functionality of priority queues implemented via heaps. For this course, we will focus on the implementation for min priority queues. We can define similar functions for a max priority queue for other implementations. Throughout this video we will strictly discuss the priority queues within the context of min-priority queues.

[Slide 2]

The only attribute for our priority queue will be the heap itself. This will be an array of the elements which are in our priority queue. Similar to graphs and trees, the priority queue will have an associated size that we can calculate based on the array size. Each element in the array will be an ordered pair where the first element is the priority and the second element is the object itself.

[Slide 3]

Our priority queue will have two pushing functions, push up and push down. These will help us to maintain the min-heap properties. 

The goal of the push up function is that if the node has lower priority than the parent node, we will push it up the heap. Similarly, the goal for the push down function is that if the node has higher priority than the children, we will push it down the heap. Both of these will be recursive functions.


[Slide 4]

Since these are both recursive functions, we wil define their base cases and recursive case. Push up has two base cases, first if the index of the parent is less than or equal to zero. This means that our input node was the root itself, so we do nothing as we have reached the root. The second case is that the parent nodes priority is already less than or equal to the input nodes priority. This means that our heap is okay in this place so we do nothing. 

The recursive case happens when neither of the base cases are true. Meaning, when the input node is not the root and the parent has a higher priority than the input. When we are in this case, we will swap the parent and input then recurse on the parent node. Let's look at an example. 

[Slide 5]

Suppose we have this attempted min-priority queue. We can come across occasions like these when we are inserting an element or after we have removed the minimum. In this priority queue, we are modeling graph edges. So the priority would correspond to the weight of the edge and the second element is the ordered pair where the source is first and the target is second. 

In this case, the node with priority 3 and node object three comma six is out of place. 

[Slide 6]

We will work through this example as we would use the array. So here, we have the array set up accordingly and \\
would call PUSHUP on index 8. 

[Slide 8]

We get the parent of node 8, which is node 4 and we compare their priorities. 

[Slide 9]

The child has priority 3 and the parent has priority 5, so we will swap them. 

[Slide 10]

Then we recurse, so we call pushup on 4. 

[Slide 11]

We get its parent, which is node 2 and compare their priorities. The child's is 3 and the parent's is 4 \\
So we will swap them. 

[Slide 13]

Again, we recurse by calling the pushup function on node 2.

[Slide 14]

We get its parent and compare their priorities. In this case, the parents priority is lower than the child, so we have completed the process. 

[Slide 15]

Here is the heap after for reference. Now we will look at the push down function. 

[Slide 16]

Pushing down is also a recursive function, so we will look at the base case and the recursive case. For the pushdown base case, we have two base cases. First, if both of the children are out of range, meaning the input node was a leaf. The second case is that both children's priorities are greater than or equal to the parent's priority, then we have a legal heap structure. In either of those cases, we do nothing as we are done.

[Slide 17]

We have broken the recursive case into two pieces. First, if the node has a right child and secondly if the node only has a left child.

[Slide 18]

First we will look at the more complicated case where the node has a right child. This implies that the node has two children. 

If the priority of the left child is less than the priority of the right child then we will attempt to swap the current node With the left child. So if we are in the case where the priority of the left child is less than the priority of the right child, then we will compare the priority of the left child to the priority of the node. If the left child has a lower priority than the parent then we will swap the node and the left child and then recurse on the left child.

If the priority on the left child is not less than the priority of the right child then we will attempt to swap the right child and the node. So if the priority of the right child is less than the priority of the node we will swap the node and the right child and then recurse on the right child.

[Slide 19]

The other recursive case, is more straightforward. This is the case when Arnold only has a left child. So if the priority of the left child is less than the priority of the node we will swap the node and the left child then recurse on the left child.

[Slide 20]

Let's look at an example. In this case the root of our heap is out of place. It has priority six while it's children have priority three and four so we will call the push down function on node one.

[Slide 21]

Looking at the array representation, we call the pushdown function on node 1. 

[Slide 22]

We get its left and right children and compare their respective priorities. 

[Slide 23]

In this case, the left child has a lower priority than the right child. So we compare its priority to the parent. 

[Slide 24]

The left child has lower priority than the parent, so we will swap them. \\
and now we call the push down function on node 2.


[Slide 26]

We get its left and right children and compare their priorities. IN this case the right has lower priority \\
So we will see if we can swap it with its parent. 

[Slide 28]

the left child has priority 4 and the parent has priority 6, \\
so we will swap them \\
and recurse on node 5.

[Slide 31]

We get the children of node 5. This node only has a left child, so we see if we can swap them. 

[Slide 32]

The priority of the left child is less than the parent, so we swap them. 

[Slide 33]

We would then recurse on node 10. The potential children of node 10, nodes 20 and 21, are out of the range of our priority queue, so we are done. 

[Slide 34]

Here is our completed priority queue for reference. 

[Slide 35]

The next function we will talk about is remove min. This will extract the node with the smallest priority from our queue. If there is only one element in our priority queue, then we can just delete the entry from our array. If there is more than one element, then we will delete the first element of our array and replace it with the last element of our array. We will then call the push down function to restructure our priority queue properly.  

[Slide 36]

The next function is called heapify. This will be what initializes our priority queue. Remember that priority queues are an application of heaps. It takes two arrays as input, ranks, which will store the priorities, and items, which will store the elements. These will be input such that the first element ranks represents the priority of the first element in items, and the second element in ranks corresponds to the priority of the second element in items and so on. As such, ranks and items must be the same size. 

[Slide 37]

Assuming that they are the same size, we will enter the if block. 

[Slide 38]

We loop through each of the elements and append the ordered pairs of priority then element, to our priority queues array. 

[Slide 39]

At this point, our useful fact from node relationships becomes useful. Starting at the node floor of size over two plus one and decrementing down to 1, we will push down the nodes. The fact that the nodes from floor of size over two plus one to n are leaves, saves us the trouble of having to sort them. We go to the nodes before them and use the push down function to get the ordering correct.  


[Slide 40]

Akin to the heapify function, we also have the insert function. This is the instance in which we want to add elements one by one to our heap. This will take as input the priority and the element. We will simply append the element to the end of our priority queue and call the push up function on that element. This will take care of the ordering for us. 


[Slide 41]

The last piece of functionality for our priority queue is the decrease key function. This function handles the case where we need to change the priority of our element at index I D X. We check that the priority of the element in our queue at index isn't already smaller than the priority we are trying to give it. If the new priority is less than the old priority, we will update it and then call the pushup function on that index. 

[Slide 42]

That concludes the functionality portion for priority queues. Again, we are just focusing on min priority queues in this course but we could define these functions very similarly to handle max-priority queues. In the next video, we will talk about a good place to priority queues. 