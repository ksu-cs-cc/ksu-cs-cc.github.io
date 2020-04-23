---
title: "Sets Overview"
pre: "1. "
weight: 10
date: 2020-04-13T00:00:26-05:00
---

{{< youtube XJSPN3tx7As >}}

#### Resources

* [Slides](/3-cc310/10-sets/01-overview-slides.pptx)

#### Video Script

[slide 2]

In this video, we will introduce sets. While most people think of sets as
mathematical concepts, they actually show up in a variety of places, especially
in computer science. Today, we are generating and storing more data than ever
before, and much of that is stored in relational databases. And what is the
basis of relational databases? You got it, sets.

Sets are also critical to a lot of theoretical computer science as well. While
we will not get into much of that theory, let’s just say that many of the
advances in high assurance software engineering, cybersecurity, and programming
languages are based on sets.

But what is a set? Basically, a set is a collection of well-defined things that
are generally related to each other. For example, the students taking this
course can be thought of as a set of students. The shirts in your closet can
form a set of shirts. The numbers greater than 3 but less than 35 also form a
set of numbers. The numbers less than 0 form another set of numbers.

The things in sets are called elements. So, if we have a set of letters, each of
the letters in the set are elements of the set.

[slide 3]

So here we have an example of two sets. Set A is a set of letters and set B is
another set of letters.

[slide 4]

One of the first things you might notice is that there are no duplicate letters
in set A. Likewise, there are no duplicate letters in set B. This is one of the
basic rules of sets, no duplicates allowed.

[slide 5]

You probably also noticed that the letters in each set are just kind of thrown
in there haphazardly. Some of you who really like things neat and orderly
probably want to sit down and rearrange the letters so that they are in order.
You can't do that. That's another basic rule of sets, there is no order! In set
A, you cannot say that element x comes before y.

[slide 6]

Another way of representing sets is to use what is called "set notation" as
shown here. Set notation simply lists the elements of a set, enclosed by curly
brackets. Now, it may look like we have ordered the set, but we have not.

[slide 7]

It is just as correct to list the elements of set A as we shown in the second
line. Both of these set notation are correct and are equivalent to each other.

[slide 8]

Now, there are a couple of special sets that you need to know about. The first
is the universal set. The universal set contains all elements within our
"universe of interest". So, you may be asking, what is a "universe of interest"?
A universe of interest is the set of all elements within a particular context.
For instance, in our example, our context is the Latin alphabet of letters. All
sets are actually a subset of the universal set, which we usually represent by
the uppercase letter U.

Then there is the opposite extreme, the empty set. The empty set contains just
what it sounds like, nothing! The empty set is unique in the mathematical sense.
That is, there is exactly one empty set and it doesn't matter what universe of
interest we are talking about

[slide 9]

Another important concept we need to understand when dealing with sets is that
of a subset. Basically, one set is a subset of another if each of the elements
in one set is also a member of the second set.

In the example shown, set B is a subset of set A, since each element of B – B,
Q, and i – are also elements in A.

[advance]

This can be shown by drawing set B completely within set A in our diagram.

Next, we will start to look at some basic operations that are extremely useful
when dealing with sets.

[slide 10]

The first of these operations is the union. If we overlap our sets so that the
common letters, B, Q, and i line up on top of each other, we effectively create
a new set consisting of all the letters in both sets A and B with no duplicate
letters.

[slide 11]

This combined set is called the union of sets A and B and includes all letters
in the green area. Now, its important to remember that the union of sets A and B
creates a new set and does not get rid of either set A or set B. So after the
operation, we will have three sets: A, B, and A union B.

The union operation is very useful when we want to combine elements for several
different sets. For instance, if we have sets of students based on the classes
they are taking, we can answer questions such as which students are taking
either English 101 or Computer Science 150. All we have to do is to perform the
union operation on the set of student in 101 and the set of student in 150.

We can also write the union set using the "cup" symbol shown below. The union
operation is very simple to understand, we just have to remember to not include
duplicate elements.

[slide 12]

The intersection operation is very similar to the union operation. However,
instead of including all letters from both sets, we only include those letters
that are common to both set A and set B. This is the overlapping part of our
sets as shown here in green, which includes only Q, B, and i. The rest of the
letters are not in the intersection.

The intersection operation is very useful when we want to find elements that are
in two different sets. For instance, in our example of sets of students in
specific classes, we can answer questions such as which students are taking both
English 101 and Computer Science 150. The answer is the intersection of those
two sets.

We can write out the intersection operation as shown using the inverted cup
symbol. Like with the union operation, the intersection operation produces a new
set and does not get rid of sets A or B. This property is true of all the
operations we will look at in this lecture.

[slide 13]

Next, we'll look at the difference operation. Basically, the difference
operation takes all the elements in one set, A, and removes all the elements
that are also in a second set, B. The result is shown in the green area. We
write the difference operation using the minus sign, A – B.

Using our example from the previous slide about students and classes, the
difference operator can help us answer questions like how many students are in
English 101 who are *not* taking Computer Science 150. Of course, the answer is
the set of students in English 101 – the set of students in Computer Science
150.

[slide 14]

Here is the same difference operation, only we have swapped the order of the two
sets. In this example, we are computing set B – set A. Based on the definition
and the diagram shown, its easy to see why the result of the difference
operation depends on the order of the sets. In this case, B – A, we take all the
elements in set B and remove all the elements of set A.

[slide 15]

A slightly different type of operation is the product, or cartesian product. The
product operation does not use elements from other sets to create its new set,
it actually creates new elements for it's new set from the elements of the other
sets. More precisely, the product operation creates new elements by pairing the
elements of the sets together.

To produce the element for A x B, we take each element of A and create a new
element in the set by pairing it with each element of set B. This produces a new
set whose elements are all pairs. As we shown the product here, each element
from set A forms its own row

[advance],

while each element from set B forms its own column

[advance].

[pause]

[slide 16]

The last operation I will introduce today is the powerset operation. The
powerset operation produces a set that includes all possible subsets of our
original set. As we see here, the powerset of A includes the empty set, all
subsets with exactly one element from A, all subsets with two elements from A,
and finally A itself.

As we see, sets can be elements in another set. In fact, the empty set is the
subset of every possible set, including itself!

[slide 17]

So we reach the end of our short introduction to sets and set operations. We
learned that sets are an unordered, collection of things, where duplicates are
not allowed. We also looked at several operations that we can use to manipulate
sets. And it turns out that these operations are underlying much of today's
database technology.
