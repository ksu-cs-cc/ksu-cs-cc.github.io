---
title: "Maps"
pre: "2. "
weight: 20
date: 2020-02-11T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/04-data-structures-algorithms/02-maps-slides.pptx)

#### Video Script

[Slide 2]

Basic maps are fairly simple. They are what we call a *key – value pair.* You
might also hear these referred to as an *associative array,* a *dictionary,* or
a lookup table. Keys act like an array index. You give the map a key and it
returns the value associated with that key.

The insertion operation for a map is called *put*, which allows you to put a new
key – value pair into the map. The *get* operation, on the other hand returns
the associated value for a given key. The *entries* and *keys* operations return
the set of *values* and *keys* from the map. And the *containsKey* and
*containsValue* operations determines if a given key or value is stored in the
map.

[Slide 3]

In our example we would use the *get* operation to lookup a particular value.
For instance, the operation call *get(Colorado)* would return the value
*Denver.*

[Slide 4]

Likewise, if we looked up to see if the key “Texas” was in our set of keys, the
*keys* operation would return false.

[Slide 5]

To implement maps more efficiently, we often use what are call “hash tables”. A
hash table stores the map *values* in an array and uses a special *hash
function* to convert any valid key to an index into the array to find the
associated *value*.

The reason we use a hash function instead of doing a lookup in a simple map is
efficiency. Instead of looping through each possible key and doing costly
comparison operations, you simply call a function and then use the index to
access the array directly.

[Slide 6]

For example, if we input “John Smith” to our hash function, we should get an
index into our array. In this case, the hash of “John Smith” returns the value
2, which we use to lookup the value 521-1234.

Maps work great for applications where you need to find information based on a
specific type of data or key. However, it is helpful to keep the keys unique.

[Slide 7]

Unfortunately, it is extremely difficult to find hash functions that return
unique values for all possible inputs. Therefore, we generally have to provide
additional logic to handle these “collisions”.

In this example, Sandra Dee and John Smith both get mapped to index 152. So, in
this case we just create a list of all the data that maps to the same index. Of
course to find the right piece of data, we will need to search the list.

[Slide 8]

In this video, we have looked at basic map data structures that make looking up
data based on keys much more efficient. In simple maps, we have a set of keys
that map directly to values and we have to search through the list of keys to
find the value we are looking for.

To make this process more efficient, we can use hash functions that map our keys
to the index of an array. However, we often have to provide additional logic to
handle collisions where the hash function maps two keys to the same index.

We will learn more about maps in future modules.
