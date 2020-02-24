---
title: "Fibonacci"
pre: "4. "
weight: 40
date: 2020-02-18T00:00:26-05:00
---

{{< youtube Qw_SJrtYI88 >}}

#### Resources

* [Slides](/3-cc310/06-recursion/04-fibonacci-slides.pptx)

#### Video Script

[slide 2]

Oftentimes problems that look like they are tailor made for a recursive function
may not work quite as well as we originally thought. Computing Fibonacci numbers
is one of those problems.

However, there are some techniques we can use to help optimize our recursive
algorithms.

[slide 3]

Fibonacci numbers form a series of number in which each number is the sum of the
previous two numbers in the series. As you can see this leads to the numbers in
the series growing very rapidly.

[slide 4]

The nice thing about computing Fibonacci numbers is that the equation is quite
simple and elegant. A Fibonacci number is simply the sum of the two Fibonacci
numbers preceding it.

For our purposes in studying recursion it is perfect. We just sum the result
from two recursive calls.

Of course, its important to know the base cases, which are also well defined. F0
= 0 while f1 = 1. This when coupled with the definition allows us to easily
compute f2 as 0 + 1, or 2.

[slide 5]

Given the nice simple definitions, creating the function “f” to compute
Fibonacci numbers is straightforward.

First, we include our two base cases. If our input number N is 0, we return 0.
If N is 1, we return 1.

[slide 6]

Next, we then include the basic definition as our recursive case. In this case,
we simply return f(N-1) + f(n-2).

I think we would all agree that this is a very elegant and straightforward
application of recursion that should work very well for us.

[slide 7]

So, if we execute our function to compute the 6th Fibonacci number, we get the
following tree that illustrates the calls made to “f”.

As you can see f(6) makes calls to f(5) and f(4), while f(5) makes calls to f(4)
and f(3), etc. on down to the base cases of f(0) and f(1).

[slide 8]

However, as we look at the calling tree more closely, we see that there are
several calls that are made multiple times. For example, f(2) is called five
separate times, which means that we recompute the value of f(2) four additional
times after we have already computed it. Obviously, these are wasted
computations. Imagine if we wanted to compute the 10th Fibonacci number. There
would be a huge number of extra computations going on.

[slide 9]

The problem lies in the recursive definition of Fibonacci numbers and our
straightforward implementation of that definition.

If we look at the line with the recursive definition, it computes f(n-1) and
then calls f(n-2). This causes f(N-2) to be computed twice, once within the
f(n-1) computation and then again separately.

Surely there has to be a better approach.

[slide 10]

Of course the obvious solution would be to compute values only once and then
save them so we don’t have to recompute them.

This is the basis of a technique called “memoization”. Essentially, any time we
do a computation, we will save the result into an array. Then, if we need to
compute a result, we will check our array to see if it has been computed before.

[slide 11]

So let’s modify our algorithm a little. We will introduce an array called FA to
save our computed results. We initialize FA so that every item has the value of
-1. Since Fibonacci numbers are all greater than 0, we know that if the value of
FA[N] is -1 then we have not yet computed that Fibonacci number.

Then, if we are not in a base case, we simply check to see if anything has been
stored in the array at that position, or if FA[N] is equal to -1. If it is, we
compute the value of f(N) using the traditional recursive formula. We then save
that value in the array and return.

However, if FA[N] does not equal -1, that means that the value in FA[N] is the
Nth Fibonacci number and we can just return it directly and eliminate a lot of
extra computation.

[slide 12]

With our memoized algorithm, all the highlighted function calls will not have to
be recomputed. But, its even better than that.

[slide 13]

In reality, when the yellow highlighted function calls are made, none of the red
highlighted function calls will need to be made. This is due to the fact that
the yellow highlighted Fibonacci numbers have already been computed and stored
in FA and thus no additional calls are needed.

[slide 14]

Now, if we look at the real call tree, we see that only 11 of the original 25
function calls are actually made. Obviously this is a significant savings in
terms of computation. And, as we attempt to compute the really large Fibonacci
numbers, the savings will become equally large.

[slide 15]

So, we have looked at the effect that a straightforward implementation of
recursive definition can have. However, the effect really depends on the type of
definition you are dealing with.

In this case, the tree recursive calls ended up recomputing the same values over
and over again. This is particularly common on tree recursion where you are
performing multiple recursive calls within the same function. If we can
decompose our problems so that the subproblems are unique, then we will be OK.
However, if the subproblems overlap, then we have the potential for doing extra
computations.

Of course the good news is that we have found a technique that can be used to
shortcut excessive computation by storing values as we compute them and then
simply looking them up instead of recomputing them.
