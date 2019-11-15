## General

Welcome to the Module 3 review, where you can find all the ideas you should know
from Module 3.

Logic involves reasoning about what is true and false and is an essential part
of programming. Aristotle, an ancient Greek philosopher, contributed to the
development of a system called Aristotelian logic, but the logical operations
involved in modern computer programming are mostly based on Boolean algebra,
a system developed by George Boole in the nineteenth century.

Logical operations can be visualized with truth tables, which enumerate the
value of a Boolean expression for every possible input value, or with Venn
diagrams.

Boolean algebra includes a variety of operations, each represented by a variety
of symbols depending on the context.

Negation, or the "NOT" operation, changes true to false and vice versa.

Conjunction, or the "AND" operation, is true if all of its operands are true
and false otherwise.

Disjunction, or the "OR" operation, is true if at least one of its operands is
true and false otherwise.

Exclusive disjunction, or the "XOR" operation, is true if an odd number of its
operands are true and false otherwise; for the special case of two operands,
it's true if exactly one is true.

[Drawing on lightboard]
[Like, make a table or something]

Say we have some Boolean variables: `x` and `y`.

In math and philosophy, and generally in more formal contexts, negation is
represented by this weird half-rectangle thing. For conjunction, there's this
wedge thing that looks like a capital 'A' with no crossbar, and flipping that
over to a V-ish thing gives you the symbol for disjunction. The symbol for XOR
isn't as standardized, but one is like the symbol for OR with a line underneath.

In programming, usually we write NOT with an exclamation mark or a tilde;
AND with an ampersand or two; OR with a vertical bar or two; and XOR with a
caret.

In computer engineering, typically Boolean expressions are written with bars
over variables, or apostrophes, for negation; AND is written as multiplication;
OR is written as addition; and XOR is written as this plus-in-circle symbol.
Expressions can also be represented visually with logic gates.

Those operations all take Boolean values and produce Boolean values, but we can
also use operations that produce Boolean values from values of other types to
compare things.

To see whether two things are equal, most programming languages use two equals
signs, which distinguishes the comparison operator from the assignment operator;
however, for various reasons, some languages, like OCaml, don't need to make
that distinction, so they can just use a single equals sign for equality tests;
meanwhile, some languages, like JavaScript, use a triple equals sign for certain
kinds of equality tests.

Usually, an exclamation mark followed by an equals sign is used to test for
inequality, but that's not universal: MATLAB uses a tilde and an equals sign;
OCaml uses angle brackets; and Julia lets you use the Unicode inequality
character directly.

Testing to see whether one quantity is greater than or less than another is
fairly obvious: programming languages typically use an angle bracket to mimic
the corresponding mathematical sign.

The "greater than or equal to" operation is generally represented by a closing
angle bracket followed by an equals sign, while "less than or equal to" is
usually represented by an opening angle bracket followed by an equals sign, with
the notable exception of Prolog, which switches the order of the symbols because
the first way looks like a left-pointing arrow and the language designers wanted
to leave that free for the user to define.

Boolean expressions can be constructed using the operators discussed previously;
the constants "true" and "false"; and Boolean variables, which just stand for
those constants.

Such expressions can be manipulated according to the rules of Boolean algebra,
some of which are similar to laws for manipulating numerical expressions
from elementary algebra.

The associative law states that x AND (y AND z) ≡ (x AND y) AND z; this also
applies to OR.

The commutative law states that x AND y ≡ y AND x; this also applies to OR.

The idempotent law states that x AND x ≡ x; this also applies to OR.

The distributive laws state that x AND (y OR z) ≡ (x AND y) OR (x AND z), and
x OR (y AND z) ≡ (x OR y) AND (x OR z), which is different from the distributive
property with addition and multiplication, where it works one way but not the
other.

The identity for AND is true: x AND true ≡ x; the identity for OR is false:
x OR false ≡ x.

Conversely, the annihilator (or eliminator) for AND is false:
x AND false ≡ false, while the annihilator for OR is true: x OR true ≡ true.

The laws of complementation state that x AND NOT x ≡ false, and
x OR NOT x ≡ true.

The law of double negation states that NOT NOT x ≡ x.

De Morgan's laws state that NOT (x AND y) ≡ (NOT x) OR (NOT y) and
NOT (x OR y) ≡ (NOT x) AND (NOT y).

Using the idea of logic gates mentioned earlier, we can use electricity to
perform arithmetic on numbers represented in binary, as explored by Claude
Shannon in his master's thesis. An example of a circuit component is a full
adder, which computes the sum and carry bits resulting from adding two bits
together with a carry bit from a previous operation. A simple circuit to
perform this computation looks like this:

[Draw on lightboard:
In1, In2 go to XOR, which goes to XOR with Cin to make S;
also, In1 and In2 go to AND, which goes to OR with the AND of that XOR and Cin
to make Cout.]

## Java

In Java, Boolean expressions are inhabitants of the type `boolean`, all
lowercase; the only two values of that type are `true` and `false`, also all
lowercase.

The Boolean AND, OR, and NOT operators are represented in Java by `&&`, `||`,
and `!`. Java also has bitwise operators,
whose behavior is related, but not identical, to the Boolean operators; bitwise
AND and OR are represented by `&` and `|`, and XOR is represented by `^`.
Importantly, the Boolean versions of AND and OR are short-circuiting operators,
which means that they don't evaluate all of their operands if they can't change
the result, which may make execution faster or even prevent the program from
crashing in certain cases.

Java's comparison operators are `==`, `!=`, `<`, `<=`, `>`, and `>=`, which
behave as previously discussed.

And finally, Java gives Boolean operators precedences between those of
additive and assignment operators.

## Python

In Python, Boolean expressions are inhabitants of the type `bool`, all
lowercase; the only two values of that type are `True` and `False`, with
initial capital letters.

The Boolean AND, OR, and NOT operators are represented in Python simply by the
words `and`, `or`, and `not`, all lowercase. Python also has bitwise operators,
whose behavior is related, but not identical, to the Boolean operators; bitwise
AND and OR are represented by `&` and `|`, and XOR is represented by `^`.

Python will interpret pretty much anything as a Boolean if you provide it where
Python expects a Boolean value: `None`, `0`, `()`, `[]`, `""`, and some other
values are interpreted as `False`, while everything else is treated like `True`.

Python's comparison operators are `==`, `!=`, `<`, `<=`, `>`, and `>=`, which
behave as previously discussed.

And finally, Python gives Boolean operators precedences between those of
additive and assignment operators.