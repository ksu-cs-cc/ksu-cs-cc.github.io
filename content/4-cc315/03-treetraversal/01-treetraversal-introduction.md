---
title: "Traversal Introduction"
pre: "1. "
weight: 31
date: 2019-02-04T10:53:26-05:00
---

{{< youtube En7FDq5XrsA >}}

#### Resources
* [Slides]({{< relref "/4-CC315/03-treetraversal/01-treetraversal-introduction-slides.md" >}})

#### Video Script

[Slide 1]

Now that we understand the terminology associated with trees and have a basis for creating trees, we can fully implement trees. 

For this module, we will recursively build fully functional trees. This means that we will be able to prevent cycles as well as implement some additional functionality. 

Don't forget that you are able to go back to the previous module to refresh your memory on tree vocabulary!

[Slide 2]

To start this module, we will introduce some new terms. We will define what it means to be an ancestor, descendant or sibling. The terms are used in the same way for general trees as they are used for family trees. 

[Slide 3]

We will use the example of the British Royal Family to get familiar with these terms. 

[Slide 4]

Descendants are defined by the parent to child relationships. In this family tree example, the descendants of Prince Charles are Princes William, Harry, George, Louis, Archie, and Princess Charlotte. We can reason through this as we would in code. Charles is the parent of William and Harry, William is the parent of George, Charlotte, and Louis, finally, Harry is the parent of Archie. We determine the children of the parent nodes to get the descendants. 

You may already recognize this as a recursive process. We can say that this is recursive with the base case being the node has no children and the recursive case being that the node does have children so we find the children's descendants. We will have a recursion refresher later in the module as no one understands recursion until after multiple times of seeing it and using it. 

[Slide 5]

Ancestors are defined by the child to parent relationships. In our royal family tree example, the ancestors of Princess Charlotte are Princes William and Charles, Queen Elizabeth the second and King George the sixth. Like the descendants, we can work our way through this as we would in code. Charlottes parent is William, Williams parent is Charles, Charles parent is Elizabeth the second, and Elizabeth the seconds parent is George the sixth. We determine the parent of the node to get the ancestors. 

This is also a recursive process. Here the base case would be that the node has no parent, meaning it is the root. The recursive case would be that the node does have a parent then we find the parents ancestors. 

[Slide 6]

Siblings are defined by sharing their parent node much like we would say two people are siblings if they share the same parent. In this example, we would say that the siblings of Princess Charlotte are Prince George and Prince Louis. This is not a relationship we define recursively. We can simply get the parent of the node in question and the retrieve that nodes children. So in our example, we would get the parent of Charlotte, which is Prince William, and then get William's children, George, Louis and Charlotte. Since Charlotte is the node whose siblings we are looking for, we would eliminate her node from the list of siblings. 

[Slide 7]

In this video we have covered three new terms. First we discussed descendants. This relationship is defined by parent to child relationships. Then we introduced ancestors which is the relationship defined by child to parent relationships. Finally we talked about siblings which are defined as the children of the parent node. A good way to remember these terms is by thinking of a family tree as the terminology is the same! 