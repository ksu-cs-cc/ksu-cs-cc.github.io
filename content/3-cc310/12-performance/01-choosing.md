---
title: "Choosing the Right Structures"
pre: "1. "
weight: 10
date: 2020-04-24T00:00:26-05:00
---

{{< youtube kP_7u0Aw10w >}}

#### Resources

* [Slides](/3-cc310/12-performance/01-choosing-slides.pptx)

#### Video Script

[slide 2]

In this course, we covered a wide variety of different data structures. We started with arrays, and learned how to build stacks and queues using arrays. Then we learned about linked lists, and how they use an entirely different structure to perform many of the same tasks that an array can perform. We also looked at how hash tables can use both structures to create a "best of both worlds" approach, and how the use of arrays combined with a hash function can build very efficient implementations of the classic set data structure. 

[slide 3]

In each module, we spent a little time discussing the performance of each data structure and the instances where it might be useful. In this module, our goal is to combine all of that information into a single, useful resource for us to help us decide which data structure we should use in our programs. This topic is a very important topic for computer programmers at all skill levels, and many times it can become one of the most important decisions we make when developing a new program. 

In this video, we'll look at three important questions we can ask ourselves when determining which data structure we should use in our programs.

[slide 4]

First and foremost, I think it is most important for us to ask the simple question "does it work"? While this may seem obvious, I feel that many times we skip right past this question and start looking at the coolest or most interesting data structure available. For example, we can easily use linked lists to store large amounts of data, but would an array work just as well? Or maybe a hash table? If we know that each element will be unique, should we use a set instead?

These are very basic questions, but they help us understand if there are any data structures that are particularly well suited to our task, or, conversly, if there are structures that simply would not work. By making that determination first, we can limit the number of data structures we must consider when looking at the next question.

[slide 5]

Once we have an idea of which data structures would work well for our program, the next question to ask is "is it understandable?". This question may also seem obvious, but I think it is a very important part of being a programmer. Just because it is _possible_ for us to use a particular data structure in our program doesn't mean that it is the best choice. 

Consider the situation where we want to store names, phone numbers, and grades for students. We could create three arrays, one to store the names, another for phone numbers, and a third for grades. Then, we just know that the elements in each array at a particular index represent the same student. That approach would totally work, right?

Compare that to a similar approach where we create a class to represent a student, and each student object contains a name, phone number, and grade as attributes. Then, we just have a single array storing student objects. Would that approach be a bit easier for another programmer to understand?

I think that many times we feel that, as programmers, we want to be the most "clever" when we write our code. Unfortunately, the "clever" solution may not be the most understandable, and sometimes it is better to just build our programs the boring, predictable way so that they are easy to understand and update later on.

[slide 6]

Finally, once we've selected data structures that will work and are understandable, then we can ask ourselves "is it performant?" Performant is a fancy word that encompasses the idea of speed, efficiency, and minimal memory usage all in a single term. This is the place where we can start looking at the performance characteristics of the data structures we've chosen and see which one would perform better. 

[slide 7]

Unfortunately, the factors of speed, efficiency, and memory usage can form a "trilemma", which is a classic type of problem in many different fields. In a trilemma, increasing one attribute can cause a decrease in the other two. A classic quote from the world of business puts it simply: "good, fast, cheap: pick any two". 

In the case of data structures, we can equate the concept of "cheap" with memory useage or simple code, and "good" with the ability of the structure to perform a variety of useful tasks. 

[slide 8]

For example, we could think of a hash table as a good and fast data structure. However, what it gains in speed it loses in understanability, since hash tables are quite a bit more complex than most of the other data structures we learned about in this course.

[slide 9]

Likewise, an array might be an example of a fast and cheap data structure. Using arrays can be super fast, and they are built-in to many different programming languages. However, they may not be very good, since arrays really don't implement the features we'd need for stacks, queues or other data structures directly. Instead, we'd have to build our own structures around the core array structure. 

[slide 10]

Finally, a linked list might be a good example of a good and cheap data structure. It has lots of cool features, but it can be slow when we have to search through the structure for a particular item. We can get much better performance from arrays and hash tables in many cases, but linked lists would still work reasonably well. 

[slide 11]

Overall, the choice of which data structure to use for a particular problem is very complex, and there are a variety factors to consider. Thankfully, by asking ourselves some simple questions, we can work through the analysis and hopefully find a data structure that works well for us. 