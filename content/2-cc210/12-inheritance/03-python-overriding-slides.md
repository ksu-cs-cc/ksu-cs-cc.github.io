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
    <pre class="stretch" style="font-size: .4em"><code class="python">class Vehicle:

  <mark>def __init__(self, name):
    self.__name = name
    self.speed = 1.0</mark>

  @property
  def name(self):
    return self.__name

  def move(self, distance):
    print("Moving")
    return distance / self.speed

  def describe(self):
    return ""</code></pre>
  </div>
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

  <mark>def move(self, distance):
    print("Moving")
    return distance / self.speed</mark>

  <mark>def describe(self):
    return ""</mark>
</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">from Vehicle import *

class Airplane(Vehicle):

  def __init__(self, name, wingspan, capacity):
    self.__name = name
    self.__wingspan = wingspan
    self.__capacity = capacity</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">from Vehicle import *

class Airplane(Vehicle):

  def __init__(self, name, wingspan, capacity):
    self.__name = name
    self.__wingspan = wingspan
    self.__capacity = capacity</code></pre><pre class="stretch" style="font-size: .4em"><code class="python">from Airplane import *

class Main:

  @staticmethod
  def main():
    a = Airplane("Test", 123, 45)
    print(a.name)

# main guard
if __name__ == "__main__":
  Main.main()</code></pre>
  </div>
</section>

<section>
    <img class="plain stretch" style="" src="/images/12.7.p.2.error.png">
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">from Vehicle import *

class Airplane(Vehicle):

  def __init__(self, name, wingspan, capacity):
    <mark style="background-color: red">self.__name = name</mark>
    self.__wingspan = wingspan
    self.__capacity = capacity</code></pre><pre class="stretch" style="font-size: .4em"><code class="python">from Airplane import *

class Main:

  @staticmethod
  def main():
    a = Airplane("Test", 123, 45)
    print(<mark style="background-color: red">a.name</mark>)

# main guard
if __name__ == "__main__":
  Main.main()</code></pre>
  </div>
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

  <mark>@property
  def name(self):
    return self.__name</mark>

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
    <pre class="stretch" style="font-size: .4em"><code class="python">class Vehicle:

  def __init__(self, name):
    self.__name = name
    self.speed = 1.0

  @property
  def name(self):
    return <mark style="background-color: red">self.__name</mark>

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
	   <img class="plain" style="width: 100%" src="/images/12.7.p.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">from Vehicle import *

class Airplane(Vehicle):

  def __init__(self, name, wingspan, capacity):
    <mark style="background-color: red">self.__name = name</mark>
    self.__wingspan = wingspan
    self.__capacity = capacity</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">from Vehicle import *

class Airplane(Vehicle):

  def __init__(self, name, wingspan, capacity):
    <mark style="background-color: green">super().__init__(name)</mark>
    self.__wingspan = wingspan
    self.__capacity = capacity</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">from Vehicle import *

class Airplane(Vehicle):

  def __init__(self, name, wingspan, capacity):
    super().__init__(name)
    self.__wingspan = wingspan
    self.__capacity = capacity</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">from Vehicle import *

class Airplane(Vehicle):

  def __init__(self, name, wingspan, capacity):
    super().__init__(name)
    self.__wingspan = wingspan
    self.__capacity = capacity

  def __landing_gear(self, set):
    if set:
      print("Landing gear down")
    else:
      print("Landing gear up")
</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">from Vehicle import *

class Airplane(Vehicle):

  def __init__(self, name, wingspan, capacity):
    super().__init__(name)
    self.__wingspan = wingspan
    self.__capacity = capacity

  def __landing_gear(self, set):
    if set:
      print("Landing gear down")
    else:
      print("Landing gear up")

  def move(self, distance):
    self.__landing_gear(False)
    print("Moving")
    self.__landing_gear(True)
    return distance / self.speed
</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">from Vehicle import *

class Airplane(Vehicle):

  def __init__(self, name, wingspan, capacity):
    super().__init__(name)
    self.__wingspan = wingspan
    self.__capacity = capacity

  def __landing_gear(self, set):
    if set:
      print("Landing gear down")
    else:
      print("Landing gear up")

  <mark>def move(self, distance):</mark>
    self.__landing_gear(False)
    print("Moving")
    self.__landing_gear(True)
    return distance / self.speed
</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">from Vehicle import *

class Airplane(Vehicle):

  def __init__(self, name, wingspan, capacity):
    super().__init__(name)
    self.__wingspan = wingspan
    self.__capacity = capacity

  def __landing_gear(self, set):
    if set:
      print("Landing gear down")
    else:
      print("Landing gear up")

  def move(self, distance):
    self.__landing_gear(False)
    print("Moving")
    self.__landing_gear(True)
    return distance / self.speed

  <mark>def describe(self):</mark>
    return "I am an airplane with a wingspan of {}
          and capacity {}".format(self.__wingspan,
          self.__capacity)
</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="python">from Vehicle import *

class Airplane(Vehicle):

  def __init__(self, name, wingspan, capacity):
    super().__init__(name)
    self.__wingspan = wingspan
    self.__capacity = capacity

  def __landing_gear(self, set):
    if set:
      print("Landing gear down")
    else:
      print("Landing gear up")

  def move(self, distance):
    self.__landing_gear(False)
    print("Moving")
    self.__landing_gear(True)
    return distance / self.speed

  def describe(self):
    return "I am an airplane with a wingspan of {}
          and capacity {}".format(self.__wingspan,
          self.__capacity)
</code></pre>
  </div>
</section>






<section>
  <pre class="stretch" style="font-size: .37em"><code class="python">from Vehicle import *
from Airplane import *

class Main:

  @staticmethod
  def main():
    vehicle = Vehicle("Boat")
    airplane = Airplane("Plane", 175, 53)
    print(vehicle.move(10))
    print(airplane.move(10))
    print(vehicle.describe())
    print(airplane.describe())

# main guard
if __name__ == "__main__":
  Main.main()
</code></pre>
<img class="plain" style="width: 100%" src="/images/12.7.p.2.test.png">
</section>



<section>
  <pre class="stretch" style="font-size: .37em"><code class="python">from Vehicle import *
from Airplane import *

class Main:

  @staticmethod
  def main():
    vehicle = Vehicle("Boat")
    airplane = Airplane("Plane", 175, 53)
    print(vehicle.move(10))
    print(airplane.move(10))
    print(vehicle.describe())
    print(airplane.describe())

# main guard
if __name__ == "__main__":
  Main.main()
</code></pre><pre class="" style="font-size: .54em"><code class="md">Moving
10.0
Landing gear up
Moving
Landing gear down
10.0

I am an airplane with a wingspan of 175 and capacity 53</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .37em"><code class="python">from Vehicle import *
from Airplane import *

class Main:

  @staticmethod
  def main():
    vehicle = Vehicle("Boat")
    airplane = Airplane("Plane", 175, 53)
    print(<mark>vehicle.move(10)</mark>)
    print(airplane.move(10))
    print(vehicle.describe())
    print(airplane.describe())

# main guard
if __name__ == "__main__":
  Main.main()
</code></pre><pre class="" style="font-size: .54em"><code class="md"><mark>Moving</mark>
10.0
Landing gear up
Moving
Landing gear down
10.0

I am an airplane with a wingspan of 175 and capacity 53</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .37em"><code class="python">from Vehicle import *
from Airplane import *

class Main:

  @staticmethod
  def main():
    vehicle = Vehicle("Boat")
    airplane = Airplane("Plane", 175, 53)
    <mark>print(vehicle.move(10))</mark>
    print(airplane.move(10))
    print(vehicle.describe())
    print(airplane.describe())

# main guard
if __name__ == "__main__":
  Main.main()
</code></pre><pre class="" style="font-size: .54em"><code class="md">Moving
<mark>10.0</mark>
Landing gear up
Moving
Landing gear down
10.0

I am an airplane with a wingspan of 175 and capacity 53</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .37em"><code class="python">from Vehicle import *
from Airplane import *

class Main:

  @staticmethod
  def main():
    vehicle = Vehicle("Boat")
    airplane = Airplane("Plane", 175, 53)
    print(vehicle.move(10))
    print(<mark>airplane.move(10)</mark>)
    print(vehicle.describe())
    print(airplane.describe())

# main guard
if __name__ == "__main__":
  Main.main()
</code></pre><pre class="" style="font-size: .54em"><code class="md">Moving
10.0
<mark>Landing gear up
Moving
Landing gear down</mark>
10.0

I am an airplane with a wingspan of 175 and capacity 53</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .37em"><code class="python">from Vehicle import *
from Airplane import *

class Main:

  @staticmethod
  def main():
    vehicle = Vehicle("Boat")
    airplane = Airplane("Plane", 175, 53)
    print(vehicle.move(10))
    <mark>print(airplane.move(10))</mark>
    print(vehicle.describe())
    print(airplane.describe())

# main guard
if __name__ == "__main__":
  Main.main()
</code></pre><pre class="" style="font-size: .54em"><code class="md">Moving
10.0
Landing gear up
Moving
Landing gear down
<mark>10.0</mark>

I am an airplane with a wingspan of 175 and capacity 53</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .37em"><code class="python">from Vehicle import *
from Airplane import *

class Main:

  @staticmethod
  def main():
    vehicle = Vehicle("Boat")
    airplane = Airplane("Plane", 175, 53)
    print(vehicle.move(10))
    print(airplane.move(10))
    <mark>print(vehicle.describe())</mark>
    print(airplane.describe())

# main guard
if __name__ == "__main__":
  Main.main()
</code></pre><pre class="" style="font-size: .54em"><code class="md">Moving
10.0
Landing gear up
Moving
Landing gear down
10.0
<mark> </mark>
I am an airplane with a wingspan of 175 and capacity 53</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .37em"><code class="python">from Vehicle import *
from Airplane import *

class Main:

  @staticmethod
  def main():
    vehicle = Vehicle("Boat")
    airplane = Airplane("Plane", 175, 53)
    print(vehicle.move(10))
    print(airplane.move(10))
    print(vehicle.describe())
    <mark>print(airplane.describe())</mark>

# main guard
if __name__ == "__main__":
  Main.main()
</code></pre><pre class="" style="font-size: .54em"><code class="md">Moving
10.0
Landing gear up
Moving
Landing gear down
10.0

<mark>I am an airplane with a wingspan of 175 and capacity 53</mark></code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .37em"><code class="python">from Vehicle import *
from Airplane import *

class Main:

  @staticmethod
  def main():
    vehicle = Vehicle("Boat")
    airplane = Airplane("Plane", 175, 53)
    print(vehicle.move(10))
    print(airplane.move(10))
    print(vehicle.describe())
    print(airplane.describe())

# main guard
if __name__ == "__main__":
  Main.main()
</code></pre><pre class="" style="font-size: .54em"><code class="md">Moving
10.0
Landing gear up
Moving
Landing gear down
10.0

I am an airplane with a wingspan of 175 and capacity 53</code></pre>
</section>




<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.p.mv.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">from Vehicle import *

class MotorVehicle(Vehicle):

  def __init__(self, name):
    super().__init__(name)
    self.number_of_wheels = 2
    self.engine_volume = 125

  def honk_horn():
    return ""</code></pre>
  </div>
</section>
