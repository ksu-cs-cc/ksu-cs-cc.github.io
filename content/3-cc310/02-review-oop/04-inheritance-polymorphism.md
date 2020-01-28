---
title: "Inheritance & Polymorphism"
pre: "4. "
weight: 40
date: 2020-01-20T00:00:26-05:00
---

{{< youtube 5CuGpd4iiUc >}}

#### Resources

* [Slides](/3-cc310/02-review-oop/04-inheritance-polymorphism-slides.pptx)

#### Video Script

Slide 2

Polymorphism literally means _many shapes_. So, what do we mean when we talk about polymorphism as related to object-oriented programming?

Basically, we mean that objects with similar characteristics basically behave alike. If you look at our example shown here. We have a few shapes: a circle, a square, and a star. Obviously, they are different in some ways, but they also have some similarities.

Notice that all our shapes have a color. We can also talk about their area and their perimeter. These characteristics are the things that make a shape, well a shape.

Slide 3

So, the concept of shape is really an abstraction. In the real world, there are circles, squares, and stars, but there are really no unique _shape_ objects. Every real shape has a particular type associated with it.

However, we often talk about shapes having a color, a perimeter and an area. These are the common characteristics that make a shape, whether it be a circle or square, a shape.

In our object-oriented terminology, we say that all shapes types _inherit_ common characteristics (such as attributes and methods) from our base shape class.

Slide 4

So, we use inheritance in object-oriented programming to implement polymorphism. But, why? What is so important about polymorphism in object orientation?

In essence, polymorphism talks about common characteristics and common behaviors among a set of related types of objects. With objects, it's not hard to see that these concepts manifest themselves as attributes and methods.

And, if we have common attributes and methods in objects, the we should be able to _share_ those common attributes and methods between objects.

Thus, the big deal with polymorphism and inheritance in object-oriented programming is that we can use it to support code reuse in a principled and organized manner!

We are not talking about cutting and pasting code here. We are talking about setting up a structure that allows us to write code once and share it automatically with all similar object classes.

Slide 5

So how exactly does inheritance work. We'll start with this example, one of my favorites: hamburgers!

First of all, we'll notice that there are definitely similarities between all the hamburgers shown. They all have bread, meat, and it looks like some ketchup and mustard.

You'll also see that all the similarities are captured in the top hamburger, which we call the _parent_.

The bottom two hamburgers, or the _children_, have everything the parent has, plus additional items such as cheese, lettuce, and best of all, bacon.  The two child burgers are different, but they are the same in terms of the items found on the parent.

Thus, we say the child burgers inherit from the parent burger.

Slide 6

A UML example of our burger hierarchy is shown here. While our example only shows attributes, we can also inherit methods as well.

If we created an instance of a Hamburger object, it would have 5 attributes: bread, patty, ketchup, mustard, and pickles.

So, if we created in instance if a Cheeseburger object it would have 6 attributes: bread, patty, ketchup, mustard, pickles and cheese.

Likewise, an object instance of a Bacon Cheeseburger would have all 5 attributes of the parent plus bacon and cheese.

As you look at this, you might have noticed that both child classes have added the cheese attribute. As designed, this would require us to create the same attribute in both classes, thus duplicating the same code in two different places. While this is a pretty trivial example, duplicating code can cause lots of problem. For example, if you changed the definition of the cheese attribute in the Cheeseburger, but not in the Bacon Cheeseburger, they would become incompatible.

So, you might ask, is there a better way?

Slide 7

The answer to that question is a definite "yes"!

It is possible to redesign our inheritance hierarchy such that the Bacon Cheeseburger is the child of the Cheeseburger class.

The key to this is the way inheritance works.  In this case, the Bacon Cheeseburger inherits all the attributes from the Cheeseburger class. And, since Cheeseburger inherits the bread, patty, ketchup, mustard, and pickles from the Hamburger class, so will the Bacon Cheeseburger.

Thus, if we created an instance of a Bacon Cheeseburger, it would have 7 attributes: bread, patty, ketchup, mustard, and pickles from the Hamburger class; cheese from the Cheeseburger class; and of course, its own bacon attribute.

Slide 8

Going back to our original shape example, I have created a UML diagram for it here. I left off the star shape to simplify the diagram.

Notice that in the abstract Shape class there is an _area_ attribute and a _getArea_ method that is inherited by the Circle and Rectangle classes. When we say Shape is an abstract class, we mean that we cannot create actual instances of that class, even though its definitions are inherited by its child classes. The fact that Shape is abstract is denoted in UML by its italicized name.

Thus, each child class takes the definition of the Shape class and adds to it. Because they are different shape types, each child class defines unique attributes and methods.

The Circle class defines a _radius_ attribute and two methods for getting and setting the radius.

The Rectangle class, as expected, defines _length_ and _width_ attributes along with the appropriate getter and setter methods.

Notice that each child class also defines a _getArea_ method, which has already been defined in the parent Shape class. This is necessary because each shape computes its area differently. Notice that the _getArea_ method in the Shape class is also italicized, which identifies it as an _abstract method_. An abstract method means that there is no implementation for it in the parent class and that any child class inheriting from the parent _must_ provide an implementation for that method. This is a great example of why abstract methods are important.

Slide 9

In this lecture we looked at polymorphism, which means literally many shapes.

Because polymorphism is such a powerful concept, we implement using inheritance in object-oriented programming.

Of course, the main goal of both polymorphism and inheritance is to reuse code in a principled and structured manner.
