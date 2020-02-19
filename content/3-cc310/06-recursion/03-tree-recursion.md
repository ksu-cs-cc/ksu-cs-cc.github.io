---
title: "Tree Recursion"
pre: "3. "
weight: 30
date: 2020-02-18T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/06-recursion/03-tree-recursion-slides.pptx)

#### Video Script

[slide 2]

When we think about recursive functions, we often think of a simple function
with a single base case that calls itself recursively to compute a function.
However, this is not the only way to use recursion.

[slide 3]

Most of what we think of as recursive functions use “linear recursion”, which
includes head and tail recursion. In this video, we will look at what we call
“tree recursion” where we can decompose our problem into multiple subproblems
and then call our function recursively on the various subproblems, which can
lead to very efficient algorithms.

[slide 4]

To illustrate tree recursion, we will use a simple recursive function *max*,
which finds the maximum of N elements in an array. However, instead of using
linear recursion, we will use tree recursion to solve it.

We decompose the problem by searching for the largest item in the first half of
the array and the largest item in the second half of the array. We do this by
recursively decomposing our problem until we get to where we only have one or
two items in our array. At this point, finding the maximum is easy.

So, let’s walk through a simple example.

[slide 5]

In the first step, we simply divide the array in 2 and then call the function
*max* on each half of the array.

[slide 6]

Max will first check to see if we have reached our base case of 1 or 2 items in
the array.

[slide 7]

Since we have not reached this state, we will continue to halve the arrays and
recursively call max on them.

[slide 8]

Now, we get to the point where we have an array of only two items, so we compute
the maximum of the two items and return it.

[slide 9]

At the next higher level, we then find the maximum from both of our subarrays by
doing a simple comparison.

[slide 10]

These values are then returned to the top level where we compare the maximums
from the subarrays and compute our final max value.

[slide 11]

Which in this case is 76.

Now, lets look at the code that implements our algorithm.

[slide 12]

MAX is set up similar to a simple linear recursive function. We have base cases
– in this case two of them – and a recursive case.

Our first base case is a check to see if we have a single item in our array. If
so, we just need to return that value since it is obviously the maximum.

[slide 13]

Our next base case is added to optimize the performance of our algorithm. If we
have two items in our array, we can directly compute the maximum of those two
values using a simple comparison and then returning the maximum of the two
values.

[slide 14]

If neither of our base cases apply, we drop through to our tree recursion case,
which is a little more complicated. First, we compute the middle element of the
current array. Once we have done this, we simply call MAX on the first half of
the array and then on the second half of the array. Eventually both calls to MAX
will return the maximum values in their respective halfs. From there, we just
perform a simple comparison of the two max values and then return the largest
one.

[slide 15]

Now let's look at the tree of recursive calls that result when we call the MAX
function on an array with 9 items.

Since we have 9 elements in the array, we need to compute the MIDDLE of the
array.

[slide 16]

Next, we call MAX on our subarray from item 1 to 4. For the remainder of this
example, we will refer to instances of the MAX function by their start and end
index values. In this case, we will refer to this as a call to MAX(1, 4) while
the initial call was to MAX(1, 9).

Again, it has more than 2 items, so we will need to recursively call MAX again.

[slide 17]

So we call MAX(1,2), which results in us finally reaching the base case where we
have exactly two items in our subarray. As described earlier, we simply compare
the two values at this point and return the greater of the two.

Notice that our tree looks pretty much like linear recursion at this point.
However, we will see our tree start to take shape on the next call.

[slide 18]

Since MAX(1,2) returned a value, we can now proceed with the call to MAX(3,4).

Again, this is a base case where we have two items in the array. Once again, we
simply compare our two values and return the greater of the two.

Once MAX(1,2) and MAX(1,4) have returned their maximum values, we can compare
these values and return the larger value to MAX(1,9).

Now that we have computed the maximum value in the first half of the array, we
can turn our attention to the second half of the array.

And notice how we now begin to see our tree start to appear.

[slide 19]

The second call to MAX in MAX(1,9) results in a call to MAX(5,9). Since it is
not a base case, we divide the array and make a call to MAX(5,6).

[slide 20]

Of course, MAX(5,6) is a base case, so we compute the maximum number and return
it to MAX(5,9).

[slide 21]

At this point, MAX(5,9) makes another recursive call to MAX(7,9).

[slide 22]

Again, MAX(7,9) is not a base case, so it decomposes the array and makes two
calls: MAX(7) and MAX(8,9).

Max(7) is the first base case in our code and it simply returns the value of
item 7.

[slide 23]

Next, Max(8,9) is called and computes the maximum of the two items, which is
returned back to MAX(7,9).

MAX(7,9) compares the values returned by MAX(7) and MAX(8,9) and then returns
the larger to MAX(5,9).

MAX(5,9) now has the two maximum values it needs to compute the overall maximum
for the second half of the array.

When MAX(5,9) returns this value to MAX(1,9), the maximum from the first half of
the array is compared to the maximum from the second half of the array to
compute the overall maximum value in the array.

[slide 24]

We have looked at a new way to use recursion to solve problems. As you might
expect, tree recursion is especially useful when working with data structures
that are based on trees. Like linear recursion, tree recursion provides the
ability to solve some complex problems in a way that is both elegant and easier
to understand.
