---
title: "Traveling Salesperson Problem"
pre: "5. "
weight: 95
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/09-MST/05-MST-TSP-slides.md" >}})

#### Video Script

[Slide 1]

In this video, we will look at a classic graph problem, the traveling salesperson problem. This problem was originally introduced as a research problem in 1832 as a guide for traveling salespeople and is still being studied to this day! The goal of this video is not to formally introduce the algorithms for finding solutions, rather to gain an appreciation for the posed problem as well as results that have come from it. 

Since it was originally posed, researchers have found new ways to solve the task and improve upon the performance time to find the solution. Even as recently as August 2020, improvements have been made on the time it takes to find solutions. 

The premise of the problem is this: given a set of cities what is the shortest loop a travelling salesperson could make such that each city is only visited once and they end up where they started. Specifically in 1832, the goal was to find an efficient route for traveling sales tours of Germany and Switzerland. 

Another way to think of the problem is if you have a list of errands to do around town and each one is at a different location. What is the most efficient way for you to complete all of the errands without backtracking and so that you end up at home. 

[Slide 2]

As with many graph attributes and functions, this is not just limited to physical travel. We can also apply the traveling salesperson problem to computer hardware. For example, in microchips creators want to minimize the length of circuits that are connecting various components. Long circuits implies longer response time as well as generally just taking up more room. As more features are introduced, the architects of microchips must get creative in the design and can utilize the traveling salesperson problem and algorithms to determine the best layout. 

Another added complexity in this case is that micro chips can have layers. This would be analogous needing to go to specific levels of a building in the errands scenario. 


[Slide 3]

As I mentioned, we won't be going over how to solve this problem in this course. This is a notoriously difficult problem to solve. For a small number of nodes which can be cities, buildings, computer components and much more, it is relatively straight forward to determine a route. 

However, consider a graph with even just 30 nodes and each node is connected to every other node. This means that there are eight hundred seventy edges which in turn means there are one point three two time ten to the thirty second power possible solutions. Of all those solutions, we want to find the most cost effective! For reference ten to the twelfth is one trillion. 

We will finish this video with an informal demonstration. 