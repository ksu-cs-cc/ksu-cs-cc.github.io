---
title: "Binary Trees In-Order Traversal"
pre: "4. "
weight: 54
date: 2019-02-04T10:53:26-05:00
---

{{< youtube uyM6L6xqn_8 >}}

#### Resources
* [Slides]({{< relref "/4-CC315/05-binarytree/04-binary-trees-in-order-slides.md" >}})

#### Video Script

[Slide 1]

In the previous video, we discussed how preorder and postorder traversals are applied to binary trees. In this video, we will introduce a new type of traversal for binary trees. This traversal is called the in-order traversal. 

Throughout the course, we have talked about how the prefix of the traversal refers to the root. This traversal is no exception! In this process, we access the root in-order with respect to the children. Procedurally, we will call the in-order traversal on the left child, access the root, then call the in-order traversal on the right child. Let's see an example! 


[Slide 2]

For this example, we will follow the same style we used when introducing preorder and postorder traversals. The binary tree will be on the left, the call stack will be on the right and the StringBuilder which is being passed along will be across the bottom.

We start at the root with the initial call to get the traversal started. Starting at 30, we would call the in-order traversal on the left child, node 10.


[Slide 3]

After calling the in-order traversal, we would call the in-order traversal on the right child of 10, which is 5.


[Slide 4]

Now we would call the in-order traversal on the left child of 5. Node 5 does not have a left child, so we would move on to records node 5's item. Next, we would call the in-order traversal on node 5's right child. Since node 5 does not have a right child, that completes the in-order traversal on Node 10's left child. 


[Slide 5]

With the completion of node 10's left child, we record the item for node 10 and then proceed by calling the in-order traversal on the right child of node 10.


[Slide 6]

We are now at node 20 and we call the in-order traversal on 20's left child. 


[Slide 7]

Now we would call the in-order traversal on the left child of 15. Node 15 does not have a left child, so we would move on to records node 15's item. Next, we would call the in-order traversal on node 15's right child. Since node 15 does not have a right child, that completes the in-order traversal on Node 20's left child. 

[Slide 8]

With the completion of node 20's left child, we record the item for node 20 and then proceed by calling the in-order traversal on the right child of node 20.

[Slide 9]

Like nodes 5 and 15, node 25 has no left child, so we record its item. Node 25 has no right child so we have completed the in-order traversal on node 25. This also completes the in-order traversals on node 20 and node 10.

[Slide 10]

Up to this point, we have completed the in-order traversal of the left child of node 30. Now we record the item of node 30 then do the in-order traversal on the right child. This would be a good place to pause the video and try to finish the traversal on your own! 

[Slide 11]

Continuing the in-order traversal on the right child of node 30, we would call the in-order function on the left child of node 45.

[Slide 12]

Once we are at node 35, we would call the in-order function on its left child. Node 35 does not have a left child, so we record the item of node 35 and then call the in-order traversal on the right child of node 35. 

[Slide 13]

Node 40 doesn't have a left child, so we record its item. Node 40 does not have a right child and thus we complete the in-order traversal for node 40. With the completion of node 40's in-order traversal, we also complete node 35's in-order traversal. 

[Slide 14]

By completing node 35's in order traversal, we have finished the left child of node 45. As such, we record the item of node 45 and continue with the in-order traversal of node 45's right child. 

[Slide 15]

Node 50 does not have a left child to do an in-order traversal on so we record node 50's item. Then we do an in-order traversal on node 50's right child. 

[Slide 16]

If node 55 had a left child, we would do an in-order traversal on it. Since there is not, we record 55's value then check for a right child. 

[Slide 17]

Now we have completed the entire binary tree! 

[Slide 18]

When doing in-order traversals, we traverse the left child, access the root, and then traverse the left child. Again, for binary trees, all of the traversal will have unique results.