---
title: "Graphs"
pre: "4. "
weight: 114
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/11-RA/04-RA-graphs-slides.md" >}})

#### Video Script

[Slide 1]

In this video we will discuss some situations where we might utilize graphs and the types details of the data we need to verify with the client. In the data types video, we discussed that graphs are well suited for relational data.

Graphs are arguably one of the most versatile data structures as the connection of nodes is exclusively user defined. Unlike trees, connections between elements can go both directions. Connections can have an associated weight which is also user defined.

[Slide 2]

When selecting a graph as our data structure, we need to consider which type of implementation to use. 

[Slide 3]

We characterized this choice based on the density of the graph. If we have a dense graph, meaning there is a large number of edges, then we would use a matrix graph. If we have a sparse graph, meaning there is a small number of edges, then we would use  a sparse graph. 

When discussing with the client or user about the implementation, we should be sure to clarify this point. It is important to consider how dense will the graph be when it is initialized but also throughout time, will the density vary. Will the application be frequently adding or removing nodes? And will that make the graph more dense or more sparse?

directed/weighted