---
title: "Basic Stack Operations"
pre: "3. "
weight: 30
date: 2020-02-11T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/05-stacks/03-basic-operations-slides.pptx)

#### Video Script

Slide 2

Now that you have a conceptual notion of how stacks work, we need to look into
the internals of a stack class. Specifically, we will take a look at the main
operations for a stack. In this video, we will look at each operation
individually by walking through the code.

Slide 3

The first operation we need to discuss is the class constructor. For a stack,
there are two main attributes that the class is responsible for. The *stack*,
which we will implement using an array, and the *top* attribute, which keeps
track of the array index at the top of the stack.

Since our stack is empty when it is created, the stack constructor should
allocate the array in memory and then initialize the *top* attribute to -1,
which indicates that the stack is empty.

Slide 4

The pseudocode for the stack constructor is shown here. Notice that we require
the calling method to explicitly provide a *capacity* value, which will be the
initial length of the array.

Slide 5

The first thing we need to do in these operations is to check our preconditions.
In this case, *capacity* must be an integer that is greater than 0. As you see
in our code, we explicitly check to see if the value is an integer value. While
this may be necessary in dynamically typed languages such as Python, in typed
languages such as Java, C, or C\#, we can explicitly define *capacity* to be an
integer type. This effectively ensures that the value passed in will be an
integer.

In either case, we must check to ensure that the capacity value is greater than
0. If either one of the precondition checks fail, we will raise an exception and
let the calling method handle it.

Slide 6

If we pass the precondition checks, we then move to the heart of the method.
There are basically two lines. One creates the *myStack* array of the
appropriate capacity while the second initializes the class *top* attribute to
-1.

Slide 7

As I mentioned in a previous slide, both the *myStack* array and the *top*
attribute are defined at the class level.

Slide 8

Next, we will look at the *push* operation, which allows us to put new items on
the stack. In our example here, we have an empty stack, presumably just created
by our constructor method.

Slide 9

When a method calls the *push* operation, we increment the *top* variable.

Slide 10

And then we store the data into the array at the index contained in *top*.

Slide 11

When we look at the code, the first thing we notice is that the code initially
checks its preconditions. In this case, the *pop* operation must ensure there is
space in the array to store the item. If *top* is already pointing to the end of
the array, then we again throw an exception.

If we pass the precondition check, the rest of the operation is simple. We
increment *top* and store the item into the array at *top*.

Slide 12

The *pop* operation allows us to remove items from the top of the stack. Again,
there are two basic steps.

Slide 13

First, we decrement the value of *top* to point to the new top of the stack.

Slide 14

Then, we return the item from the old top of the stack.

You might ask why we decrement *top* before returning the item. I think looking
at the code will clarify this question. Basically, when we use the *return*
statement, we exit the current operation, which would leave us with *top*
pointing at the old top of the stack, which is certainly not what we want.

Slide 15

The *pop* method is straightforward and structured very similarly to the *push*
operation.

We first check the preconditions, which in the case of *pop* is that the stack
is not empty. If it is we again throw an exception. You might be beginning to
notice a pattern here. The first thing we do in these operations is to check our
preconditions. This is a great programming habit to get into and is definitely
considered a "best practice".

Finally, if the stack is not empty, we perform the two actions I just described.
We decrement *top* and then return the item at *top+1* in the myStack array.

Slide 16

Next we will look at the *isFull* operation, which is a really simple method.
Basically it just returns the Boolean value of whether *top + 1* is equal to the
length of the stack. If it is, then *isFull* returns true, otherwise, it returns
false.

You might notice that there are no preconditions to check. It doesn't matter
what state the stack is in, we can always return whether or not the stack is
full.

Slide 17

The *isEmpty* operation is structured exactly like the *isFull* operation. The
only difference is that we return the value of whether *top* is equal to -1. If
it is, then the stack is empty.

Slide 18

The *peek* operation is also almost identical to another operation we have
already looked at, in this case the *pop* operation. The only difference here is
that we do not decrement the *top* attribute. Thus, we return the item at the
top of the stack without altering the stack at all.

Notice here, that we have used the *isEmpty* operation to check to see if *top*
is equal to -1, which we did explicitly in the *pop* operation. Actually, we
should always use the *isEmpty* operation instead of checking if *top* is equal
to -1. The reason for this is due to the maintainability of the code. While we
are currently using -1 to represent an empty array, it is possible that we might
someday change the way we represent the stack in our code - which is more common
than you might think. By calling the *isEmpty* operation, if a change does
occur, we only have to make a change to the *isEmpty* operation and all the
other methods that call it can stay the same.

I should also point out that how we use the item passed back from the *peek*
function depends on the type of data stored in the stack. If the data is a base
type, the values are usually passed directly, while more complex data such as
arrays or objects are passed by reference. If the data returned by the *peek*
method is a reference, then you can actually manipulate the data on the top of
the stack directly. However, if the data is passed by value, changing the value
of the returned item will not affect the value on the top of the stack.

Slide 19

In many languages, such as Python, you can add space directly to an array or
list. In these languages, the *doubleCapacity* operation is very simple and we
won't cover it here.

In most traditional languages such as Java or C\# you cannot simply add space to
an array. Therefore, we have to follow a three step process.

First, we must create a new array with double the capacity of our current array.
Next, we will need to copy the contents from the current array into the new
array. And then, finally, we can point our *myStack* attribute to point at the
new array.

Notice that we do not need to change the value of *top* since the top of the
array in the new array will be in the same place as it was in the old array.

Slide 20

For the *doubleCapacity* operation, we have no preconditions since it doesn't
really matter if the array is empty or full. We are just changing the amount of
storage available in the array.

Slide 21

Therefore, the first step will be to actually create the new array with a
capacity twice the size of our original array.

Slide 22

Next, we use a for loop to loop through each item in the current array, copying
it to the new array.

Slide 23

Finally, we point *myStack* at our new array and we have effectively doubled the
size of our array and thus the allowable size of the stack.

When we exit the *doubleCapacity* function, *myStack* will be pointing at our
new array, so no external methods will even know that anything changed.

Also, the memory locations taken up by the old array will effectively be
orphaned – meaning there are no attributes or variables pointing at them – so
eventually the memory will be reclaimed and reused.

Up to this point, all the operations we've looked at are constant time
operations. However, the *doubleCapacity* operation – and the *halveCapacity*
and *toString* operations that follow – have a loop, which will introduce a
greater time complexity. In this case, it is directly related to the size of the
stack. Thus its time complexity would be on the order of N.

Slide 24

The *halveCapacity* operation is actually the exact same as the *doubleCapacity*
operation, with two changes. First, we now have a precondition. Since we don't
want to lose any items off the stack, we need to make sure that all the items
can actually fit into the new, smaller stack. And second, the new array is
created with only one half of the capacity of the old array.

Slide 25

As always, the first step is to check our precondition. In this case, if *top* +
1 is greater than one half the capacity of the current array, then we throw an
exception since the items on the stack will not fit into the new array.

Slide 26

However, if we pass our preconditions, we create a new array, half the size of
the old array.

Slide 27

Next, we copy the items from the old array into the new array.

Slide 28

And finally, we point *myStack* at the new array.

Slide 29

All objects are generally required to implement a *toString* method to override
the default *toString* function provided by the base *Object* class. This is
especially important if you want your output formatted in a specific manner.

In our case, we want ours to list the items in the stack from top to bottom. The
overall process is straightforward.

First, we create an empty output string. Next, we loop through the stack from
top to bottom appending the string version of each item onto the output string.
And finally, we return the output string.

Slide 30

Here again we do not have a precondition. If there is nothing in the stack we
will simply return an empty string, which represents the stack perfectly.

Slide 31

Finally, once we loop through the stack from top to bottom, we get the output
string "dcba", which is returned to the calling method.

Slide 32

In this video, we have looked at several basic stack operations and the
pseudocode required to implement them. Almost all the operations are
straightforward. However, there were several cases where we were required to
carefully check the preconditions so the operations worked as advertised.
Finally, we saw that many of the operations run in constant time, while more
complex operations such as *doubleCapacity*, *halveCapacity* and *toString* run
in N time.
