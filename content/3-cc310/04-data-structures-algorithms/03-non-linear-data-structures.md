---
title: "Non-Linear Data Structures"
pre: "3. "
weight: 30
date: 2020-02-11T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/04-data-structures-algorithms/03-non-linear-data-structures-slides.pptx)

#### Video Script

[Slide 2]

Non-linear data structures allow us to store data using multiple dimensions. One
of the key elements of non-linear structures is that we can use them to capture
relationships beyond that of a simple ordering. In fact, the relationships
between the data stored in these types of data structures are often as important
and sometimes even more important than the data we actually store in them.

Like linear data structures, there are several different non-linear data
structures we can use, each with their own set of strengths and weaknesses.

[Slide 3]

The most general version of a non-linear data structure is the *graph*, as shown
in this diagram. Formally, a graph is a set of *nodes* that are connected by a
set of *edges*. Data is generally the main data storage, although edges may also
contain data.

Graphs excel at storing data that also have important relationships. For
example, graphs are often used to capture structures such as city maps or social
networks.

We typically use graphs when the relationships between the data are important
and there are no well-defined requirements for what those relationships might
look like. Graphs are extremely general and flexible.

[Slide 4]

A *tree* is a graph with special constraints that we can use to increase the
efficiency of data storage and retrieval.

These constraints require that each *tree* be a graph with a single *root* node
with one or more *child* nodes. Child nodes can also be *parent* nodes that have
their own children as well. The parent-child relationship is the key
relationship in a tree and what produces its hierarchical structure.

Trees are very useful for storing data that has been or needs to be sorted in
some way. Such trees generally have efficiency advantages over storing and
retrieving data in simple linear structures.

Trees are also tailored made to store hierarchical data such as family trees or
class inheritance structures. These trees can make answering questions like “Who
was John Adams’ great-grandmother?” a fairly straightforward and efficient
process.

[Slide 5]

A special kind of tree is called a *trie*, which is typically used to represent
textual data. While their scope of use is narrow – generally limited to things
like a spell-checker or keyword completion – the fact that those applications
are embedded in so many other applications makes *tries* a very important data
structure.

Essentially tries are trees where the edges represent the next letter to be
added to a word. In our example, you can see how you start at the root node,
which starts with no letters. You then walk down the tree following the first
letters in the word to find complete words. If you follow this trie and the user
has input the letters “t” and ”e” into the text editor, your word completion
application could suggest “tea”, “ted” and “ten” as possible completions. The
key to trie’s is how little computation is required to produce these results.

[Slide 6]

Finally, we come to a heap. A *heap* is a specialized version of a tree whose
goal is to always be able to quickly retrieve either the smallest or largest
element in the data structure.

A heap has some specific rules we have to follow, but first you need to know
whether your goal is to return the smallest or largest elements.

Assuming we want to access the largest number, we would store the largest number
at the root node and require that each parent node be larger than all of its
children. We also attempt to minimize the height of the tree, which is the
number of levels in the tree.

These rules allow a heap to be the most efficient data structure for managing
*priority queues,* where we always want to retrieve the highest (or lowest)
priority item each time we retrieve an item from the heap. Because of this,
heaps are very important in creating efficient algorithms that deal with ordered
data.

Heaps are a special type of a tree that is concerned with efficiency over
everything else. But, because they are so specialized, they only have a few
applications.

[Slide 7]

Non-linear structures are generally much more flexible than linear structures.
We can use the edges between data nodes to capture a wide variety of
relationships. The most general form of a non-linear structure is a graph.
Graphs can be designed to be very specific to an application domain and capture
several types of data and relationships.

However, we also looked at some specialized data structures, that while they
sacrifice generality, they provide very efficient data storage and retrieval for
applications that fit within their constraints.

It should also be pointed out that linear data structures can also be defined in
terms of a non-linear structure such as a graph. If you think about it, a list
is nothing more than a graph where each node can have at most one child node.
While this works theoretically, thinking of lists and graphs separately is
generally easier since the ways we manipulate lists is typically much more
straightforward than the way graphs work.
