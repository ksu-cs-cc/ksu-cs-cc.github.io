---
title: "Tries: Word Functions"
pre: "6. "
weight: 46
date: 2019-02-04T10:53:26-05:00
---

{{< youtube En7FDq5XrsA >}}

#### Resources
* [Slides]({{< relref "/4-CC315/04-tries/06-tries-word-functions-slides.md" >}})

#### Video Script

[Slide 1]

We hve two functions to wrap up our trie implementation and those are maximum word length and word count. We will first look at maximum word length. 


[Slide 2]

As the name implies, we want this function to return the length of the longest word. Like the previous functions, we will work through an example. Looking at this trie, we can tell that 'dates' is the longest word but we will examine how we could determine the longest word algorithmically. 


[Slide 3]

Starting at the root, we would go to each child and find its longest word by using the longest word function. 


[Slide 4]

Then we do the same for each of that nodes children, and repeat the process. 

[Slide 5]

Once we get to a leaf, if it is a word, then we return zero. 


[Slide 6]

The longest word for each of these children is zero. 


[Slide 7]

In this case, both children have the same longest word. We would take the highest of the two and add one. 


[Slide 8]

Then we continue with the other children doing the same recursive process. 

[Slide 9]

We have a child with longest word with length zero. 

[Slide 10]

And we continue down the other child recursively. We have a leaf that is the end of a word, so we return zero. 


[Slide 11]

We return one plus the highest child for the longest word of the parent. 


[Slide 12]

The children of node `t` had longest words with length zero and one. So the longest word for `t` is two characters and continue in this style. 

[Slide 13-17]

Fast forwarding a bit, we end up with the longest word having a length of 5. Recall that 'dates' was our longest word and this matches with our result! 

[Slide 18]

Here we have the formal pseudocode for getting the length of the longest word. The base case is that we are at a leaf which is the ending of a word. In which case, we return zero. In the recursive case, we get the maximum word length for all of the children and return one plus the maximum. We have a 'tracker' called MAX which is initialized to negative one as we can have lengths of zero. 

[Slide 19]

The next function is word count, which returns the number of words in our trie. This will follow a similar process to our maximum word length function. Our base case is if we are at a word then return one. In the recursive case, we sum the number of words in each child. This concludes the functions for our implementation of a trie. 