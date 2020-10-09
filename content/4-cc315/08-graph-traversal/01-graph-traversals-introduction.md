---
title: "Graph Traversal Introduction"
pre: "1. "
weight: 81
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/08-graph-traversal/01-graph-traversals-introduction-slides.md" >}})

#### Video Script

[Slide 1]

Graphs can represent a wide variety applications. For this module we will look at search algorithms we can use to extract information from them. To give some motivation, we will look a quick example of where these searches and traversals can be quite beneficial. 

In this example, we will use a maximum flow algorithm to determine the maximum number of vehicles that can leave Bill Snyder Family Stadium, in the top middle, and get to I70, in the bottom middle. 

I have chosen key intersections which play heavily in the exit strategy of fans who are trying to get to I70, those are circled in red. 

[Slide 2]

We can turn the previous map into a graph. Each intersection that was circled and the key points like the stadium and I70 are all represented as nodes. Each edge represents the route from one place to another. The values on each edges represents the vehicle capacity for some amount of time. These are fictional numbers that I have selected to reflect traffic flow. When determining infrastructure needs, the city, county, or state would evaluate this formally. 

For example, 50 is the number of cars that go from the stadium to Kimball and Tuttle Creek Boulevard.

We can use this abstraction to determine the maximum number of cars that can go from the stadium to the interstate. 


[Slide 3]

The procedure starts by assuming no cars are traveling. /slide4/

We then find a path from the stadium to the interstate that has still has some room for cars. /slide5/

We allow the maximum number of cars to travel via this route. While 177 can have 100 cars, the bottle neck at Kimball allows us to only let 50 cars through. /slide6/

Now we find another path that still has room and proceed in the same fashion. /slide7/

We allow the maximum number of cars through /slide8/

and find another path that still has room/slide9/

and allow for the maximum number of cars to go through.


[Slide 10]

We would then look for another path that still has room. All of the outgoing edges of the stadium have been filled so there is no more room for cars to leave. 

[Slide 11]

Thus, we end up with the following max flow diagram. Notice that the edge from Fort Riley Boulevard and 17th to Fort Riley Boulevard and Seth Child is gone? Since no cars were routed this way, we no longer needed it. 

[Slide 12]

We can now say that the maximum amount of people that can leave the stadium for I70 is one hundred ten. We can see this both in the outgoing edges of the stadium 

[Slide 13]

as well as the incoming edges for I70. For maximum flow graphs, it is crucial that we don't lose cars or gain cars. This means that the same amount that leaves the stadium must be the same amount that arrives at I70. 


[Slide 14]

Determining the maximum flow is not limited to ust traffic. It can be used for electrical wiring, water systems, emergency exits, and much more. Calculating the maximum flow of a graph is an example how we can use graphs to create abstractions of real world data and how we can use searches and traversals to leverage that data. 

In this module, we will learn traversal and path searching techniques so we can use graphs to their full potential. 