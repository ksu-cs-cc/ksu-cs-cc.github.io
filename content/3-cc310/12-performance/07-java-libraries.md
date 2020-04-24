---
title: "Java Collections Library"
pre: "7. "
weight: 70
date: 2020-04-24T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/12-performance/07-java-libraries-slides.pptx)

#### Video Script

[slide 2]

Up to this point, we've focused on creating our own data structures in this course. This is important because it helps us fully understand how they are built, how they differ, and the performance characteristics each one provides. 

Thankfully, most common programming languages today include a wide variety of basic data structures we can use. In this video, we'll quickly review the data structures that are part of the Java Collections library, which we can use in our programs from here on out.

For all of these, I encourage you to review the official documentation provided in the Java API reference, as well as the Java tutorials and other online resources. They provide a plethora of information and examples for how to use these structures in our programs.

First, Java has an ArrayList class that implements a resizeable array. In effect, it gives us the same performance characteristics of an array, while automatically handling resizing as the container grows as needed. However, because it needs to shift elements around when elements are inserted at the beginning of the array, it may not be an ideal choice for some structures.

Java also includes a LinkedList class that serves as a great implementation of a doubly-linked list. This is also the recommended class for both stacks and queues, since it provides constant time insertion and removal from either end of the structure. In fact, the LinkedList class in Java provides special methods just for using it as a stack or a queue!

Java also includes a class called HashMap that is an implementation of a hash table, just like we explored in this class. Every Java object also includes a hash code function, so this structure can be used to get near constant time access and retrieval of data based on hashable keys. 

Finally, Java includes a special version of a hash table that implements a set, called the HashSet class. This provides near constant time set operations as well. Unfortunately, it doesn't include many of the classic set operations such as union or subset, but those operations can be simulated using other operations such as removing or retaining all elements from a second set.

In addition, you should definitely review the methods available in the Java Collections and Arrays classes, as they include many standard algorithms that work for a variety of data structures in Java. This includes implementations for sorting, searching, and shuffling data as well as finding minimum and maximum values.

[slide 3]

One of the most useful features of the Java Collections library is the use of Generics. Generics is a difficult concept to describe without getting super technical, but in effect it allows us to declare the data type that our collection should be storing when we create it, and then the Java compiler will help us enforce that type restriction throughout our code. This is much simpler than the Object-based structures we built in this class. You probably got pretty tired of always having to remember to cast the objects you retrieved from the structure back to the correct type!

This slide shows an example of using Generics with an ArrayList. In the highlighted line, we used the class name Integer inside of angled backets to show that this ArrayList should store items that are Integers. 

Now that we've done that, Java will automatically convert our numeral integer values to Integer objects, and then when we retrieve them it can reverse the process. So, no more having to worry about casting and converting data types!

In addition, if we try to place an element in the ArrayList that is not an integer, the Java compiler will raise an error when we try to compile the code, helping us detect and correct those errors quickly.

The Java Collections library is a very powerful part of the Java programming language. Now that we understand what these data structures can do, we can use them effectively in our own programs. 