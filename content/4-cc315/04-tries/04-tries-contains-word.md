---
title: "Tries: Contains Word"
pre: "4. "
weight: 44
date: 2019-02-04T10:53:26-05:00
---

{{< youtube zG1aSR1iivI >}}

#### Resources
* [Slides]({{< relref "/4-CC315/04-tries/04-tries-contains-word-slides.md" >}})

#### Video Script

[Slide 1]

In this video we will look at how to determine if a word is in a trie. Suppose we have this tree to the left and we are wanting to add the word 'data'. We would start at the root of our trie and work through the word 'data' letter by letter. First is letter 'd', which is a child of our root. 

[Slide 2]

Then from node 'd' we would be looking for child 'a'. We could say that we are now searching for the word 'a', 't', 'a' from the node 'd'.


[Slide 3]

Now from node 'a' we look for child 't'. Here we could say that we are searching for the word 't' 'a' from the node 'a'.


[Slide 4]

Now we have traversed to 'dat' and we are searching for word 'a' from the node 't'. 


[Slide 5]

At this point we have traversed 'data', ending at 'a' which has its is_word attribute as true. So we would return true because 'data' is in our trie. Now that we have an example under our belts, lets look at the pseudocode of searching for a word in our trie. 


[Slide 6]

Here we have the pseudocode for searching for a word in our trie. We will work through this piece by piece. Working through our example, you may have noticed that this is a recursive process. 


[Slide 7]

Similar to the base case for our add word and remove word functions, the base case for our contains word function is when the word length is zero. This means we have made it all the way to the end of our word. Once we get to the end of our word, we can simply return the nodes `is_word` attribute.


[Slide 8]

The recursive case for our contains word function first breaks the word into the first letter and the remainder. We find the child that corresponds to that first letter. If there is not a child like this, then we return false because the word will not exist. If this child does exist, then we call the contains word function on the remainder of the word from the child. 