---
title: "Postorder Traversal"
pre: "6. "
weight: 36
date: 2019-02-04T10:53:26-05:00
---

{{< youtube En7FDq5XrsA >}}

#### Resources
* [Slides]({{< relref "/4-CC315/03-treetraversal/06-treetraversal-postorder-slides.md" >}})

#### Video Script

[Slide 1]

When we talk about preorder and postorder traversals, the prefix of the traversal refers to the root. So in a postorder traversal we will run the postorder traversal on the children then record the root. 


[Slide 2]

The algorithms for traversals are rather straight forward. Rather than just printing the node item, we will pass a `StringBuilder` and build it as we are recursing though the tree. 

For the postorder traversal, we first run the postorder traversal on each of the children then append the item of the root to our `StringBuilder`.

As we discussed in the preorder traversal video, general tree traversals can result in different strings. This is due to the fact that there is no fixed order on the children of a node. 


[Slide 3]

To give an example traversal, we will walk through it with this format. On the left is the tree, on the right is the call stack, and across the bottom is our `StringBuilder` that will be passed throughout the recursion. We start by calling the `POSTORDER` function from the root of our tree. 
We then call the `POSTORDER` function on each of the children of `A`.

[Slide 4]

We will start with node `B`


[Slide 5]



First we append the item of our node to the stringbuilder. Then we call the preorder function on each of node `A`s children. We will start with node `B`


[Slide 6]

We append `B` then call the preorder function on its children. 


[Slide 7]

We append `F` then call the preorder function on its children. Node `F` has no children so we continue with the children of `B` which will be node `G` next. 


[Slide 8]

We append `G` then call the preorder function on its children. Node `G` has no children so we continue with the children of `B`. Node `B` has only the two children which we have already recorded. Then we continue with the children of `A` and call the preorder function on node `C`. 


[Slide 9]

We will record `C`, then call preorder on `C`s children. The only child is node `H`.


[Slide 10]

We record `H` and call the preorder function on `H`s children. Node `H` has no children so we return to node `C` which only had `H` as a child so we return to `A` and continue calling the preorder function on its children. 

[Slide 11]

Next is node `D` so we record its item. 

This is a good place to pause the video and try to work the rest of the traversal out for yourself! Again, for this video, we will work from left to right on the children. However it is possible that you come up with a different solution. We will discuss more examples of possible solutions! 

To continue, we call the preorder function on each of `D`s children and we will start with `I`.

[Slide 12]

We will record `I`, then call preorder on `I`s children. Node `I` has no children so we continue with `D`s children. Next would be node `J`


[Slide 13]

We record `J` then call the preorder function on its children. We would do node `L` next. 


[Slide 14]

We will record `L`, then call preorder on `L`s children. Node `L` has no children so we continue with `J`s children. Next would be node `M`.


[Slide 15]

We will record `M`, then call preorder on `M`s children. Node `M` has no children so we continue with `J`s children. We have visited each of `J`s children so we return to `D` and continue calling the preorder function on its children. The only child that is left for `D` is node `K`.


[Slide 16]

We will record `K`, then call preorder on `K`s children. Node `K` has no children so we continue with `D`s children. We have now visited all of `D`s children so we continue with `A`s children. The last node is node `E`


[Slide 17]

We record `E` and call the preorder function on `E`s children. Node `E` has no children so we return to node `A`. We have now visited all of `A`s children. Thus, we are done with the traversal! 


[Slide 18]

As I mentioned previously, it is possible to have different preorder traversals for this tree. Here I have listed three possible preorder traversals. This is not a complete list!

When looking at these to verify that they are correct preorder traversals, we check that when a node is written its children are written immediately after. We can also check that a nodes parent is written before itself. 


[Slide 19]

Here we have three examples that are not valid preorder traversals. This would be another good place to pause the video to see if you can determine why these are not valid! 

Let's start with the first one. The first element is `A`, since this is the root of the tree this is correct. The next element is `G`; this would imply that `G` is a child of `A`. This is not the case and thus makes this an invalid preorder traversal. This is not the only error in this traversal. Both `G` and `F` are written before their parent, `B`. Also, `H` is before its parent `C`.

In the second traversal, node `E` is recorded first. For a preorder traversal, this would imply that `E` is the root of this tree. As a rule of thumb, the root of the tree should be the first character in a preorder traversal. 

In the third traversal, we start with `A` which is correct. Next we have `B` which is correct since node `B` is a child of node `A`. The next character is `C`. Based on our tree this is not correct. Having `C` as the next character would imply one of two things either `C` is a child of `B` or `B` has no children. Neither of these are true in our case. The premise of the issue in this instance is that the children of `B` need to be immediately after `B`. 


[Slide 20]

We have just covered preorder traversals in this video. The key takeaway from this should be that in a preorder traversal, the root always comes before its children. We record the root then run the preorder traversal on the nodes children. 