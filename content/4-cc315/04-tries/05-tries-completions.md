---
title: "Tries: Completions"
pre: "5. "
weight: 45
date: 2019-02-04T10:53:26-05:00
---

{{< youtube urFTpJwqRVY >}}

#### Resources
* [Slides]({{< relref "/4-CC315/04-tries/05-tries-completions-slides.md" >}})

#### Video Script

[Slide 1]

One of the more analytically complex functions for tries is completions. The functionality of completions will be to return all of the words that exist in our trie that could complete the input string. For motivation of how this will work, suppose we have this trie and our user types 'c''a'. 

[Slide 2]

We would traverse down our tree with the letters they have already typed, first 'c'

[Slide 3]

Then we would go to 'a' and now we would search through all of the children finding words. We would expect the words 'cat' and 'can'


[Slide 4]

Lets work through another example in detail. We could get the completions of of 'd' 'a'. We would anticipate getting back: 'data', 'date', 'dates', and 'day'. Lets walk through this example to get a better understanding. We would call the completions function from the root on the string 'd''a'. 


[Slide 5]

We would traverse to node 'd' and call the completions function from 'd' on the string 'a'. 


[Slide 6]

From node 'a', we would call the completions function on the empty string. We do this as we have reached the end of our prompt string and we are now searching for words within this sub-trie. 


[Slide 7]

Node 'a' has two children so we will need to call the completions function from both of them. Suppose that we start with node 't'. Remember, we have reached the end of our input string. So we would call the completions function with the empty string from node 't'.


[Slide 8]

Node 't' has two children so we will need to call the completions function from both of them. Suppose that we start with node 'a'. Node 'a' itself is the end of a word, so we will need to return that. We must also traverse the children of 'a'. Node 'a' has no children, so we return from node 'a'.


[Slide 9]

Node 'a' returns the array with the letter 'a' in it to node 't'. We must continue traversing the children of node 't'. Next will be node 'e'.


[Slide 10]

Node 'e' is the end of a word so we need to be sure that we return the letter 'e' to node 't'. Before that, we must traverse node 'e's children. 


[Slide 11]

Node 'e' has a child , node 's'.  This node has no children and is the end of a word.


[Slide 12]

We return the letter 's' to node 'e'.


[Slide 13]

Now we can see how we start to build the words. When we return 's', we will insert the letter 'e' right before it, making the string 'e''s'. 

[Slide 14]

Now node 'e' will return the array with 'e' and 'e''s' in it. 


[Slide 15]

Now we are back to node 't' and we have completed the completions on its children. Now we put them all together. We get 't''a' from child 'a' and we get 'te' and 'tes' from child 't'. So node 't' will return 't''a', 't''e', and 't''e''s' to node 'a'. 

[Slide 16]

We must now continue with the children of node 'a'. We have covered node 't' so now we do the completions on node 'y'. 


[Slide 17]

Node 'y' has no children, so we return from node 'y' with the array that contains just 'y'.


[Slide 18]

Now we are back to node 'a' and we have completed the completions on its children. Now we put them all together. We get 'a''t''a', 'a''t''e', and 'a''t''e''s' from child 't' and we get 'ay' child 'y'. So node 'y' will return the array of those strings. 


[Slide 19]

Now we are back to node 'd'. Since we are only looking for the strings that start with 'd''a', we do not traverse child 'o'. At this point, we return to the root with our completed words: data, date, dates, and day.


[Slide 20]

As I mentioned before, the completions function is a more complex trie function. I have included the pseudocode here and we will work through it piece by piece as we did with other functions. 


[Slide 21]

Recall that in our example, we first traversed the tree while working through the input string. This if block of our completions function corresponds to that. 


[Slide 22]

Here, we build in an extra if statement which allows for us to handle the case where the input string isn't captured within our trie. The else proceeds to work through the input string as we did initially in our example. 


[Slide 23]

The else block of our function is built for when we have traversed the entirety of our input string. 


[Slide 24]

The last key part that I want to draw attention to, is when we are building the words. Recall that in our example, we took the item of the node we were at and inserted it at the beginning of each of the completions returned by the nodes children. In these two places in the pseudocode, we are applying that principle. 


[Slide 25]

Let's go back to our example of 'c''a'. We would call completions from the root on 'c''a'.


[Slide 26]

Now from 'c' we call completions on 'a'.


[Slide 27]

Next from 'a', we run the completions function on the empty string. 


[Slide 28-29]

This would put us in the else block, so we run the completions on each child. 


[Slide 30]

From node 'a' would get 't' from node `t` and 'n' from node `n` and we start building our words by appending 'a' to the words from 'a's children. 


[Slide 31]

Then node 'a' returns 'a''t' and 'a''n' to node `c` and we insert the letter 'c' in the beginning of each of those words. 


[Slide 32]

Finally, node `c` will return 'cat' and 'can' to the root and we are finished! That completes the overview for the completions function for our tries implementation.