---
title: "Merge Sort"
pre: "3. "
weight: 30
date: 2020-03-20T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/07-searching-sorting/03-merge-slides.pptx)

#### Video Script

[slide 2]

Now we will look at another common sorting algorithm called *merge sort*. Merge
sort is a recursive process that uses a *divide and conquer* approach to
sorting.

The basic idea of the merge sort algorithm is to divide our container in half
over and over until we get to the point where we have a container with only 1 or
2 elements in it. Then we swap those elements if they are out of order.

Once both halves are sorted, we merge them back together into a single ordered
container.

[slide 3]

So lets look at an example to help us understand the merge sort a little better.

For our example, we’ll use an unsorted array of numbers.

[slide 4]

The first step is to divide our container into two parts.

We will use the thick lines around our container elements to show which elements
we are currently working on.

Since the first half of the array has more than 2 elements, we will divide it
again.

[slide 5]

Now, we have divided the container down to the point where we have exactly two
elements in each container. At this point, sorting the container simply requires
us to compare the two values in the container and swap them if necessary.

[slide 6]

Since 5 is less than 8, we swapped the values to get a sorted subarray.

[slide 7]

Then, we move on to the next subarray. However, the elements in this subarray
are already sorted, so we do not have to do any swapping.

[slide 8]

The next step is to merge our two subarrays back into a single array of size 4.
We do this by looking at the first elements of both subarrays and copying the
smallest of the two into our temporary array.

[slide 9]

In this case, 3 was less than 5, so we copied the 3 into the temporary array.
Next, we compare the current element in the first subarray, which is still 5,
against the next element in the second subarray, which is 6.

[slide 10]

In this case, 5 is less than 6 so we copy 5 into the temporary array.

[slide 11]

Now we compare 8 and 6.

[slide 12]

Of course, 6 is less so we copy it into the temporary array. Now that we have
copied all the items in the second subarray into the temporary array, we just
need to copy the remaining items from the first subarray into the temporary
array.

[slide 13]

After copying the 8, we now have the temporary array completely sorted, so we
copy those values from the temporary array into the first half of our original
array.

[slide 14]

Once we’ve sorted the first half of the array, we can turn our focus to the
second half.

[slide 15]

We again divide the array into two subarrays, and, since they are both of size
2, we can stop dividing.

[slide 16]

Next, we look at the elements in the first subarray, which are already sorted.

[slide 17]

Then, we look at the second subarray.

[slide 18]

However, the second subarray is out of order, so we swap the elements.

[slide 19]

Once both subarrays are sorted, we begin the process of merging them into our
temporary array. We compare the first two elements in the subarray, 2 and 0.

[slide 20]

After copying 0 into the temporary array, we compare 2 and 1.

[slide 21]

When we copy 1 into the temporary array, we can now just copy the rest of the
first subarray since the second subarray has been completely copied.

[slide 22]

After copying the 2 and the 9 into our temporary array we are done.

[slide 23]

Next we copy the temporary array into the second half of our array leaving us
with two sorted halves of the array.

[slide 24]

Once again, we create a temporary array, this time large enough to hold the
entire contents of our original array.

[slide 25]

We begin our merging process by looking at the first two elements in the two
halves of the array.

[slide 26]

In this case, 0 is the smallest so we copy it into temp.

[slide 27]

We then copy 1 …

[slide 28]

Followed by 2 …

[slide 29]

3 …

[slide 30]

5 …

[slide 31]

6 …

[slide 32]

and 8.

[slide 33]

Finally, we copy the remaining elements from the second half of the array into
temp, which is just the number 9.

[slide 34]

After copying the values from temp back into our array, our array is sorted.

[slide 35]

So how do we do this in code?

First of all, we are going to use a *recursive* algorithm, which means we need 1
or more base cases and a case where the function calls itself.

[slide 36]

The first base case is when the size of the array we are sorting is exactly one.
Of course, no sorting is actually needed, so the function simply returns.

[slide 37]

The second base case occurs when there are exactly two elements left in the
array. In this case, all we need to do is check to see if they are out of order
in line 6 and then swap the values in lines 7 through 9 if they are.

[slide 38]

Finally, we have our recursive case. First, we find the middle of the array in
line 13. Then we call MERGESORT recursively on the first half of the array in
line 14 and the second half of the array in line 15.

Then, once those merge sorts have been completed, we simply merge the two halves
together via a helper function call to MERGE in line 16.

Thinking back on our example, you’ll find that this algorithm implements that
process exactly.

[slide 39]

Of course, the MERGE function plays a major role in our MERGESORT. It looks a
litttle daunting, but it is fairly straightforward.

[slide 40]

It begins by creating some variables to help us keep track of what we’re doing.
The tempArray variable will hold the newly merged array, while Index1 points to
the element being considered in the first half of the array, and index2 points
to the element we are considering in the the second half. Finally, newIndex
keeps track of our where we are inserting the value into tempArray.

[slide 41]

The first loop compares items from the two halves of the array and adds them to
tempArray. This continues until one of the halves of our array has been
completely added to the tempArray. It simply compares the two elements under
consideration in the two halves of the array in line 7 and then copies the
smallest of those values into tempArray in either line 8 or 9.

[slide 42]

Once the first loop has completed, one of the two following loops need to be
executed. Which loop is executed depends on which half of the array still has
elements left to be added to tempArray. If index1 is less than half, that means
that there are still items left in the first half of the array that need to be
copied into tempArray. The loop then causes those items to be copied. The second
loop works the same way as the first, it just checks the second half of the
array instead of the first.

[slide 43]

Notice that exactly one of these two loops will execute.

The first loop exits when either index1 is greater than half, or index2 is
greater than end. So, when we exit the first loop, we know that one of these two
conditions are false. Also notice that only 1 of these conditions will be false
since we increment either index1 or index2 inside the loop, but never both at
the same time. Thus, when we exit the first loop, we know that one of these
conditons will be false and one will be true.

Now, since the conditions of the first loop are the same as the conditions
required to enter the two subsequent loops, one of the loops will be executed
while the other will not.

[slide 44]

Finally, the last loop starting on line 26 copies the sorted elements from the
temporary array back into the original array.

[slide 45]

So, now that we understand merge sort, we also need to understand the time that
it will take to execute.

Instead of delving into the detailed mathematics, we will try to develop an
intuition for the algorithm.

[slide 46]

We’ll begin by looking at all the recursive calls made by the algorithm on a
given array. As you can see, the top array is divided into two, each of those
halves is divided into 2 and so on until we get to subarrays with a length of
either 1 or 2. Each divided array or subarray represents a recursive call.

[slide 47]

In our example, we have to consider swapping values at each of the size 2
subarrays as highlighted in our figure. If we consider the worst-case scenario,
the array would be in reverse order forcing us to swap all our numbers each time
we got to an array size of 2.

In our example, we only have to make 2 swaps, while in the worst case, we would
have to make all 4 swaps.

So, how many swaps would that be? As it turns out, a good estimate would be N /
2 times. If we have an array with exactly 16 elements, there are at most 8 swaps
we could make. With 10 elements, we can make at most 4.

[slide 48]

So, the number of swaps is on the order of N time complexity.

[slide 49]

So what about the complexity of the merge operation? Let’s look at our example.

We have 3 rows in our example. In each of these rows, we will need to merge all
N elements at least once. The worst case for the last row would be the situation
where we had two element subarrays that held all N numbers, which is what we
have in our example.

So, we just need to multiply N by the number of rows. It turns out that the
number of rows will be equal to the number of times we can divide N in half. So,
for an array of size 8, we can divide it in half exactly 3 times. But what about
57, 234 thousand, or 1.36 million?

[slide 50]

It turns out that the number we are looking for is log 2 of N.

[slide 51]

The easiest way to think about the value of log2 of N is that it is the solution
of x in the equation of 2 to the x equals N.

[slide 52]

In this example, our N is 8, so the solution is 2\^3 = 8, which gives us our
answer of 3 rows.

[slide 53]

If we put that all together, we have N from the number of swaps and log N from
the number of rows, so we get an overall time complexity of N \* lg(N).

While N \* lg(N) is larger than N, it will always be smaller than N squared,
which makes it a sort algorithm to be considered for the right applications.

[slide 54]

In this video, we have discussed merge sort, which recursively divides a data
structure into 2 parts until it gets to the place where it can easily compare 2
values against each other. Once it orders the 2 elements in the arrays, it
merges them back together to form the original array in sorted order.

We also looked at the time complexity of merge sort and found it to be on the
order of N \* lg(N).
