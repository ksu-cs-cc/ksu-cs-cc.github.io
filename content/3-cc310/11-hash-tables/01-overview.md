---
title: "Hash Tables Overview"
pre: "1. "
weight: 10
date: 2020-04-21T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/11-hash-tables/01-overview-slides.pptx)

#### Video Script

[slide 2]

Throughout this course, we've explored many different types of data structures. Each one has their own strengths and weaknesses. So, at this point, we may want to ask ourselves: what would an ideal data structure look like? Ideally, we'd like to find a data structure where we can insert and remove elements in constant time, but also be able find them in constant time. Is that even possible? Let's take a look.

[slide 3]

We started with simple unosorted arrays. However, if we want to find and retrieve a specific element from an unsorted array, we have to search through the entire array, which would run on the order of N time. 

We can improve that by sorting the array, which cuts our searching and retrieval time down to order of lg (N) time. This is pretty good! However, if we want to insert elements into an array in sorted order, it runs on the order of N time since we may have to shift elements backwards in the array. That's not very good.

Linked lists may seem a bit better, since insertion can be done in constant time. Unfortunately, since we can't directly access elements in a linked list like we can with array indices, we are back to doing a linear search to find and retieve elements. 

So, it seems like neither of these data structures is truly ideal. Could we combine them somehow to get the "best of both worlds"?

[slide 4]

In this module, we will explore the "hash table" data structure. To implement a hash table, we need three components. First, we'll use an array, which allows us to use array indices to directly jump to a particular location in the array quickly. Then, we'll use a set of buckets, where each bucket is an instance of a linked list. Since the data will be stored in these buckets, we can add and remove data in constant time! Finally, to bring it all together, we'll need a "hash function" which allows us to determine which bucket our data belongs in.

[slide 5]

Structurally, a hash table looks like this. We have an array acting as our primary container, and each element in the array is an instance of a linked list acting as a "bucket" that contains the elements in the hash table. So, when we add elements to the hash table, we simply determine what bucket to place it in, and then add that element to the linked list that is stored there.

[slide 6]

The key part of a hash table is the _hash function_. A hash function is a special type of function that can take in any object as input, and it will produce an integer that represents that object as output. We'll discuss how to make a good hash function later in this module. Thankfully, both Java and Python already include implementations of a hash function that work for most basic objects, and there is also a very easy way to combine those functions to create hash functions that work with our own classes. 

Right now, all we need to know is that a hash function takens in any object as input, and it produces an integer that represents that object. If we give it the same object, we should always get the same result. 

[slide 7]

Let's look at an example to see how this works. In this example, we are using integers as our keys. So, the hash function will simply compute the result of the key modulo the size of the array, which in this case is 4. That way, each key, no matter what it is, will be assigned a value from 0 to 3, which corresponds to one of the buckets in the hash table.

[slide 8]

So, what would happen if we want to place the number 16 into our hash table? First, we must compute the index of the bucket it should be stored in using our hash function.

[slide 9]

In this case, the result of 16 % 4 is 0, since 16 is evenly divisible by 4 without any remainder. 

[slide 10]

So, we know that the element 16 should be placed in the bucket at array index 0. 

[slide 11] 

Since each element in the array is a linked list, we can simply append the value 16 to the list. That's all there is to it! We've added our first element to our list.

[slide 12]

What if we want to add 7 to the list? In that case, we'll repeat the process once again. First, we'll compute the index using the hash function.

[slide 13]

Since 7 % 4 is 3, we know it belongs in the list at array index 3. We'll append 7 to the list there.

[slide 14]

We can repeat the process again for the element 13

[slide 15]

It should be stored in array index 1, so we'll append it to the list there.

[slide 16]

What if we want to add the number 12 to the list? 

[slide 17]

In this case, 12 % 4 is also 0, which is the same index we received when our input was 16. This is called a _hash collision_, and can be a problem if we don't have a plan to deal with it. So, what should we do when we need to add an element to a bucket that already contains an element? 

[slide 18]

This is where the value of having each bucket be a linked list comes in. We can simply go to the linked list at array index 0, and then add the new element to that list. So, we can have multiple items stored in the same bucket, as long as they are unique.

[slide 19]

Now that we've stored a few items in our hash table, how can we quickly and easily retrieve those times? This is one of the most powerful features of a hash table - we can use the same hash function on a given key to look up its location in the hash table and confirm if it is there quickly.

In this case, we are given the key 7, which we once again use as input to our hash function to compute the index in the array where it would be located.

[slide 20]

The index we get is 3, so we look at the list that is at array index 3 and see if it contains 7. Since it does, we know that 7 is in the hash table, and we can retrieve it!

[slide 21]

 As we'll see later in this module, we actually use hash tables to store key-value pairs, so in this way we can return the _value_ that is paired with 7 as the _key_.

[slide 22]

What if we want to find the element 12 in the hash table? Once again, we'll get the index 0 from our hash function...

[slide 23]

So we'll look at the list at array index 0. 

[slide 24]

Here, we can use the list iterator methods to iterate through each element in the list. So, we'll look at the first element in the list, which is 16

[slide 25]

Since that is not the element we want, we'll follow the next pointer in the list to the second element.

[slide 26]

Here, we found 12, which is the element we are looking for! So, we can return the value associated with it back to the calling function. 

However, notice that we had to search through 2 items in this list to find what we wanted. This isn't that many, but it might cause a problem as we add more elements. Remember, we want to build an ideal data structure that has constant time retrieval. If the lists are more than just 1 item, we are not able to get constant time performance. So, we want to minimize the number of hash collisions, which result in multiple elements being stored in the same list. 

[slide 27]

As we store more key-value pairs in a hash table, the number of hash collisions will increase. The more collisions we have, the less efficient our hash table will become. It won't take long to erase all the benefits of having a hash table in the first place. So, what can we do?

[slide 28]

At some point, it makes sense to increase the capacity of the array, much like we did with stacks and queues that we implemented using arrays. 

Notice that we have to update our hash function to compute index values that cover the entire range of our new array. In this case, we now must have indexs that range from index 0 to index 7. 

[slide 29]

Of course, this creates a another problem. What if we want to retrieve item 13? 

If we run 13 through our new hash function, we get an index of 5, which is not where 13 was stored. So, how do we solve this?

[slide 30]

The solution is to _rehash_ our table every time we increase or decrease the size of the array. When we rehash our table, we simply compute new indexes for all key-value pairs and add them into the new array at the appropriate location as we have done here. Now, if we want to retrieve 13, it will be right where we stored it, at index 5.

Notice how much room we now have to store new key-value pairs. There is a 50-50 chance that the next item we will store will not cause a collision and, if it does, there will be at most one other key-value pair in the same bucket.

Now that we know what to do when we have a crowded hash table, the question is, when do we need to do it?

[slide 31]

There are three key things we use when making this decision. First, there is the _capacity_ of the current array. Here we have an array of capacity 4. Next, we have the _size_ of the hash tables in terms of the number of key-value pairs stored in the table. In this example, we also have 4 key-value pairs: 16, 12, 13, and 7. And finally, there is the _load factor_ (or ratio) between the size of the hash table and its capacity, `size / capacity`.

Typically, when the load factor reaches a specified threshold, we double the capacity of the array and then rehash the table using the new array. The load factor threshold we choose is a tradeoff between space and time. The larger the array, the more memory you use, but you have fewer collisions. And obviously, the smaller array you use, the more collisions you will have and the greater the time required to retrieve key-value pairs from the table. Through research and experience, it has been shown that a load factor of 0.75 generally works best.

Thus, each time we add a key-value pair to the hash table, we should check to see if the load factor of the table has exceeded our threshold of 0.75. In the example given, the size of the table is 4 key-value pairs and the capacity of the array is 4. This yields a load factor of 1.0 which is clearly greater than our threshold of 0.75. We should definitely increase the size of our array and rehash the table.

[slide 32]

In this video, we introduced the concept of a hash table, which is a data structure that aims to provide the ideal of constant time insertion and constant time retrival operations. It consists of an array of buckets, usually implemented as linked lists, combined with a _hash function_ that determines which bucket a particular key belongs in. By carefully maintaining the balance between the size and capacity of the hash table, combined with a good hash function, we can guarantee that most insertions and retrievals run in constant time in the best case.