---
title: "Time Complexity"
pre: "6. "
weight: 60
date: 2020-01-31T00:00:26-05:00
---

{{< youtube J_o9ud01yHU >}}

#### Resources

* [Slides](/3-cc310/03-program-contract-performance/06-time-complexity-slides.pptx)

#### Video Script

[Slide 2]

As programmers, you will often need to compare solutions to a specific problem
to determine the best solution. In general, that is a hard question. Are we
concerned about the time the algorithm takes? Or, are we more concerned with the
amount of memory space it uses? Of course, sometimes its both.

In this video, we will discuss "time complexity", which will allow us compare
algorithms based on how efficient they are.

Of course, one way to determine how efficient an algorithm is, is to time it
when running against a large number of datasets. However, this is often not
feasible, especially when you haven't actually coded the algorithms yet.

[Slide 3]

The other way is to analyze the algorithm to determine best-case and worst-case
scenarios based on the size of the data the algorithm works on. This is what we
do when we talk about the time complexity of an algorithm. The goal is to come
up with an equation based on key parts of the code, specifically loops,
comparisons, and assignments.

Since loops cause repetition, we usually use them as a multiplier. Comparisons
and assignments are simple sequential constructs that only cause an additive
effect.

[Slide 4]

First, we will look at our linear algorithm for finding the maximum and minimum
values in a list.

We will look at the loops, comparisons, and assignments to give us an equation
that captures the time complexity of the algorithm.

We will not consider the initialization part of the algorithm since it is purely
sequential and would only add a constant factor to our equation. We will also
ignore the input and output for now to simplify the analysis.

[Slide 5]

In this algorithm, there is one loop that encompasses all our operations. Thus
each operation within the loop may be executed each time through the loop.
Therefore, loops multiply the effect of the comparison and assignment operations
and tend to dominate the time complexity for most algorithms.

In this case, our loop is a 'for' loop from 1 to N. Thus it will execute exactly
N times when the algorithm runs. We will use this fact to help determine the
overall impact of the assignment and comparison operations.

[Slide 6]

There are exactly two comparisons that are executed each time through the loop
as shown. Since we go through the loop N times, the number of comparisons in the
algorithm will be 2 times N, or 2N.

[Slide 7]

Assignments are a little trickier. In this case, we have two possible
assignments, but neither is guaranteed to execute since they depend on the value
of the variable 'x'.

Therefore, we try to characterize their impact in terms of best-case and
worst-case behavior.

Since they may not be executed at all, the best-case number would be 0 times N,
or 0.

However, for the worst-case scenario, on first glance, it looks like both could
be executed. However, a quick look will tell us that in actuality, at most only
one of the assignments will be made each time through the loop. This is because
'x' cannot be strictly greater than 'max' and strictly less than 'min'.

[Slide 8]

If we take those equations and combine them, we can get a best and worst-case
scenario. We take the time complexity for comparisons and add them to the time
complexity for assignments, both in the best and worst-case situations.

Here the worst-case is 2N + N, or 3N, and the best case is 2N.

[Slide 9]

Now we will do an analysis of the pairs algorithm for finding the minimum and
maximum values in a list.

In this case, our loop goes from 1 to N, however it also has a 'step 2'
qualifier, which means that it really only goes through 1/2 of the elements of
the list.

So, in this case, our loop multiplier is 1/2 * N, or N/2.

[Slide 10]

Since we are looking at two numbers at the same time, we have to add an extra
comparison operation to the algorithm to determine which of the two numbers are
larger and smaller.

This results in 3 comparison operations and thus our time complexity for
comparisons is 3 * N/2, or 1.5N.

[Slide 11]

Now, due to the increased complexity of this algorithm, we actually have 6
possible assignment operations.

The first four assignment operations - those highlighted in yellow - are based
on the comparison 'x > y', which means only two of those assignments will be
executed each time through the loop.

And, like the linear algorithm, we have our two possible assignments, which are
highlighted in green. However, in this case, it is possible for us to execute
anywhere from 0 to 2 of these assignments.

So, if we look at the worst-case scenario, we can execute 4 assignment
operations each time through the loop. And, in the best-case, we would only
execute 2 assignment operations.

Since we go through the loop N/2 times, our worst-case time complexity for
assignments is 4 * N/2, or 2N, while our best-case time complexity is 2 *
N/2 or N.

[Slide 12]

Like we did for the linear algorithm, we will take those equations and combine
them to get the best and worst-case scenarios.

Here the worst-case is 1.5N + 2N, or 3.5N, and the best case is 1.5N + N, or
2.5N.

[Slide 13]

So, let's compare the algorithms. Based on our analysis of the best- and
worst-case scenarios, it easy to see that the linear algorithm will actually be
faster than the pairs algorithm. We know this by comparing the complexity
equations directly.

In the worst-case scenario the linear algorithm will run in 3N time, while the
pairs algorithm will run in 3.5N time.

Likewise, in the best-case scenario the linear algorithm will run in 2N time,
while the pairs algorithm will run in 2.5N time.

Note, we never have to worry about whether the pairs algorithm's best-case is
better than the linear algorithms worst-case since they are both based on N, the
number of elements in the array. We only compare using the same data.

[Slide 14]

To make this a little clearer, lets plug in some real numbers. In this case,
lets assume that our input is an array of 10,000 numbers. This would equate to N
being equal to 10,000.

[Slide 15]

Next, we compute the worst-case analysis for the linear algorithm, which is
30,000 operations.

[Slide 16]

When we compare that against the worst-case analysis for the pairs algorithm, we
see that the pairs algorithm will perform 5,000 more operations than the linear
algorithm.

[Slide 17]

So, lets look at the best-case analysis for the same scenario.

[Slide 18]

In this case, the linear algorithm will perform 20,000 operations

[Slide 19]

While the pairs algorithm will run 25,000 operations, or 5,000 more than the
linear algorithm.

[pause]

So, we've shown how to compute time complexity equations that will allow us to
compare two algorithms to help us understand which will take the least amount of
time. Equally important, the analysis also gives us insight into how the
algorithms will scale with the extremely large amounts of data we are seeing in
many applications these days.
