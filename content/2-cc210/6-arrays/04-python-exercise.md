---
title: "Python Exercise"
pre: "4.P. "
weight: 41
date: 2019-02-21T00:00:26-05:00
---

{{< youtube w8R3G6kE5M8 >}}

#### Resources

* [Slides]({{< relref "/2-cc210/6-arrays/04-python-exercise-slides.md" >}})

#### Video Script

Here's one more example program in this chapter that we can go through. Let's take a look!

As before, we'll start with the same program skeleton we've already seen to handle user input. So, we'll start with this code in our program.

Next, we'll need to handle input. In this case, we need to accept two integers, giving the rows and columns in our list. After that, we'll make sure that both of them are greater than 0. If not, we'll just print an error.

If the inputs are both greater than 0, we'll use them to create a new 2D list. In Python, we'll just create an empty list, and then we'll have to create new lists inside of that list as we read input.

Now that we have our list, we need to fill it with data. So, we could use just a single for loop to do this, repeating `m * n` times. However, it would be very difficult to figure out which row and column we should place each input into. So, instead, we can use two nested for loops to handle the input. The outermost loop will iterate across the rows using `i`, and the innermost loop will handle the columns using `j`. So, when we access `array[i][j]`, we'll be accessing the item in the row with index `i` and the item in that row at column index `j`.

However, before we reach the innermost loop, we'll need to append a new empty list onto the end of our `array` variable. This will create a multidimensional list in Python for us.

Also, since the innermost loop is using `j` to go across the columns, we'll access every column in the first row first, since `i` will always be 0 during that first iteration.

Then, once the innermost loop is done, we'll go back to the outermost loop, increment `i` to 1, and then repeat the inner loop starting at 0 again. So, we'll access all columns in the second row.

This process will continue for each row in the 2D list, making sure that it is all filled with the appropriate input.

As it turns out, when we are working with multidimensional lists, many times we'll end up using a nested loop structure like this one, where we have one loop for each dimension in the list.

Finally, once we've filled in the list, we need to print it out transposed. So, we want to print each row as a column, and each column as a row. It turns out that the easiest way to do this is to simply reverse the order of the for loops. So, if we place the loop for the rows inside the loop with the columns, we'll access each item in the first column, and we can print them out on a single line, making them into a row. Here we are using the `print` method with the `end` of each line set to a blank, so each item will be printed on the same line as the previous one.

Finally, notice that we have an empty `print` method after the innermost for loop. That will end the current line of output so we can start the next row of output on a new line.

That's all there is to it. Make sure you take the time really understand this particular example, because the project for this module will involve working with 2D lists again. Good luck!