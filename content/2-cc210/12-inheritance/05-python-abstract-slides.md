---
type: "reveal"
hidden: true
---

<section>
    <img class="plain stretch" style="" src="/images/12.7.p.uml.png">
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.vehicle.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">class Vehicle:

  def __init__(self, name):
    self.__name = name
    self.speed = 1.0

  @property
  def name(self):
    return self.__name

  def move(self, distance):
    print("Moving")
    return distance / self.speed

  def describe(self):
    return ""
</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.vehicle.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python"><mark>from abc import ABC, abstractmethod</mark>

class Vehicle:

  def __init__(self, name):
    self.__name = name
    self.speed = 1.0

  @property
  def name(self):
    return self.__name

  def move(self, distance):
    print("Moving")
    return distance / self.speed

  def describe(self):
    return ""
</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.vehicle.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">from abc import ABC, abstractmethod

class Vehicle<mark>(ABC)</mark>:

  def __init__(self, name):
    self.__name = name
    self.speed = 1.0

  @property
  def name(self):
    return self.__name

  def move(self, distance):
    print("Moving")
    return distance / self.speed

  def describe(self):
    return ""
</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.vehicle.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">from abc import ABC, abstractmethod

class Vehicle(ABC):

  def __init__(self, name):
    self.__name = name
    self.speed = 1.0

  @property
  def name(self):
    return self.__name

  def move(self, distance):
    print("Moving")
    return distance / self.speed

  <mark>@abstractmethod</mark>
  def describe(self):
    return ""
</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.vehicle.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">from abc import ABC, abstractmethod

class Vehicle(ABC):

  def __init__(self, name):
    self.__name = name
    self.speed = 1.0

  @property
  def name(self):
    return self.__name

  def move(self, distance):
    print("Moving")
    return distance / self.speed

  @abstractmethod
  def describe(self):
    return ""
</code></pre>
  </div>
</section>
