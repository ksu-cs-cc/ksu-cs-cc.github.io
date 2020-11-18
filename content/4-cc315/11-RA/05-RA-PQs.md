---
title: "Priority Queues"
pre: "5. "
weight: 115
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/11-RA/05-RA-PQs-slides.md" >}})

#### Video Script

[Slide 1]

In this video we will discuss some situations where we might utilize priority queues and the types details of the data we need to verify with the client. In the data types video, we discussed that priority queues are well suited for prioritized data.


[Slide 2]

In this course, we looked exclusively and minimum priority queues as we were trying to minimize path costs in graphs. We can similarly define maximum priority queues where the first element is the element with the highest priority. It is good to verify with the client how they are wanting to order the priority. For example, suppose we were creating a program to determine the next patient in an emergency room. We would want to sort our priorities such that the most urgent cases got seen first. 