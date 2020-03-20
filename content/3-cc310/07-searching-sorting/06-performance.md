---
title: "Performance"
pre: "6. "
weight: 60
date: 2020-03-20T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/07-searching-sorting/06-performance-slides.pptx)

#### Video Script

[slide 2]

We have been introduced to four sorting algorithms in this module. We have also
looked at a basic time complexity analysis for each of these algorithms. Next,
we will compare these sorting algorithms against each other based on their
performance, ultimately trying to understand when to use each algorithm.

Once we have a handle on sorting, we will look at when it makes sense to use
sorting and searching together instead of just doing a simple linear search.

So, here are the complexity equations for our sorting algorithms. They all look
impressively mathematical, but what does they really mean?

[slide 3]

First, we plot a graph comparing the time complexity of our sorting algorithms.
The graph shows the number of items to sort on the X axis, while the relative
runtimes of the various algorithms are shown on the Y axis.

As we can see, the Selection Sort and Bubble sort algorithms run significantly
slower than the other two sort algorithms leaving us to wonder why we would ever
want to use them.

So that brings us to Merge Sort and the average case for Quicksort, which both
run in N \* lg(N) time. As shown in the chart, as the size of N grows, the time
complexity advantage of these algorithms becomes clear.

Based on this chart, we might conclude that we should always use merge sort! It
is guaranteed to run in N \* lg (N) time, with no troublesome worst-case
scenarios to consider, right? Unfortunately, as with many things in the real
world, it isn’t that simple.

[slide 4]

Which algorithm we choose most often comes down to what we know about our data.
The way we get the data greatly impacts the performance of sorting algorithms.

[slide 5]

For example, what if we expect to get data that is nearly sorted? What if most
of the items are already sorted and less than 10% or less are only slightly out
of order? Believe it or not, in this case, it might actually make sense to use a
simple bubble sort that was optimized to stop sorting when it made a pass
through the container without making a swap. Since only a few elements are
slightly out of order, it should only take a few passes to get them back in the
correct places. Even though bubble sort runs in N squared time, it may run much
faster in this situation.

[slide 6]

What if our data is random and uniformly distributed? In this case, we may want
to choose Quicksort. Even though quicksort is very slow in the worst case,
experience has shown that it will outperform other sorting algorithms in that
situation.

[slide 7]

However, if we really know nothing about our data set, it is probably best to
choose merge sort, which is guaranteed to work in N \* lg(N) time in the worst
case.

[slide 8]

So, now take a look at our searching algorithms. As you recall, our basic linear
search algorithms run in order N time while binary search runs in order lg(N)
time. As the graph makes clear, binary search will run much faster than linear
search, especially as the number of items in our data set increases.

Both of these are significantly faster than any of our sorting algorithms.

[slide 9]

Since a single linear search is much faster than any of the sorting algorithms
we’ve looked at, the question becomes, when should we sort our data to speed up
our searches?

This is actually a very hard question since there are so many factors that come
into play, such as the type of data we are dealing with, the size of the data
set, and how many searches we expect to perform.

However, it is generally true that the larger the data set and the more times we
need to search it, the more we gain by sorting our data first.

[slide 10]

To clarify that a bit, let's look at an example. Let's assume that we need to
search a data set 10 times. We will simulate the running time based on the size
of the data set. The orange line represents running 10 linear searches on the
unsorted data set, while the blue line represents 10 binary searches after
sorting the data set using merge sort.

As we can see, it is more efficient to perform a merge sort, which runs in N \*
lg (N) time and then perform 10 binary searches running in lg (N) time, than it
is to perform 10 linear searches running in N time.

Obviously, the savings become more pronounced as the size of the data set grows.

[slide 11]

In fact, this analysis suggests that it may only take as few as 7 searches to
see this benefit, even on smaller data sets. So, if we are writing a program
that needs to search for a specific value in an array more than about 7 times,
it is probably a good idea to sort the array before doing our searches, at least
from a performance standpoint.

[slide 12]

In this video, we looked at the various sorting algorithms to see how they
compared in terms of time complexity. We looked at charts that provided us a
better idea of what those time complexity equations mean when compared against
each other. However, we also talked about why time complexity might not be the
only thing to consider when deciding on which algorithms to go with. In fact, we
showed several examples of how the data itself is the most important factor to
consider when deciding on which algorithm to use.

Then, we looked at when it might make sense to sort our data instead of just
using a simple linear search. We found that for fairly small amounts of data
that we would be searching only a few times, sorting before searching often
makes a lot of sense.
