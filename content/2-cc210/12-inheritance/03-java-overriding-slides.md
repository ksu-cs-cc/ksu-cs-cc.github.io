---
type: "reveal"
hidden: true
---

<section>
    <img class="plain stretch" style="" src="/images/12.7.j.uml.png">
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.vehicle.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Vehicle{

  private String name;
  public double speed;

  public String getName(){ return this.name; }

  public Vehicle(String name){
    this.name = name;
    this.speed = 1.0;
  }

  public double move(double distance){
    System.out.println("Moving");
    return distance / this.speed;
  }

  public String describe(){
    return "";
  }

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.vehicle.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Vehicle{

  private String name;
  public double speed;

  public String getName(){ return this.name; }

  <mark>public Vehicle(String name){
    this.name = name;
    this.speed = 1.0;
  }</mark>

  public double move(double distance){
    System.out.println("Moving");
    return distance / this.speed;
  }

  public String describe(){
    return "";
  }

}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.vehicle.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Vehicle{

  private String name;
  public double speed;

  public String getName(){ return this.name; }

  public Vehicle(String name){
    this.name = name;
    this.speed = 1.0;
  }

  <mark>public double move(double distance){
    System.out.println("Moving");
    return distance / this.speed;
  }</mark>

  <mark>public String describe(){
    return "";
  }</mark>

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .34em"><code class="java">public class Airplane extends Vehicle{

  private double wingspan;
  private int capacity;

  public Airplane(String name, double wingspan, int capacity){
    this.name = name;
    this.wingspan = wingspan;
    this.capacity = capacity;
  }
}</code></pre>
  </div>
</section>

<section>
    <img class="plain stretch" style="" src="/images/12.7.j.2.error.png">
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .34em"><code class="java">public class Airplane extends Vehicle{

  private double wingspan;
  private int capacity;

  public Airplane(String name, double wingspan, int capacity){
    <mark style="background-color: red">this.name = name;</mark>
    this.wingspan = wingspan;
    this.capacity = capacity;
  }
}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.vehicle.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Vehicle{

  private String name;
  public double speed;

  public String getName(){ return this.name; }

  <mark>public Vehicle(String name){
    this.name = name;
    this.speed = 1.0;
  }</mark>

  public double move(double distance){
    System.out.println("Moving");
    return distance / this.speed;
  }

  public String describe(){
    return "";
  }

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .34em"><code class="java">public class Airplane extends Vehicle{

  private double wingspan;
  private int capacity;

  public Airplane(String name, double wingspan, int capacity){
    <mark style="background-color: red">this.name = name;</mark>
    this.wingspan = wingspan;
    this.capacity = capacity;
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .34em"><code class="java">public class Airplane extends Vehicle{

  private double wingspan;
  private int capacity;

  public Airplane(String name, double wingspan, int capacity){
    <mark style="background-color: green">super(name);</mark>
    this.wingspan = wingspan;
    this.capacity = capacity;
  }
}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .34em"><code class="java">public class Airplane extends Vehicle{

  private double wingspan;
  private int capacity;

  public Airplane(String name, double wingspan, int capacity){
    this.wingspan = wingspan;
    <mark style="background-color: red">super(name);</mark>
    this.capacity = capacity;
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .34em"><code class="java">public class Airplane extends Vehicle{

  private double wingspan;
  private int capacity;

  public Airplane(String name, double wingspan, int capacity){
    this.wingspan = wingspan;
    <s><mark style="background-color: red">super(name);</mark></s>
    this.capacity = capacity;
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .34em"><code class="java">public class Airplane extends Vehicle{

  private double wingspan;
  private int capacity;

  public Airplane(String name, double wingspan, int capacity){
    <mark style="background-color: green">super(name);</mark>
    this.wingspan = wingspan;
    this.capacity = capacity;
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .34em"><code class="java">public class Airplane extends Vehicle{

  private double wingspan;
  private int capacity;

  public Airplane(String name, double wingspan, int capacity){
    super(name);
    this.wingspan = wingspan;
    this.capacity = capacity;
  }
}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .34em"><code class="java">public class Airplane extends Vehicle{

  private double wingspan;
  private int capacity;

  public Airplane(String name, double wingspan, int capacity){
    super(name);
    this.wingspan = wingspan;
    this.capacity = capacity;
  }

  public void landing_gear(boolean set){
    if(set){
      System.out.println("Landing gear down");
    }else{
      System.out.println("Landing gear up");
    }
  }
}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .34em"><code class="java">public class Airplane extends Vehicle{

  private double wingspan;
  private int capacity;

  public Airplane(String name, double wingspan, int capacity){
    super(name);
    this.wingspan = wingspan;
    this.capacity = capacity;
  }

  public void landing_gear(boolean set){
    if(set){
      System.out.println("Landing gear down");
    }else{
      System.out.println("Landing gear up");
    }
  }

  @Override
  public double move(double distance){
    this.landing_gear(false);
    System.out.println("Moving");
    this.landing_gear(true);
    return distance / this.speed;
  }
}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .34em"><code class="java">public class Airplane extends Vehicle{

  private double wingspan;
  private int capacity;

  public Airplane(String name, double wingspan, int capacity){
    super(name);
    this.wingspan = wingspan;
    this.capacity = capacity;
  }

  public void landing_gear(boolean set){
    if(set){
      System.out.println("Landing gear down");
    }else{
      System.out.println("Landing gear up");
    }
  }

  @Override
  <mark>public double move(double distance){</mark>
    this.landing_gear(false);
    System.out.println("Moving");
    this.landing_gear(true);
    return distance / this.speed;
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .34em"><code class="java">public class Airplane extends Vehicle{

  private double wingspan;
  private int capacity;

  public Airplane(String name, double wingspan, int capacity){
    super(name);
    this.wingspan = wingspan;
    this.capacity = capacity;
  }

  public void landing_gear(boolean set){
    if(set){
      System.out.println("Landing gear down");
    }else{
      System.out.println("Landing gear up");
    }
  }

  <mark>@Override</mark>
  public double move(double distance){
    this.landing_gear(false);
    System.out.println("Moving");
    this.landing_gear(true);
    return distance / this.speed;
  }
}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .34em"><code class="java">public class Airplane extends Vehicle{

  private double wingspan;
  private int capacity;

  public Airplane(String name, double wingspan, int capacity){
    super(name);
    this.wingspan = wingspan;
    this.capacity = capacity;
  }

  public void landing_gear(boolean set){
    if(set){
      System.out.println("Landing gear down");
    }else{
      System.out.println("Landing gear up");
    }
  }

  @Override
  public double move(double distance){
    this.landing_gear(false);
    System.out.println("Moving");
    this.landing_gear(true);
    return distance / this.speed;
  }

  <mark>@Override
  public String describe(){</mark>
    return String.format("I am an airplane with a wingspan of
            %f and capacity %d", this.wingspan, this.capacity);
  }
}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.airplane.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .34em"><code class="java">public class Airplane extends Vehicle{

  private double wingspan;
  private int capacity;

  public Airplane(String name, double wingspan, int capacity){
    super(name);
    this.wingspan = wingspan;
    this.capacity = capacity;
  }

  public void landing_gear(boolean set){
    if(set){
      System.out.println("Landing gear down");
    }else{
      System.out.println("Landing gear up");
    }
  }

  @Override
  public double move(double distance){
    this.landing_gear(false);
    System.out.println("Moving");
    this.landing_gear(true);
    return distance / this.speed;
  }

  @Override
  public String describe(){
    return String.format("I am an airplane with a wingspan of
            %f and capacity %d", this.wingspan, this.capacity);
  }
}</code></pre>
  </div>
</section>

<section>
  <pre class="" style="font-size: .4em"><code class="java">public class Main{

  public static void main(String[] args){
    Vehicle vehicle = new Vehicle("Boat");
    Airplane airplane = new Airplane("Plane", 175, 53);
    System.out.println(vehicle.move(10));
    System.out.println(airplane.move(10));
    System.out.println(vehicle.describe());
    System.out.println(airplane.describe());
  }
}</code></pre>
<img class="plain" style="width: 100%" src="/images/12.7.j.2.test.png">

</section>


<section>
  <pre class="" style="font-size: .4em"><code class="java">public class Main{

  public static void main(String[] args){
    Vehicle vehicle = new Vehicle("Boat");
    Airplane airplane = new Airplane("Plane", 175, 53);
    System.out.println(vehicle.move(10));
    System.out.println(airplane.move(10));
    System.out.println(vehicle.describe());
    System.out.println(airplane.describe());
  }
}</code></pre>
  <pre class="" style="font-size: .4em"><code class="md">Moving
10.0
Landing gear up
Moving
Landing gear down
10.0

I am an airplane with a wingspan of 175.000000 and capacity 53</code></pre>
</section>

<section>
  <pre class="" style="font-size: .4em"><code class="java">public class Main{

  public static void main(String[] args){
    Vehicle vehicle = new Vehicle("Boat");
    Airplane airplane = new Airplane("Plane", 175, 53);
    System.out.println(<mark>vehicle.move(10)</mark>);
    System.out.println(airplane.move(10));
    System.out.println(vehicle.describe());
    System.out.println(airplane.describe());
  }
}</code></pre>
  <pre class="" style="font-size: .4em"><code class="md"><mark>Moving</mark>
10.0
Landing gear up
Moving
Landing gear down
10.0

I am an airplane with a wingspan of 175.000000 and capacity 53</code></pre>
</section>

<section>
  <pre class="" style="font-size: .4em"><code class="java">public class Main{

  public static void main(String[] args){
    Vehicle vehicle = new Vehicle("Boat");
    Airplane airplane = new Airplane("Plane", 175, 53);
    <mark>System.out.println(vehicle.move(10));</mark>
    System.out.println(airplane.move(10));
    System.out.println(vehicle.describe());
    System.out.println(airplane.describe());
  }
}</code></pre>
  <pre class="" style="font-size: .4em"><code class="md">Moving
<mark>10.0</mark>
Landing gear up
Moving
Landing gear down
10.0

I am an airplane with a wingspan of 175.000000 and capacity 53</code></pre>
</section>

<section>
  <pre class="" style="font-size: .4em"><code class="java">public class Main{

  public static void main(String[] args){
    Vehicle vehicle = new Vehicle("Boat");
    Airplane airplane = new Airplane("Plane", 175, 53);
    System.out.println(vehicle.move(10));
    System.out.println(<mark>airplane.move(10)</mark>);
    System.out.println(vehicle.describe());
    System.out.println(airplane.describe());
  }
}</code></pre>
  <pre class="" style="font-size: .4em"><code class="md">Moving
10.0
<mark>Landing gear up
Moving
Landing gear down</mark>
10.0

I am an airplane with a wingspan of 175.000000 and capacity 53</code></pre>
</section>

<section>
  <pre class="" style="font-size: .4em"><code class="java">public class Main{

  public static void main(String[] args){
    Vehicle vehicle = new Vehicle("Boat");
    Airplane airplane = new Airplane("Plane", 175, 53);
    System.out.println(vehicle.move(10));
    <mark>System.out.println(airplane.move(10));</mark>
    System.out.println(vehicle.describe());
    System.out.println(airplane.describe());
  }
}</code></pre>
  <pre class="" style="font-size: .4em"><code class="md">Moving
10.0
Landing gear up
Moving
Landing gear down
<mark>10.0</mark>

I am an airplane with a wingspan of 175.000000 and capacity 53</code></pre>
</section>

<section>
  <pre class="" style="font-size: .4em"><code class="java">public class Main{

  public static void main(String[] args){
    Vehicle vehicle = new Vehicle("Boat");
    Airplane airplane = new Airplane("Plane", 175, 53);
    System.out.println(vehicle.move(10));
    System.out.println(airplane.move(10));
    <mark>System.out.println(vehicle.describe());</mark>
    System.out.println(airplane.describe());
  }
}</code></pre>
  <pre class="" style="font-size: .4em"><code class="md">Moving
10.0
Landing gear up
Moving
Landing gear down
10.0
<mark> </mark>
I am an airplane with a wingspan of 175.000000 and capacity 53</code></pre>
</section>

<section>
  <pre class="" style="font-size: .4em"><code class="java">public class Main{

  public static void main(String[] args){
    Vehicle vehicle = new Vehicle("Boat");
    Airplane airplane = new Airplane("Plane", 175, 53);
    System.out.println(vehicle.move(10));
    System.out.println(airplane.move(10));
    System.out.println(vehicle.describe());
    <mark>System.out.println(airplane.describe());</mark>
  }
}</code></pre>
  <pre class="" style="font-size: .4em"><code class="md">Moving
10.0
Landing gear up
Moving
Landing gear down
10.0

<mark>I am an airplane with a wingspan of 175.000000 and capacity 53</mark></code></pre>
</section>

<section>
  <pre class="" style="font-size: .4em"><code class="java">public class Main{

  public static void main(String[] args){
    Vehicle vehicle = new Vehicle("Boat");
    Airplane airplane = new Airplane("Plane", 175, 53);
    System.out.println(vehicle.move(10));
    System.out.println(airplane.move(10));
    System.out.println(vehicle.describe());
    System.out.println(airplane.describe());
  }
}</code></pre>
  <pre class="" style="font-size: .4em"><code class="md">Moving
10.0
Landing gear up
Moving
Landing gear down
10.0

I am an airplane with a wingspan of 175.000000 and capacity 53</code></pre>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.mv.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class MotorVehicle extends Vehicle{

  public int number_of_wheels;
  public double engine_volume;

  public MotorVehicle(String name){
    super(name);
    this.number_of_wheels = 2;
    this.engine_volume = 125;
  }

  public String honk_horn(){
    return "";
  }
}</code></pre>
  </div>
</section>
