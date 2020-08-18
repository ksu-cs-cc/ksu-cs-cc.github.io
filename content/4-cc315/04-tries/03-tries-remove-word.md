---
title: "Tries: Removing Words"
pre: "3. "
weight: 43
date: 2019-02-04T10:53:26-05:00
---

{{< youtube En7FDq5XrsA >}}

#### Resources
* [Slides]({{< relref "/4-CC315/04-tries/03-tries-remove-word-slides.md" >}})

#### Video Script

[Slide 1]

In this video we will look at how to remove words from a trie. Suppose we have this tree to the left and we are wanting to remove the word 'hope'. We would start at the root of our trie and work through the word 'hope' letter by letter. First is letter 'h', which is a child of our root. 

[Slide 2]

Then from node 'h' we would be looking for child 'o'. We could say that we are removing word 'o' 'p' 'e' from node 'h'.


[Slide 3]

Now from node 'o' we look for child 'p'. Here we could say that we are removing word 'p' 'e' to node 'o'.


[Slide 4]

Now we have traversed to 'hop'. Now we are left with child 'e'. Now we are removing word 'e' from node 'p'. 


[Slide 5]

Visually, we remove the double outline from node 'e' however, in code, we would set the is_word attribute to false. Unlike when we added a word, we have a few more tasks to complete. We want to clean up the tree so that we aren't consuming unnecessary memory. We see that node 'e', which we have ended on, is a leaf and is not the ending of a word, so we remove it. 


[Slide 6]

Then we are back at 'p'. Again, this is a leaf and is not the ending of a word, so we remove it from our trie. If we did have the word 'hop' in our trie, meaning the 'p' had a double line, then we would not delete node 'p'.


[Slide 7]

Now we have completed removing the word 'hope' from our trie. 


[Slide 8]

Here we have the pseudocode for removing a word from our trie. We will work through this piece by piece. Working through our example, you may have noticed that this is a recursive process. 


[Slide 9]

The base case for our remove word function is when the word length is zero. This means we have made it all the way to the end of our word. Once here, we have a special consideration that we did not encounter in our example. If we are at the end of our word and it is already not a word, then we return false because we have not actually removed the word. If we are at the end of our word and it is a word, then we set its `is_word` attribute to false and return true. 


[Slide 10]

The recursive case for our remove word function first breaks the word into the first letter and the remainder. We find the child that corresponds to that first letter. If there is not a child like this, then we return false because we are not able to remove the word since it doesn't exist. If the child does exist then we call the remove word function on the remainder of the word from the child. After that, we clean up our tree and return from the function. In the next video we will look at determining if a trie contains a particular word. 