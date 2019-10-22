---
type: "reveal"
hidden: true
---

<section>
	<h2>Problem Statement</h2>
</section>
<section>
  <h3>Modified Blackjack</h3>
  <ol style="font-size: .5em">
    <li>The game consists of a single player playing against the dealer, played by our program in this example.</li>
    <li>Each player is initially dealt two cards from a standard 52 card deck. Each card's value is its face value, with face cards having a value of 10, and aces are valued 11.</li>
    <li>The object of the game is to get a higher total value than the other player, without going over 21.</li>
    <li>The game consists of several steps:<ol>
      <li>Both the player and the dealer review the two cards they are dealt. Both the player and the dealer can see the opponent's hand as well.</li>
      <li>The player is given the option to draw additional cards. The player may continue to draw cards until she or he chooses to stop, or their total value is greater than 21.</li>
      <li>If the player stops before going over 21, the dealer must draw cards to try and beat the player. The dealer stops drawing cards either when their total beats the player, or the dealer's total is greater than 21.</li>
      <li>At the end, the participant with the greatest card value that is less than or equal to 21 wins the game. If it is a tie, the dealer wins.</li>
    </ol></li>
  </ol>
</section>
<section>
  <h2>*~*sigh*~*</h2>
	<img class="stretch plain" src="https://media.giphy.com/media/Fjr6v88OPk7U4/source.gif">
  <p class="imagecredit">Image Credit: <a href="https://giphy.com/gifs/eye-roll-bitch-please-Fjr6v88OPk7U4">Giphy</a></p>
	<p>Let's break it down into smaller parts</p>
</section>

<section>
  <h2>Use Classes!</h2>
	<img class="stretch plain" src="https://media.giphy.com/media/3NtY188QaxDdC/source.gif">
  <p class="imagecredit">Image Credit: <a href="https://giphy.com/gifs/3NtY188QaxDdC">Giphy</a></p>
	<p>Let's break it down into <b style="color:#512888">classes</b></p>
</section>

<section>
  <img class="stretch plain" src="/images/11.6.p.10.blackjack.png">
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:
  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  # Properties
  @property
  def suit(self):
    return self.__suit

  @property
  def name(self):
    return self.__name

  @property
  def value(self):
    return self.__value
  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  <mark># Properties ...</mark>
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  def __init__(self, a_suit, a_number):

  # Properties ...
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  def __init__(self, a_suit, a_number):
    this.__suit = a_suit

  # Properties ...
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  def __init__(self, a_suit, a_number):
    this.__suit = a_suit
    this.__name = str(a_number)
    this.__value = a_number

  # Properties ...
  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  def __init__(self, a_suit, a_number):
    this.__suit = a_suit
    <mark>this.__name = str(a_number)
    this.__value = a_number</mark>

  # Properties ...
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  def __init__(self, a_suit, a_number):
    this.__suit = a_suit
    if:

    else:
      <mark>this.__name = str(a_number)
      this.__value = a_number</mark>

  # Properties ...
  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  def __init__(self, a_suit, a_number):
    this.__suit = a_suit
    if <mark>a_number == 1</mark>:

    else:
      this.__name = str(a_number)
      this.__value = a_number

  # Properties ...
  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  def __init__(self, a_suit, a_number):
    this.__suit = a_suit
    if a_number == 1:
      <mark>this.__name = "Ace"
      this.__value = 11</mark>
    else:
      this.__name = str(a_number)
      this.__value = a_number

  # Properties ...
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  def __init__(self, a_suit, a_number):
    this.__suit = a_suit
    if a_number == 1:
      this.__name = "Ace"
      this.__value = 11
    <mark>elif a_number == 11:
      this.__name = "Jack"
      this.__value = 10
    elif a_number == 12:
      this.__name = "Queen"
      this.__value = 10
    elif a_number == 13:
      this.__name = "King"
      this.__value = 10</mark>
    else:
      this.__name = str(a_number)
      this.__value = a_number

  # Properties ...
  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  def __init__(self, a_suit, a_number):
    this.__suit = a_suit
    if a_number == 1:
      this.__name = "Ace"
      this.__value = 11
    elif a_number == 11:
      this.__name = "Jack"
      this.__value = 10
    elif a_number == 12:
      this.__name = "Queen"
      this.__value = 10
    elif a_number == 13:
      this.__name = "King"
      this.__value = 10
    else:
      this.__name = str(a_number)
      this.__value = a_number

  # Properties ...
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  def __init__(self, a_suit, a_number):
    <mark>if not (a_suit == "Spades" or a_suit == "Hearts"
       or a_suit == "Clubs" or a_suit == "Diamonds"):
     raise ValueError("The suit must ...")
    if a_number &lt; 1 or a_number > 13:
      raise ValueError("The card number ...")</mark>
    this.__suit = a_suit
    if a_number == 1:
      this.__name = "Ace"
      this.__value = 11
    elif a_number == 11:
      this.__name = "Jack"
      this.__value = 10
    elif a_number == 12:
      this.__name = "Queen"
      this.__value = 10
    elif a_number == 13:
      this.__name = "King"
      this.__value = 10
    else:
      this.__name = str(a_number)
      this.__value = a_number

  # Properties ...
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  def __init__(self, a_suit, a_number):
    if not (a_suit == "Spades" or a_suit == "Hearts"
       or a_suit == "Clubs" or a_suit == "Diamonds"):
     raise ValueError("The suit must ...")
    if a_number &lt; 1 or a_number > 13:
      raise ValueError("The card number ...")
    this.__suit = a_suit
    if a_number == 1:
      this.__name = "Ace"
      this.__value = 11
    elif a_number == 11:
      this.__name = "Jack"
      this.__value = 10
    elif a_number == 12:
      this.__name = "Queen"
      this.__value = 10
    elif a_number == 13:
      this.__name = "King"
      this.__value = 10
    else:
      this.__name = str(a_number)
      this.__value = a_number

  # Properties ...
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  def __init__(self, a_suit, a_number):
    <mark>...</mark>

  # Properties ...
  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.card.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Card:

  def __init__(self, a_suit, a_number):
    ...

  # Properties ...

  def __str__(self):
    return "{} of {}".format(this.__name, this.__suit)
  </code></pre>
  </div>
</section>



<section>
  <img class="stretch plain" src="/images/11.6.p.10.blackjack.png">
</section>



<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Deck:

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python"><mark>from Card import *</mark>

class Deck:

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">from Card import *

class Deck:

  <mark>def __init__(self):</mark>

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">from Card import *

class Deck:

  def __init__(self):
    <mark>self.__card_deck = []</mark>

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">from Card import *

class Deck:

  def __init__(self):
    self.__card_deck = []
    <mark>suits = ["Spades", "Hearts", "Diamonds", "Clubs"]</mark>
    <mark>for suit in suits:</mark>

  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">from Card import *

class Deck:

  def __init__(self):
    self.__card_deck = []
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    for suit in suits:
      <mark>for i in range(1, 14):
        self.__card_deck.append(Card(suit, i))</mark>

  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">from Card import *

class Deck:

  def __init__(self):
    self.__card_deck = []
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    for suit in suits:
      for i in range(1, 14):
        self.__card_deck.append(Card(suit, i))

  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">from Card import *

class Deck:

  def __init__(self):
    self.__card_deck = []
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    for suit in suits:
      for i in range(1, 14):
        self.__card_deck.append(Card(suit, i))

  def __str__(self):
    output = ""
    for a_card in self.__card_deck:
      output += str(a_card) + "\n"
    return output
  </code></pre>
  </div>
</section>


<section>
  <img class="stretch plain" src="/images/stop.png">
  <h3>Let's Test It!</h3>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%; opacity: 0" src="/images/11.6.p.10.python_ordered.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Deck import *

class Main:

  @staticmethod
  def main():
    a_deck = Deck()
    print(a_deck)

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.python_ordered.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Deck import *

class Main:

  @staticmethod
  def main():
    a_deck = Deck()
    print(a_deck)

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">from Card import *

class Deck:

  def __init__(self): ...
  def __str__(self): ...
  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">from Card import *

class Deck:

  def __init__(self): ...
  def __str__(self): ...

  <mark>def shuffle(self, times):</mark>
  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">from Card import *

class Deck:

  def __init__(self): ...
  def __str__(self): ...

  def shuffle(self, times):
    <mark>for i in range(0, times):</mark>
  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python"><mark>import random</mark>
from Card import *

class Deck:

  def __init__(self): ...
  def __str__(self): ...

  def shuffle(self, times):
    for i in range(0, times):
      <mark>first = random.randint(0, 52)
      second = random.randint(0, 52)</mark>
  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">import random
from Card import *

class Deck:

  def __init__(self): ...
  def __str__(self): ...

  def shuffle(self, times):
    for i in range(0, times):
      first = random.randint(0, 52)
      second = random.randint(0, 52)
      <mark>if first != second:
        temp = self.__card_deck[first]
        self.__card_deck[first] = self.__card_deck[second]
        self.__card_deck[second] = temp</mark>
  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">import random
from Card import *

class Deck:

  def __init__(self): ...
  def __str__(self): ...

  def shuffle(self, times):
    <mark>if times <= 0:
      raise ValueError("The deck must ...")</mark>
    for i in range(0, times):
      first = random.randint(0, 52)
      second = random.randint(0, 52)
      if first != second:
        temp = self.__card_deck[first]
        self.__card_deck[first] = self.__card_deck[second]
        self.__card_deck[second] = temp
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">import random
from Card import *

class Deck:

  def __init__(self): ...
  def __str__(self): ...

  def shuffle(self, times):
    if times <= 0:
      raise ValueError("The deck must ...")
    for i in range(0, times):
      first = random.randint(0, 52)
      second = random.randint(0, 52)
      if first != second:
        temp = self.__card_deck[first]
        self.__card_deck[first] = self.__card_deck[second]
        self.__card_deck[second] = temp
  </code></pre>
  </div>
</section>


<section>
  <img class="stretch plain" src="/images/stop.png">
  <h3>Let's Test It!</h3>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%; opacity: 0" src="/images/11.6.p.10.python_shuffle.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Deck import *

class Main:

  @staticmethod
  def main():
    a_deck = Deck()
    a_deck.shuffle(1000)
    print(a_deck)

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.python_shuffle.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Deck import *

class Main:

  @staticmethod
  def main():
    a_deck = Deck()
    a_deck.shuffle(1000)
    print(a_deck)

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">import random
from Card import *

class Deck:

  def __init__(self): ...
  def __str__(self): ...
  def shuffle(self, times): ...

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">import random
from Card import *

class Deck:

  def __init__(self): ...
  def __str__(self): ...
  def shuffle(self, times): ...

  <mark>def draw(self):</mark>

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">import random
from Card import *

class Deck:

  def __init__(self): ...
  def __str__(self): ...
  def shuffle(self, times): ...

  def draw(self):
    <mark>output = self.__card_deck[self.__card_position]
    self.__card_position += 1
    return output</mark>

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">import random
from Card import *

class Deck:

  def __init__(self):
    <mark>self.__card_position = 0</mark>
    ...

  def __str__(self): ...
  def shuffle(self, times): ...

  def draw(self):
    output = self.__card_deck[self.__card_position]
    self.__card_position += 1
    return output

  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.deck.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">import random
from Card import *

class Deck:

  def __init__(self):
    self.__card_position = 0
    ...

  def __str__(self): ...
  def shuffle(self, times): ...

  def draw(self):
    output = self.__card_deck[self.__card_position]
    self.__card_position += 1
    return output

  </code></pre>
  </div>
</section>


<section>
  <img class="stretch plain" src="/images/11.6.p.10.blackjack.png">
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.hand.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Hand:

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.hand.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">from Card import *

class Hand:

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.hand.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">from Card import *

class Hand:

  def __init__(self):
    self.__card_hand = []

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.hand.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">from Card import *

class Hand:

  def __init__(self):
    self.__card_hand = []

  @property
  def value(self):
    value = 0
    for card in self.__card_hand:
      value += card.value
    return value

  def __str__(self):
    output = ""
    for card in self.__card_hand:
      output += str(card) + "\n"
    return output
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.hand.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .37em"><code class="python">from Card import *

class Hand:

  def __init__(self):
    self.__card_hand = []

  @property
  def value(self):
    value = 0
    for card in self.__card_hand:
      value += card.value
    return value

  def __str__(self):
    output = ""
    for card in self.__card_hand:
      output += str(card) + "\n"
    return output

  def add_card(self, input):
    if not isinstance(input, Card):
      raise ValueError("Input must be a Card object")
    self.__card_hand.append(input)
  </code></pre>
  </div>
</section>


<section>
  <img class="stretch plain" src="/images/11.6.p.10.blackjack.png">
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.dealer.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">class Dealer:

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.dealer.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *

class Dealer:

  def __init__(self, a_hand):
    if not isinstance(a_hand, Hand):
      raise ValueError("A_hand must be a Hand object")
    self.__my_hand = a_hand

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.dealer.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *

class Dealer:

  def __init__(self, a_hand):
    if not isinstance(a_hand, Hand):
      raise ValueError("A_hand must be a Hand object")
    self.__my_hand = a_hand

  def __str__(self):
    output = "The dealer currently holds: \n"
    output += str(self.__my_hand)
    output += "for a total of {}".format(self.__my_hand.value)
    return output

  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.dealer.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *

class Dealer:

  def __init__(self, a_hand): ...
  def __str__(self): ...

  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.dealer.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *

class Dealer:

  def __init__(self, a_hand): ...
  def __str__(self): ...

  def make_moves(self, player_value):

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.dealer.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *

class Dealer:

  def __init__(self, a_hand): ...
  def __str__(self): ...

  def make_moves(self, player_value):
    while self.__my_hand.value &lt; player_value and
                      self.__my_hand.value &lt;= 21:
      # we need to draw a card here!

  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.dealer.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *

class Dealer:

  def __init__(self, a_hand): ...
  def __str__(self): ...

  def make_moves(self, player_value):
    while self.__my_hand.value &lt; player_value and
                      self.__my_hand.value &lt;= 21:
      # <mark>we need to draw a card here!</mark>

  </code></pre>
  </div>
</section>

<section>
  <h3>Option 1: Make Deck Static</h3>
  <p><b>Pros:</b></p>
  <ul>
    <li>Requires few code changes</li>
    <li>Can use deck from anywhere</li>
  </ul>
  <p><b>Cons:</b></p>
  <ul>
    <li>Can only have one deck</li>
    <li>Not standard</li>
  </ul>
</section>

<section>
  <h3>Option 2: Pass Deck to Dealer</h3>
  <p><b>Pros:</b></p>
  <ul>
    <li>No modification to deck</li>
    <li>More object-oriented</li>
  </ul>
  <p><b>Cons:</b></p>
  <ul>
    <li>Have to manage deck instance</li>
    <li>Easy to lose objects in code</li>
  </ul>
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.dealer.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *

class Dealer:

  def __init__(self, a_hand): ...
  def __str__(self): ...

  def make_moves(self, player_value):
    while self.__my_hand.value &lt; player_value and
                      self.__my_hand.value &lt;= 21:
      # we need to draw a card here!

  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.dealer.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *

class Dealer:

  def __init__(self, a_hand, <mark>a_deck</mark>):
    if not isinstance(a_hand, Hand):
      raise ValueError("A_hand must be a Hand object")
    <mark>if not isinstance(a_deck, Deck):
      raise ValueError("A_deck must be a Hand object")</mark>
    self.__my_hand = a_hand
    <mark>self.__the_deck = a_deck</mark>

  def __str__(self): ...

  def make_moves(self, player_value):
    while self.__my_hand.value &lt; player_value and
                      self.__my_hand.value &lt;= 21:
      # we need to draw a card here!

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.dealer.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *

class Dealer:

  def __init__(self, a_hand, a_deck):
    if not isinstance(a_hand, Hand):
      raise ValueError("A_hand must be a Hand object")
    if not isinstance(a_deck, Deck):
      raise ValueError("A_deck must be a Hand object")
    self.__my_hand = a_hand
    self.__the_deck = a_deck

  def __str__(self): ...

  def make_moves(self, player_value):
    while self.__my_hand.value &lt; player_value and
                      self.__my_hand.value &lt;= 21:
      <mark>new_card = self.__the_deck.draw()
      print("The dealer draws a {}".format(str(new_card)))
      self.__my_hand.add_card(new_card)</mark>

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.dealer.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *

class Dealer:

  def __init__(self, a_hand, a_deck):
    if not isinstance(a_hand, Hand):
      raise ValueError("A_hand must be a Hand object")
    if not isinstance(a_deck, Deck):
      raise ValueError("A_deck must be a Hand object")
    self.__my_hand = a_hand
    self.__the_deck = a_deck

  def __str__(self): ...

  def make_moves(self, player_value):
    while self.__my_hand.value &lt; player_value and
                      self.__my_hand.value &lt;= 21:
      new_card = self.__the_deck.draw()
      print("The dealer draws a {}".format(str(new_card)))
      self.__my_hand.add_card(new_card)

  </code></pre>
  </div>
</section>

<section>
  <img class="stretch plain" src="/images/11.6.p.10.blackjack.png">
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.player.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *
from Deck import *

class Dealer:

  def __init__(self, a_hand, a_deck):
    if not isinstance(a_hand, Hand):
      raise ValueError("A_hand must be a Hand object")
    if not isinstance(a_deck, Deck):
      raise ValueError("A_deck must be a Hand object")
    self.__my_hand = a_hand
    self.__the_deck = a_deck

  def __str__(self):
    output = "The dealer currently holds: \n"
    output += str(self.__my_hand)
    output += "for a total of {}".format(self.__my_hand.value)
    return output
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.player.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *
from Deck import *

class <mark>Dealer</mark>:

  def __init__(self, a_hand, a_deck):
    if not isinstance(a_hand, Hand):
      raise ValueError("A_hand must be a Hand object")
    if not isinstance(a_deck, Deck):
      raise ValueError("A_deck must be a Hand object")
    self.__my_hand = a_hand
    self.__the_deck = a_deck

  def __str__(self):
    output = "The <mark>dealer</mark> currently holds: \n"
    output += str(self.__my_hand)
    output += "for a total of {}".format(self.__my_hand.value)
    return output
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.player.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *
from Deck import *

class <mark>Player</mark>:

  def __init__(self, a_hand, a_deck):
    if not isinstance(a_hand, Hand):
      raise ValueError("A_hand must be a Hand object")
    if not isinstance(a_deck, Deck):
      raise ValueError("A_deck must be a Hand object")
    self.__my_hand = a_hand
    self.__the_deck = a_deck

  def __str__(self):
    output = "The <mark>player</mark> currently holds: \n"
    output += str(self.__my_hand)
    output += "for a total of {}".format(self.__my_hand.value)
    return output
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.player.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *
from Deck import *

class Player:

  def __init__(self, a_hand, a_deck):
    if not isinstance(a_hand, Hand):
      raise ValueError("A_hand must be a Hand object")
    if not isinstance(a_deck, Deck):
      raise ValueError("A_deck must be a Hand object")
    self.__my_hand = a_hand
    self.__the_deck = a_deck

  def __str__(self):
    output = "The player currently holds: \n"
    output += str(self.__my_hand)
    output += "for a total of {}".format(self.__my_hand.value)
    return output
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.player.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *
from Deck import *

class Player:

  def __init__(self, a_hand, a_deck): ...
  def __str__(self): ...


  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.player.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Hand import *
from Deck import *

class Player:

  def __init__(self, a_hand, a_deck): ...
  def __str__(self): ...

  <mark>def make_moves(self):</mark>

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.player.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python"><mark>import sys</mark>
from Hand import *
from Deck import *

class Player:

  def __init__(self, a_hand, a_deck): ...
  def __str__(self): ...

  def make_moves(self):
    <mark>with sys.stdin as reader:</mark>

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.player.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">import sys
from Hand import *
from Deck import *

class Player:

  def __init__(self, a_hand, a_deck): ...
  def __str__(self): ...

  def make_moves(self):
    with sys.stdin as reader:
      <mark>while self.__my_hand.value <= 21:</mark>

  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.player.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">import sys
from Hand import *
from Deck import *

class Player:

  def __init__(self, a_hand, a_deck): ...
  def __str__(self): ...

  def make_moves(self):
    with sys.stdin as reader:
      while self.__my_hand.value <= 21:
        <mark>print("You currently have a value of {}".format(
              self.__my_hand.value))
        print("Would you like to draw another card (y/n)?: ")
        input = reader.readline().strip()</mark>

  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.player.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">import sys
from Hand import *
from Deck import *

class Player:

  def __init__(self, a_hand, a_deck): ...
  def __str__(self): ...

  def make_moves(self):
    with sys.stdin as reader:
      while self.__my_hand.value <= 21:
        print("You currently have a value of {}".format(
              self.__my_hand.value))
        print("Would you like to draw another card (y/n)?: ")
        input = reader.readline().strip()
        <mark>if input == "y" or input == "Y":
          new_card = self.__the_deck.draw()
          print("The dealer draws a {}".format(str(new_card)))
          self.__my_hand.add_card(new_card)
        elif input == "n" or input == "N":
          break;
        else:
          print("Invalid input!")</mark>

  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.player.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">import sys
from Hand import *
from Deck import *

class Player:

  def __init__(self, a_hand, a_deck): ...
  def __str__(self): ...

  def make_moves(self):
    with sys.stdin as reader:
      while self.__my_hand.value <= 21:
        print("You currently have a value of {}".format(
              self.__my_hand.value))
        print("Would you like to draw another card (y/n)?: ")
        input = reader.readline().strip()
        if input == "y" or input == "Y":
          new_card = self.__the_deck.draw()
          print("The dealer draws a {}".format(str(new_card)))
          self.__my_hand.add_card(new_card)
        elif input == "n" or input == "N":
          break;
        else:
          print("Invalid input!")
      <mark>print("You end your turn with a value of {}".format(
              self.__my_hand.value))</mark>

  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
     <img class="plain" style="width: 100%" src="/images/11.6.p.10.blackjack.player.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .35em"><code class="python">import sys
from Hand import *
from Deck import *

class Player:

  def __init__(self, a_hand, a_deck): ...
  def __str__(self): ...

  def make_moves(self):
    with sys.stdin as reader:
      while self.__my_hand.value <= 21:
        print("You currently have a value of {}".format(
              self.__my_hand.value))
        print("Would you like to draw another card (y/n)?: ")
        input = reader.readline().strip()
        if input == "y" or input == "Y":
          new_card = self.__the_deck.draw()
          print("The dealer draws a {}".format(str(new_card)))
          self.__my_hand.add_card(new_card)
        elif input == "n" or input == "N":
          break;
        else:
          print("Invalid input!")
      print("You end your turn with a value of {}".format(
            self.__my_hand.value))

  </code></pre>
  </div>
</section>


<section>
  <img class="stretch plain" src="/images/11.6.p.10.blackjack.png">
</section>

<section>
  <div style="width: 100%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Deck import *
from Hand import *
from Dealer import *
from Player import *

class Main:

  @staticmethod
  def main():

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>


<section>
  <div style="width: 100%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Deck import *
from Hand import *
from Dealer import *
from Player import *

class Main:

  @staticmethod
  def main():
    <mark>the_deck = Deck()</mark>

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>


<section>
  <div style="width: 100%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Deck import *
from Hand import *
from Dealer import *
from Player import *

class Main:

  @staticmethod
  def main():
    the_deck = Deck()
    <mark>the_deck.shuffle(1000)</mark>

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>

<section>
  <div style="width: 100%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Deck import *
from Hand import *
from Dealer import *
from Player import *

class Main:

  @staticmethod
  def main():
    the_deck = Deck()
    the_deck.shuffle(1000)
    <mark>player_hand = Hand()
    player_hand.add_card(the_deck.draw())
    player_hand.add_card(the_deck.draw())
    a_player = Player(player_hand, the_deck)</mark>

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>

<section>
  <div style="width: 100%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Deck import *
from Hand import *
from Dealer import *
from Player import *

class Main:

  @staticmethod
  def main():
    the_deck = Deck()
    the_deck.shuffle(1000)
    player_hand = Hand()
    player_hand.add_card(the_deck.draw())
    player_hand.add_card(the_deck.draw())
    a_player = Player(player_hand, the_deck)
    <mark>dealer_hand = Hand()
    dealer_hand.add_card(the_deck.draw())
    dealer_hand.add_card(the_deck.draw())
    a_dealer = Dealer(dealer_hand, the_deck)</mark>

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>


<section>
  <div style="width: 100%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Deck import *
from Hand import *
from Dealer import *
from Player import *

class Main:

  @staticmethod
  def main():
    the_deck = Deck()
    the_deck.shuffle(1000)
    player_hand = Hand()
    player_hand.add_card(the_deck.draw())
    player_hand.add_card(the_deck.draw())
    a_player = Player(player_hand, the_deck)
    dealer_hand = Hand()
    dealer_hand.add_card(the_deck.draw())
    dealer_hand.add_card(the_deck.draw())
    a_dealer = Dealer(dealer_hand, the_deck)
    <mark>a_player.make_moves()</mark>

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>


<section>
  <div style="width: 100%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Deck import *
from Hand import *
from Dealer import *
from Player import *

class Main:

  @staticmethod
  def main():
    the_deck = Deck()
    the_deck.shuffle(1000)
    player_hand = Hand()
    player_hand.add_card(the_deck.draw())
    player_hand.add_card(the_deck.draw())
    a_player = Player(player_hand, the_deck)
    dealer_hand = Hand()
    dealer_hand.add_card(the_deck.draw())
    dealer_hand.add_card(the_deck.draw())
    a_dealer = Dealer(dealer_hand, the_deck)
    a_player.make_moves()
    <mark>a_dealer.make_moves(player_hand.value)</mark>

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>


<section>
  <div style="width: 100%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Deck import *
from Hand import *
from Dealer import *
from Player import *

class Main:

  @staticmethod
  def main():
    the_deck = Deck()
    the_deck.shuffle(1000)
    player_hand = Hand()
    player_hand.add_card(the_deck.draw())
    player_hand.add_card(the_deck.draw())
    a_player = Player(player_hand, the_deck)
    dealer_hand = Hand()
    dealer_hand.add_card(the_deck.draw())
    dealer_hand.add_card(the_deck.draw())
    a_dealer = Dealer(dealer_hand, the_deck)
    a_player.make_moves()
    a_dealer.make_moves(player_hand.value)

    <mark>if player_hand.value <= 21 and dealer_hand.value > 21:
      print("The player wins!")
    elif player_hand.value <= 21 and player_hand.value > dealer_hand.value:
      print("The player wins!")
    elif dealer_hand.value <= 21:
      print("The dealer wins!")
    else:
      print("There is no winner")</mark>

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>


<section>
  <div style="width: 100%">
  <pre class="stretch" style="font-size: .35em"><code class="python">from Deck import *
from Hand import *
from Dealer import *
from Player import *

class Main:

  @staticmethod
  def main():
    the_deck = Deck()
    the_deck.shuffle(1000)
    player_hand = Hand()
    player_hand.add_card(the_deck.draw())
    player_hand.add_card(the_deck.draw())
    a_player = Player(player_hand, the_deck)
    dealer_hand = Hand()
    dealer_hand.add_card(the_deck.draw())
    dealer_hand.add_card(the_deck.draw())
    a_dealer = Dealer(dealer_hand, the_deck)
    a_player.make_moves()
    a_dealer.make_moves(player_hand.value)

    if player_hand.value <= 21 and dealer_hand.value > 21:
      print("The player wins!")
    elif player_hand.value <= 21 and player_hand.value > dealer_hand.value:
      print("The player wins!")
    elif dealer_hand.value <= 21:
      print("The dealer wins!")
    else:
      print("There is no winner")

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>


<section>
  <img class="stretch plain" src="/images/11.6.p.10.python_output.png">
</section>
