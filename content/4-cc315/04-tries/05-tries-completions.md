---
title: "Tries: Completions"
pre: "5. "
weight: 45
date: 2019-02-04T10:53:26-05:00
---

{{< youtube En7FDq5XrsA >}}

#### Resources
* [Slides]({{< relref "/4-CC315/04-tries/05-tries-completions-slides.md" >}})

#### Video Script

[Slide 1]

One of the more analytically complex functions for tries is completions. The functionality of completions will be to return all of the words that exist in our trie that could complete the input string. For example, we could get the completions of of 'd' 'a'. We would anticipate getting back: 'data', 'date', 'dates', and 'day'. Lets walk through this example to get a better understanding. We would call the completions function from the root on the string 'd' 'a'. 


[Slide 2]

We would traverse to node 'd' and call the completions function from 'd' on the string 'a'. 


[Slide 3]

From node 'a', we would call the completions function on the empty string. We do this as we have reached the end of our prompt string and we are now searching for words within this sub-trie. 


[Slide 4]

Node 'a' has two children so we will need to call the completions function from both of them. Suppose that we start with node 't'. Remember, we have reached the end of our input string. So we would call the completions function with the empty string from node 't'.


[Slide 5]

Node 't' has two children so we will need to call the completions function from both of them. Suppose that we start with node 'a'. Node 'a' itself is the end of a word, so we will need to return that. We must also traverse the children of 'a'. Node 'a' has no children, so we return from node 'a'.


[Slide 6]

Node 'a' returns the array with the letter 'a' in it to node 't'. We must continue traversing the children of node 't'. Next will be node 'e'.


[Slide 7]

Node 'e' is the end of a word so we need to be sure that we return the letter 'e' to node 't'. Before that, we must traverse node 'e's children. 


[Slide 8]

Node 'e' has a child , node 's'.  This node has no children and is the end of a word.


[Slide 9]

We return the letter 's' to node 'e'.


[Slide 10]

Now we can see how we start to build the words. When we return 's', we will insert the letter 'e' right before it, making the string 'e''s'. 

[Slide 11]

Now node 'e' will return the array with 'e' and 'e''s' in it. 


[Slide 12]

Now we are back to node 't' and we have completed the completions on its children. Now we put them all together. We get 't''a' from child 'a' and we get 'te' and 'tes' from child 't'. So node 't' will return 't''a', 't''e', and 't''e''s' to node 'a'. 

[Slide 13]

We must now continue with the children of node 'a'. We have covered node 't' so now we do the completions on node 'y'. 


[Slide 14]

Node 'y' has no children, so we return from node 'y' with the array that contains just 'y'.


[Slide 15]

Now we are back to node 'a' and we have completed the completions on its children. Now we put them all together. We get 'a''t''a', 'a''t''e', and 'a''t''e''s' from child 't' and we get 'ay' child 'y'. So node 'y' will return the array of those strings. 


[Slide 16]

Now we are back to node 'd'. Since we are only looking for the strings that start with 'd''a', we do not traverse child 'o'. At this point, we return to the root with our completed words: data, date, dates, and day.


[Slide 17]

As I mentioned before, the completions function is a more complex trie function. I have included the pseudocode here and we will work through it piece by piece as we did with other functions. 


[Slide 18]

Recall that in our example, we first traversed the tree while working through the input string. This if block of our completions function corresponds to that. 


[Slide 19]

Here, we build in an extra if statement which allows for us to handle the case where the input string isn't captured within our trie. The else proceeds to work through the input string as we did initially in our example. 


[Slide 20]

The else block of our function is built for when we have traversed the entirety of our input string. 


[Slide 21]

The last key part that I want to draw attention to, is when we are building the words. Recall that in our example, we took the item of the node we were at and inserted it at the beginning of each of the completions returned by the nodes children. In these two places in the pseudocode, we are applying that principle. That completes the overview for the completions function for our tries implementation. 