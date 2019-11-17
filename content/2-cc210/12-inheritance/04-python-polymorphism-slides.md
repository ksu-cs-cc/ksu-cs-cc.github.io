---
type: "reveal"
hidden: true
---

<section>
    <img class="plain stretch" style="" src="/images/12.7.p.uml.png">
</section>

<section>
  <pre class="stretch" style="font-size: .33em"><code class="python">from Car import *
from Airplane import *

class Main:

  @staticmethod
  def main():
    plane = Airplane("Plane", 123, 45)
    print(plane.name)
    print(plane.describe())
    print(plane.move(10))

    car = Car("Car", 4)
    print(car.name)
    print(car.describe())
    print(car.move(10))

# main guard
if __name__ == "__main__":
  Main.main() </code></pre>
  <img class="plain" style="height: 350px" src="/images/12.7.p.4.test1.png">
</section>

<section>
  <pre class="stretch" style="font-size: .4em"><code class="python">class Main:

  @staticmethod
  def main():
    plane = Airplane("Plane", 123, 45)
    print(plane.name)
    print(plane.describe())
    print(plane.move(10))

    car = Car("Car", 4)
    print(car.name)
    print(car.describe())
    print(car.move(10))
</code></pre>
<pre class="" style="font-size: .45em; height: 400px"><code style="height: 450px" class="md">Plane
I am an airplane with a wingspan of 123 and capacity 45
Landing gear up
Moving
Landing gear down
10.0
Car
I'm a sedan
Moving
10.0</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .4em"><code class="python">class Main:

  @staticmethod
  def main():
    <mark>plane = Airplane("Plane", 123, 45)</mark>
    print(plane.name)
    print(plane.describe())
    print(plane.move(10))

    car = Car("Car", 4)
    print(car.name)
    print(car.describe())
    print(car.move(10))
</code></pre>
<pre class="" style="font-size: .45em; height: 400px"><code style="height: 450px" class="md">Plane
I am an airplane with a wingspan of 123 and capacity 45
Landing gear up
Moving
Landing gear down
10.0
Car
I'm a sedan
Moving
10.0</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .4em"><code class="python">class Main:

  @staticmethod
  def main():
    plane = Airplane("Plane", 123, 45)
    <mark>print(plane.name)</mark>
    print(plane.describe())
    print(plane.move(10))

    car = Car("Car", 4)
    print(car.name)
    print(car.describe())
    print(car.move(10))
</code></pre>
<pre class="" style="font-size: .45em; height: 400px"><code style="height: 450px" class="md"><mark>Plane</mark>
I am an airplane with a wingspan of 123 and capacity 45
Landing gear up
Moving
Landing gear down
10.0
Car
I'm a sedan
Moving
10.0</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .4em"><code class="python">class Main:

  @staticmethod
  def main():
    plane = Airplane("Plane", 123, 45)
    print(plane.name)
    <mark>print(plane.describe())</mark>
    print(plane.move(10))

    car = Car("Car", 4)
    print(car.name)
    print(car.describe())
    print(car.move(10))
</code></pre>
<pre class="" style="font-size: .45em; height: 400px"><code style="height: 450px" class="md">Plane
<mark>I am an airplane with a wingspan of 123 and capacity 45</mark>
Landing gear up
Moving
Landing gear down
10.0
Car
I'm a sedan
Moving
10.0</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .4em"><code class="python">class Main:

  @staticmethod
  def main():
    plane = Airplane("Plane", 123, 45)
    print(plane.name)
    print(plane.describe())
    <mark>print(plane.move(10))</mark>

    car = Car("Car", 4)
    print(car.name)
    print(car.describe())
    print(car.move(10))
</code></pre>
<pre class="" style="font-size: .45em; height: 400px"><code style="height: 450px" class="md">Plane
I am an airplane with a wingspan of 123 and capacity 45
<mark>Landing gear up
Moving
Landing gear down
10.0</mark>
Car
I'm a sedan
Moving
10.0</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .4em"><code class="python">class Main:

  @staticmethod
  def main():
    plane = Airplane("Plane", 123, 45)
    print(plane.name)
    print(plane.describe())
    print(plane.move(10))

    <mark>car = Car("Car", 4)</mark>
    print(car.name)
    print(car.describe())
    print(car.move(10))
</code></pre>
<pre class="" style="font-size: .45em; height: 400px"><code style="height: 450px" class="md">Plane
I am an airplane with a wingspan of 123 and capacity 45
Landing gear up
Moving
Landing gear down
10.0
Car
I'm a sedan
Moving
10.0</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .4em"><code class="python">class Main:

  @staticmethod
  def main():
    plane = Airplane("Plane", 123, 45)
    print(plane.name)
    print(plane.describe())
    print(plane.move(10))

    car = Car("Car", 4)
    <mark>print(car.name)</mark>
    print(car.describe())
    print(car.move(10))
</code></pre>
<pre class="" style="font-size: .45em; height: 400px"><code style="height: 450px" class="md">Plane
I am an airplane with a wingspan of 123 and capacity 45
Landing gear up
Moving
Landing gear down
10.0
<mark>Car</mark>
I'm a sedan
Moving
10.0</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .4em"><code class="python">class Main:

  @staticmethod
  def main():
    plane = Airplane("Plane", 123, 45)
    print(plane.name)
    print(plane.describe())
    print(plane.move(10))

    car = Car("Car", 4)
    print(car.name)
    <mark>print(car.describe())</mark>
    print(car.move(10))
</code></pre>
<pre class="" style="font-size: .45em; height: 400px"><code style="height: 450px" class="md">Plane
I am an airplane with a wingspan of 123 and capacity 45
Landing gear up
Moving
Landing gear down
10.0
Car
<mark>I'm a sedan</mark>
Moving
10.0</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .4em"><code class="python">class Main:

  @staticmethod
  def main():
    plane = Airplane("Plane", 123, 45)
    print(plane.name)
    print(plane.describe())
    print(plane.move(10))

    car = Car("Car", 4)
    print(car.name)
    print(car.describe())
    <mark>print(car.move(10))</mark>
</code></pre>
<pre class="" style="font-size: .45em; height: 400px"><code style="height: 450px" class="md">Plane
I am an airplane with a wingspan of 123 and capacity 45
Landing gear up
Moving
Landing gear down
10.0
Car
I'm a sedan
<mark>Moving
10.0</mark></code></pre>
</section>


<section>
  <pre class="" style="font-size: .4em"><code class="python">class Main:

  @staticmethod
  def main():
    car = Car("Car", 4)
    print(car.honk_horn())
</code></pre>
</section>


<section>
  <pre class="" style="font-size: .4em"><code class="python">class Main:

  @staticmethod
  def main():
    car = Car("Car", 4)
    print(<mark>car.honk_horn()</mark>)
</code></pre>
</section>


<section>
  <pre class="" style="font-size: .4em"><code class="python">class Main:

  @staticmethod
  def main():
    car = Car("Car", 4)
    print(car.honk_horn())
</code></pre>
  <img class="plain" style="height: 100px" src="/images/12.7.p.4.test2.png">
</section>

<section>
  <h3>Rules</h3>
  <ol>
    <li>Treat child class as any parent class</li>
    <li>Use attributes and methods based on object class and any parent classes</li>
    <li>Overriden methods will use code in child class</li>
  </ol>
</section>



<section>
  <pre class="stretch" style="font-size: .4em"><code class="python">class Main:

  @staticmethod
  def main():
    vehicles = []
    vehicles.append(Airplane("Plane", 123, 45))
    vehicles.append(Car("Car", 4))
    vehicles.append(Truck("Truck", 157))

    for v in vehicles:
      print(v.name)
      print(v.describe())
      print(v.move(10))</code></pre>
  <img class="plain" style="height: 450px" src="/images/12.7.p.4.test3.png">
</section>