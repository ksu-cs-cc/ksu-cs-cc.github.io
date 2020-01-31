---
title: "Correctness"
pre: "3. "
weight: 30
date: 2020-01-31T00:00:26-05:00
---

{{< youtube >}}

#### Resources

* [Slides](/3-cc310/03-program-contract-performance/03-correctness-slides.pptx)

#### Video Script

[Slide 2]

How do know your method is correct? We could run an exhaustive set of tests.
However, unless you really test every possible combination of inputs to your
method, you cannot prove your method works in all cases.

The other possibility is "proving" your method runs correctly. This is related
to proving certain theorems are true in math. In our case, the theorem is a
method.

[Slide 3]

Conceptually, proving that a method runs correctly is straightforward. You
simply assume the method's preconditions are true and then, using the code
within the method, show that the method's postconditions must be true.

Usually, that's easier said than done.

The hard part is using the code to show the method's postconditions are true.
Obviously, you need to know what method you are trying to prove to build your
strategy on how to do this.

[Slide 4]

In this video, we will use the 'maximum' method found in the textbook.

They key part of our proof will be showing that the loop in the method is
correct. This will involve knowing the loop precondition, its loop invariant,
and the loop postcondition.

[Slide 5]

So we use a straightforward strategy.

First, we assume the preconditions are true. These are the baseline facts we can
use to establish other facts based on the code.

Second, we use the method preconditions and code before the loop to establish
the loops preconditions.

Third, we demonstrate through the code that the loop invariant is true at the
end of the loop each and every time the loop is executed.

Fourth, we show that the loop postcondition is true. Usually, this is based on
the loop invariant being true.

Finally, we show that the method postcondition is true based on the loop
postcondition and any code after the loop.

Next, we'll walk through our strategy.

[Slide 6]

Here are all the preconditions, postconditions, and invariants for the program
as shown in your textbook.

We will prove these are true and then use them to ultimately prove the method
postcondition.

[Slide 7]

First, we assume the method precondition is true. In this case that 'numbers' is
an array that has at least one number in it.

[Slide 8]

Next, we use the fact that 'numbers' has at least one number in it and the
statement 'max = numbers[0]' to try to prove loop precondition.

Since 'numbers' has at least one number in it, the statement 'max = numbers[0]'
will store the first value in 'numbers' into the variable 'max'.

This effectively establishes the loop precondition, which states that 'max'
contains the value stored in 'number[0]'.

[Slide 9]

Now for the hard part: showing that the loop invariant is true at the end of the
loop for each time through the loop. So, given the loop postcondition, we must
establish that 'max' contains the maximum value stored in 'numbers' up to and
including the current loop index i.

Each time through the loop, it is easy to see that if the value in 'numbers[i]'
is larger than 'max', then we update 'max' so that it is always the largest
value stored in 'numbers' up to and including the index 'i'.

Thus, we can conclude that the loop invariant is true each and every time
through the loop.

[Slide 10]

Given the fact that the loop invariant is true, we now need to show that the
loop postcondition is true.

Notice that the loop postcondition is almost the same statement as the loop
invariant except for the words "up to and included index i".

However, given the loop range of 1 to the length of the 'numbers' array, we can
be sure that we have looked at every number in the 'numbers' array.

Thus, given that our loop invariant is true, and we have looked at every number
in the array, we can be sure that the loop postcondition is true.

[Slide 11]

Finally, we need to show that the method's postconditions are true.

Given that one of the postconditions is almost identical to the loop
postcondition and 'max' cannot be modified after the loop, showing that this
postcondition is true is trivial.

[Slide 12]

However, the second postcondition – that 'numbers' is not modified by the method
– takes a little more effort.

If we look back through each statement in the method, we see that there are no
statements that assign any new values to elements of the 'numbers' array, thus
the postcondition must hold.

[Slide 13]

In this video, we have shown how we can prove the correctness of a method by
showing that the method's postconditions are true, given that the method's
preconditions are also true.

We looked at an example method where we also had to prove that a loop was
correct by using the loop's precondition, invariant, and postcondition.

While we did not perform a formal proof, hopefully this example will give you a
basic understanding of the concept of proving correctness of a program.
