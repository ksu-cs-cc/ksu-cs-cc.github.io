---
title: "Python Standard Types"
pre: "8. "
weight: 80
date: 2020-04-24T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/12-performance/08-python-libraries-slides.pptx)

#### Video Script

[slide 2]

Up to this point, we've focused on creating our own data structures in this course. This is important because it helps us fully understand how they are built, how they differ, and the performance characteristics each one provides. 

Thankfully, most common programming languages today include a wide variety of basic data structures we can use. In this video, we'll quickly review the data structures that are part of the Python language's standard types, which we can use in our programs from here on out.

For all of these, I encourage you to review the official documentation provided in the Python reference documents, as well as the Python tutorials and other online resources. They provide a plethora of information and examples for how to use these structures in our programs.

First and foremost, Python includes built-in support for tuples, allowing us to combine multiple data items into a single object. Tuples are very powerful because they allow us to quickly combine and store related values in a single variable, such as x and y coordinates in a 2D game. 

Throughout this course, we've been using Python Lists in the same way that we would use arrays in other languages. However, Python lists also implement many additional features, such as the ability to resize as needed. However, Python lists have the same performance characteristics as arrays in other languages. For example, inserting or removing elements from the beginning of a list in Python runs in the order of N time, since it will try to shift elements around in memory as needed. So, even though they are called "lists", it is better to think of them as arrays. 

Python also includes a Deque type (short for double ended queue) that serves as a great implementation of a doubly-linked list. This is also the recommended class for both stacks and queues, since it provides constant time insertion and removal from either end of the structure. In fact, the Deque type in Python provides special methods just for using it as a stack or a queue!

Python also includes a type called a dictionary that is an implementation of a hash table, just like we explored in this class. Python also includes a hash method that works with most objects, so this structure can be used to get near constant time access and retrieval of data based on hashable keys. 

Finally, Python includes a special type for a set, which uses a hash table behind the scenes. This provides near constant time set operations as well. We can even use it in combination with some of the binary operators such as the ampersand for intersection and the minus sign for set difference. 

In addition, you should definitely review the methods available in for all of the Python types discussed here. Many of these data structures include methods for sorting and searching that use efficient implementations based on the structure of the container. 

The standard types in Python are a very powerful part of the Python programming language. Now that we understand what these data structures can do, we can use them effectively in our own programs. 