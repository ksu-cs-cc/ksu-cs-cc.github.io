---
title: "Types of Data"
pre: "2. "
weight: 112
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/11-RA/02-RA-data-types-slides.md" >}})

#### Video Script

[Slide 1]

When building the requirements for a project, it is important to first understand the characteristics of the data. By understanding the data, we can determine which structures are or are not suitable for the task at hand. We will discuss six formats of data that we may encounter and what structure could be suitable. 

We should note that in some cases, there is not a clear cut best answer. In most cases, we can use more than one structure in conjunction with others. 

[Slide 2]

The first type of data we may encounter is unique data. This means that each piece of data only appears in the data set only once. We can think of these as typical unique identifiers like, social security number, phone number, physical addresses, and much more. 

There are a handful of cases in which we may work with only the unique elements. If we needed a program which assigns new students a school ID number, we could consider the available school ID numbers to be a unique data set. 

In real world applications, unique datasets typically do not stand alone. Elements are typically connected to other pieces of information.

[Slide 3]

In instances where we need to simply store the unique data, sets are a good structure. The set data structure acts like a bag of elements where we don't care about one elements relationship to another element. 

[Slide 4]

By contrast, elements of a linear data set rely on knowing which element it is before or after. Linear data can literally be thought of as elements forming a line. How the line is created and how elements are removed can vary widely on the given task. For example, if our dataset was a train schedule, then it would be important that trains which arrived first could leave first. 


[Slide 5]

Linear data can be modeled by a handful of structures, we have arrays, linked lists, stacks and queues. It is important, especially when contemplating the use of a stack or queue, to remember how the data will be utilized. For example, if we used a stack, which is a last in first out structure, then the train that arrives first thing in the morning may not leave with passengers until the evening. 


[Slide 6]

The next type of data that we may encounter is associative data. These data sets are characterized by elements being key value pairs where the key is unique. These can be conceptualized as a dictionary where all of the words are unique but they could have similar definitions. An example of this type of data set could be clients of a veterinarian. The key could be the owners name and the value would correspond to all of their pets and their associated files. 


[Slide 7]

Of the structures we have learned about, associative data fits very well with hash tables. That being said, in real world applications, such as the client data set, a relational database would be used. Relational databases are typically introduced in a course dedicated to them alone. 


[Slide 8]

The next type of data is hierarchical data. With this type of data, we have the notion of elements being on levels and we can characterize if one element is above, below, or on the same level as another. We may encounter this type of data when modeling product descriptions or government organization schemas. 


[Slide 9]

Hierarchical data is best suited to be used by trees. The specific type of tree is dependant on the data set itself. If there are strict constraints on how parents and children as well as siblings are organized then we could use a more specific type of tree, such as a binary tree or a trie. 

[Slide 10]

If a client comes to us with a project that involves hierarchial data, we will start considering a tree. Then we should walk through the criteria for a tree. Recall that trees have a single root, children can have only one parent, there can be no disconnected components, and there must be no cycles. It is good practice to walk through different use cases with the client. Is there a case when an element has more than one predecessor? Is there a case where users could traverse from an element back to the same element? Furthermore, we would need to consider if we need a more specialized tree. 


[Slide 11]

In this course, we looked into two specific types of trees, binary trees and tries. There are many different types of trees beyond those which we discussed in this course. We will focus on these types though to discuss the hallmarks of when to use one over another. 

If there aren't restrictions on the relationships of siblings or children with respect to their parent, then a generic tree will do. 

If we have a data set where there is a clear ordering on the elements and the client wants to leverage this ordering, then a binary tree is a good choice. We defined these such that descendants to the left of a node will be less than the node and descendants to the right will be greater. Binary trees have many advantages when it comes to performance for tasks such as searching for elements. We will discuss this in more detail in the next module. 

If the data has a lot of elements with similar prefixes, then we could use a trie. Tries are especially useful in applications such as autocompletion utilities. The elements are not limited to strings, they can be a sequence of button clicks, directions, and much more. 

[Slide 12]

Relational data can be summarized as data points having potentials connections to any other data point. The connections will typically be user defined either based on physical distance or similarity between elements. Similarity is a very broad term in this context. Suppose we have a client that wants to create a system that recommends breeds of dogs to a user based on a breed of dog they like. We could determine which breeds to recommend based on the similarity to other breeds. This could factor in things like average weight, height, color, and much more. 


[Slide 13]

Relational datasets, like the dog breed example, are well suited to be represented by graphs. Nodes would be the dog breed and the edges would connect the nodes with the weights corresponding to the similarities. Graphs allow for multiple elements to connect to any other number of elements. These connections can go in either direction in contrast to trees where connections were strictly one way.

Graphs are arguably one of the most versatile data structures as the connection of nodes is exclusively user defined. Connections can have an associated weight which is also user defined.

[Slide 14]

When selecting a graph as our data structure, we need to consider which type of implementation to use. 

[Slide 15]

We characterized this choice based on the density of the graph. If we have a dense graph, meaning there is a large number of edges, then we would use a matrix graph. If we have a sparse graph, meaning there is a small number of edges, then we would use  a list graph. 

When discussing with the client or user about the implementation, we should be sure to clarify this point. It is important to consider how dense will the graph be when it is initialized but also throughout time, will the density vary. Will the application be frequently adding or removing nodes? And will that make the graph more dense or more sparse?

[Slide 16]


Another requirement to determine would be if the graph needs to be weighted and or directed. In the example of the dog breeds, we would most likely use a undirected weighted graph. In situations where elements are just connected, we don't need to worry about a weight. 

[Slide 17]

The last type of data that we will cover is prioritized data. In this form of data, data points have an associated priority. Like similarity, priority can be quite broad in this context. The priority of items in a data set can range from cost of a task to energy expended for a task. We may be inclined to think that prioritized data and associative data are one in the same. However, with prioritized data, elements can have the same priority. In associative data, the keys must be unique. 


[Slide 18]

In this case, the name of the data set reveals the structure we would use: priority queues. Depending on the particular task we may choose a minimum priority queue or a maximum priority queue. This is dependant on if the client wants to access elements with the lowest priority or greatest priority.

[Slide 19]

It is good to verify with the client how they are wanting to order the priority. For example, suppose we were creating a program to determine the next patient to see in an emergency room. We would want to sort our priorities such that the most urgent cases got seen first. 


[Slide 20]

Based on the format of the data, we can get an idea of what structures we may use. Once we have a preliminary structure in mind though, we will need to take more functional aspects into account. In the next videos, we will look at examples of situations where we may use each structure from 315 and some questions we should ask ourselves about the specifics. 