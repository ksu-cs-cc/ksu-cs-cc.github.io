---
title: "Using Sets"
pre: "3. "
weight: 30
date: 2020-04-13T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/10-sets/03-using-sets-slides.pptx)

#### Video Script

[slide 2]

In this video, we are going to look at how sets and set operations can be used
to answer questions based on a set of data.

While you might not actually write an application like the one we are using,
this application will give you good insight into how relational databases work.
Relational databases organize data into tables that can be related to each other
based on data that is common to the different tables. We say we query the
database when we ask questions and use set operations to retrieve data to answer
our questions. 

[slide 3]

In this application, we will assume that we have three sets of data: workers,
family, and students. Each element in the sets represent people who fall into
the specific category.

[slide 4]

While some people only exist in one set in our database, several exist in
multiple sets.

So now we want to know, exactly what type of questions can I answer with these
sets and our set operations.

[slide 5]

An easy question to answer is how many people are in a particular set.

[advance]

In this case, all we have to do is call the getSize function for a particular
set, in this case, the workers set.

[advance]

Here the answer is 7, which is also easy to ascertain from the list of sets
shown. However, its not too hard to understand that if we had 585 students,
counting the exact number of students in the set is best left to the computer.

[slide 6]

So, lets look at a little more difficult question such as how many workers *and*
students there are. Looking at the list, we might be tempted to say, there are 7
workers and 7 students, so there must be 14 total, right? Wrong.

[advance]

To get the correct answer, we can use our union operation to create a set that
is a union of the workers and students set and then count that.

[advance]

Since Jordan is actually both a worker and a student, the total number of
workers and students is 13, not 14.

[slide 7]

So, let's see just how smart our database system is. Does it know that Jordan
both works and is a student?

[advance]

To see who is in both sets, we use the intersection operation and then convert
to a string for printout.

[advance]

And amazingly, the system does know that only Jordan is a student and works as
well.

[slide 8]

Let's try a little tougher question. Which family members do not go to school.
Clearly, unions and intersections are not going to help us here.

[advance]

To see which elements are in one set but not another, we can use the set
difference operation. Here, we want the operation family – students.

[advance]

And the answer is Amy, Scott, Lauren, and Zachary. Even with this small of a
dataset, it is getting a little tricky to manually compute these values. Lucky
for us, we have our set operations to do the work for us.

[slide 9]

So, let's try one more question, this time, even a little more difficult. Now,
we want to know who works, but does not go to school in the family. This
requires us to look across three sets to determine the answer.

[advance]

There are actually a couple of equivalent approaches we can take to get our
answer. One way to think about it is that we need to know who is in the
intersection of workers and family that does not go to school. That is the first
set of operations shown.

However, we can also think about it as the set of workers who are not in
students, but *are* in the family. In other words, the set difference between
workers and students, intersected with family.

[advance]

Regardless of which approach you use, the answer is still the same: Amy, Lauren,
and Zachary.

[slide 10]

In this video we have looked at a very simplistic version of a database system
and showed how we could use our basic set operations to answer questions that
might not be obvious to the naked eye, especially as the amount of data gets
large. Now, I certainly don't mean to suggest that database systems are this
simple internally, but they are based on sets and set operations.
