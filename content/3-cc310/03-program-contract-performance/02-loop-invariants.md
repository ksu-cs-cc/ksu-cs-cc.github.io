---
title: "Loop Invariants"
pre: "2. "
weight: 20
date: 2020-01-31T00:00:26-05:00
---

{{< youtube >}}

#### Resources

* [Slides](/3-cc310/03-program-contract-performance/02-loop-invariants-slides.pptx)

#### Video Script

[Slide 2]

When trying to understand what a method does, we can use preconditions and
postconditions to explain exactly how it works.

We can use these same concepts to define exactly what loops are doing. Every
loop has a precondition and a postcondition. However, we also introduce a new
concept called a loop invariant.

[Slide 3]

A loop invariant is a condition that is true after each iteration of the loop.
Of course, the invariant is only required to hold if the loop precondition is
true.

We can use loop invariants to help us in writing loops as well as showing that
our loops will run correctly and produce the required loop postcondition. They
can also be helpful in debugging our code when things go wrong.

[Slide 4]

To demonstrate these concepts, we will use the 'maximum' function, which finds
the maximum number in an array called 'numbers'.

Here we show the precondition for the 'maximum' function. It states that the
variable 'max' must be initialized to the first value in the 'numbers' array.
The precondition is vital to ensuring that the loop will actually produce its
desired result.

Like a method, if the loop precondition is not true, we cannot guarantee what
the output will be.

[Slide 5]

Next, we have the postcondition. The postcondition tells us what will be true
after the loop exits.

Here the postcondition states that the value stored in the variable 'max' will
be the largest number stored in the 'numbers' array.

The postcondition tells us what the overall purpose of the loop is.

[Slide 6]

Finally, we will look at the loop invariant. While the definition of the loop
invariant as "a condition that is true after each iteration of the loop", it is
often hard to define on real examples.

However, if we know the loop postcondition, we can use that to help us define
the invariant since the loop postcondition and the loop invariant are usually
closely related.

In fact, since the loop invariant is true every time through the loop, it will
also hold at the end of the loop.

Here our postcondition states that max contains the maximum value stored in the
'numbers' array.

To convert this to an invariant, you might think about what part of that
postcondition is true each time through the loop. Since we use the index 'i' to
check each value in the array in order, the loop invariant should ensure that
'max' contains the maximum value stored in the 'numbers' array up to where we
have currently checked.

To state that more precisely, we would say that 'max' contains the maximum value
stored in 'numbers' up to and including the index 'i'.

[Slide 7]

The real power of loop invariants come when trying to prove that the method that
contains our loop is correct. In the next section of this module, we will show
how to use preconditions, postconditions, and loop invariants to prove a method
is correct. Or, in other words, that the method will produce what is guaranteed
by its postcondition, assuming its precondition is true.
