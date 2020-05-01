---
title: "Algorithm Performance"
pre: "6. "
weight: 60
date: 2020-04-24T00:00:26-05:00
---

{{< youtube pu5SPVUescU >}}

#### Resources

* [Slides](/3-cc310/12-performance/06-algorithms-slides.pptx)

#### Video Script

[slide 2]

Let's briefly review the different searching and sorting algorithms we covered in this course and how their performance compares to one another.

First, as we saw several times in our analysis of data structures, there are two basic methods we can use to search for a particular element. First, we can perform a linear search, which requires us to look at each individual element in the structure until we find the one we want. So, that algorithm runs on the order of N time.

We can improve that by quite a bit using binary search, which allows us to find an element in the order of lg(N) time. However, that comes with a very important caveat - it assumes that we can access individual elements in our data structure in constant time, and that the data structure is sorted. So, using binary search on a sorted array definitly runs on the order of lg(N) time, but the same process performed on a linked list would run in order of N time, and could actually be worse than performing a linear search. So, while it may look better mathematically, we also have to keep in mind the data structure we are using.

We also explored many different ways to sort our data. Again, this analysis assumes that we can access individual elements quickly, so these algorithms may perform differently when implemented on a linked list instead of an array.

The two most basic sorting algorithms, selection sort and bubble sort, both run on the order of N^2 time. So, while these algorithms are simple to implement and understand, they have very poor performance and may not be used in practice. The only exception would be the fact that bubble sort could be written to terminate early if it determines that the array is completely sorted before it performs all of the iterations. In that case, the real-world performance of bubble sort on a nearly sorted array may be blazingly fast!

We also learned about the merge sort algorithm, which uses a divide and conquer method to sort an array of data. It runs on the order of N lg(N) time, even in the worst case. Merge sort is a great solution when we want to have guaranteed good performance. However, since most merge sort implementations require extra data storage for merging the data back together, it may not be the best choice if memory is limited.

Finally, we learned the quicksort algorithm, which uses another divide and conquer approach to sort an array. In the best case, if we choose our pivot element well, we can expect the algorithm to run on the order of N lg(N) time, just as fast as merge sort. In fact, research has shown that quicksort tends to be faster in practice! However, quicksort does have a very bad worst case, where the pivot element is always chosen to be the smallest or largest element in the list. In that case, the performance drops all the way to the order of N^2, which is quite a bit slower. 

