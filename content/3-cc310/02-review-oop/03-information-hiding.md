---
title: "Information Hiding"
pre: "3. "
weight: 30
date: 2020-01-20T00:00:26-05:00
---

{{< youtube prZ8vQbJQm0 >}}

#### Resources

* [Slides](/3-cc310/02-review-oop/03-information-hiding-slides.pptx)

#### Video Script

Slide 2

One of the foundational principles of object-oriented programming is encapsulation.  Encapsulation basically means to enclose something as if you put it inside a capsule. There is a clear separation between what's inside the capsule and what is outside.

In object-oriented programming, we use encapsulation to enclose both data and behavior within an object. This object defines a boundary that separates the object's data and behavior from the outside world.

Slide 3

Encapsulation is used to hide that data and behavior form external objects.

However, if we make it so that all the data and behavior of our object is hidden, it becomes virtually useless. Therefore, we need to find a way to restrict access to only that data and behavior that is necessary to make our object useful. We call this concept information hiding.

The goal of information hiding is to provide access to only those behaviors and data that are absolutely necessary for external objects to effectively interact with an object.

To do this, we typically only provide access to specific behaviors that are designed to interact with other objects. This ensures that an object can tightly control these behaviors and protect the object from misuse.  Access to data is typically given through special behaviors that control what data an external object can see or change.

Slide 4

Let's use a Coffee Machine as an example. If we make all attributes and methods globally accessible, we essentially give external objects free reign to do whatever they want with our data and behavior. It is like having a coffee machine with no external case where users can poke and prod at the internal structures and mechanisms of the machine while it is working. While some users would play nice and only do the right things, others would take advantage of the opportunity to mess with the internals, almost certainly leading to problems and a broken machine.

For instance, in our Coffee Machine class, external objects can directly manipulate the machine configuration and potentially change the associated brewing unit, or worse, delete it all together. Likewise, an external object could call the Brew Espresso method without first putting beans in the machine or selecting how to brew the coffee. At best, this will probably lead to inconsistent results and more probably wrong results or program exceptions.

Slide 5

We can use information hiding to solve these problems. We do this using public and private attributes and methods. External objects can access public methods and attributes; however, they get no access to the private methods and attributes.

In our Coffee Machine class, we have made all our attributes private. This is considered a 'best practice' in object-oriented programming. We can always allow external objects access through the use of getter and setter methods if needed. Remember, getter methods allow external objects to read the value of attributes while setter methods allow them to change the values of attributes. This approach is highly preferred since it allows us to ensure that changes made to the attributes will be controlled by the object itself.

For example, a class might have an integer attribute whose value should be between 1 and 10. By forcing external objects to use a setter method to change the value of that attribute, the setter method can ensure that the new value is in fact within the correct range.

The private methods 'Brew Espresso and Brew Filter Coffee' are hidden since they are used by the Brew Coffee method to implement its behavior and should not be called directly by an external object.

Slide 6

The public methods of a class make up what we call the class interface. (Remember, you shouldn't have any public attributes.)

The class interface is all an external object really knows about a class.

Slide 7

In both UML and object-oriented programming languages, we generally have a special interface entity. In general, an interface provides an abstract view of the methods an external object can use on objects that implement that interface.

As we will discover in later courses interfaces are very helpful in making our systems modular and easy to change.

Slide 8

To recap, objects encapsulate both data and behavior. And it's this encapsulation allows us to hide information from external objects.

We implement data hiding in objects by making all attributes and some methods private and only allowing access through a few public methods specifically designed to interact with external objects.

These publicly accessible methods define the class interface.
