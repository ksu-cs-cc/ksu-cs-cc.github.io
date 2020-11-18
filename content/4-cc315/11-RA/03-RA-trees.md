---
title: "Trees"
pre: "3. "
weight: 113
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/11-RA/03-RA-trees-slides.md" >}})

#### Video Script

[Slide 1]

In this video we will discuss the types details of the data we need to verify with the client when using a tree. In the data types video, we discussed that trees are well suited for hierarchical data.


[Slide 2]

If a client comes to us with a project that involves hierarchial data, we will start considering a tree. Then we should walk through the criteria for a tree. Recall that trees have a single root, children can have only one parent, there can be no disconnected components, and there must be no cycles. It is good practice to walk through different use cases with the client. Is there a case when an element has more than one predecessor? Is there a case where users could traverse from an element back to the same element? Furthermore, we would need to consider if we need a more specialized tree. 


[Slide 3]

In this course, we looked into two specific types of trees, binary trees and tries. There are many different types of trees beyond those which we discussed in this course. We will focus on these types though to discuss the hallmarks of when to use one over another. 

If there aren't restrictions on the relationships of siblings or children with respect to their parent, then a generic tree will do. 

If we have a data set where there is a clear ordering on the elements and the client wants to leverage this ordering, then a binary tree is a good choice. We defined these such that descendants to the left of a node will be less than the node and descendants to the right will be greater. Binary trees have many advantages when it comes to performance for tasks such as searching for elements. We will discuss this in more detail in the next module. 

If the data has a lot of elements with similar prefixes, then we could use a trie. Tries are especially useful in applications such as autocompletion utilities. The elements are not limited to strings, they can be a sequence of button clicks, directions, and much more. 


[Slide 4]

