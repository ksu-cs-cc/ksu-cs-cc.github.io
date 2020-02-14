---
title: "Algorithms"
pre: "4. "
weight: 40
date: 2020-02-11T00:00:26-05:00
---

{{< youtube u-GYlZYCG-8 >}}

#### Resources

* [Slides](/3-cc310/04-data-structures-algorithms/04-algorithms-slides.pptx)

#### Video Script

[Slide 2]

To use data structures effectively, we must have a set of operations on those
structures. These operations are often complex and require an *algorithm* to
implement the operation. We also use algorithms when we use the data structure
operations to perform an even larger function, such as finding our way through a
maze as captured in our example.

An *algorithm* is best defined as a “finite list of specific instructions for
performing a task.” In the real world, we see algorithms all the time. A recipe
for cooking your favorite dish, instructions for how to fix a broken car, or a
method for solving a complex mathematical equation are all examples of
algorithms.

[Slide 3]

Next, we’ll look at some of the algorithmic techniques that we use to design
algorithms. You can think of an algorithmic technique as a basic approach to
solving a problem. Our list is not exhaustive, but does include some of the more
common approaches, including brute force, divide and conquer, greedy, and
recursion.

[Slide 4]

If we solve a problem by “brute force” we generally mean that we don’t think
about it much, we just apply whatever force is needed to solve the problem. In
algorithms this is captured by simply trying all possible solutions and either
taking the first one we find or doing a complete search and taking the very best
solution.

For example, if our problem is to find the closest two points among a set of
points, the brute force approach would be to simply compute the distance between
every pair of points and select the pair with the smallest distance.

[Slide 5]

Our resulting algorithm will look something like this. We have an outside loop
and an inside loop. In both loops, we loop through all possible points and
compute the distance. If the distance is less than our minimum, then we save the
pair and the distance.

While this algorithm will find the minimum pair, it is not very efficient.
Looking at the code, if we have *N* points, it would take *N squared* steps to
solve the problem!

[Slide 6]

Another common algorithmic technique is *divide and conquer*. A divide and
conquer algorithm first divides the problem into at least two smaller problems.
Then it solves each of those problems individually. Generally, we keep
subdividing the subproblems until they get small enough to solve easily.

[Slide 7]

A great example of divide and conquer is the *binary search* algorithm. If we
have an array of sorted data as shown in our example, we can easily find any
value in the array using a divide and conquer process.

The process is pretty simple. We take the entire array and look at the middle
item, in this case 23. If the value we are looking at is less than 23, we look
at the middle item between the beginning of the array and item 23. We keep doing
this until we find our item, if in fact it exists.

So, for example, if we want to find the value 42, we look first at the item in
the middle of the list – 23. This is not what we’re looking for.

[Slide 8]

So, since 42 is greater than 23, we look at the part of the array between 23 and
the end of the list. We pick the middle point in the part of the list, which is
56, which again is not our number.

[Slide 9]

Since this is not the value we are looking for, we simply repeat the process
with the array between 23 and 56, which includes only one item. Luckily, that is
our desired number 42.

Notice that the total number of comparisons we performed was only 3, while if we
had searched from the beginning of the array, we would have had to search
through 5 different numbers before finding 42.

If we were to compute the efficiency in terms of time complexity, we would come
out with the time complexity of *log(N)*, while a linear search would yield a
time complexity of *N*. \*\*[advance]\*\* By the way, log(n) is much better than
*n* in terms of time complexity as illustrated by this graph.

[Slide 10]

The greedy approach is a strategy that simply makes decisions one at a time
based on the data it has available, without trying to look ahead to avoid
potential problems. By not searching for the best possible solution like brute
force, and not trying to divide the problem like divide and conquer, greedy
solutions tend to come very fast.

For example, we can use a greedy algorithm to determine the fewest number of
coins needed to give change for *36* cents, given that we have coins worth *20*
cents, *10* cents, *5* cents and *1* cent. Our greedy approach says to choose
the largest coin that is less than the amount still owed.

[Slide 11]

Thus, if we owe 36 cents, we choose our 20 cent coin, which would leave us owing
16 cents.

[Slide 12]

Next, we would choose our 10 cent coin, leaving only 6 cents.

[Slide 13]

Next, we would choose the 5 cent coin and then the 1 cent coin.

[Slide 14]

However, it should be noted that while this works on our example using 20, 10,
5, and 1 cent coins, it will not work on just any set of coins. For example, if
we add an 18 cent coin to our existing set of coins, the minimum needed would be
two 18 cent coins and not the 4 our algorithm would produce.

And, while greedy algorithms work quickly, they may or may not give you good
answers, if they can find one at all.

[Slide 15]

Our next technique is *recursion*. Recursion is similar to the divide and
conquer method we discussed earlier. However, *recursion* itself is complicated
and is often one of the most challenging concepts for a novice programmer to
learn. However, we’ll take it slow and spend an entire module on recursion later
in the course.

Essentially, recursion refers to an operation calling itself inside its own
code, which may seem a little strange at first. However, if you think of it like
divide and conquer where we are trying to solve smaller and smaller problems it
makes more sense.

Google tries to mess with you a little when you type in the search term
“recursion” as shown in the figure. Usually, when Google says “Did you mean:”,
it gives you a similar word to what you typed in (usually the correct spelling).
However, in this case, it actually provides the same word you typed in
“recursion”, which, if you click on it, brings you back to this same page.
That’s kind of how recursion works.

[Slide 16]

So let’s look at a quick example. First we’ll show how to compute the factorial
function using a loop.

Its fairly straightforward, we simply multiply our result by our loop index I
and each time through the loop. The end result returns N factorial.

[Slide 17]

The recursive version of the factorial function computes the same value, it just
replaces the loop with a recursive call to itself.

A recursive function has two basic parts: the *base case* and a *recursive
case*. The base case occurs when we are ready to stop calling the recursive
function. It is usually a very simple case in which the answer is known
directly. Once we get to the base case, the recursive calls stop and we begin
returning the values needed to compute our final solution. So for the factorial
function, we know by definition that 1 factorial is equal to 1. Thus, if N
equals 1, we simply return the answer 1.

The second part, the recursive case, reduces our problem to a smaller version of
itself. In this case, we reduce N factorial to N \* (N – 1) factorial. We then
call our function again to solve the problem N – 1 factorial and multiply the
result by N to find the solution to N factorial

So, if we have a problem that can be reduced to a smaller instance of itself, we
may be able to use recursion to solve it!

[Slide 18]

Non-linear data structures such as graphs allow for a wide variety of techniques
and algorithms, depending on your specific needs. We typically refer to these
algorithms as *graph traversal* algorithms.

A graph traversal algorithms construct their answers by moving along the edges
of a graph, from node to node. A good example of this is finding the fastest
route in a map application, where the edges are streets and the nodes are the
intersections of the streets.

One example of such an algorithm is *Dijkstra’s Algorithm*, which can be used to
find the shortest path between two selected nodes in a graph as shown in our
example. Here you see the algorithm running, finding the shortest path between
node a and node b.

[Slide 19]

In this video we explored a number of *algorithmic techniques* we can use to
develop algorithms that take advantage of data structures to solve complex
problems. Throughout the rest of this course, as well as a subsequent course,
we’ll explore these algorithmic techniques in more detail so you will be well
versed in their appropriate use.
