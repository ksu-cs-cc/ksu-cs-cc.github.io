---
title: "Weighted Graphs"
pre: "4. "
weight: 64
date: 2019-02-04T10:53:26-05:00
---

{{< youtube x4_myCOtFnk >}}

#### Resources
* [Slides]({{< relref "/4-CC315/06-graphs-M/04-graphs-weighted-graphs-slides.md" >}})

#### Video Script

[Slide 1]

The next portion of this module will cover specific types of graphs. The first we will discuss are weighted graphs. Weighted graphs are characterized by the edges of the graphs having values associated with them. These values can be monetary cost, distance, time, and more abstract things such as movie similarities, 


[Slide 2]

In this first example of a weighted graph, we have a segment of Japan's bullet train. Each node represents a station that the bullet train visits and each edge is the route between the stations. The edges in this example characterize the amount of time travelled between the stations. For example, the train ride from Osaka to Kyoto will be twenty eight minutes. 

Travellers can use this type of information to maximize their sightseeing while minimizing their travel time. 


[Slide 3]

When talking about weighted graphs, we can also discuss unweighted graphs. These are graphs in which the edges have no weights. They can look something like this example. 


[Slide 4]

When we encounter unweighted graphs, we treat edge as though it has weight equal to one. We use unweighted graphs when there is a uniform distance between connected nodes. For example, when we worked with trees, each edge would have weight one to represent one generation. 


[Slide 5]

In this video we have discussed weighted and unweighted graphs as well as potential applications. The weights of the edges will play a large part in our graph classes as they can convey a deeper understanding of the data. In the remaining portion of the module will discuss more features of graphs as well as the implementation. 