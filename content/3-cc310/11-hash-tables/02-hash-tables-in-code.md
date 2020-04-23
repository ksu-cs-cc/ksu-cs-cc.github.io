---
title: "Hash Tables in Code"
pre: "2. "
weight: 20
date: 2020-04-21T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/11-hash-tables/02-hash-tables-in-code-slides.pptx)

#### Video Script

[slide 2]

In this video, we will cover how to implement a hash table in code using arrays and linked lists. A hash table is a bit more complicated than several of the other data structures we've learned so far in this course, but the code itself is deceptively since we can rely on the techniques we've already learned for working with arrays and linked lists. 

[slide 3]

Specifically, since we are using linked lists in our implementation, we'll assume that our linked list supports the operations listed on this slide. We'll only need a few of these operations, but it helps to know that they are all available if needed. 

[slide 4]

First, let's look at the implementation of a hash function. As discussed in the textbook, a good hash function has three key properties. First, a good hash function is uniform, which means the function should map keys uniformly to the range of array indexes. Second, the function should be efficient. It should be able to be computed quickly. And finally, the function should be deterministic, which is another way of saying that the hash function should always map a given key to the same index value.

[slide 5]

Thankfully, both Java and Python include implementations of a hash function for a variety of the basic data types we want to use. So, we can just rely on those functions in our hash table. On this slide, we see a `computeIndex` function for both Java and Python. It simply uses the built-in function for finding a hash code, and then computes the result modulo the capacity of the internal array of the hash table to determine the index where the key should be located. 

[slide 6]

The other thing we'll need for our implementation is a way to store key-value pairs in a linked list. In Python, we can use the built in Tuple data type, which allows us to combine any two variables into a single tuple using parentheses.

In Java, we'll need to build our own `Tuple` class. So, our `Tuple` class should include two objects, a `key` and a `value`, as well as a constructor to initialize those values. We may also want to include other operations, such as getters, setters, toString, and equals, depending on how we plan to use the Tuple class. By now, we are pretty familiar with doing this for our own data structures, so we won't cover those details here.

[slide 7]

Now we can look at the overall structure of our hash table class. First, it includes three attributes - the size, giving us the number of elements stored in the table; the load factor, which helps us make sure our hash table is operating efficiently, and an array of doubly linked lists that actually store the data. 

This slide also shows the constructor, which is very simple. In the constructor, we initialize our array to either a given capacity, or a default capacity of 16 in this case. Then, we'll need to use a loop to initialize each element in the array to be an empty doubly-linked list. Finally, we'll set the size to 0, and our load factor to 0.75, which research has shown to be an effective balance between speed and memory usage. 

That's all we need to build our hash table class. Now, let's look at a few operations to see how it works.

[slide 8]

Of course, we'll need an implementation of a computeIndex function to help us find the index of a key based on its hash. We've already shown examples of this function in both Java and Python, but here is the pseudocode showing how it works. It simply uses the hash function to compute the hash of the key, then uses the modulo operation to convert that hash into an array index based on the capacity of our array. It's really simple, and quite efficient!

[slide 9]

Now let's look at one of the more complex operations, `put`, which is used to add a new key-value pair to the hash table. The `put` operation contains several steps, so let's review each one.

[slide 10]

First, we use the computeIndex method to compute the array index where the given key should be placed in the array. In most of our hash table operations where we recive a key as input, this is usually the first step.

[slide 11]

Then, we'll need to go to the linked list stored in that index of the hash table, and check to see if that key is in the list. So, we'll start by resetting the iterator of that list, and then getting the first element using the `reset()` and `getNext()` methods. We'll store the current element in the `current` variable. In this case, it is important to remember that `current` is a `Tuple`, storing a key-value pair. 

[slide 12]

Next, we'll use a while loop to iterate through each element in the list. This code should look very familiar - it is very similar to the code we used in earlier modules working with linked lists. 

Inside of the loop, we'll use an if statement to determine if the current tuple's key is the same as the key we received as input. If it is, we should simply update the value stored in that tuple to the new value we were given, and then return. By definition, a hash table cannot store the same key twice, so if we call the `put` operation with the same key, we'll assume that we just want to update the value stored with that key. 

[slide 13]

If the loop completes and we don't find the key in the list, then we'll just append it to the list. Notice that we are creating a new `Tuple` and then using the `append` method to add it to the list. We also need to increment the size of our hash table by 1 since we've inserted a new key-value pair.

[slide 14]

Finally, we'll need to check and see if our hash table has exceeded its load factor threshold. If so, we'll use the `doubleCapcity()` operation to increase the capacity and rehash all of the elements. We'll look at how that operations works a bit later in this video.

There we go! That's all it takes to add a new element to the hash table. It may seem a bit complex, but nearly all of this code is related to operations we've seen with other data structures.

[slide 15]

At this point, let's take a step back and analyze the performance of the `put` operation. Recall that the goal of our hash table data structure is to acheive constant time insertion. 

So, what would the best case look like? Ideally, we want our elements evenly spread across the buckets of the hash table. If our load threshold is less than 1, that means we expect to have no more than 1 element per bucket in the best case, and in many cases we should have several empty buckets as well. So, that means that the while loop in the `put` opeation will look at no more than 1 element, and then the value is either updated if the key is found, or a new key-value pair is appended to the list. Thankfully, appending to a linked list is a constant time operation, so, in the best case, we expect our `put` operation to also be in constant time. That means that, as our hash table gets larger, the time it takes to add a new item to the list should remain constant.

[slide 16]

What about the worst case? What would that look like? 

For a hash table, the worst case is that all the elements end up in a single bucket. This can happen if the hash function is not very good, or if the data isn't properly distributed. For example, if our hash table has capacity 4, but we only put in keys that hash to multiples of 4, they will all end up in the same bucket. That's not good!

In that case, the while loop in our `put` operation will have to look at every element in the hash table, which runs on the order of N time. At that point, the performance of our hash table is no better than a linked list!

Thankfully, in the real world, this worst case scenario is very rare and unlikely to happen in practice, as long as we have a good hash function!

[slide 17]

The `get` operation is nearly identical to the `put` operation. We start by getting the index of the bucket where we expect to find the key. Then, we'll use the list iterator functions to iterate through the items in the list, looking for the key. If we find it, then we can return the associated value. If not, we'll just return null at the end of the function, outside of the loop. 

Just like the `put` operation, the `get` operation is expected to run in constant time under normal circumstances, but the worst case can be as bad as order N time.

[slide 18]

The `remove` operation is exactly the same as the `get` operation, except that we also must remove the key-value pair from the list if it is found using the `removeCurrent` method. We'll also need to decrement the size by 1. 

[slide 19]

We may also wish to make a copy of this hash table. In this case, instead of being given an index in the array based on a key, we'll use a for loop to iterate through each index of the array.

Inside of that loop, we'll use the same while loop to iterate through each element in the list at that array index, and put those key-value pairs into the new hash table. 

This two loop structure is how we can iterate through each element of the hash table. The code for the `toString()` method is very similar.

[slide 20]

The last operation we'll look at is the `doubleCapacity()` operation. This method is called when the load factor of the hash table exceeds the threshold we have set. When that happens, we need to double the capacity of the array, and then rehash all of the elements and store them in their proper locations again. 

We start by creating a new array with twice the capacity, and initialize each element to a new list. 

Then, we'll use the same two-loop structure from the `copy()` method to iterate through each element in our existing hash table. 

Inside of the innermost loop, when we find an element, we'll recompute the index using our new capacity and the hash of the key, and then append that tuple to the correct list at the newly computed index. 

Finally, we'll update our `hashTable` array to be the new array. 

[slide 21]

In this video, we looked at pseudocode for several operations needed to build a hash table data structure. Thankfully, most of the code itself uses structures and techniques we are already familiar with. 

We also discussed how to evaluate the performance of these hash table operations, and discovered that we can indeed acheive constant time insertion and retrieval, provided that the elements are properly distributed across the buckets of the hash table. 

