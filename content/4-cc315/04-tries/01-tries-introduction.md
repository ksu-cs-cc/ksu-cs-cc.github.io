---
title: "Tries Introduction"
pre: "1. "
weight: 41
date: 2019-02-04T10:53:26-05:00
---

{{< youtube BNA3tbURiZk >}}

#### Resources
* [Slides]({{< relref "/4-CC315/04-tries/01-tries-introduction-slides.md" >}})

#### Video Script

[Slide 1]

In this module, we will talk about a specific type of tree called a trie. These are trees which contain a user defined vocabulary. Nodes which are the ends of words will be depicted as a double lined node. For example, in this trie we have five words in the vocabulary. 

We build words by traversing from the root to a double lined node. For example, we could start at the root, then go to `t` then `h` and finally `e` making the words `the`. 

While the words `toad`, `gold`, and `toll` are real words, they are not words in this user defined vocabulary. The words that are contained in this trie are: `the`, `go`, `goal`, `goat`, and `golf`.

In this example, we do see that a majority of the words end at leaves. It is not necessary for words to end on leaves. We can also see that the word `go` does not end in a leaf. 

This particular example shows words that are part of the English vocabulary. However, tries are not limited to this. The only constraint on tries is that the nodes must contain characters.


[Slide 2]

Here we have another example of a trie that shows emojis as our vocabulary. Under our trie, I have listed the four words that are contained in our trie. In the next videos, we will discuss the nuances of creating tries.