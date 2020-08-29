---
title: "Postorder Traversal"
pre: "6. "
weight: 36
date: 2019-02-04T10:53:26-05:00
---

{{< youtube eEZmsK-loUU >}}

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

We will start with node `B`. We then call the `POSTORDER` function on its children. 


[Slide 5]

We will do `F` first. The next step would be to run the `POSTORDER` function on on the children of `F`. Node `F` has no children, so we record `F`. Then move on to the next child of node `B`, which is node `G`



[Slide 6]

The next step would be to run the `POSTORDER` function on on the children of `G`. Node `G` has no children, so we record `G`. Then move on to the next child of node `B`.

[Slide 7]

Node `B` has no more children so we record `B` in our `StringBuilder`. Now we move on to another child of `A`


[Slide 8]

We run the `POSTORDER` function on `C`. Then we move on to the children of `C`. 


[Slide 9]

Node `C` has one child, node `H`. Our next step would be to run the `POSTORDER` traversal on the children of `H`. Node `H` has no children so we record `H` in our `StringBuilder`. We would then move on to the next children of node `C`.


[Slide 10]

Node `C` only has `H` as a child which we have already recorded. Thus, we record `C` in our `StringBuilder`. Now we continue with the children of node `A`


[Slide 11]

The next child is node `D`. This would be a good spot to pause the video and try to finish out the postorder traversal for yourself! 

The next step is to run the `POSTORDER` function on the children of node `D`. 

[Slide 12]

Node `I` will be the next node we visit. We would run the `POSTORDER` function on the children of node `I` however it does not have any children. So we record `I` in our `StringBuilder` and then continue with the children of node `D`. 

[Slide 13]

The next child of node `D` will be node `J`, so we run the `POSTORDER` traversal on the children of node `J`. 


[Slide 14]

We will do node `L` first. We would run the `POSTORDER` function on the children of `L`. Node `L` has no children so we record `L` in our `StringBuilder` and continue with the children of `J`.


[Slide 15]

Now we are at `M`. We would run the `POSTORDER` function on the children of `M`. Node `M` has no children so we record `M` in our `StringBuilder` and continue with the children of `J`.


[Slide 16]

Node `J` has no more children so we record the `J` in our `StringBuilder` and continue with the children of `D`.


[Slide 17]

The last child of `D` is `K`. Node `K` has no children so we have no nodes to run the `POSTORDER` traversal on and thus we record `K` in the `StringBuilder`. Then we continue with the children of `D`.


[Slide 18]

Node `K` was the last child of `D` so we record `D` in our `StringBuilder`. Then we continue with the children of node `A`. 


[Slide 19]

The last child of `A` is `E`. Node `E` has no children to run the `POSTORDER` traversal on so we record `E` in our `StringBuilder`. Then we continue with the children of `A`.


[Slide 20]

Since `E` was the last child of node `A`, we can now record node `A` in our `StringBuilder` and we are done! 


[Slide 21]

As I mentioned previously, it is possible to have different postorder traversals for this tree. Here I have listed three possible postorder traversals. This is not a complete list!

When looking at these to verify that they are correct postorder traversals, we check that when a node is written its children are written immediately before it. We can also check that a nodes parent is written after itself. 


[Slide 22]

Here we have three examples that are not valid postorder traversals. This would be another good place to pause the video to see if you can determine why these are not valid! 

In this first example, we start with `G` then `F` and then `B`. Up to this point, we are okay. The children have appeared in the traversal before their parent. Next we have `C`. This is where our traversal goes wrong. What is written in this traversal would imply one of two things. Either node `C` is a leaf or `C` is the parent node of `B`. Neither of these are true statements. Node `C` is the parent node of `H`, thus, `H` must appear before `C`.

For the second example, we start with `E` then `H` and then `C`. We are okay so far. Next we have `L` then `M` and then `K`. Here is the issue for this traversal. This would imply that `K` is either a sibling of `L` and `M` or that `K` is their parent. We know that `J` is the parent node of `L` and `M` and thus must come immediately after them. 

This last example is actually a preorder traversal! Postorder traversals will always end with the root. 

[Slide 20]

We have just covered postorder traversals in this video. The key takeaway from this should be that in a postorder traversal, the root always comes after its children. We run the postorder traversal on the nodes children then record the nodes value. 