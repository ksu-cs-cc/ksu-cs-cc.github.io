---
title: "Max & Min Linear"
pre: "4. "
weight: 40
date: 2020-01-28T00:00:26-05:00
---

{{< youtube >}}

#### Resources

* [Slides](/3-cc310/03-program-contract-performance/04-min-max-linear-slides.pptx)

#### Video Script

[Slide 2]

Throughout this section, we will develop two different algorithms for finding
the maximum and minimum numbers from a list of numbers. First, we will
investigate an algorithm that looks at each number individually and keeps track
of the minimum and maximum found so far in the list.

To perform this algorithm, we will need to have our list as shown on the left.
In this example, our list has 6 numbers in it. We also need an index variable
'i' to keep track of where we are in the list, and 'min' and 'max' variables to
keep track of the minimum and maximum values we have found so far in the list.

[Slide 3]

We initialize our algorithm by setting our index 'i' to 1. Effectively, this
points at the first item in our list.

[Slide 4]

The first step of the algorithm is to look at the value of item 1 in the 'List'
and store it in both the 'min' and 'max' variables.

[Slide 5]

Next, we increment 'i' to 2 and then compare the value of item 2 in the 'List'
to 'min' and 'max'.

If that value is less than 'min', we replace the current value of 'min' with the
value of item 2 in the 'List'.

If the value of item 2 in the list is greater than 'max', we replace the value
of 'max' with the value in item 2 of 'List'.

[Slide 6]

In this case, 2 is less than 3, so we store the value of item 2 in the list into
'min'.

[Slide 7]

Once that step is completed, we increment 'i' again. Now 'i' is 3 and we compare
the value in item 3 of the List against both 'min' and 'max'.

[Slide 8]

In this case, the value of item 3 in the List - 6 - is greater than the value of
'max', which is 3. Thus, we store the value 6 into 'max' and continue to the
next item in the list.

[Slide 9]

Next, we increment 'i' to 4 and, since item 4 in List has the value of 1, we can
see that it will be less than the current value of 'min'.

[Slide 10]

So we replace 'min' with the value 1.

[Slide 11]

Now, we increment 'i' to 5 and compare item 5 in the List against 'min' and
'max'.

[Slide 12]

In this case, the value in item 5 of the List is 9, which is greater than the
old value of 'max', which was only 6. We store the value 9 in 'max' and move on.

[Slide 13]

Finally, we increment 'i' to 6, which is our last item in the List.

[Slide 14]

Since the value of item 6 is 0, we replace 'min' with 0.

[Slide 15]

Thus, we have effectively stepped through each item in the list and saved the
minimum and maximum values from the list.

[Slide 16]

Now, we will look at a formalized version of our process. Here is a flowchart
depicting the algorithm we just used to find the min and max values.

[Slide 17]

We'll break the algorithm into two parts. The first, which we see here, is the
initialization part of the algorithm that comes before the loop.

Here, we prompt the user for a number, which represents the first number in our
list.

After reading the input and storing it in variable 'x', we set 'min' and 'max'
to be equal to the value in 'x'.

[Slide 18]

Now we enter the loop. For this example, we will go through the loop exactly 10
times, so we use a 'for' loop from 1 to 10.

[Slide 19]

Our first step is to get the next number in our list from the user.

[Slide 20]

Next, we check to see if the value in 'x' is greater than our current 'max'. If
it is, we set 'max' to the value of 'x'. If 'x' is less than or equal to 'max',
we simply do nothing.

[Slide 21]

Now we will check to see if 'x' is less than 'min'. If it is, we set 'min' to
the value of 'x'. If 'x' is greater than or equal to 'min', we again do nothing.

[Slide 22]

Finally, we loop back to the top of our loop and increment 'i'.

[Slide 23]

After we have looped through each item in the List – setting 'min' and 'max' as
appropriate – we are done, and our algorithm exits.

[pause]

In this video, we have seen how we can step through items in a list in a linear
fashion to find the minimum and maximum values in the list. We also converted
that process to an algorithm we can use to create a program to do that
automatically for us.
