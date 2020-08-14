---
title: "Truth Tables"
pre: "3.5 "
weight: 20
date: 2020-05-27T10:53:26-05:00
---

{{< youtube T_olVh6K6IQ >}}


#### Resources

* [Slides](/1-cc110/03-bits-and-boolean-algebra/slides/03-Bits-and-Boolean-Algebra.pdf)

#### Video Script

##### Overview

Let's go through an example of some Boolean logic now that we've covered some of the operators and some of the rules that govern the Boolean algebra behind it. A lot of times what you'll see in computer science, especially when you're dealing with Boolean logic and complex algorithms, our truth tables, truth tables showcase all the different options for each Boolean variable inside of a Boolean logic statement, as well as what output those particular facts for those variables actually produce. So let's take a look at an example that we've already kind of done with end. So we've already explored the statement A and B, and C. You've already seen what the Venn diagram for that looks like, but we can also explore what that looks like again here in just a second, but let's take a look at all possible values that we could actually input for A, B, and C. And if you remember, we're only going to have two values binary values, either one, or zero or true or false. Now, both work synonymously. And you'll find both in truth tables. And in fact, what the examples that you'll be working with, we actually do use ones and zeros for true and false. So if you remember one means true, zero means false. But let's take a look at how we can actually fill out our truth table here with those particular values. Now, I'm going to go ahead and use T for true and false. But as you could imagine, you could substitute one for true and zero for false and everything would be identical. 

So what we would actually start with our truth table here as each of our columns here represent each of our variables or each of our facts as part of our Boolean logic statement though For a, what we're actually going to do here, easy way to fill this out is we're going to want to fill out all the different possibilities. So if we exhaustively go through each of our variables here, you may find that each one has two possible values. And then if we multiply this out, if it's powers of two, we have eight possible outcomes or combinations of these values. You'll notice that I have eight different rows in my truth table. That's going to represent all of the different combinations that I actually have for this Boolean logic statement. Now generally, when we try to figure out how many different combinations we have the number of options we have for our variable to the power of the number of variables that we actually have, so that in this case would be two to the power of three. So two times, two times To write two times two is four times two is eight. This is the total number of possible combinations of truths or our facts that we actually could get out of this Boolean logic statement. 

##### Filling in the Truth Table

So let's elaborate on that and fill out our truth table accordingly. The easiest way to start out for our truth table is go down one column first, because there's kind of a general pattern that you can follow on filling this out. If we just fill half of our rows with false and then half of our rows with true we can work that out. So the column fills out pretty easily. This the pattern that you can kind of follow for the second column works as such, if you just fill in half of the falses, or half of the rows that was false of the first column with true and half of them with false and a similar pattern for the sets of trues down here. So if I make an imaginary line right here in the middle, we can try to fill out all the falses first. So, I want to fill out half of these with false and half of these with true. So let's start with false first. So false, false, and then True, true. Down here, I'm going to do the same exact thing. false, false, true, true. And I'm going to continue the same pattern where I'm going to fill half of what I just filled in and see with falses, and half of what I just filled in with true. So for this set of falses, here, I'm going to have false true. With the set I'm going to have false true. Now, this pattern doesn't exactly always hold, especially as you start adding a fourth column But with three variables, it's pretty easy to fill out using this particular pattern. But if you find yourself filling out a truth table for more than three facts, all we're actually doing is exhaustively writing out all of the different combinations of true and false values or each set of variables. Now, let's go through and try to evaluate the output here, or our truth table. This particular statement is fairly easy with a and b, and c. Because we've already seen that with an and statement, both sides of the operator must be true for the whole statements to evaluate to true. 

So in my output here, I'm going to write out what this set of facts this row of facts evaluates to for our Boolean logic statement up above. So I'm just going to kind of put row numbers here 123. And then let's write our output. Over here, so, false and false and false, is going to evaluate to false because no sides are true and similar ID here, false and false is false. And true. is also False. False and true is False. False and False. False and true. And notice I'm evaluating this from left to right, right, because my statement is a and b, and c, so I'm evaluating the A and B first, and then I'm adding that result with C. So false and true is False. False and true is false. true and false is false, false and false is false. true and false is false, false and true is false. True and true is true. But true and false is false. True and true is true, true and true is true. Now on our truth table, we have a completed evaluation of what our Boolean logic statement A and B and C can actually cover, right, so we have all the different combinations of values, or truth of A, B, and C. And then we've also evaluated those truth values as part of our output. So now we know when this statement is true, and when the statement is false. 

##### Venn Diagram

In lecture in the previous video, we saw what the AND operator looked like for our Venn diagram as well. So let's kind of draw that over here, just so we kind of have what that looks like again, and or the statement just as we kind of had over in our truth table, we're only going to fill in the spot where a true B is true and C is true, where essentially that means the output of our country table is true. So if I just kind of put a, b and c here, and then we also remember, we have a square on the outside that represents everything that is not A, B, or C. I will be giving you some more examples of this or where I'm going to actually give you the truth table, then you're going to try to generate the Boolean logic statement and the Venn diagram and even some logic gates. 

##### Logic Gates

But let's try to draw the logic gates for this as well. And the examples that you'll be doing our logic gates are written like this. So we have our three inputs A, B, and C. Now if you remember the logic gate for and looks like this. Let's draw that. So what we want to do is start out by drawing the logic gate for the first part. Have the logical statement, which is a and b. So to do that, you can kind of imagine electrical wires kind of coming off of the sources of A and B, or your individual variable. So I'm going to draw kind of a little wire out over here into my open space on the right from a and then my second input to that statement is B. So I'm going to draw a wire out from there. And I'm going to draw my gate. So it looks like a D, and my output there. Now I can draw the second part of the statement, which is and C. So I'm going to draw a line from C and draw out here and it's okay if your wires go at a 90 degree angle or a little bit of a curved connect the logic gates together. And now that I have the output from a and b, and the output the input from C, we're going to join those together with another and gate. So the logic gate drawing of a and b and c can be viewed as that. Now everything that I just did apart from generating your truth table are going to be reviewed and practice in a few examples. 
