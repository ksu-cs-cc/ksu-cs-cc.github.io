---
title: "Selection & Bubble Sort"
pre: "2. "
weight: 20
date: 2020-03-20T00:00:26-05:00
---

{{< youtube 76NNveliJQM >}}

{{< youtube IyyfpADUpaU >}}

#### Resources

* [Slides](/3-cc310/07-searching-sorting/02-selection-bubble-slides.pptx)

#### Video Script

[slide 2]

*Sorting* is the process we use to arrange a set of items into some predefined
order. In programming, we use ordered containers, which enforce an ordering
between the values in the container.

By sorting the items in a container, we can more quickly find specific items.

We generally sort items in an *ascending* or *descending* order. *Ascending*
order means that the smallest value will be first, and each successive value
gets progressively larger until we reach the largest value in the container.
*Descending* order is the opposite – we start with the largest value and then
work our way down to the smallest value.

There are several standard sorting algorithms we can use to sort containers.
Each has its own space and time complexity. In this video, we’ll introduce you
to two of the simplest algorithms, selection sort and bubble sort.

[slide 3]

First, we will look at *selection sort*, which is one of the simpler sorting
algorithms to understand. The basic idea behind selection sort is to search for
the minimum value in an array and put it in the first location of the array. We
then repeat the process for the remaining items in the array, placing the next
smallest value in the second location, and so on. Eventually, we will have
sorted the array.

As the algorithm works, there will naturally be two parts of the array. The part
of the array that has already been sorted, and the remaining part of the array
that has not yet been sorted. Once we place an item into the sorted part of the
array, it does not change. We then work on sorting the remaining unsorted part
of the array.

[slide 4]

So, lets look at the code to implement this. The first thing you’ll notice is
that we start with a loop that will look at each location in our array. Within
this loop, we will find the minimum value in the remainder of the array and then
swap the value at the current location with the minimum value we found. The
index variable separates the sorted part of the array from the unsorted part of
the array. Everything below index – 1 has already been sorted.

[slide 5]

The next few lines in the array are basically the same as the FINDMIN function
we saw earlier in this module. As you recall, the algorithm basically steps
through each location in the unsorted part of the array and finds the minimum
value and stores its index in the variable MIN.

[slide 6]

After finding the minimum value, we then simply swap the current index value
with the MIN value and we’re done. We then loop back to the top of the array and
start the process for the next index location.

When our function completes sorting the entire array, the loop exits and the
function returns. The array is sorted and since arrays are passed by reference,
the calling function will have access to the sorted array as well.

[slide 7]

So let’s look at how the algorithm works on an unsorted array of numbers as
shown in this figure. We start our outer loop with index set to 0. We initialize
min to 0 and then start the inner loop, where index2 also starts at 0.

Each time through the inner loop, we compare to see if the value at the index2
location in the array is less than the value at the min location. If it is, we
store the value of index2 into min. So, the first time through the loop, both
index2 and min point to the same value at location 0, so we do not need to swap
array values.

[slide 8]

When we loop back up to the top of the inner loop, we increment index2 and then
compare the value at index2, 5, against the value at min, 8.

[slide 9]

Since 5 is less than 8, we set the value of min to the value of index2, which is
1.

[slide 10]

We loop back up to the top of the inner loop and increment index2 to 2.

[slide 11]

Since the array value at index 2 is less than the array value at min, we once
again update min with the value from index2.

[slide 12]

Next, we increment index2 to 3 and do our comparison. This time, however, the
value at index2 is not less than the value at min, so we do nothing.

[slide 13]

So, we go back to the top of the inner loop and increment index2 to 4. Here, the
value at index is less than the value at min,

[slide 14]

so, once again we copy the value from index2 into min.

[slide 15]

We increment index2 again. And the value at index2 is greater than our current
minimum value, so we do nothing.

[slide 16]

We increment index2 to 6, and this time we find another minimum value.

[slide 17]

Again, we copy the value of index2 to min.

[slide 18]

Finally, we increment index2 to 7, which is the last location in the array.
However, we once again find that the value at location 7 is less than our min,

[slide 19]

So we store 7 in min.

[slide 20]

At this point, the inner loop exits, and we move into the swap code, where we
swap the value in the array at location index with the value in the array at
location min.

[slide 21]

The swap is shown here between array locations 0 and 7. Notice at this point
that location 0 has the smallest value in the array.

[slide 22]

Once the swap is completed, we loop back to the top of the outer loop where we
increment index and set min equal to index.

Then, we enter the inner loop, which starts with index2 equal to index, or 1.

Now, we have everything set to continue sorting the unsorted part of the array,
which is the part that is white. The part of the array in purple has been
completely sorted and we do not need to revisit those locations.

[slide 23]

We continue to follow our algorithm and find a new minimum value in array
location 2, which causes us to update min.

[slide 24]

We increment index2 to 3, which is greater than our minimum, so we do not need
to update min.

[slide 25]

Then, when we increment index2 to 4, we find another minimum value, 2. We update
the value in min to 4 and continue on.

[slide 26]

Once again, the index2 value of 5 does not yield a lesser value.

[slide 27]

However, once we increment index2 to 6, we find a new minimum. In this case the
value 1. So, we update min to the new minimum location.

[slide 28]

Finally, we increment index2 to 7, which is the last location in the array.
Since its value is not less than our current minimum, we know the current
location in min, 6, is the minimum value left in the unsorted part of the array.

[slide 29]

So, we swap the values in the array at locations 1 and 6 as shown in the diagram
and we are done with the second iteration of the outer loop.

[slide 30]

When we start the third iteration of the outer loop, index is equal to 2, so
according to our algorithm, both min and index2 will get set to 2 as well.

Again, we can notice that the purple part of the array has been completely
sorted and now holds the 2 smallest values in the array.

[slide 31]

From here on out, we will just show the results of each iteration of the outer
loop and skip over the details of the inner loop execution.

After the third iteration of the outer loop, you can see that we have found the
next smallest value in the array at location 4.

[slide 32]

Thus, we swap the array values at locations 2 and 4.

[slide 33]

And now we have sorted the first three locations in the array.

The fourth iteration through the outer loop finds the minimum value at location
4 as shown.

[slide 34]

We then swap locations 3 and 4.

[slide 35]

On the fifth iteration of the outer loop, the minimum value is found in location
6.

[slide 36]

We then swap locations 4 and 6 to complete the fifth iteration.

[slide 37]

We start our sixth iteration with only three items left to sort. We follow the
same algorithm to find the minimum value in location 6.

[slide 38]

We then swap locations 5 and 6 and we are almost there.

[slide 39]

In the seventh iteration, we only have two unsorted locations of the array left.
Our algorithm correctly finds the smaller of the two in location 7.

[slide 40]

So, we swap the last two locations. Now we are done with our outer loop.

[slide 41]

So we exit the function and return a fully sorted array.

[slide 42]

So, how fast do we expect the selection sort to execute?

Since selection sort will look at each and every location in the array the same
number of times regardless of the values in the array, we don’t have to worry
about a worst-case scenario. Selection sort will run in roughly the same amount
of time regardless of the array values. Of course, the number of elements in the
array will matter a great deal to the runtime.

If our array has N elements, the algorithm will look at all N elements during
the first iteration, N-1 during the second iteration, N-2 during the third
iteration, and so on until we get to the final 2 elements in the array.

[slide 43]

Written out, this is equivalent to N + (N – 1) + (N – 2) dot, dot, dot until we
eventually get down to + 2 + 1.

[slide 44]

After doing a few mathematical computations, we can show that this is roughly
equal to N \* (N / 2), or N squared over 2.

[slide 45]

However, since we are talking in terms of time complexity, we simply say that
the selection sort algorithm runs on the order of N squared.

A good way to think about N squared is that each time the number of elements in
the array doubles, the algorithm will take about 4 times as long to execute.

[slide 46]

Next, let’s look at another simple sorting algorithm, *bubble sort*. The idea
behind bubble sort is to iterate through an array and swap adjacent locations if
they are out of order.

The reason this is called the “bubble sort” is that during our first iteration
through the array, the largest item in the array will be “bubbled” to the end of
the array. In fact, each subsequent iteration will do the same for the next
largest value, until eventually the entire array is sorted.

[slide 47]

The Bubble Sort is similar to selection sort in that we have an inner loop and
an outer loop. However, the outer loop is really used more as a counter to
control how many times we are required to go through the inner loop in order to
get a completely sorted array.

Each time through the outer loop, one additional location will be sorted at the
end of the array.

[slide 48]

The inner loop is where the real work is done. The inner loop steps through the
unsorted part of the array from index 0 to the next to the last array item that
has not been sorted. Thus, our first time through the outer loop, index = 0 and
our for loop goes from 0 to the length of the array – 2. You might ask why the
“- 2” and not “- 1”? The reason is that since we are comparing the value at one
location in the array against the value at the next location, we only have to
loop through the next to last item in the array. The last item will be sorted
automatically.

[slide 49]

The code inside the inner loop is very simple. First we compare to see if the
value in the array at location index2 is greater than the next value at index 2
+ 1.

[slide 50]

If it is, we simply swap the values. If it is not, we just move on to compare
the next two locations.

[slide 51]

So lets walk through the bubble sort algorithm on our array example. As we enter
the outer loop and then the inner loop, both index and index2 are set to 0 by
their respective for loops.

[slide 52]

Inside the inner loop, we do our comparison of the first two array locations.

[slide 53]

Since 8 is greater than 5, we swap the values.

[slide 54]

Then, we start our second iteration of the inner loop. This time we compare
location 1 against location 2.

[slide 55]

And, since 8 is greater than 3, we swap the values in the array.

[slide 56]

We continue to the third iteration of the inner loop, where we compare locations
2 and 3.

[slide 57]

Again, 8 is greater than 6, so we swap the values.

Notice how the value 8 has “bubbled” down the array. This is where the algorithm
gets its name. 8 will continue to bubble down the array until it runs into a
value that is greater than 8.

[slide 58]

The fourth iteration through the inner loop compares location 3 and 4.

[slide 59]

Again, 8 is larger than 2, so the values are swapped.

[slide 60]

Iteration 5 starts the same as all the other iterations by comparing locations 4
and 5.

However, this time 8 is not greater than 9, so no swap is performed.

[slide 61]

Iteration 6 compares locations 5 and 6.

[slide 62]

And this time, 9 is greater than 1, so the values are swapped.

So once 8 met up with a larger number, the 8 stopped bubbling down the array,
but the 9 took its place and started its downward bubble.

[slide 63]

Finally, we get to the next-to-last location in the array, location 6. So, in
iteration 7, we compare location 6 against the last location in the array,
location 7.

[slide 64]

Of course 9 is greater so we swap the two values. The inner loop now ends, so we
will loop back up to the outer for loop.

As we can see, 9 was the largest value in our array and it has bubbled down the
array all the way to the last location. So, effectively, the last location shown
has been completely sorted and we no longer have to consider it. From now on, we
will only worry about sorting the rest of the array.

[slide 65]

We will not walk through the inner loop again in our slides, but this figure
does show the result of the second iteration of the outer loop after the inner
loop has been performed.

Notice that every value in the array has moved by at least one location and that
the next largest value in the array, 8, has bubbled down to location 6.

[slide 66]

The third time through the outer loop yields similar results. Again, every value
has moved by at least one place and the value 6 has bubbled down to location 5.

[slide 67]

The results of the fourth iteration are similar with 5 bubbling down the array.

[slide 68]

The fifth iteration moves 3 to the end of the array.

[slide 69]

Iteration 6 bubbles 2 to the end.

[slide 70]

And finally iteration 7 of the outer loop swaps the last two numbers resulting
in a completely sorted array.

[slide 71]

So, like selection sort, the bubble sort algorithm ends and returns. Again,
since arrays are passed by reference, the sorted version of the array is
available to the calling function.

[slide 72]

The time complexity analysis of the bubble sort is similar to that of the
selection sort we discussed previously. However, this time, we can analyze both
comparisons and swaps.

Since we do one comparison each time through the inner loop, we can use our
analysis from the selection sort to conclude that the time complexity for
comparisons is also N squared.

Since swaps are only done sometimes in the inner loop, we need to look at the
worst case. Unfortunately, the worst case for swapping will be when the array
was already sorted in reverse order, which would require a swap each time
through the inner loop. Of course, this results in the same time complexity as
for comparisons, or N squared.

Thus, overall we say that the bubble sort algorithm runs on the order of N
squared time. Actually, this is often the case when your algorithm includes
nested loops. In these algorithms, if the outer loop and inner loop both iterate
over your data structure of N items, you can be pretty sure that your time
complexity is at least N squared.

[slide 73]

We have looked at two fairly simple algorithms – selection sort and bubble sort
– for sorting items in a data structure. While we have used an array of numbers,
be aware that as you develop more complex data structures, we can use these
algorithms on them as well.

However, both algorithms have the same problem. They both run in order N squared
time. While for small values of N this is not usually important. However, if you
are talking millions, billions, or even trillions of items, N squared gets to be
really big really fast!

Luckily there are other sorting algorithms that run much faster than N squared.
