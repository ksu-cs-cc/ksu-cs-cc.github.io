---
title: "Quicksort"
pre: "4. "
weight: 40
date: 2020-03-20T00:00:26-05:00
---

{{< youtube 8_jc6gP0RXY >}}

#### Resources

* [Slides](/3-cc310/07-searching-sorting/04-quick-slides.pptx)

#### Video Script

[slide 2]

Quicksort is widely considered to be one the fastest general-purpose sorting
algorithms available. It shares a lot of concepts with merge sort, but with a
unique twist that has some desirable features. Like merge sort, it can be
categorized as a recursive, divide and conquer algorithm.

[slide 3]

The overall process for quicksort is based on using a pivot value to divide a
container into two parts. The first part will have values less than the pivot
value while the second part will have values greater than the pivot value. Once
we have the two parts, we recursively sort the two parts of the container. By
using a pivot value, we avoid having to merge the two parts of the array back
together, which saves a lot of time. We can simply append the first part of the
container to the second part of the container.

[slide 4]

So, lets walk through an example. We have an unsorted array as shown. Our main
choice to make before starting the process is what our pivot value will be. For
our purposes, we will simply choose the last value in the array.

The value of index will be our index for looping through the array, while the
pivot index will keep track of the dividing point between values less than the
pivot value and values greater than the pivot value in the array as we sort it.

[slide 5]

Therefore, we initialize both our index and pivot index to 0 and set pivot value
to the last element in the array, which is 6.

We start the process by looking at the value in the array at the index location
and comparing that against our pivot value. Since 8 is not less than 6, we do
not need to do any swapping.

[slide 6]

So we increment index to 1 and compare the value at that index against the pivot
value. This time, 5 is less than our pivot value 6, so we swap the value at
index with the value at the pivot index.

[slide 7]

Once we swap the values of 5 and 8, we increment our pivot index by 1.

[slide 8]

We then increment index 2 and compare 3 against our pivot value 6.

[slide 9]

Once again, 3 is less than 6, so we swap the value at index with the value at
the pivot index and then increment the pivot index.

[slide 10]

Next, we again increment 3 and do the comparison of the value at index to the
value at the pivot index.

[slide 11]

Since 0 is still less than 6, we swap the values and increment the pivot index
to 3.

[slide 12]

We increment index to 4 and check the values at index and pivot index.

[slide 13]

Again 2 is less than 6, so we do another swap and increment the pivot index.

[slide 14]

This time, when we increment index to 5, the value at the index, 9, is not less
than 6, so no swapping is performed, and we do not increment the pivot index.

[slide 15]

So, we continue on, incrementing our index to 6. Once again, the value at our
index, 1, is less than 6.

[slide 16]

So we swap the value at index with the value at the pivot index and increment
the pivot index.

[slide 17]

Finally, we increment the index and reach the end of our array. Here, the index
points to our pivot value.

[slide 18]

Since we are actually checking to see if the value at index is less than or
equal to our pivot value, which it is, we go ahead and swap the values.

[slide 19]

Now we end up with our pivot value, 6, at location 5, which was the last pivot
index. What this last step does is to put our pivot value between the part of
the array that is less than the pivot value and the part of the array that is
greater than our pivot value.

Notice that by choosing the last element in the array as our pivot value, our
algorithm automatically places the pivot value between the two parts of the
array. If we had chosen another value, we would have had to find that value and
move it to the appropriate place in the array.

[slide 20]

Now comes the recursive part. After we finish partitioning the array, we call
quicksort on the first part of the array and the second part of the array. We
reset our indexes and again choose our pivot value as the last element in the
array.

We start by checking index 0, which contains the value 5. In this case 5 is
greater than our pivot value 1, so we do nothing.

[slide 21]

When we increment index to 1, we run into the same situation. The value at index
1 is 3, which is again less than 1, so we do nothing.

[slide 22]

Finally, when we increment index to 2 we find a value, 0, that is less than the
pivot value.

[slide 23]

So, we swap the value at index with the value at the pivot index and then
increment pivot index.

[slide 24]

When we increment index to 3, we once again find a value that is greater than
the pivot value, causing us to do nothing.

[slide 25]

Finally, we reach the end of this part of the array and find our pivot value 1.

[slide 26]

We swap the pivot value with the value at the pivot index as shown.

[slide 27]

Now we have divided the first part of the array into two additional parts. We
then make a recursive call to quicksort on the first part of the array. However,
since this array only has one element, we simply return as there is no sorting
to be done.

[slide 28]

So, we call quick sort on the 2 part of the array. Now we will be incrementing
index from 2 to 4. We initialize our pivot value to 3, which is the last value
in the part of the array we are working on. We also initialize pivot index to 2
since that is the first location in this part of the array.

We then compare the value at index 2, which is 5, against our pivot value 3.
Since 5 is greater than 3, we do not do a swap.

[slide 29]

Next, we increment index to 3 and find that the value at that index, 2, is less
than 3.

[slide 30]

So we swap the value at index with the value at the pivot index, resulting in
the swap of 2 and 5.

[slide 31]

Finally, we get to the last index in this part of the array, which of course,
contains our pivot value.

[slide 32]

We swap the pivot value with the value at the pivot index.

[slide 33]

We are done with this call to quick sort and return the index to 3, which is our
pivot value.

Next, we will call quick sort on the array from index 2 to 2 and from index 4 to
4 as recursive calls. However, since they are both single elements, they will
simply return.

[slide 34]

At this point, we return again since both the first and second parts of the
array have been sorted.

[slide 35]

Now we are at the top-level quick sort call with the first part of the array
completely sorted.

Next, we call quick sort again on the second part of the array, the part from
index 6 to index 7.

[slide 36]

Since the array we are now sorting is only two elements, the partition helper
function will result in partitioning the array into a single partition with an
index 6. Notice that index 7 was the pivot value, so it was returned. The final
call to quick sort will be on the single element array at index 6, which,
obviously, will just return immediately.

[slide 37]

As the recursive calls unwind, the end result is a completely sorted array, as
promised.

[slide 38]

Now, lets take a quick look at the code that implements quick sort.

We already said that quicksort is recursive, so we expect it to have at least
one base case and one recursive case. The base case is shown in lines 2 through
4, which checks to see if the array is either empty or contains one element. If
it does, we know the array is sorted and we can just return.

[slide 39]

The recursive case is shown on lines 5 – 7. It uses a helper function called
PARTITION in line 5 to split the array based on a pivot value. PARTITION returns
the location of the pivot value, which is stored in pivot index. Then, lines 6
and 7 recursively call the quicksort function on the two partitions of the
array. Pretty simple!

[slide 40]

The first two lines in the partition function just set the initial values for
pivot value and pivot index. We set pivot value to the last element in the array
and set pivot index to 0.

[slide 41]

Then, the function loops through each element in the array in lines 4 through
11. Line 5 determines if the value at that location is less than our pivot value
and, if it is, swaps that value with the value at pivot index and then
increments pivot index.

[slide 42]

Finally, we return the value of pivot index – 1, which is the new location of
our pivot value. The calling function will use this returned value to split the
array into two part for its recursive calls.

[slide 43]

So, how long does it take quicksort to work? As we discussed earlier, it is
generally considered to be the best general-purpose sorting algorithm out there.
However, if we do a worst-case analysis, we find that its runs in order N
squared time. However, we generally do not find the worst-case condition, so we
need to look at an average case scenario to see its speed.

To do the analysis, we need to make a few assumptions that may or may not hold
for a specific application. First, we assume the data is fairly evenly spread
out between the highest and lowest values in the array. Second, we assume we
choose a pivot value fairly close to the average value in the array.

Then, if we consider the 15-element array shown and we assume we always choose
the average element as our pivot point, we’d end up with a tree of recursive
calls shown.

In this diagram, each level, or row, of the tree looks at approximately N
elements. Also, the number of rows can be approximated by lg (N). Combined, we
can conclude that quicksort – on average – runs in order of N \* lg (N) time.

[slide 44]

As we stated in the introduction, quick sort is often considered the fastest
sort algorithm for general situations. While it’s worst-case time is not as fast
as merge-sort and it’s average case time is equivalent to merge sort, the way
quick sort works tends to do less comparisons and swaps than merge sort.

However, as with all general guidance, there are exceptions. Basically, it
depends on your data. If your data does not meet the assumptions we made during
our time complexity analysis, the actual time may be better or worse. Also, the
actual data structure you are working with can make a difference as well.
