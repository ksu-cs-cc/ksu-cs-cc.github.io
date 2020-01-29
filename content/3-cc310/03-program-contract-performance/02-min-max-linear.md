---
title: "Max & Min Linear"
pre: "2. "
weight: 20
date: 2020-01-28T00:00:26-05:00
---

{{< youtube >}}

#### Resources

* [Slides](/3-cc310/03-program-contract-performance/02-min-max-linear-slides.pptx)

#### Video Script

Slide 2

Throughout this section, we will develop two different algorithms for finding the maximum and minimum numbers from a list of numbers. First, we will look at an algorithm that looks at each number individually and keeps track of the minimum and maximum found so far in the list.

To perform this algorithm, we will need to have our list as shown on the left. In this example, our list has 6 numbers in it. We also need a counter to keep track of where we are in the list, and the Min and Max variables which will keep track of the minimum and maximum values we have found so far in the list.

Slide 3

We initialize our algorithm by setting counter to 1. Effectively, this points at the first item in our list.

Slide 4

The first step of the algorithm is to look at the value of item 1 in the List and store it in both the Min and Max variables.

Slide 5

Next, we increment our Counter variable to 2. We then compare the value of item 2 in the List to Min and Max.

If that value is less than Min, we replace the current value of Min with the value of item 2 in the List.

If the value of item 2 in the list is greater than Max, we replace the value of Max with the value in item 2 of List.

Slide 6

In this case, 2 is less than 3, so we store the value of item 2 in the list – which in this case is the value 2 – into Min.

Slide 7

Once that step is completed, we increment our Counter value again. Now Counter is 3 and we compare the value in item 3 of the List against both Min and Max.

Slide 8

In this case, the value of item 3 in List, 6, is greater than the value of Max, which is 3. We store the value 6 into Max and continue to the next item in the list.

Slide 9

Now, since item 4 in List has the value of 1, we can see that it will be less than the current value of Min.

Slide 10

So we replace Min with the value 1.

Slide 11

Next, we increment Counter to 5 and compare item 5 in the List against Min and Max.

Slide 12

In this case, the value in item 5 of the List is 9, which is greater than the old value of Max, which was only 6. We store the value 9 in Max and move on.

Slide 13

We increment Counter to 6, which is our last item in List.

Slide 14

Since the value of item 6 is 0, we replace Min with 0.

Slide 15

Thus, we have effectively stepped through each item in the list and saved the minimum and maximum values from the list.

Slide 16

Here we have a flowchart depicting the algorithm we just used to find the min and max values.

Slide 17

We assume we start with N numbers in a list. We use a for loop to loop through each item in the list and use a temporary variable called Value to hold the current value we are examining in the list.

If this is the first item in the list, then we know we haven't been through the list yet, so we need to initialize the values of Max and Min.

Slide 18

We set both Min and Max to the value from the list and then loop back to the top of the loop and increment counter.

Slide 19

If Counter is not equal to 1, then we know we have already initialized Min and Max.

Thus, now we compare the value to Max. If it is greater to Max, then we store the value in Max.

Slide 20

Next we check whether the value is less than Min. If it is, we store the value in Min.

Slide 21

Then we loop back to the top of the for loop and increment Counter.

Slide 22

After we have looped through each item in the List – setting Min and Max as appropriate – we are done, and our algorithm exits.

[pause]

In this video, we have seen how we can step through items in a list in a linear fashion to find the minimum and maximum values in the list. We also converted that process to an algorithm we can use to create a program to do that automatically for us.
