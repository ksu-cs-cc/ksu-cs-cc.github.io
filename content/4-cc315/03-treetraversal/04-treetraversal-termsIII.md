---
title: "Traversal Terms III"
pre: "4. "
weight: 34
date: 2019-02-04T10:53:26-05:00
---

{{< youtube En7FDq5XrsA >}}

#### Resources
* [Slides]({{< relref "/4-CC315/03-treetraversal/04-treetraversal-termsIII-slides.md" >}})

#### Video Script

[Slide 1]

We can now talk about navigating trees. We have loosely discussed paths when we talked about ancestors, heights, and other vocabulary. We will formally define what a path as well as a traversal. Both of these concepts are ways that we can transform our hierarchical data structure into linear structures. 

[Slide 2]

To motivate this new vocabulary, we will use the following tree as an example. 

Suppose that we wanted to find a path between node `A` and node `J`. We can define this visually as taking the edge between `A` and `B` then the edge between `B` and `D` and finally `D` to `J`. 

[Slide 3]

Here we have outlined the path and listed the path. As an aside, we can note that paths in trees will always be unique. Meaning that there is only one way to get from one node to another. This is because nodes cannot have multiple parents.

[Slide 4]

One goal of traversals is to transform the hierarchial data into linear data. All data that is stored and used in computers is a linear series of zeros and ones. 

To be able to accurately record and read hierarchical data from a linear format, we must follow standards. This allows us to be able to correctly read and write trees regardless of operating system, software, and so on. 

For general trees, there are two main types of traversals: preorder and postorder traversals. These are both defined recursively. Next, we will over each type of traversal in separate videos. 