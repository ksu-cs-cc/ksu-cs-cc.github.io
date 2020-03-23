---
title: "Binary Search"
pre: "5. "
weight: 50
date: 2020-03-20T00:00:26-05:00
---

{{< youtube D64RE4R2keI >}}

#### Resources

* [Slides](/3-cc310/07-searching-sorting/05-binary-slides.pptx)

#### Video Script

[slide 2]

Now that we have a good set of sorting algorithms in our bag of tricks, the
question is "can we use that to our advantage to speed up our searches?"

If we are going to do a lot of searching on a particular data set, it might make
sense to sort the data first so we can do a better job of searching.

In this video, we will investigate an algorithm called "binary search", which is
the most popular algorithm for searching ordered sets of data.

[slide 3]

The strategy of the binary search algorithm is to compare the value in the
middle of the container with the value we are looking for. If our container is
sorted in ascending order there are three possible outcomes:

If the value in the middle is equal to the value we are searching for, we have
found the correct element and we can return.

If the value in the middle is less than the value we are searching for, then we
need to search for the value in the top half of the container.

If the value in the middle is greater than the value we are searching for, then
we need to search for the value in the bottom half of the container.

Once we have found the value we are searching for, we can easily find any of the
same values in the array by a simple linear search of the elements immediately
before and after the element holding the value we are searching for. Since the
container is sorted, all similar values should be grouped together. If we want
our algorithm to return the index of the first occurrence of the desired value,
we can simply search toward the front of the container until we find the first
occurrence.

[slide 4]

So lets look at an example of binary search before we delve into the code.

In this example, we have an array of integers that have already been sorted by a
sorting algorithm.

To carry out binary search, we need to keep track of 4 numbers. First, we have
to know the value we are searching for. This is generally an input to the search
algorithm.

Then, we need to keep track of the starting index of the part of the array in
which we are searching. We will begin at the index 0 of the array, but this
index may change depending on our search. We also need to keep track of the last
index of the part of the array we are searching. Again, this will begin at the
end of the array.

And finally, we will compute the middle of the array. This is calculated by
adding the start and end values and then dividing by 2.

[slide 5]

In this example, let's assume we will be searching for the number -3. As we just
said, we will begin with start set to 0 and end set to 7, the first and last
index of our array.

[slide 6]

Next, we calculate the value of middle.

[slide 7]

Which in this case is the index 3.

So, we look in the array at index 3, which holds the value 3. Since 3 is greater
than our value -3, we will need to continue searching the bottom half of the
array.

[slide 8]

Notice, that after looking at only one element in our array, we have effectively
eliminated the need to search one half of the array.

We re-calculate middle after updating the end index. In this case middle equals
1, so we check the value in our array at index 1.

[slide 9]

In this case, the value at index 1 is -3, so we have found our match. We simply
return the index value of middle and we are done.

[slide 10]

Lets use our array and search for another value. In this case we will search for
the value 19.

Once again, we initialize our search with start = 0 and end = 7.

[slide 11]

We calculate middle, which again is 3.

We then check the value in our array at index 3, which is not equal to the value
we are searching for, 19.

[slide 12]

So, we set start = 4 and search again.

[slide 13]

This time we calculate middle to be 5 and we check the value there.

Unfortunately, 19 is greater than 12. So, to continue searching the top part of
the array, we set start to 6.

[slide 14]

With start = 6 and end = 7, we calculate middle to be 6. And, if we look at the
value in the array at index 6, we find 19.

[slide 15]

We have once again found our search value of 19.

Now that we are done, we return the middle value of 6.

Notice that if we had used a linear search, we will have had to check 7
different locations in the array before we found the value we were searching
for.

However, using binary search, we only looked at 3 different locations before
finding our value 19. That's a pretty good improvement!

[slide 16]

So now lets look at an algorithm for implementing binary search. You can
actually implement binary search using either an iterative algorithm or a
recursive algorithm. We will look at the iterative algorithm first, and then
take a look at the recursive version.

[slide 17]

Binary search starts by setting the initial values of start and end on lines 2
and 3 to the first and last indexes in the array. Then, the loop starts on line
4 and will repeat as long as the start index is less than or equal to the end
index. If start is greater than end, then we have searched the entire array
without finding our search value. In this case, the loop ends and we return -1
on line 14.

[slide 18]

Once inside our the loop, we calculate the middle index on line 5. Then we check
to see of the middle index points to our search value on line 6. If it does, we
simply return the middle index and stop.

It is important to note that this algorithm will just return the index to *an*
instance of our serach value in the array, although it may not be the first
instance.

If we want to find the first instance, we’d have to add a loop at line 7 to
search forward in the array until we find the first instance of our search value
before returning.

[slide 19]

If we didn't find our search value, then we determine where to continue our
serach in lines 8 and 10. Lines 9 and 10 update either the end or start indexes
as needed, and we start the search again by looping back to the top.

[slide 20]

Now we will look at a recursive version of the program, which is actually very
similar to the iterative version.

The recursive version moves the loop’s termination condition to the base case,
ensuring that it returns -1 if the start index is greater than the end index.
Otherwise, it performs the same process of calculating the middle index and
checking to see if it contains our search value. If it does not, it uses
recursive calls in lines 9 and 11 to search the first half or second half of the
array, whichever is appropriate.

[slide 21]

Computing the time complexity of binary search is actually very similar to the
merge sort that we looked at earlier. Basically, we need to determine how many
times the algorithm can check a value in the array – denoted by the grey cell at
each level - against our search value. The worst case is when the value does not
exist in the array. Like the merge sort, we cut the part of the array we are
searching in half after each comparison, so our time complexity will be the
same, lg(N). Compared to the other search algorithms we've looked at, this is
very fast!

[slide 22]

So, now that we know how fast binary search is, let's go back and compare it 
against our other sorting algorithms. Again, binary search runs on the order 
of lg(n) time.

As we can see, the function lg(N) is even smaller than N. So, performing a 
binary search is much faster than a linear search, which we already know runs 
in the order of N time. 

[slide 23]

However, a single linear search is much faster than any of the sorting algorithms
we’ve look at. So, the question become, when should we sort our data to speed up 
our searches?

This is actually a very hard question since there are so many factors that come 
into play, such as the type of data we are dealing with, the size of the data 
set, and how may searches we expect to perform.

However, it is generally true that the larger the data set and the more times we 
need to search it, the more we gain by sorting our data first. 

[slide 24]

To clarify that a bit, let's look at an example. Let's assume that we need to 
search a data set 10 times. We will simulate the running time based on the size 
of the data set. The orange line represent running 10 linear searches on the 
unsorted data set, while the blue line represents 10 binary searches after 
sorting the data set using merge sort.

As we can see, it is more efficient to perform a merge sort, which runs in 
N lg (N) time and then perform 10 binary searches running in lg (N) time, than 
it is to perform 10 linear searches running in N time. 

Obviously, the savings become more pronounced as the size of the data set grows.

In fact, this chart suggests that it may only take as few as 7 searches to see 
this benefit, even on smaller data sets. So, if we are writing a program that 
needs to search for a specific value in an array more than about 7 times, it 
is probably a good idea to sort the array before doing our searches, at least 
from a performance standpoint.

[slide 25]

In fact, this analysis suggests that it may only take as few as 7 searches to 
see this benefit, even on smaller data sets. So, if we are writing a program 
that needs to search for a specific value in an array more than about 7 times, 
it is probably a good idea to sort the array before doing our searches, at 
least from a performance standpoint.

[slide 26]

In this video, we looked at the binary search, the most popular search 
algorithm for sorted data structures. We demonstrated how the algorithm looks 
at the middle value in the array and then recursively searches either the top 
half of the bottom half of the array depending on whether the middle value is 
greater or lesser than our search value. 

We also showed that the time complexity of the binary search is lg(N), which 
is must faster than the previous search algorithms we've looked at. We also 
looked at combining sorting and searching and showed that even for small 
data sets, it doesn't require too many searches to making sorting worthwhile.

Clearly, binary search is an algorithm you want to keep handy!

