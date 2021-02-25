---
title: "Orders & Combos"
pre: "6. "
weight: 60
date: 2021-02-22T00:53:26-05:00
---

This page lists the milestone requirements for **Milestone 6** of the **CC 410 Restaurant Project**. Read the requirements carefully and discuss any questions with the instructors or TAs. 

## Purpose

The **CC 410 Restaurant Project** project for this semester is centered around building a point of sale (POS) system for a fictional restaurant named _Starfleet Subs_, based in the [Star Trek](https://en.wikipedia.org/wiki/Star_Trek) universe. 

The sixth milestone involves creating combo meals and orders from the items selected in the GUI. We'll use this milestone to explore some software design patterns in our code, as well as learn about using test doubles in our unit tests. With this milestone, most of the work on the core functionality of the GUI will be complete.

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

### New Classes

`starfleetsubs.data.menu.Order` - this class should represent a collection of `OrderItem` objects that make up an order.

* It should implement the **Iterator Pattern**, such that it can be used in a for each loop or enhanced for loop to iterate through all items in the list. 
* It should also support standard collection methods such as:
  * Getting the number of items in the collection (`size()` in Java or `__len__()` in Python). 
  * Determining if a given instance of an `OrderItem` object is contained in the collection. Recall that this should use the identity test, not the equality test(`contains(item)` in Java or `__contains__(item)` in Python).
  * Getting a single item from the collection based on the index of that item (either a `get(i)` method in Java or `__getitem__(i)` in Python).
  * Any other standard collection methods that you feel are helpful. See the [Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html) interface in Java or [Emulating Container Types](https://docs.python.org/3/reference/datamodel.html#emulating-container-types) in Python for additional methods that may be useful.
* It should have the following attributes:
  * A private list `items` of `OrderItems`, with methods to add and remove items, as well as the iterator pattern methods discussed above.
    * **NOTE** - in most languages, the default method to remove an item from a collection will rely on equality testing, not instance testing. So, you may wish to write this method yourself instead of relying on the underlying collection, in order to keep this and the GUI in sync.
  * A private integer representing the `orderNumber` for this order. It will be generated using the `OrderNumberSingleton` class discussed below. It should only include a getter. 
  * A private **static** float for the `taxRate`, which is set to 0.12 (12%) by default. It should include **static** methods to get and set the tax rate, which will be used by all `Order` objects. The tax rate must be a valid percentage value ranging from 0.0 to 1.0, inclusive.
* It should also have getters for these three virtual attributes or properties:
  * float `subtotal` - the total sum of the prices for each item in the order.
  * float `tax` - the `subtotal` multiplied by the `taxRate`
  * float `total` - the `subtotal` plus the `tax`. 
  * int `calories` - the total number of calories in the order.
* All dollar amounts **should not** be rounded to two decimal places by this class. that will be handled by the GUI. 

`starfleetsubs.data.menu.Combo` - this class should implement the `OrderItem` interface, and represent a combo meal consisting of an entrée, side, and drink. 
* It should have the following attributes:
  * A string `name` - the name of the combo, which does not require a getter or setter. This attribute can be set to `null` or `None`.
  * An `Entree` named `entree` - the entrée in the combo. This attribute can be set to `null` or `None`.
  * A `Side` named `side` - the side in the combo. This attribute can be set to `null` or `None`.
  * A `Drink` named `drink` - the drink in the combo. This attribute can be set to `null` or `None`. 
  * A **static** float `discount` - it has a value 0.5 ($0.50) by default. It should include **static** methods to get and set the discount, which will be used by all `Combo` objects.
* It should also comply with the `OrderItem` interface:
  * A getter for `price` that returns the sum of the prices of each item. **If all three items in the combo are populated**, the discount is applied to this total. Otherwise, no discount is applied.
  * A getter for `calories` that returns the sum of the calories of each item.
  * A getter for `specialInstructions` that returns the name of the combo, if set, followed by the line `"$0.50 Discount Applied"` if all three items are populated. It should not include any other items. 
* It should also include the following methods:
  * A constructor that accepts a string for the `name`. The constructor should allow the name to be omitted or set to `null` or `None`. The `name` will only be set by the `ComboBuilder` class discussed below, but users will also be able to configure a custom combo via the GUI that does not include a name. The constructor should set the `entree`, `side` and `drink` attributes to `null` or `None` initially.
  * An `addItem()` method that accepts an `OrderItem` object and places it in the appropriate attribute (`entree`, `side` or `drink`). It should replace the existing item in that attribute, if any. If the `OrderItem` is not one of the three types listed above, it should throw an appropriate exception.
  * A `getItems()` method that returns list of the items included in the combo, if any. If none are included, then return an empty list.  

`starfleetsubs.data.menu.ComboBuilder` - a class that implements the **Builder Pattern** to build the available combos described below. 
* It should include a single public **static** method `buildCombo()` that accepts an integer as input, and builds and returns the `Combo` object indicated by the integer. 
* For simplicity, it may also include a public **static** getter for the number of combos available. 

`starfleetsubs.data.menu.OrderNumberSingleton` - a class that implements the **Singleton Pattern** to generate new order numbers.
* The class should have a non-static integer `nextOrderNumber` attribute, which is initially set to 1
* It should have one public **static** method `getNextOrderNumber()` that will return the next order number. 
  * This method should call a private method to get the actual singleton instance stored as a static attribute in the class. 
  * It should access the `nextOrderNumber` attribute through that singleton instance.
  * This method should also use thread synchronization techniques to ensure that only a single thread can actually access and update the `nextOrderNumber` attribute (a `synchronized` statement in Java or a lock in a `with` statement in Python).

`starfleetsubs.gui.PanelFactory` - a class that implements the **Factory Method Pattern** to return an instance of a GUI panel for a given entrée, side, or drink.
* It should include one public **static** method that is overloaded to accept two different sets of parameters:
  * `getPanel(String name, parent)` should accept the name of a menu item item as a string, and return a panel that represents a new instance of that item, with the `parent` GUI element as its parent. You should be able to directly feed an action command from a button click in the GUI directly to this method and get the appropriate panel.
  * `getPanel(OrderItem item, parent)` should accept an instance of an `OrderItem` and return a panel that represents that item, with the `parent` GUI element as its parent.
* For now, do not worry about updating this class to handle `Combos` as `OrderItems`. We'll address that in the next milestone. 

### Updated Classes

`Menu` - update to include the following items:
* A `getCombos()` method that returns all pre-configured combos described below. This method should use the `ComboBuilder` class discussed below.
* Updated the `getFullMenu()` method to include the combos returned from `getCombos()` in its output.

`OrderPanel` - update to include the following items:
* The `actionPerformed` method should be updated to use the `PanelFactory` class to acquire the appropriate GUI panel based on the action command received from button that was clicked.

`SidebarPanel` - update to include the following items:
* When clicking the "Edit" button, it should use the `PanelFactory` class to acquire the appropriate GUI panel based on the item selected in the tree. 
* This class should now include a private `Order` attribute that stores the items in the order. 
  * It should be instantiated by the `SidebarPanel` constructor. The order number should be updated in the GUI as well.
  * It should be kept up to date as items are added to and removed from the order.
  * Whenever the order is changed, it should update the subtotal, tax, and total elements in the GUI 
* The GUI should include two new buttons:
  * "New Order" - clicking this button will create a new `Order` instance and reset all appropriate GUI elements for a new order. This will delete any existing order.
    * You may wish to implement a modal dialog that asks the user to confirm before deleting the existing order. See [How to Make Dialogs](https://docs.oracle.com/javase/tutorial/uiswing/components/dialog.html) for Java or [Dialog Windows](https://tkdocs.com/tutorial/windows.html#dialogs) for Python. This is not required but highly recommended!
  * "Checkout" - clicking this button will have no effect at this time. It will be implemented in the next milestone.

### Unit Tests

All new classes should include full unit tests that achieve a high level of code coverage and adequately test all aspects of the class. In addition, some previous tests may be updated to match new requirements.

## Time Requirements

Completing this project is estimated to require 3-8 hours.

{{% notice tip %}}

_A rough estimate for this milestone would be around !! TODO CHANGEME !! lines of new or updated code. -Russ_

{{% /notice %}}

## Grading Rubric

This assignment will be graded based on the rubric below:

!! TODO CHANGEME !!

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

##### Order

* `SizeIs0Initially()` - test that the size of the order is initially 0.
* `TotalsAre0Initially()` - test that the subtotal, tax, and total are 0 initially.
* `TaxRateSetInitially()` - test that the tax rate is set to 0.12 initially.
* `NegativeTaxRateThrowsException()` - test that setting the tax rate to a negative value throws an exception.
* `TaxRateOver100ThrowsException()` - test that setting the tax rate to a value over 1.0 throws an exception.

##### Combo

`DefaultConstructorSetsName()` - the default constructor should set the name. This is visible as the first element in the special instructions list.
`DefaultConstructorAcceptsNullName()` - the default constructor should accept `null` or `None` for the name.
`DefaultConstructorSetsItemsToNull()` - the default constructor should set the entree, side, and drink elements to `null` or `None`. 
`DefaultDiscountCorrect()` - the default discount of $0.50 is initially set correctly.