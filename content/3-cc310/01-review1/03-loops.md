---
title: "Loops"
pre: "3. "
weight: 30
date: 2020-01-13T00:00:26-05:00
---

{{< youtube >}}

#### Resources

* [Slides](/3-cc310/01-review1/03-loops-slides.pptx)

#### Video Script

[Slide 1]

[Slide 2]

Loop are powerful programming constructs that allow your programs to perform functions multiple times over large sets of data.

There are basic types of loops that we are interested in. First there are loops that repeat while or until a specific condition is true. Then there are loops that repeat a specific number of times. We will look at both types.

[Slide 3]

A While loop is one of the types of loops that repeats while a specific condition is true. _**[advance]**_ In our example, that condition is `a < 5`. If `a < 5` is true, _**[advance]**_ then we enter the loop and execute the `a = a + 1` statement. _**[advance]**_ After execution, _**[advance]**_ the program loops back to the condition check. _**[advance]**_ At this point, if `a< 5` becomes false due to the `a = a + 1`, _**[advance]**_ then we will exit the loop.

Now there are a couple things to keep in mind when using While loops.  First, it is possible that the condition will not be true at the beginning of the loop. For example, if the value of variable `a` was 6 when we tried to execute the loop, the condition `a < 5` would be false and we would immediately exit.

Second, you need to make sure that the condition will eventually evaluate to false in order to exist the loop. For instance, if we accidentally typed our condition as `a > 5` instead of `a < 5` _**[advance]**_, once we entered the loop, we would never exit. This is because the variable `a` would have to have a value greater than 5 to enter the loop and since we add 1 to the value of variable `a` each time through the loop, the condition would always be true. This is what we call an infinite loop.

[Slide 4]

A For loop is a loop that allows you to go through the loop a specific number of times. For loops are useful for iterating through data structures such as arrays where you have a specific number of items.

_**[advance]**_ In our example, execution begins at the top of the loop where an counter variable - in this case `i` - is used to count and control the number of times through a loop. In our example, we initialize `i` to 1 and then start the loop. _**[advance]**_ Each time through the loop the program will execute the `a = a + i` instruction _**[advance]**_ and then loop back to the top of the loop.

_**[advance]**_ Each time through the loop the program will increment the counter variable `i`. _**[advance]**_ As long as the `i` is in the range of 1 to 10, the program will stay in the loop and execute the `a = a + i` instruction, once For-Each time through the loop. When the counter variable `i` gets incremented from 10 to 11, the condition that `i` is in the range of 1 to 10 becomes false and the Done branch out of the loop is taken. _**[advance]**_

Like the While loop, you need to take care when using For loops. Specifically, it is very important *not* to modify the loop counter variable within the loop. It is easy to "accidentally" modify the counter in such a way so that our program gets stuck in an infinite loop.

[Slide 5]

In the previous version of the For loop, the counter was incremented by one each time through the loop. While this is the most common situation, there are times when you would like to increment the counter by more than one, say for instance when you are only interested in using odd numbers. _**[advance]**_ In this example, we have modified our loop counter by adding a "step 2" qualifier. In a for loop, the step is the amount we want to increment the counter variable by each time through the loop. So for this example, the counter variable `i` will be equal to 1 the first time through the loop, 3 the second time, 5 the third time, and so on. The last time through the loop, `i` will be equal to 9. When program execution returns to the top of the loop, `i` will be incremented by 2 and so its value will become 11 and the loop will exit.

[Slide 6]

The For-Each loop is specifically designed to iterate over a list or set of items. It is similar to a for loop except that the program does not need to know that actual number of items in the list. For example, if we had a list of 10 number from 1 to 10 _**[advance]**_ this For-Each loop would produce the same output as the For loop without the step qualifier. However, one difference would be that the list is not necessarily guaranteed to be performed in order in a For-Each loop.

The fact that there is no guaranteed order is actually very useful. _**[advance]**_ Consider this list, which contains a somewhat random set of numbers. These numbers might represent anything from the distance between two points to a set of sales receipts.

[Slide 7]

Actually, the items in the list do not need to be numbers at all. As shown in this example, list contains a number of objects that represent animals. Our For-Each loop goes through each animal in the list and prints out the type of the animal, such as "dog" or "cat". The For-Each loop is very powerful in that it can loop through a set of any type of objects and allow the program to perform a set of functions on those objects.

Loops are powerful mechanisms that allow programs to perform repetitive actions on all sorts of data. When coupled with sequential operations and If-Then statements, these three types of statements provide everything you need to code very complex algorithms.
