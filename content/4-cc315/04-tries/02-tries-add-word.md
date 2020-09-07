---
title: "Tries: Adding Words"
pre: "2. "
weight: 42
date: 2019-02-04T10:53:26-05:00
---

{{< youtube kasaXiMbj9A >}}

#### Resources
* [Slides]({{< relref "/4-CC315/04-tries/02-tries-add-word-slides.md" >}})

#### Video Script

[Slide 1]

In this video we will look at how to add words to a trie. Suppose we have this tree to the left and we are wanting to add the word 'hope'. We would start at the root of our trie and work through the word 'hope' letter by letter. First is letter 'h', which is a child of our root. 

[Slide 2]

Then from node 'h' we would be looking for child 'o'. This is already a child of 'h' so we traverse to it. We could say that we are adding word 'o' 'p' 'e' to node 'h'.


[Slide 3]

Now from node 'o' we look for child 'p'. There is not a child 'p' for 'o' so we simply instantiate a new node with item 'p' and make it a child of 'o'. Here we could say that we are adding word 'p' 'e' to node 'o'.


[Slide 4]

Now we have traversed to 'hop'. While this is a word, it is not the word we are trying to add. Now we are left with child 'e'. Node 'p' has no children, so again, we must create node 'e' and make it a child of node 'p'. Now we are adding word 'e' to node 'p'. 


[Slide 5]

Visually, we give node 'e' a double outline however, in code, we would set the is_word attribute to true. That completes the adding of the word 'hope'. Now that we have an example under our belts, lets look at the pseudocode of adding a word. 


[Slide 6]

Here we have the pseudocode for adding a word to our trie. We will work through this piece by piece. Working through our example, you may have noticed that this is a recursive process. 


[Slide 7]

The base case for our add word function is when the word length is zero. This means we have made it all the way to the end of our word. Once here, we have a special consideration that we did not encounter in our example. If we are at the end of our word and it is already a word, then we return false because we have not actually added the word. If we are at the end of our word and it is not already a word, then we set its `is_word` attribute to true and return true. 


[Slide 8]

The recursive case for our add word function first breaks the word into the first letter and the remainder. We find the child that corresponds to that first letter. If there is not a child like this, then we create it ourselves, like when we added 'p' and 'e' in our example. Then we add the remainder of our word to that node. And that is how we add a word to our trie. Next we will see how to remove a word from our trie. 