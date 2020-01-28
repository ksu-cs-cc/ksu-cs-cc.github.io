---
title: "Objects & Classes"
pre: "2. "
weight: 20
date: 2020-01-20T00:00:26-05:00
---

{{< youtube OcBIBGdkNTs >}}

#### Resources

* [Slides](/3-cc310/02-review-oop/02-objects-classes-slides.pptx)

#### Video Script

Slide 2

So, the question is: What is an object? And, why is an object so important for programming?

An object is simply 'an entity that contains both data and behavior'.

If you think about computation in general, there are two basic components that we are really interested in. Data, which is both an input to a problem and the output from a problem. And the process or function that we apply to the input data in order to get the output data.

Of course, by behavior, we mean that process or function.

So, let's look at some everyday examples of objects.

Slide 3

A car is a good example of a common object that is familiar to most people.

First off, let's describe a car.

This car is blue. It has 4 wheels.  It has 4 doors. It has 2 headlights and 2 tail lights. It also has an engine. And we could go on and on.

When we describe and object, we talk about its characteristics.  Or in object-oriented terms, its attributes.

So, what about its behavior? What can a car do?

Well, you can drive a car. You can open the doors. You can turn on the headlights. You can change a tire. And once again, we could continue with a list of other things that a car can do.

We can think of these behaviors as the functions of a car. In object-oriented terms, the functions of a car are its methods.

Slide 4

So, let's look at another example. Let's talk about a person.

How do we describe people?

The person is tall. The person has red hair. The person has green eyes. The person is funny, or laid back, or has a 'type A' personality. The person's name is Sally.

Once again, we describe a person in terms of their characteristics or attributes.

So, what do people do? A person eats, sleeps, reads, runs, walks, and studies.

Of course, a person can also drive a car. In this case, a person would use the behavior of another object: the car - to carry out its own behavior. Of course, in object-oriented terms, this would correspond to a person object calling a car object.

Slide 5

How are objects created?  Real world objects are created by other objects that perform functions to create new objects.

For instance, if we want to create a building, we would first create blueprint, or detailed description of what we wanted the building to look like. Then we would perform functions to create the building based on the blueprint.

We do the same thing with objects. Before we can create an object, we must create a blueprint for those objects. In object-oriented programming, this blueprint is called a class.

Once we have a class, we can create new objects by performing a function, which we call a constructor method. A constructor method creates a new object based on the blueprint provided by the class.

Slide 6

Here is a slightly different way to think about objects and classes.

In this example, the cookie cutter is the class and we use that class to create new objects. In this case, the objects are cookies made from our nice fresh dough.

The major difference between this example and object-oriented programming is that the objects in this example taste much better!

Slide 7

When we want to describe our classes to other people, we often use abstract representations. The standard for representing classes and object-oriented systems is the Unified Modelling Language, or UML.

Here is an example of a UML class for a Person. Notice that the characteristics of a person are captured as attributes, while the functions the person can perform as captured as methods.

We also have a special method ' the constructor ' that can be called by other objects. When the constructor is called, a new person is created with all the required attributes and methods.

[pause]

Hopefully this lecture has given you a better idea of what and object is and how we describe attributes and methods of objects using classes.
