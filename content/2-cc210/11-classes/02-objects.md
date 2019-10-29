---
title: "Objects"
pre: "2. "
weight: 20
date: 2019-09-24T00:00:26-05:00
---

{{< youtube pCMFGDodroQ >}}

#### Resources

* [Slides]({{< relref "/2-cc210/11-classes/02-objects-slides.md" >}})

#### Video Script

Once we have defined the attributes and methods that make up a particular class in our code, the next step is to create actual variables in our code that represent these items. For that, we need to look at the rest of the UML class diagram for this example program.

Specifically, we need a class to represent the actual program itself. Typically, we can think of this class as the "main" class, though in a later module we'll learn a slightly different way to look at it.

So, just like a class representing a student or a teacher, this main class can also have attributes and methods.

Since we are writing a program that represents a school, we'll probably need attributes to store all of the students and teachers at that school. In that case, we'll add attributes to the main class for each of those items. When we do, we'll quickly hit a roadblock since each attribute should also have a data type. We can't say that a student or a teacher can be represented by a single integer, or floating point value, or even a string. So, we'll need some new data type to describe those variables. We'll come back to this in a second.

Our program might also include some methods that help us update the data. For example, we could have a method to add a student or a teacher to the school, or a special method that starts a new school year by updating the students' ages, giving promotions, and calculating grades.

Of course, we would expect the `new_student()` and `new_teacher()` methods to return a new student or teacher, right? How can we show that in a diagram.

It turns out that this is the "secret sauce" that allows object-oriented programming to work. When we are defining these new classes, we are actually creating a new data type that we can use to represent each individual student or teacher. This is done through a process called "instantiation" where we create a concrete version of a class, called an object or an instance, that represents a specific person or teacher in this case. That object can then be stored in a variable, with the data type of that variable matching the name of the class that the object was created from.

So, in our UML class diagram for the program itself, we can update the data type of the `students` and `teachers` variables to be an array or list of `Student` and `Teacher` objects, respectively. Likewise, we can update the return types of the `new_student()` and `new_teacher()` methods to match.

This is the really powerful feature of object-oriented programming. We can create our own data types by defining classes, and then use those classes to represent individual objects in the real world. Those objects then can have attributes that describe them, and methods that can be performed by them or on them to update their values.

In the rest of this module, we'll explore how to do this in code.
