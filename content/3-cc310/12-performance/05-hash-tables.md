---
title: "Hash Table Performance"
pre: "5. "
weight: 50
date: 2020-04-24T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/12-performance/05-hash-tables-slides.pptx)

#### Video Script

[slide 2]

Now let's look at the performance of a hash table. Hash tables are a unique combination of arrays and linked lists that try to achieve the "best of both worlds" in terms of performance. However, because of the structure of a hash table, we must be careful when analyzing the performance of each operation since there are clearly best and worst cases.

In the best case, the capacity of the hash table is much larger than the number of elements that it is storing, and the elements are equally spread across the buckets that make up the structure. So, ideally, each bucket stores either 0 or 1 elements, and looking at just a single element in a linked list is a constant time operation.

In the worst case, however, all of the elements in the hash table end up in the same linked list, usually because the choice of hash function doens't work well with the data being stored in the structure. So, that means that many operations require iterating through a linked list that contains N elements, running in the order of N time.

Let's start by looking at the insert operation. If the data is properly distributed, then it should run in constant time. We use the hash function to find the bucket that it should be stored in, and then we look at just a few elements in that bucket. Overall, it runs very quickly.

In the worst case, we end up looking through a bucket that contains every element in the hash table, and the operation runs on the order of N time. This is not very good at all!

The same happens when we try to access or remove an element. In the best case, it runs in constant time. However, the worst case runs on the order of N time. 

The only exception to this is the operation to find a particular value in the hash table. Since we aren't given a key, we must simply look through each element, which is once again a linear search that runs on the order of N time.

Thankfully, in practice the performance of a hash table is nearly constant time, and the worst case scenario is very rare. So, we can dependably use hash tables when we need to store key-value pairs in our program, and know that the data can be stored and accessed very quickly. 