---
title: "Linear Search"
pre: "1. "
weight: 10
date: 2020-03-04T00:00:26-05:00
---

{{< youtube -V75q4CnlXw >}}

#### Resources

* [Slides](/3-cc310/07-searching-sorting/01-linear-slides.pptx)

#### Video Script

[Slide 2]

It may be your car keys, your book, your pen, or your phone, but I’d be willing
to bet you search for things almost every day of your life. The same goes with
computers. Computers store lots and lots of data and the only way to find the
data we need is to search for it.

Today we’ll look at one of the most basic search algorithms called “linear
search”. Linear search consists of searching for a specific piece of information
by walking through a data structure, one item at a time, until we find it. There
are no tricks or optimizations here. We just do a straightforward search until
we find the information we are looking for.

Linear search can be applied in almost any situation, and it doesn’t matter
whether the data structure is ordered or not.

[Slide 3]

To carry out a search, we generally create a search function. To simplify our
discussion, we’ll assume that we are going to create a “find” function that
takes as input, two parameters: a number to search for, and an array of numbers
to search.

The “find” function will return the index in the array where we found the number
we are searching for. We can return -1 to indicate that we did not find that
number since -1 is not a valid index value.

In reality, we can search a one-dimensional array, a two-dimensional array, or
some other complex data structures.

[Slide 4]

Now, let’s walk through the basic process of searching an array. In this
example, we assume that we are going to search our array for the number 3.

Since we need to walk through the array one item at a time, we will initialize
our index to 0, which is the first element of the array.

At this point, we perform our comparison to see if our number, 3, is equal to
the item in the array at index 0. In this case, the item in the array at index 0
is 8, so we do not find a match.

[Slide 5]

So we will increment our index by one to look at the next item in the array. We
then compare our number 3 against the item in the array at index 1. However,
once again, the item at index 1 in our array, the number 4, is not equal to the
number 3 that we are searching for.

[Slide 6]

So we increment our index by 1 and perform another comparison operation. This
time, the item in the array at index 2 is 3, which does match the number 3. At
this point we have found our match and so we return the value of our index from
the function.

You might be asking, why are we searching for a number in the array if we
already know what the number is? That’s probably a valid question. Of course,
one reason is that we just might need to know if a specific number is in our
array. But an even better reason occurs when we are looking for more than just
simple numbers. Imagine the case where our array holds complex objects such as
student educational records. In this case, we might search an array of student
records based on the name of the student. Then, once we find the student we are
searching for, we will also have access to all the other information about the
student such as their major or current GPA.

[Slide 7]

Encoding this process is relatively straightforward. First, we define the
function “find” with the two input parameters: the number of interest and the
array to search.

[Slide 8]

Next, we set up the main loop in the algorithm where we initialize and increment
the array index. Notice that our array goes from 0 to the size of the array – 1.
Since arrays are indexed starting from 0, we must make sure we subtract one from
the size of the array to ensure we don’t get an error.

[Slide 9]

Inside the loop is where we perform the comparison between the current item in
the array and the number we are searching for.

[Slide 10]

If we have a match, we simply return the index of the array where the match
occurred. If we do not find a match, we loop back to the top of the for loop and
increment our index to point at the next item in the array.

[Slide 11]

Finally, if we loop through the entire array without finding our number, then we
will exit the for loop and return -1, indicating that we did not find our number
in the array.

[Slide 12]

You might have noticed that there are actually two 3’s in our example array and
that our search algorithm only found the *first* 3. But what if we were
interested in finding the *last* 3 instead of the *first* 3? How would we need
to modify our algorithm.

The answer is really pretty simple. Instead of searching the array from item 0
to item 7, we simply search it in reverse, from item 7 to item 0.

[Slide 13]

The way we reverse the loop is easy. We simply initialize our index to the “size
of the array – 1” and then use a “-1” step to decrement our index down to 0.

Otherwise the rest of the algorithm is exactly the same. So, lets see how this
works.

[Slide 14]

When the function starts, we enter the for loop and initialize index to the
“size of the array – 1”. Since the array has 8 elements in it, the size is 8 and
thus we initialize index to 8 – 1, or 7.

We do our normal comparison and, since the item in the array at index 7 is not
equal to our number 3, we simply loop back to the top of the for loop.

[Slide 15]

Then, since the for loop has a -1 step, it *decrements* the index value to 6.
Now we can do our comparison and, since they don’t match, loop back to the top
of the for loop.

[Slide 16]

Finally, we decrement our index to 5. Now the array value at index 5 is 3, which
matches our number 3. The function will then return index 5, completing our
function call.

[Slide 17]

So there you have it. A straightforward linear search of an array. Since we
basically have to search through each location in the array, it shouldn’t be a
surprise that linear searches operate in linear, or order N time. This should be
obvious since the larger the number of items in our array, the more time it will
take to find the number we are searching for.

Linear searches are really as good as we can do unless we have more information
about the way things are stored in our data structure. We can do this by using
more complex data structures such as maps, or by ordering our data in the array.
