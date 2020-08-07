---
title: "Recursion"
pre: "2. "
weight: 32
date: 2019-02-04T10:53:26-05:00
---

{{< youtube En7FDq5XrsA >}}

#### Resources
* [Slides]({{< relref "/4-CC315/03-treetraversal/02-treetraversal-recursion-slides.md" >}})

#### Video Script

[Slide 1]

In CC310, we discussed recursion. Do not worry if this is not something you understood then. Recursion is a topic in computer science that virtually no one understands the first few times they see it, myself included. 

[Slide 2]

When talking about recursion, we define two cases: the base case and the recursive case. 

The base case captures what we should do once we get to the bottom of our problem. The base case is something we can solve directly. The recursive case breaks the problem into smaller pieces and works towards the base case. The recursive portion will include calling the method we are in currently. Recursive solutions can look very different for various problems. 

[Slide 3]

Let's work through an example to refresh. Suppose that we want to multiply any two whole numbers without using multiplication symbol or for loops. For example, we can do multiplication iteratively using addition. If we wanted to evaluate five times four, we would sum five four times via a loop.

[Slide 4]

Now using recursion, we have the same premise just implemented differently. We want to sum five four times via recursion. Our base case is when we take any number times zero, we get zero. The recursive case works to get to the point where we will have a number times zero. In the recursive case, we will add the number `m` plus the result of `MULTIPLY` `m` and `n-1`, a smaller version of the problem. 

Let's work through five times four. 

[Slide 5]

We start with `m` equal to five and `n` equal to four. So `n` is not 0 and thus we are in the else block and we call `MULTIPLY` on five and four minus one which is three. 

[Slide 6]

We can think of 'pausing' our first call of the function while we call `MULTIPLY` on `m` equal five and `n` equal to three. Variable `n` is not equal to zero so we call the multiply function on five and two.

[Slide 7]

We have two calls of `MULTIPLY` on 'pause' and start a third call on five and two. Variable `n` is not zero, so we make another recursive call of `MULTIPLY` on five and one. 

[Slide 8]

Now we have three calls on 'pause' with a fourth call on five and one. We then make another recursive call of `MULTIPLY` on five and zero. 

[Slide 9]

We have now made it to the base case! Variable `n` is equal to zero. There are four calls of `MULTIPLY` on the stack. Now we start the process of slowly 'undoing' the recursion that we have done. 

[Slide 10]

Since `n` equals zero, we return zero. This returns zero to the `MULTIPLY` call prior to it. 

[Slide 11]

Then we can return the sum of five plus zero since we completed `MULTIPLY(5,0)` which returned zero. Now we return five from our fourth call of `MULTIPLY`.

[Slide 12]

Now that we have completed `MULTIPLY(5,1)`, we can return the sum of five and five. Now we return ten from our third call of `MULTIPLY`.

[Slide 13]

Now that we have completed `MULTIPLY(5,2)`, we can return the sum of five and ten. Now we return fifteen from our second call of `MULTIPLY`.

[Slide 14]

Now that we have completed `MULTIPLY(5,3)`, we can return the sum of five and fifteen. Now we return twenty from our first call of `MULTIPLY` and we are done! 

We started by wanting to evaluate five times four. Now we can confirm that it is 20 by using recursion. 

[Slide 15]

Again, recursion is not something anyone understands the first time that they see it. Please feel free to refer back to this video as you need! 

[Slide 16]

The takeaway for this video is that recursion has two key components: the base case and the recursive case. The base case is a problem that we can 'easily' solve. The recursive case breaks our problem into smaller problems with the intent of getting to the base case eventually. 