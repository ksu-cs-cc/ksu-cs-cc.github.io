---
title: "Max & Min Pairs"
pre: "5. "
weight: 50
date: 2020-01-31T00:00:26-05:00
---

{{< youtube >}}

#### Resources

* [Slides](/3-cc310/03-program-contract-performance/05-min-max-pairs-slides.pptx)

#### Video Script

[Slide 2]

Now we are going to look at the problem of finding the minimum and maximum
values in a list using a different algorithm. Instead of looking at each number
in the list separately, we will look at them in pairs. We will use this
algorithm and the linear version covered earlier to investigate how the
differences lead to differences in performance.

Like the linear algorithm, we will have an index 'i' that keeps track of where
we are in the list. Except in this algorithm, we will increment it by 2 instead
of 1 each time through the list.

We will also keep track of the 'min' and 'max' values that we have seen, like we
did in the linear algorithm.

Finally, we will add two new variables to track the minimum and maximum for our
current pair of numbers. These variables are called 'lastmin' and 'lastmax'.

The flow of our process is pretty straightforward. We will look at two numbers
at a time from the list. We will put the smallest of those two numbers in the
'lastmin' variable, and the largest of those numbers in the 'lastmax' variable.

Next, we will compare 'lastmin' with the 'min' and the 'lastmax' with the 'max'
. If either of the last 2 numbers are larger or smaller than the 'min' or larger
than the 'max' , we will update the values of 'min' and 'max' .

[Slide 3]

The first step is initiated by setting our index 'i' to 1. This will allow us to
look at the first two numbers in the list.

[Slide 4]

Since these are the first two numbers, we automatically store the smaller of the
two, 2, in 'lastmin' and store the larger, 3, in 'lastmax'.

[Slide 5]

Likewise, we store 'lastmin' in 'min' and 'lastmax' in 'max' .

[Slide 6]

Next, we increment our index by 2 and thus skip down in the list to the third
entry.

[Slide 7]

Again, we compare the numbers in the third and fourth places in our list and
store the smaller in 'lastmin' and the larger in 'lastmax'.

In this case, we store 5 in 'lastmin' and 6 in 'lastmax'.

[Slide 8]

Finally, we compare 'lastmin' against 'min'. Since 5 is not smaller than the
'min', which is 2, we do not change 'min'.

However, when we compare 'lastmax' against 'max' , we find that 6 is greater
than the current 'max' , which is 3, so we update 'max' with the content of
'lastmax'.

[Slide 9]

We increment our index 'i' by 2 again and look at entries 5 and 6 in the list.

[Slide 10]

After comparing the entry values, we store 0 in 'lastmin' and 4 in 'lastmax'.

[Slide 11]

We again compare the 'lastmin' and the 'lastmax' against 'min' and 'max' . In
this case 'lastmin' is smaller than 'min', so we update 'min' with the value 0.
But, we have no changes to 'max'.

As we can see from a quick inspection, we have found both the minimum and
maximum numbers from our list.

[Slide 12]

Next, we put our algorithm into a flowchart, which is identical to the one in
your textbook. The only difference between the process we just walked through
and this algorithm is that instead of having a pre-defined list to work with, we
will prompt the user to input the number of the list when they are needed.

[Slide 13]

We'll break the algorithm into two parts. The first, which we see here, is the
initialization part of the algorithm that comes before the loop.

Here, we prompt the user for a number, which represents the first number in our
list.

After reading the input and storing it in variable 'x', we set 'min' and 'max'
to be equal to the value in 'x'.

[Slide 14]

Now we enter the loop. For this example, we have 10 items to look at, so we use
a 'for' loop from 1 to 10. However, since we will be comparing pairs, we will
include a 'step 2' to our loop.

[Slide 15]

Each time through the loop, we will prompt the user for two number, which we
store in 'x' and 'y'.

We then compare whether 'x' is greater than 'y'.

[Slide 16]

If 'x' is greater, then we follow the true branch and set 'lastmin' to 'y' and
'lastmax' to 'x'.

[Slide 17]

However, if 'y' is greater, we follow the false branch and set 'lastmin' to 'x'
and 'lastmax' to 'y'.

[Slide 18]

Once we have determined the minimum and maximum of 'x' and 'y', we check to see
if 'lastmax' is greater than the global maximum stored in 'max'.

If it is, we update the value of 'max' . If not, we do nothing.

[Slide 19]

Next, we check if the value of 'lastmin' is less than the global minimum stored
in 'min'.

If it is, then we update the value of 'min'. If not, we again do nothing.

[Slide 20]

Finally, we follow our loop back up to the top of our for loop and increment
index 'i'. If the updated value of 'i' is less than or equal to 10, we go
through the loop again.

Notice that with the 'step 2', we will go through the loop exactly 5 times.

[Slide 21]

Once our index 'i' gets incremented past 10, we exit the loop and we are done.
We have our minimum and maximum values from the list.

[pause]

In this video, we looked at how we can loop through our list two at a time, with
the goal of increasing the efficiency of our algorithm. We also converted our
process to an algorithm we can use to create a real program.

In the next section, we will compare the linear and pairwise algorithms to see
which is actually better in terms of performance.

.
