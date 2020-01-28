---
title: "Associations"
pre: "5. "
weight: 50
date: 2020-01-20T00:00:26-05:00
---

{{< youtube mNHRPclA0DI >}}

#### Resources

* [Slides](/3-cc310/02-review-oop/05-associations-slides.pptx)

#### Video Script

Slide 2

Object-oriented programming works by having one object call methods of a second object to perform computation or share data.

However, in order for object A to call a method in object B, object A must know how to find, or reference object B.

If A and B are in a long-term relationship: meaning they interact with each other over a fairly long period of time - they will need to store their references long-term as an attribute. When one object holds a reference to another object in an attribute, we call this a _link_. Examples of such long-term relationships might include a person owning a house, or a student being enrolled in a class.

Slide 3

While links are actual instances of one object maintaining a reference to another object. At the class level, we capture the definition of these links as _associations_.  An association is related to a link in the same way a class is related to an object. A link is an _instance_ of an association.  

In the class diagram shown, we denote an association as a line between two classes. Each association has a name and may have role names for each class in the association.

Slide 4

To make our example a little more concrete, let's assume our two classes are Person and Car and the association between them is the _owns_ relation. This makes sense because a Person owns a Car.

Each class also has a role name in the association. In this case the Person is the owner and the Car is simply the car. We often use the role names to define the attributes that will hold the reference to the other object.

In this case, we might have an attribute of type Car in person that references an object of type Car. We would typically give this attribute the name defined by its role name, _car_.

The same is true for the Car class who would have an attribute named _owner_, which would be of type Person.

This type of association is called a two-way association since each class in the association keeps a reference to the other.

Slide 5

In this class diagram, instead of a simple line, we use an arrow pointing from one class to the other. (By the way, I've left off the association and role names to simplify the diagram: in a complete UML diagram, you are always expected to name your associations and roles.)

An arrow is used to denote the "navigability" of the association. In this case, it means that class A will have a refence to class B, but class B does not maintain a reference to class A. This would be the situation where the Person knew which Car it owned, but the Car had no idea which Person actually owned it.

Such one-way associations are quite common in object-oriented programming since keeping track of two-way associations can be prone to inconsistencies.

Slide 6

As we already discussed above, an association with a simple line denotes a two-way association. It is basically equivalent to having arrows on both ends of the association.

A two-way association type has the constraint that says if object A has a link to object B, then object B must have a link that points back to object A.

Two-way associations can be difficult to implement and require that there be code designed to ensure that this constraint is always satisfied.

Slide 7

To this point, we've assumed that an object has a reference to only one other object in an association. However, this is not always the case.

Objects can reference multiple objects of the same class type. For instance, a person may own multiple cars, or for that matter, zero cars.

To denote these situations, we use the concept of multiplicity, which can be confusing.

Basically, multiplicity defines how many of each type of object a single object may be linked to at any point in time.

In this example, an object of Class A can hold a reference to exactly 1 object of Class B.

Slide 8

In general, the multiplicity notation allows us to specify a minimum number of references as well as a maximum number of references.

As shown here, the minimum number is _m_ and the maximum number is _n_.  These multiplicities form constraints that must be ensured by the object's methods. As you might expect, maintaining this constraint is not simple.

First, the attribute implementing the association must be a collection type for any situation other than a simple 1:1 association.

Next, the constructor must ensure that no less than _m_ and no more than _n_ references to objects are available when an object is created. This may be accomplished by having the constructor require the appropriate number of references be passed to it, or the constructor may actually go out and create the required number of objects to reference.

Finally, every time a change is made to the association attribute, it must be checked to ensure that the constraint is not violated.

Slide 9

Here we have a simple 1:1 relationship, which can be implemented as an attribute that references an object of Class B. This short cut notation basically says that the minimum is 1 and the maximum is 1.

The only tricky part here is that the attribute must always reference exactly one object of Class B. So, as discussed in the previous slide, the constructor must ensure that this constraint is not violated at creation and the object's methods must ensure that the attribute always points to an object.

Slide 10

In this example, the star in the multiplicity means _unlimited_, which effectively states that an object of Class A can hold 1 or more references to Class B type objects.

Obviously, the association attribute in Class A must be able to point to a collection of objects of Class B.

Again, the Class A methods must ensure that the minimum constraint of having at least 1 object in the collection is maintain.  

Slide 11

As in the previous example, the star means _unlimited_, but in this case there is no minimum number of objects that must be referenced.

This multiplicity is fairly easy to implement since you will simply need to use a collection to hold the refences and ensure that only objects of Class B are allowed into the collection. You do not need to worry about enforcing a minimum constraint.

Slide 12

And probably the easiest multiplicity to implement is the 0 to 1 multiplicity. Essentially this multiplicity means that a Class A object may hold a refence to a Class B object, but it doesn't have to.

This is easily implemented as an attribute of type Class B, assuming you are working in a typed language such as Java or C. For untyped languages, you will need to ensure that the attributed only points to objects of Class B. And, there is no minimum constraint.

Slide 13

Associations describe relationships between classes. They are necessary for any non-trivial program and result in links, or refences between objects in the system.

Whether an association is one-way or two-way determines if just one or both objects must keep references to each other. As we discussed, two-way associations are more complex and difficult to maintain.

Finally, multiplicity determines the number of objects that may be referenced by given object. This multiplicity dictates what type of structure is used to hold the references as well as the complexity of maintaining the multiplicity constraints.
