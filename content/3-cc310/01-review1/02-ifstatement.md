---
title: "If Statements"
pre: "2. "
weight: 20
date: 2020-01-13T00:00:26-05:00
---

{{< youtube >}}

#### Resources

* [Slides](/3-cc310/01-review1/02-ifstatement-slides.pptx)

#### Video Script

[slide 1]

[slide 2]

In order for our programs to perform complex behaviors, they need to be able to make decisions based on the conditions of their variables. The most common construct in programming languages for making decisions is the "If-Then" construct.

[slide 3]

A traditional If-Then statement is shown here. Generally, there is a block of code before we get to an If-Then statement, which we refer to here as the "before code block". _**[advance]**_ This code usually is important in setting the values of variables that will be used in Boolean expression that control the actual execution of the If-Then statement.

_**[advance]**_ Next we have the If-Then statement itself. If the Boolean expression part of the statement evaluates to true, then the "then code block" part of the statement is executed. _**[advance]**_  Once the "then code block" completes, _**[advance]**_ the "after code block" is executed. _**[advance]**_

[slide 4]

However, if the Boolean expression evaluates to false, the "then code block" is ignored and the "else code block" is executed. _**[advance]**_ Once the "else code block" completes, the "after code block" is executed. _**[advance]**_

_**[advance]**_ An example of a simple If-Then statement is shown in this flowchart. In this example, the "before code block" corresponds to the "Input: x" block of the flowchart _**[advance]**_, the Boolean expression corresponds to the "x > 0" control block _**[advance]**_, the "then code bloc" corresponds to the "Output: x" block _**[advance]**_, the "else code block" corresponds to the "Output: (-1 * x)" block _**[advance]**_, and finally the "after code block" corresponds to the "Output: "Goodbye" block. _**[advance]**_

[slide 5]

The execution in this example follows the basic flow I just described in using the pseudocode example. _**[advance]**_

The execution begins at the start block and thus the first thing that happens is the "Input: x" block. Let’s assume the user inputs the number "3", which is stored in variable "x". _**[advance]**_

Next, we evaluate whether "x > 0". In this case it evaluates to true, _**[advance]**_ which causes the "Output: x" block to execute. The "Output" block prints out the value of 3 _**[advance]**_ and execution continues on to the "Output: Goodbye" block. The program prints "Goodbye" _**[advance]**_ and then proceeds to the "End" block _**[advance]**_ where execution ceases.

[slide 6]

However, if the user inputs a number less than 0, here we’ll assume "-3", the Boolean expression "x >= 0" will evaluate to false and the "else code block" will be taken as shown.

[slide 7]

A nested If-Then statement is exactly what it sounds like. We simply replace either the "then code block" and/or the "else code block" with another If-Then statement. This allows your program to carry out much more complex decisions, possibly based on the values of multiple variables. In this example, _**[advance]**_ we have replaced the "else code block" with a second If-Then statement.

_**[advance]**_ We will use another flowchart to demonstrate a more concrete example of a nested If-Then construct. In this example, the "before code block" is not shown, but we can assume it sets the value of variable "a", which is used in the Boolean expressions of the example.

_**[advance]**_ Execution begins by evaluating the value of "a". If "a < 0" is true, _**[advance]**_ then the "Output "The value is less than zero"" block is executed and control passes to the "after code block", which is also omitted from this example.

[slide 8]

Now, let’s assume that the variable "a" has a value greater than 0, say 23. Then in this case "a < 0" is false and we follow the false branch. _**[advance]**_ Since "a" is not equal to 0, we also follow the false branch out of the "a = 0" control block, print "The value of a is greater than zero" and continue to the "after code block".

[slide 9]

Finally, let’s assume that the variable "a" has been set to exactly 0. Then in this case "a < 0" is false and we again follow the false branch. _**[advance]**_ However, this time "a" is equal to 0, so we follow the true branch out of the "a = 0" control block, print "The value of a is equal to zero" and continue to the "after code block".

As you can see, a nested If-Then statements allows your program to make complex decisions based on the values stored in the program variables. For even more complex decisions, we can nest multiple If-Then statements, thus providing us almost unlimited capabilities for automated decision making.  
