## General

Welcome to the Module 1 review, where you can find all the ideas you should know
from Module 1.

First of all, what is computer programming? Basically, it's giving a computer
instructions to make it do what you want. In theory, that just requires
programming a Turing machine, a simple model of computation invented
by Alan Turing in the 1930s. Alonzo Church
developed another model of computation in the '30s called lambda calculus, and
both Turing machines and lambda calculus are capable of computing anything
computable ("computable", by the way, is a technical term, though you needn't
know anything about that for this course).

In practice, directly implementing anything interesting using Turing machines or
lambda calculus is inefficient and tedious, so modern computers have more
complex architectures and are typically programmed in high-level programming
languages that look somewhat like human languages, like Haskell, Lisp, C,
Python, and Java. Programs written in such languages must be translated to
machine code so the computer can actually execute them; two different kinds of
programs for doing that translation are compilers---which translate the entire
program into an executable file---and interpreters---which translate and execute
the program one piece at a time without producing a full machine language
program.



## Java

Now for the Java bit. Java was invented in the 1990s by a Canadian fellow named
James Gosling along with some other folks at Sun Microsystems. Java programs are
compiled to Java bytecode that can then be executed on the Java Virtual Machine.
Java was designed to look a lot like C++, so it's generally in the C family of
languages.

With the history lesson out of the way, here are the main programming concepts
you should know from this module.

Usually, the first program one writes when
learning a new language does nothing but print some form of the message
"Hello world" to the screen (punctuation and capitalization vary).

A keyword is a word that has some special built-in meaning to a programming
language,
which is a concept similar but not identical to that of a reserved word, which
can't be used as an identifier.

Speaking of which, an identifier is a word that the programmer gives meaning,
usually by making it the name used to refer to a variable, function, class, or
other entity.

A function, or subroutine, is a piece of a program that performs a specific
task; "method" is a related term that can be treated as synonomous to "function"
for now. Functions allow a programmer to write a bunch of code once and use, or
_call_, it in multiple places.

A declaration lets the computer know that you want to use a particular name to
refer to something later in the program; in Java, this can be done separately
from that thing's definition, which actually tells the computer what the thing
is, and in the case of a method or class consists of its body, which is
enclosed by braces.

Java source files use the extension `.java` and can be created and edited in
any text editor.

Java requires that everything in a program be inside a class, which can be
declared with the `class` keyword. For boring technical reasons, if you use
the `public` keyword before `class`, the class must have the same name
as the file containing it, but if you remove the `public` declaration, you
can name the file whatever you want.

To write a Java program, you have to memorize the magic incantation
`public static void main(String[] gorilla)`;
this declares the `main`
method, where execution begins when the program is run. It's customary to use
the name `args` (for "arguments") instead of `gorilla`, but it's totally
arbitrary and `gorilla` is more fun.

To print something to the screen, there's another bit of sorcery called
"system dot out dot ell enn"; this is a method that you call by writing
its name and putting the thing to print in parentheses.

Written text in most programming languages is represented by _strings_, which
are written between double quotes.

Each statement in Java must end with a semicolon, sort of like ending sentences
with periods in human languages.

The terminal is a text-based interface to the operating system; Codio uses an
operating system called Ubuntu, which is a GNU/Linux distribution, so knowing
some GNU/Linux terminal commands (which also apply to MacOS X and other
Unix-like systems) will be helpful for this course.

The command `pwd` prints the working directory, or current folder, to the
screen; `ls` lists the files and other directories within a directory; and
`cd` changes the working directory.

Java programs can be compiled to Java bytecode by the `javac` command; after
a file is compiled, the program can be run with the `java` command followed
by a space and the name of the class containing the `main` method you want
to run.


## Python

Now for the Python bit. Python was invented around 1990 by a Dutch fellow named
Guido van
Rossum and is usually interpreted. Two incompatible versions exist: Python 2 and
Python 3, though support for Python 2 ends at the beginning of 2020 and, to
quote the Python wiki, "Python 2 is legacy, Python 3 is the present and future
of the language". Python incorporates elements of various programming paradigms
and is a decent first language because its syntax is more similar to English
than many languages. Python's design philosophy is embodied in a number of
aphorisms describing the so-called "Zen of Python"; you can see these by typing
`import this` at the Python prompt.

With the history lesson out of the way, here are the main programming concepts
you should know from this module.

Usually, the first program one writes when
learning a new language does nothing but print some form of the message
"Hello world" to the screen (punctuation and capitalization vary).

A keyword is a word that has some special built-in meaning to a programming
language,
which is a concept similar but not identical to that of a reserved word, which
can't be used as an identifier.

Speaking of which, an identifier is a word that the programmer gives meaning,
usually by making it the name used to refer to a variable, function, class, or
other entity.

A function, or subroutine, is a piece of a program that performs a specific
task; "method" is a related term that can be treated as synonomous to "function"
for now. Functions allow a programmer to write a bunch of code once and use, or
_call_, it in multiple places.

Python source files use the extension `.py` and can be created and edited in
any text editor.

To print something in Python, one can call the `print` function by writing
its name and putting the thing to print in parentheses.

Written text in most programming languages is represented by _strings_, which
are written between double quotes; Python also lets you use single quotes.

The terminal is a text-based interface to the operating system; Codio uses an
operating system called Ubuntu, which is a GNU/Linux distribution, so knowing
some GNU/Linux terminal commands (which also apply to MacOS X and other
Unix-like systems) will be helpful for this course.

The command `pwd` prints the working directory, or current folder, to the
screen; `ls` lists the files and other directories within a directory; and
`cd` changes the working directory.

To run Python programs from the terminal, you can use the command `python3`
followed by a space and the name of the file containing the program you want to
run; Python also has an interactive mode, or REPL (for read-eval-print loop),
where you can enter Python statements and expressions and immediately see the
results; it's invoked with the `python3` command with no file provided, or
by using the `-i` flag.