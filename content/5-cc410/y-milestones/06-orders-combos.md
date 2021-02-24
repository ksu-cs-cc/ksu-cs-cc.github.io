---
title: "Orders & Combos"
pre: "6. "
weight: 60
date: 2021-02-22T00:53:26-05:00
---

This page lists the milestone requirements for **Milestone 6** of the **CC 410 Restaurant Project**. Read the requirements carefully and discuss any questions with the instructors or TAs. 

## Purpose

The **CC 410 Restaurant Project** project for this semester is centered around building a point of sale (POS) system for a fictional restaurant named _Starfleet Subs_, based in the [Star Trek](https://en.wikipedia.org/wiki/Star_Trek) universe. 

The sixth milestone involves creating combo meals and orders from the items selected in the GUI. With this milestone, most of the work on the core functionality of the GUI will be complete.

## General Requirements

This milestone must follow these professional coding standards:

* **All code must be object-oriented.**
  * All executable code must be within a class
    * Python package files such as `__init__.py` and `__main__.py` are exempt.
  * Classes must be organized into packages based on common usage.
* **This project must include automation for compilation, unit testing, style checking, documentation generation, and execution.**
  * Java: Use Gradle with the `application` plugin. The project should compile without errors.
  * Python: Use tox configured to use Python 3.6 and a requirements file to install libraries.
* **All code must properly compile or be interpreted.**
  * Java: It must compile using Gradle.
  * Python: It must be interpreted using Python 3.6. Where specified, type hints should be included in the code, and all code should pass a strict Mypy type check with low imprecision percentage.
* **Where specified, code should contain appropriate unit tests that achieve the specified level of code coverage.**
  * Java: Use JUnit 5. You may choose to use Hamcrest for assertions.
  * Python: Use pytest. You may choose to use Hamcrest for assertions.
* **Where specified, code should contain appropriate documentation comments following the language's style guide.**
  * Java: Use javadoc to generate documentation.
  * Python: Use pdoc3 to generate documentation.
* **All code submitted must be free of style errors.** We will be using the [Google Style Guide](https://google.github.io/styleguide/) for each language. 
  * Java: Use Checkstyle 8.38+ and the [Google Style Configuration](https://raw.githubusercontent.com/checkstyle/checkstyle/checkstyle-8.38/src/main/resources/google_checks.xml). 
    * You may modify the configuration to allow 4 space indentations instead of 2 space indentations.
  * Python: Use Flake8 with the `flake8-docstrings` and `pep8-naming` plugins. Code should conform to PEP 8 style with Google style docstrings. 
* Submissions to Canvas should be tagged GitHub releases that are numbered according to [Semantic Versioning](https://semver.org/).

## Assignment Requirements

`Order` class
`Combo` class - 
`OrderNumberSingleton` class - Singleton Pattern
`PanelFactory` class - Factory Pattern
`ComboBuilder` class - Builder Pattern
`Menu` - update to include `getCombos()` and fix `getFullMenu()`

  
## Time Requirements

Completing this project is estimated to require 3-8 hours.

{{% notice tip %}}

_A rough estimate for this milestone would be around 3000-3500 lines of new or updated code. It could vary widely based on how you choose to implement the various portions of the GUI. Most of the new code (around 2000-2500 lines) is contained in the unit tests, which are highly redundant. It took me less than an hour to take a working set of unit tests for `TheRikerPanel` and use that as a template to create the rest of the unit tests. My current model solution contains 849 unit tests, and I was able to achieve 100% code coverage on all GUI `OrderItem` panels. -Russ_

{{% /notice %}}

## Grading Rubric

This assignment will be graded based on the rubric below:

* New GUI elements ("Cancel", "Delete" and tree element): 5%
* Tree element displays order items correctly: 5%
* "Save" buttons work properly for all items: 25%
* "Cancel" buttons work properly for all items: 5%
* "Edit" button works properly for all items: 25%
* "Delete" button works properly for all items: 5%
* Unit Tests: 20%
* Updated UML Diagram: 10%

The following deductions apply:

* Any portion of the project which will not compile (Java), pass a strict type check (Python), or execute properly will be given a grade of 0.

This is not an exhaustive list of possible deductions. The instructors will strive to provide reasonable and fair grading, but we can't predict all possible defects. It is up to the student to ensure that the project is complete and correct before submission. 

## Submission

Submit this assignment by creating a release on GitHub and uploading the release URL to the assignment on Canvas. You **should not** submit this Codio project or mark it as complete in Codio, in case you need to come back to it and make changes later.

---
---
---

## Combos

###### 1 - Original Series

The Kirk, Bones McCoy, Altair Water

###### 2 - Next Generation

The Riker, Data Chips, The Picard

###### 3 - Voyage Beyond

The Janeway, Enterprise, The Guinan

###### 4 - Warrior's Way

The Gagh, Borg, The Worf

###### 5 - Galaxy Class

The Scotty, Enterprise, The Troi

###### 6 - Judgement of Humanity

The Q, Borg, The Picard

## Unit Tests

##### Combo

`DefaultConstructorSetsName()` - the default constructor should set the name. This is visible as the first element in the special instructions list.
`DefaultConstructorAcceptsNullName()` - the default constructor should accept `null` or `None` for the name.
`DefaultConstructorSetsItemsToNull()` - the default constructor should set the entree, side, and drink elements to `null` or `None`. 
`DefaultDiscountCorrect()` - the default discount of $0.50 is initially set correctly.