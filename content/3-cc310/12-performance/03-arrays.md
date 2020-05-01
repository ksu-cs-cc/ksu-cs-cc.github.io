---
title: "Array Structure Performance"
pre: "3. "
weight: 30
date: 2020-04-24T00:00:26-05:00
---

{{< youtube An_SzFppNJA >}}

#### Resources

* [Slides](/3-cc310/12-performance/03-arrays-slides.pptx)

#### Video Script

[slide 2]

Let's start by looking at the performance characteristics of arrays. They are some of the simplest and most commonly found data structures, since nearly every programming language supports them in some fashion. 

Adding elements to an unsorted array can always be done in constant time - we simply have to keep track of the index of the last element added to the array, and then we can add our new elements after that. The only interesting case happens when we run out of space. In that case, we may have to resize the array and copy the elements to a new version, which may seem like a costly operation, but if we only do that once in a while the cost is actually negligible so we won't worry about that here. 

Accessing an element in an array is also a constant time operation. All we have to do is use the index of the element, and our computer can immediately find it in memory without any additional work. Arrays are lightning fast!

Unfortunately, if we want to search for a particular element, we must use a linear search method, which runs in the order of N time. In effect, we'd have to look at each element in the array until we found the one we were searching for. 

Finally, if we wish to find and delete an element from the array, that would also run on the order of N time. We'll search linearly through the array until we find the element to be removed, and then shift all elements after that element forward one index. No matter where our deleted element was in the array, we end up looking at all of them.

[slide 3]

We can improve the performance of an array a bit by sorting it. However, once the array is sorted, we now must make sure that new elements are inserted into the proper place. In the best case, that requires performing a binary search process, which runs in order of lg(N) time. However, in the worst case, we may have to shift all the elements in the array back one space. This would occur if we are inserting an element at the beginning. So, in the worst case, it would require us to shift all N elements, so the operation runs on the order of N time. 

Thankfully, accessing elements in a sorted array is still a constant time operation.

The biggest improvement from using sorted arrays comes when we must search for an element. In that situation, we can use a binary search to cut the time from order N to order lg(N). As we saw in an earlier module, just a few searches over the entire use of the data structure makes sorting it worthwhile. 

Lastly, the delete operation has the same performance as the insert operation. In the best case, we can just use binary search to find an remove the element, which runs in order lg(N), but we may have to shift up to N elements around, making the whole operation run in order N time. 

So, sorted arrays can be faster than unsorted arrays in some situations, but slower in others. We can avoid this by reading all of our data first, then sorting the array once, and only using it for searches afterward. That avoids the costly insert and delete operations!

[slide 4]

We can also use arrays to implement both stacks and queues. By doing so, we are able to limit the delete operation to just the front or the end of the structure, which makes those operations run in constant time. So, stacks and queues based on arrays can be quite fast, especially if we don't need to search through the entire structure to look for a particular item.

As we can see, arrays are very fast and efficient data structures, even though they are very simple in nature.
