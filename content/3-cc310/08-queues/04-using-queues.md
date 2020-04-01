---
title: "Using Queues"
pre: "4. "
weight: 40
date: 2020-03-27T00:00:26-05:00
---

{{< youtube 05zPOJ8B5cA >}}

#### Resources

* [Slides](/3-cc310/08-queues/04-using-queues-slides.pptx)

#### Video Script

[slide 2]

Now we want to take a look at how we might use queues in a real world
application. One area where queues are used is to control the order in which
certain tasks are performed. These tasks can be computational or, as in our
application, be real world tasks in places like factories.

[slide 3]

The application we will look at today involves the assembly of automobiles in a
factory. Specifically we want to organize and control which cars go first when
putting on their windshields. We assume we have a single station where we put on
the windshield. However, cars can come from several locations to get their
windshield installed.

Without any type of mechanism to control which car gets serviced first, mass
chaos could be the result.

[ADVANCE – wait until animation ends]

Clearly this is not a good situation!

[slide 4]

What we need is a way to organize this process. But the question is, how?

Aha!, you say! I've just been studying this great new data structure called a
queue. In a queue, items are placed in the queue one at a time and then taken
out in a first in first out order. It would be perfect for this application.

[slide 5]

And you would be correct. A queue would create order from chaos and would neatly
organize the process of ordering and selecting the next car for service.

Unfortunately, there is one hitch. In all the chaos, we forgot that we wanted to
institute a priority system where higher priority cars got to be served before
all lower priority cars.

Does this mean that a queue will not work after all?

[slide 6]

Fortunately no! While a single queue will not meet our needs exactly, multiple
queues can be used to help us out. If we have 3 priorities - say high, medium,
and low – we will need to use 3 queues, one for each priority.

When a car comes to get their windshield installed, they will be placed in the
appropriate queue based on their priority. Then, when the windshield station is
ready for a new car, we can give them a car from the highest priority queue that
has a car in it.

[slide 7]

This process is actually pretty simple. In our example, we have cars in each of
our three queues waiting to get their windshields installed.

[slide 8]

If the windshield station calls asking for the next car, we go to the high
priority queue and select the next car – the purple car - and send it to the
station.

[slide 9]

When the windshield station finishes working on the purple car, it sends it to
the next station and calls to get the next car.

So, once again, we check the high priority queue first. However, this time, the
queue is empty, so we move to the medium queue.

[slide 10]

We then take the first car – the yellow car – out of the medium queue and send
it to the windshield station for installation.

[slide 11]

The same thing happens when the yellow car is finished. The windshield station
calls for the next car and we first check the high priority queue. However, it
is still empty, so we go to the medium priority queue where we select the gray
car and send it to the windshield station.

[slide 12]

When the gray car is finished, the windshield station calls again for another
car. So, like the last couple of times, we check the high priority queue and
find it empty. So, we check the medium priority queue. However, this time the
medium queue is also empty, so we check the low priority queue. Of course there
are cars waiting there, so we send the red car to the windshield station for its
service.

Now, while the red car is getting its windshield installed, a new purple car
arrives.

[slide 13]

Since all purple cars are high priority, the purple car is placed in the high
priority queue.

[slide 14]

When the red car is finished, we start our process again. We first look at the
high priority queue and, since it is no longer empty, we select the purple car
[ADVANCE] and send it to the windshield station to get its windshield installed
ahead of all the other cars in the low priority queue.

[slide 15]

Now, the software we are interested in creating is the software that controls
the cars coming into and out of our prioritizing system. We will create a class
called Controller, which will contain the three queues and the operations that
allow cars to enter and exit the system.

As shown here, at the class level, we simply declare three queues: high, medium,
and low.

Next, we have our constructor. In the constructor we actually create the new
queues with specific capacities. Since we expect to have more low priority cars
than medium priority cars, and more medium priority cars than high priority
cars, we initialize the queues with different capacities based on our estimate
of the maximum number of cars that might be waiting in any one queue at a given
time.

[slide 16]

The first operation that we will provide to access our controller is the
receiveCar function, which is designed to insert cars into our control system.
When some other station along the assembly line finishes their work on a car,
that station will call the receiveCar operation to send that car to the
windshield station.

The inputs to the operation are the car and its priority. The operation itself
is rather simple. We use a case statement with three cases - high, medium, and
low – obviously corresponding to the high, medium, and low queues. For example,
if the priority of the incoming car is medium, the medium case will be selected,
and the car will be enqueued in the medium queue. Recall, that if there is no
space in the queue, the queue will raise an exception. Instead of trying to
catch that exception in this function, we choose to automatically pass it on to
the calling function where it can be dealt with.

If, for some reason, the priority of the incoming car is not high, medium, or
low, then the receiveCar function will raise its own exception in the else case.

[slide 17]

The other operation we will provide to access our controller is the getCar
function. The getCar is designed for the windshield station to call when it is
ready for another car. In this case, we use a set of nested if – else statement
to check which queues have any cars in them, which is checked in our code as an
"if not isEmpty" condition. Of course, we do this in priority order so we first
check to see if the high priority queue has any cars in it and return the first
car in the high priority queue if it does. If the high priority queue is empty,
we then check the medium priority queue, and then finally the low priority
queue. If all three queues are empty, control will fall through to the else
statement where we raise an exception signifying that there are no cars waiting.
In this case, with any luck, the workers on the windshield station will get to
go home early!

[slide 18]

In this video, we have presented a real world scenario where the use of queues
can help create order out of chaos. We actually used three queues to create a
priority system where the highest priority cars will always get serviced before
any lower priority cars, but all cars within a specific priority will be
serviced in a first in first out order. We then showed code to implement such a
system, which relied heavily on the queue operations we have been studying.
