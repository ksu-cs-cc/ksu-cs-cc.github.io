---
title: "Traversal Terms II"
pre: "3. "
weight: 33
date: 2019-02-04T10:53:26-05:00
---

{{< youtube 86uWWXaanCo >}}

#### Resources
* [Slides]({{< relref "/4-CC315/03-treetraversal/03-treetraversal-termsII-slides.md" >}})

#### Video Script

[Slide 1]

In the last video we talked about some new relationships we can define in trees. We will now discuss more terms that help us to characterize a nodes position within the tree. These new terms are: level, depth, and height. 

[Slide 2]
As with previous videos and course content, we will use this tree throughout the video as a guiding example. 

[Slide 3]

The first term we will discuss is level. The level is a measurement corresponding to a nodes distance from the root. The level for the root is always one. As we move away from the root, the level increases. 

[Slide 4]

The next measurement corresponding to a nodes distance from the root is the depth. The depth for the root is always zero. As we move away from the root, the depth increases. Depth and level are very similar. The level is equal to one plus the depth. 

[Slide 5]

The final term for this video is height. We define the height of a node as the longest path to a leaf descendant. The height of a leaf will always be zero. 

You may notice a recursive pattern in this figure. The base case for this is if the node is a leaf then the height is zero. We are in the recursive case when the node is not a leaf. In this case, return the height of the highest child plus one. 