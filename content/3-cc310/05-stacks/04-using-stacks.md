---
title: "Using Stacks"
pre: "4. "
weight: 40
date: 2020-02-11T00:00:26-05:00
---

{{< youtube  >}}

#### Resources

* [Slides](/3-cc310/05-stacks/04-using-stacks-slides.pptx)

#### Video Script

[Slide 2]

In this video, we will walk through how we can use stacks in a real-world
example. Our scenario will involve searching a maze to find a path to a specific
location and then returning by a direct path to our starting location.

While it may sound like a "toy" problem, it is not. Just think about a robot
that needs to search an area filled with real world objects, to find a specific
location or object. Once that location or object is found, the robot then needs
to return in a direct path to home base. You might imagine similar applications
in drones and self-driving cars.

[Slide 3]

In our scenario, we have a basic 4 x 5 maze, where some of the cells are blocked
off. We will be given a starting location and a goal location. Our goal is to
find a path to the goal location and then traverse the maze back home as quickly
as possible.

[Slide 4]

To implement this scenario, we are given the maze stored in a 2-dimensional
array along with two values, one for the start cell, and one for the goal cell.

We will use a stack to keep track of the locations that we have traveled through
on our way to the current cell. Each stack location will store the *x* and *y*
coordinates of the cell along with the direction we are headed.

In our implementation, we assume that we always face "up" when we enter a new
cell. If we cannot move in our current direction, we will turn to the next
direction and try there. We will always follow the sequence of directions "up",
"right", "down" and "left". If we try all four directions and do not find a path
to the goal, we will set the direction to "done", which indicates we have tried
all directions without success. When this happens, we will pop the current cell
off of the stack and "backtrack" to the previous cell we had visited. We'll see
how this works later in the video.

[Slide 5]

So, since our starting location is **0,0**, we push that cell onto the stack
with the direction "up". We then try to move in that direction. Since that
direction is blocked, we increment our direction to "right".

[Slide 6]

Notice that the top cell in the stack has changed it's value from **0,0,u** to
**0,0,r**. We can do this without popping the cell of the stack, modifying it,
and pushing it back on to the stack by using the *peek* operation. By using the
*peek* operation, we can get access to the top cell in the stack and modify it
while it remains on the stack.

Our next step is to attempt to move in our current direction, or to the right.

[Slide 7]

In this case, we are successful and so we push our current cell and direction
**0,0,u** onto the stack and try to continue our exploration.

Notice that when we push a new cell onto the top of the stack, we also increment
the direction of the previous top of the stack. This will allow us to know which
direction we should explore if we have to backtrack to this cell during our
search.

[Slide 8]

Since the upwards cell is open, our move is successful and we once again push
our current cell onto the stack and update the direction of the previous top of
the stack.

Here we run into trouble. We try to move upward again, but are stopped by the
blockage in cell **1,1**.

[Slide 9]

Since we can't move upward, we increment the direction to "right", update the
top of the stack, and try again. Unfortunately, we are also blocked going to the
right.

[Slide 10]

Now we increment our direction to "down" and update the top of the stack. While
it looks like we should be able to move to cell **0,1** since it is empty, we
also have another check we need to do.

Since **0,1** is already in the stack at location 1, we do not want to go there
since doing so would cause us to continue exploring other cells from **0,1** and
cause us to skip trying to go to the left from our current cell.

Thus, to keep us from skipping possible paths, we will also need to check the
stack to see if we have been to the cell we are trying to move to. If we have,
we do not move to that cell. We simply increment our direction and try to move
to the left.

[Slide 11]

However, when we try to move left, we run into another block, which is really
bad news since we have now tried to explore all directions out of cell **1,1**.

When we get into this situation, we increment our direction to "done", which
tells us it is time to backtrack and look for another path.

[Slide 12]

We backtrack by popping the stack and moving to the cell at the new top of the
stack, which we have already visited.

Since we already updated its direction to point toward where we should continue
our search, its just a matter of continuing our search from the cell on top of
the stack.

[Slide 13]

Luckily, **0,2** is open, so we move to that cell and push it onto the stack.

[Slide 14]

However, when we try to move upward to cell **1,2** we are blocked. Therefore,
we increment our direction to "right" and try again.

[Slide 15]

This time, cell **0,3** is open, so we move to that cell and push it onto the
stack. We then attempt to move to the next cell, **1,3**.

[Slide 16]

Since **1,3** is unblocked, we move to it and push it onto the stack.

[Slide 17]

At this point, we discover that our current cell **1,3** is our goal cell and
thus we have found our path.

All we have to do to discover our path to our goal is to read that path off the
stack in bottom to top order, much like the *toString* operation.

[Slide 18]

Now we'll take a quick look at a codified version of the algorithm we have been
following.

I don't really want to get into the details of the algorithm here. I will leave
that to you to do a little digging, with the help of the textbook, to make sure
you understand it.

What I want to do here is to highlight how we use the stack in the algorithm.

[Slide 19]

I've highlighted the code to show where all the method calls to the stack class
are. This algorithm actually does a pretty good job of using most of the main
stack operations.

Obviously, we start by pushing the start cell onto the stack using the *push*
method. Later, pushing cells onto the stack will be how we build our path.

Next, we use the *isEmpty* method to see if we have failed in our search. If we
have popped all the cells off the stack, we have returned back to the start cell
without finding our goal.

Then, to be able to access our current location, we use the *peek* method.

To backtrack, we use the *pop* method when we have exhausted all possible paths
of exploration out of the current cell.

Finally, before we use the *push* operation to add to our path, we check the
*isFull* method. If the stack is full, we then call the *doubleCapacity* method
to add space to push our next cell.

All in all, this path finding algorithm demonstrates how to use several stack
methods and is a very good example of the power of using a stack.

[Slide 20]

Of course, we haven't made our way back home yet.

[Slide 21]

Luckily, our path back home is stored succinctly in the stack. All we have to do
is read the locations from top to bottom to find our way home again.

[Slide 22]

The algorithm for returning home is actually very simple. While the stack is not
empty, we just pop the stack and move to the location of the cell we just
popped.

[Slide 23]

For our example, we start by popping the first cell and moving to that location.

[Slide 24]

In this case, we are already in the goal state of **1,3** so we don't actually
move at all.

However, the next cell on the stack does require a move to **0,3**.

[Slide 25]

Once we move to **0,3**, we once again will pop the stack and move to that cell,
which will be **0,2**.

[Slide 26]

Once at **0,2** we simply continue popping and moving. Our next location is
**0,1**.

[Slide 27]

We're almost there, so we pop and move again.

[Slide 28]

Finally, we are home. The algorithm checks to see if the stack *isEmpty*, and
since it is, the algorithm is done.

[Slide 29]

We have looked at a useful application for stacks in this video. Specifically,
we created an algorithm for searching a maze for the location of a goal cell. We
showed how the algorithm uses stacks to backtrack when our search got stuck. We
also saw how to find a direct path to the goal by reading the nodes in the stack
once we arrived at the goal. Finally, we saw how to find our way back home
without searching by simply popping the cell at the top of the stack and then
moving to that location.
