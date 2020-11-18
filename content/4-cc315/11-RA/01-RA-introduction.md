---
title: "Introduction"
pre: "1. "
weight: 111
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zcCtPamophM >}}

#### Resources
* [Slides]({{< relref "/4-cc315/11-RA/01-RA-introduction-slides.md" >}})

#### Video Script

[Slide 1]

This module as well as the next module will focus on translating the data structures we learned into the real world. We will discuss the requirements analysis in this module and then a performance analysis in the next. 

[Slide 2]

When we are brought on to a project or someone proposes a new project to us, one of the first steps should be to complete a thorough requirements analysis. This is twofold process where we gather information to verify that we understand the intended functionality. Then the second step is to clearly define the requirements. These requirements are then the basis upon which we build the software or project. Understanding the requirements is a crucial step in building software that functions as the customer wants and building it properly.

[Slide 3]

While doing the requirements analysis, there are three key factors that should define the final requirements. 

First, are these requirements quantifiable. Building quantifiable requirements means that we must have specific details of what the client wants. For example, suppose a client simply says that they want a program which loads files in and converts them to another file type. While on the surface this may seem specific, it is actually quite vague. Follow up questions could include
- are the input files all of the same type such as text files, pngs, jpegs? or will there be a variety of file types
- similarly, are the outputs expect to be all of the same file type? 
It is important to ask these types of questions in analysis and development so when implementation comes, we know what to expect. 

The second criteria is to build requirements which are relevant. From the previous example, we may be tempted to add in the ability to convert audio files. However, that won't be relevant to the client if the use case for the converter is exclusively text files. 

The third criteria is that the requirements must be detailed and the more detail the better. As we build the requirements, if we try to be more and more detailed, this can raise areas of uncertainty in the desired functionality. This is a great time to go back the client and request more information. As I mentioned, the more detailed you make your requirements, the better they will work for you. By spending more time in the development and analysis phase, we can expedite the implementation phase. 

[Slide 4]

When building our requirements there are three questions we should ask ourselves about the proposed solution:
- does it work?
- would someone else understand what I did?
- does it perform well?

We will address the first two questions in this module and the last question will be answered in the next module. 

[Slide 5]

The first question was, does it work? When we ask ourselves this question, we think about the following. 

First, does this maintain real world relationships. Going back to our example of the file conversion, it wouldn't make sense to try to convert an audio file to an image. This is not a real world relationship. 

Secondly, does this capture all of the aspects and intricacies of the data? For example, if we are implementing a tree, are we maintaining the proper relationships between parents and children. 

Lastly, is this an efficient way to implement this. This question can also fall into the category of performance. In this context, we are referring to the use cases of the data. Is there a better way that we could go about accessing elements that may make it more efficient. 


[Slide 6]

The second guiding question was, will someone else understand this. There is a certain amount of novelty in a solution, however, we want to be cautious about being too clever. If we were part of a software development team, it is important to find solutions that can be easily understood in case a project needs to be handed off. We should also be in the habit of properly documenting our code. Some problems that we may encounter could actually require a clever solution. It is especially important in these cases to document and comment our code. 


[Slide 7]

The final question addresses the actual performance of the requirements and implementation which we will examine in the next module. However, we can keep this in the back of our minds as we move through this module. We need to ensure that our solution is efficient in terms of both time and space. 


[Slide 8]

As we work through the rest of this module, it is good to keep all of these factors in mind. We will discuss the types of data we may encounter and some characteristics of the various data structures we introduce in this course. Our goal is to properly build up the requirements such that they meet the desired criteria. 