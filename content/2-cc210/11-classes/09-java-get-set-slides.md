---
type: "reveal"
hidden: true
---

<section>
  <div style="float: right; width: 50%">
    <img class="plain" style="width: 100%" src="/images/11.6.j.9.propertyuml.property.png">
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Property{
  private String name;

  public Property(){
    name = "";
  }

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <img class="plain" style="width: 100%" src="/images/11.6.j.9.propertyuml.property.png">
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Property{
  <mark>private</mark> String name;

  public Property(){
    name = "";
  }

}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <img class="plain" style="width: 100%" src="/images/11.6.j.9.propertyuml.property.png">
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Property{
  private String name;

  public Property(){
    name = "";
  }

  <mark>public String getName(){
    return name;
  }</mark>

}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <img class="plain" style="width: 100%" src="/images/11.6.j.9.propertyuml.property.png">
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Property{
  private String name;

  public Property(){
    name = "";
  }

  public String getName(){
    return name;
  }

  <mark>public void setName(String a_name){
    if(a_name.length() == 0){
      throw new IllegalArgumentException(
        "Name cannot be an empty string!");
    }
    this.name = a_name;
  }</mark>

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <img class="plain" style="width: 100%" src="/images/11.6.j.9.propertyuml.property.png">
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Property{
  private String name;

  public Property(){
    name = "";
  }

  public String <mark>getName</mark>(){
    return name;
  }

  public void <mark>setName</mark>(String a_name){
    if(a_name.length() == 0){
      throw new IllegalArgumentException(
        "Name cannot be an empty string!");
    }
    this.name = a_name;
  }

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <img class="plain" style="width: 100%" src="/images/11.6.j.9.propertyuml.property.png">
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Property{
  private String name;

  public Property(){
    name = "";
  }

  public String getName(){
    return name;
  }

  public void setName(String a_name){
    if(a_name.length() == 0){
      throw new IllegalArgumentException(
        "Name cannot be an empty string!");
    }
    this.name = a_name;
  }

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Main{
  public static void main(String[] args){
    Property prop = new Property();
    String name = prop.getName();
    System.out.println(name);
    prop.setName("test");
    System.out.println(prop.getName());
  }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Property{
  private String name;

  public Property(){
    name = "";
  }

  public String getName(){
    return name;
  }

  public void setName(String a_name){
    if(a_name.length() == 0){
      throw new IllegalArgumentException(
        "Name cannot be an empty string!");
    }
    this.name = a_name;
  }

}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Main{
  public static void main(String[] args){
    Property prop = new Property();
    String name = <mark>prop.getName()</mark>;
    System.out.println(name);
    prop.setName("test");
    System.out.println(prop.getName());
  }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Property{
  private String name;

  public Property(){
    name = "";
  }

  public String getName(){
    return name;
  }

  public void setName(String a_name){
    if(a_name.length() == 0){
      throw new IllegalArgumentException(
        "Name cannot be an empty string!");
    }
    this.name = a_name;
  }

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Main{
  public static void main(String[] args){
    Property prop = new Property();
    String name = prop.getName();
    System.out.println(name);
    <mark>prop.setName("test")</mark>;
    System.out.println(prop.getName());
  }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Property{
  private String name;

  public Property(){
    name = "";
  }

  public String getName(){
    return name;
  }

  public void setName(String a_name){
    if(a_name.length() == 0){
      throw new IllegalArgumentException(
        "Name cannot be an empty string!");
    }
    this.name = a_name;
  }

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Main{
  public static void main(String[] args){
    Property prop = new Property();
    String name = prop.getName();
    System.out.println(name);
    prop.setName("test");
    System.out.println(<mark>prop.getName()</mark>);
  }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Property{
  private String name;

  public Property(){
    name = "";
  }

  public String getName(){
    return name;
  }

  public void setName(String a_name){
    if(a_name.length() == 0){
      throw new IllegalArgumentException(
        "Name cannot be an empty string!");
    }
    this.name = a_name;
  }

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Main{
  public static void main(String[] args){
    Property prop = new Property();
    String name = prop.getName();
    System.out.println(name);
    prop.setName("test");
    System.out.println(prop.getName());
  }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public class Property{
  private String name;

  public Property(){
    name = "";
  }

  public String getName(){
    return name;
  }

  public void setName(String a_name){
    if(a_name.length() == 0){
      throw new IllegalArgumentException(
        "Name cannot be an empty string!");
    }
    this.name = a_name;
  }

}</code></pre>
  </div>
</section>
