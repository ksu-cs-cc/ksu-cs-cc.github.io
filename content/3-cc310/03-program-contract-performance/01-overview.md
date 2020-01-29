---
title: "Overview"
pre: "1. "
weight: 10
date: 2020-01-28T00:00:26-05:00
---

{{< youtube >}}

#### Resources

* [Slides](/3-cc310/03-program-contract-performance/01-overview-slides.pptx)

#### Video Script

[Slide 2]

Programming by contract is useful in helping us determine how to create software as well as how to use software. Take for example this bank account class.

It seems obvious. A bank account has an account number and a balance, and you can deposit money or withdraw money, transfer or withdraw money to or from another account, and earn interest on your money.

But if we're really going to use this class, we might want to know a little more detail. For example, what exactly do the methods produce. More importantly, what will this class do with the money that is in the account. Are there fees involved with each transaction? When we perform these transfers, can our account go negative? What interest rates are allowable? Must they be positive, or can they be negative? When we earn interest, does that just compute the amount of interest, or does it actually deposit that amount into our account? These are all questions we need to know in order to use the bank account class safely and effectively.

So how do we do that? As we see in this example, simple descriptions are not going to cut it. We need to have precise details available to us.

In the real world, when two parties need to perform complex transactions, they generally draw up contracts to make sure that each side knows what they're getting into. We will use this as our inspiration for what we call programming by contract.

[Slide 3]

If we think about a simple method like the earn interest method of the bank account, we can gain some insights. First, we need to know what is required in order to use this method effectively. We call these conditions the method's preconditions. And then, we will want to know what will be the result of using the method in the correct way. These are the method's postconditions.

For the earn interest example, we are interested and knowing exactly what is expected of the rate that we pass as an input parameter. From its data type we know that rate is a real number, but that's about it. What is more important is what are the allowable values associated with that real number. Specifically, we need to know what the minimum rate is and what is the maximum rate. And we probably also want to know if there's some relationship between that rate and any of the objects attributes.

[Slide 4]

So, what is the minimum rate? A few years ago, I would have told you the minimum interest rate would have to be greater than 0. However, this is no longer the case, as we've seen negative interest rates in other parts of the world. Therefore, since this is a percentage rate, interest rate should be between negative one and positive one. Thus, the minimum rate must be greater than -1 and the maximum rate must be less than 1.

Then there is the question of a required relationship between the rate and the object's attributes. It could be the case that there are different rates depending on what the balance is. This is often the case in banks. However, to simplify the matter , we will assume that there is no relationship between them. And, it seems clear that the account number is not related to the interest rate either.

So, we will assume the only preconditions to using the earn interest method is that the rate be between -1 and 1.

[Slide 5]

Next, we must determine the method's postconditions, or the results produced by the method. I think it is obvious why this would be important to the class user. We certainly don't want the earned interest method to take all the money out of our account.

We probably have many questions about this method. For instance, how is the dollar amount computed? We probably also want to know if the earn interest method will cause my account to go negative. And finally, we want to know if the method just computes the interest rate, or actually puts money into or withdraws money out of my account. Often, these questions can be answered with a few simple equations.

[Slide 6]

In this case, they can. Here we have two simple equations. The first shows how the dollar amount is computed. Not only does this tell us what the dollar amount is, but it also answers our question about whether our balance can go negative. Since rate is always less than -1, the value of  'balance * rate' can never be more than the original balance. Thus, our account will never go negative.

The second equation, 'balance = balance + dollar amount', answers our questions about whether the interest earned is actually deposited into our account. In this case it is.

Once we know the preconditions and post conditions for the earn interest method, we can write the method to ensure those conditions hold. And, we can also use the method effectively, being certain that we are using it correctly.

[Slide 7]

Programming by contract uses two key concepts. Preconditions and post conditions.

Defining preconditions and post conditions is useful for both the class user and the class programmer.

Knowing the preconditions and postconditions helps a class user by allowing them to make sure they are using the method correctly and are expecting the correct output.

The programmer for a method can use the preconditions and postconditions to help write the method. To ensure that given the correct inputs, it produces the correct outputs. They can also use these conditions to help write unit tests.
