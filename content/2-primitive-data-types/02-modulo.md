---
title: "Modulo"
pre: "2. "
weight: 20
date: 2019-02-05T10:53:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides]({{< relref "/2-primitive-data-types/02-modulo-slides.md" >}})

#### Video Script

One new mathematical operation that is very important to programming is the modulo operation. In code, we typically use the percent sign for this operation, as in this example.

The modulo operation produces the remainder of a division. Remember long division? That's where this comes from.

So, in this example, `9 % 5` returns 4, which is the is the same as saying `9 / 5`, which is 1 with a remainder of 4.

In fact, many times, the modulo operation is referred to as "clock arithmetic" because of the similarities. Consider this example from Wikipedia. If the time is 9:00, and we want it to be 4 hours later, we know that it will be 1:00. That is because `(9 + 4) % 12 = 1`. On the clock, we see the hour hand cycle around the top, starting back over at 1.

Another way to visualize the modulo operation is by looking at a number line. In this example, we have a number line on the first line, followed by a line showing just the multiples of 4. Then, the bottom line shows the result of any value mod 4. So, if we want to find `6 % 4`, we can just look for 6 in the top line, then find the result in the bottom.

Finally, we can use the modulo operation to calculate some handy facts. First off, if we take any number and perform the modulo operation with 2, we can find out if that number is even or odd. Specifically, if the result is 0, we know that it must be even since it is divisible by 0. If not, it is an odd number.

In fact, we can perform that operation to find out if a number is evenly divisible by any other number, as long as the result of the modulo operation is 0. For example, we can do `15 % 5` and find that the result is 0, so we know that 15 is evenly divisible by 5. Pretty cool, right?

We can also use that fact to determine how many extras would be in a group. So, we could do `19 % 8` to find out how many extras would be left over after dividing 19 people into groups of 8. Since the result is 3, we'd know that there are 3 people left over. If we did groups of 9, we'd do `19 % 9` and find the result is 1, so maybe that is a bit better.

Finally, as we learned previously, we can use the modulo operation to convert from 24-hour time to 12-hour time. So, we know that 1500 hours in 24-hour time is 3:00 PM in 12-hour time, since `15 % 12 = 3`.

Hopefully these examples help you understand the modulo operation a bit more.
