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

  <mark>private</mark> String name;
  public double speed;

  public String getName(){ return this.name; }

  <mark>public</mark> Vehicle(String name){
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

  <mark>protected</mark> String name;
  public double speed;

  public String getName(){ return this.name; }

  <mark>protected</mark> Vehicle(String name){
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

  protected String name;
  public double speed;

  public String getName(){ return this.name; }

  protected Vehicle(String name){
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
    <pre class="stretch" style="font-size: .4em"><code class="java">public <mark>abstract</mark> class Vehicle{

  protected String name;
  public double speed;

  public String getName(){ return this.name; }

  protected Vehicle(String name){
    this.name = name;
    this.speed = 1.0;
  }

  public double move(double distance){
    System.out.println("Moving");
    return distance / this.speed;
  }

  public <mark>abstract</mark> String describe(){
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
    <pre class="stretch" style="font-size: .4em"><code class="java">public abstract class Vehicle{

  protected String name;
  public double speed;

  public String getName(){ return this.name; }

  protected Vehicle(String name){
    this.name = name;
    this.speed = 1.0;
  }

  public double move(double distance){
    System.out.println("Moving");
    return distance / this.speed;
  }

  public abstract String describe()<mark>{
    return "";
  }</mark>

}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.vehicle.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public abstract class Vehicle{

  protected String name;
  public double speed;

  public String getName(){ return this.name; }

  protected Vehicle(String name){
    this.name = name;
    this.speed = 1.0;
  }

  public double move(double distance){
    System.out.println("Moving");
    return distance / this.speed;
  }

  public abstract String describe()<mark>;</mark>

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/12.7.j.vehicle.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public abstract class Vehicle{

  protected String name;
  public double speed;

  public String getName(){ return this.name; }

  protected Vehicle(String name){
    this.name = name;
    this.speed = 1.0;
  }

  public double move(double distance){
    System.out.println("Moving");
    return distance / this.speed;
  }

  public abstract String describe();

}</code></pre>
  </div>
</section>
