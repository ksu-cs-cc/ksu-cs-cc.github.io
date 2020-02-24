---
title: "Recursion Overview"
pre: "1. "
weight: 10
date: 2020-02-18T00:00:26-05:00
---

{{< youtube GALIjmSovzM >}}

#### Resources

* [Slides](/3-cc310/06-recursion/01-overview-slides.pptx)

#### Video Script

[slide 2]

Recursion is a very powerful technique for solving complex problems in a few,
understandable lines of code. In general, recursion is another way to implement
loops.

[slide 3]

So let's look at the definition of recursion. Here is a definition from a
dictionary that is, well, not really all that useful. As you can see, it is a
recursive definition that uses the term recursive definition to define
recursion. Let’s try another one.

[slide 4]

Ah, this is much better and way more useful! It is a “thing that is defined in
terms of itself”. That’s a little better. But what does that mean in
programming?

Basically, recursion occurs when a function calls itself.

The goal of recursion is to break a problem down into a simpler subproblem of
itself until you get to the point where the solution is trivial, or at least
straightforward.

[slide 5]

So here’s an example of a recursive function. The goal of this function is to
read in a sequence of characters and print them out in reverse order until we
read in an asterisk.

You’ll notice that the function REVERSE calls itself in line 6. While this is
where the recursion happens, there are other parts of the function that we need
to understand in order to appreciate what recursion actually does for us.

[slide 6]

The first thing we need to understand is the concept of a “base case”. Remember
I said that the goal of recursion is to decompose a problem into smaller
subproblems of itself until we get to the point where the subproblem is easy to
solve. Well, that occurs in the base case.

In the REVERSE function, the base case occurs when we read in an asterisk
character in line 2. In this case, the asterisk character should cause us to
stop reading in characters and to start printing out the characters we have read
in, in reverse order.

Thus, we don’t really do anything with the asterisk other than to stop reading
in additional characters. So, we simply return from the function call without
doing anything.

[slide 7]

So what happens when we don’t read in an asterisk? In the REVERSE function, we
simply want to read in another character over and over until we do read an
asterisk and execute our base case. We do this by recursively calling the
REVERSE function again in line 6.

When we recursively call REVERSE, you can think of it as creating a completely
new version of the REVERSE function, complete with new parameters and variables.
In this way, a recursive call is really just like a normal function call from
the computer’s perspective.

So, when we call REVERSE again, it simply starts like the previous version of
REVERSE and reads in a new character in line 2. And, while we have a new set of
parameters and variables in the new REVERSE function, the old REVERSE function
will remember its variable values as well.

[slide 8]

Eventually REVERSE will stop calling itself once it reads in an asterisk. This
starts the *return* process. Notice that immediately after the call to REVERSE
returns, the function writes in the character that was read in line 2 of this
instance of the function and then returns itself. In the REVERSE function, this
will continue to occur until every character that was read in is written out in
reverse order.

[slide 9]

This particular type of recursion is called “head recursion” since we call the
recursive function *before* doing computations to solve our problem. Here, line
7 – the write character statement – is considered the computation.

[slide 10]

Now let’s try to look at a little more detail concerning just how recursion
works. In our example, we have called REVERSE for the first time. We assume we
have performed line 2 to read in a character, which was an “n”. Then, since the
character was not an asterisk, the REVERSE function is called in line 6.

[slide 11]

Next, we create a new version, or instance of the REVERSE function and start
execution from the start. In this case, we read in an “o” character, which again
caused us to call REVERSE recursively.

[slide 12]

A new REVERSE call causes us to create a new instance of the function and start
execution at line 2. Here we read in another character, this time “w”, and then
call REVERSE yet again.

[slide 13]

Finally, we create a new instance of REVERSE and this time we actually read in
an asterisk. The asterisk is our base case and will cause the function to return
immediately.

[slide 14]

When instance 4 returns, instance 3 then calls line 7, the write character
statement. The character “w” is printed, which is the character that was read
earlier in this function instance. Once written, the function returns.

[slide 15]

In instance 2, the same thing happens again. This time we write character “o”
and return.

[slide 16]

Finally, we have returned all the way to instance 1 of REVERSE. When execution
returns to instance 1, we pick up in line 7 and print out the character “n” and
return to the original calling program.

Therefore, while we read in the characters “n”, “o”, and “w”, we printed them
out in reverse order as “won”.

Of course, one of the main benefits of writing REVERSE as a recursive function
is that we did not have to know ahead of time how many characters we would be
reading in. The other real option is to use an array, or some other data
structure to save the characters as we read them, and then write them out in
reverse order once we read an asterisk. If we had chosen to use an array, we
would have been out of luck if we had read in more characters than there were
spots to hold them in the array.

[slide 17]

So, what do you think would happen if we swapped the order of lines 6 and 7?

[slide 18]

In this case, instead of implementing “head recursion”, we would be implementing
“tail recursion”, which puts all computation ahead of the recursive function
call.

Tail recursion can be very useful since all we do after executing our base case
it to perform several function returns. The benefit to tail recursion lies in
the fact that it can be optimized by good compilers. If we know we are
performing tail recursion, then there is no additional computation to be
performed once we call the recursive function, so there is really no use in
storing all the variables and parameters from the earlier recursive calls. Once
a tail recursive function calls itself again, we can basically throw away the
current instance and just keep track of the currently executing instance.

[slide 19]

While optimization might be nice, you probably want to know what the effect of
swapping the computation and the recursive call is on the output?

Here is this example, we show the same sequence of three recursive calls to
REVERSE after reading in the same character “n”, “o”, and “w”.

[slide 20]

Since we will write the character before calling REVERSE again, the characters
will print out in the order in which they were input.

Tail recursion basically produces a *first in first out* ordering of the
computation. This makes sense since tail recursion requires all the computation
to take place before the call to the recursive function.

Head recursion, on the other hand, produces a *last in first out* ordering of
the computation. This is evident by the fact that the original REVERSE function
wrote out characters in reverse order.

[slide 21]

We have looked at the concept of recursion and shown one simple example of its
use. We showed how each instance of the function call keeps track of its own
variables so that it can complete its computation once control has been returned
to it.

Finally, we talk about the difference between *head* and *tail recursion* and
how they relate to *first in first out* and *last in first out* ordering.
