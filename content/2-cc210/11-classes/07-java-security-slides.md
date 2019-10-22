---
type: "reveal"
hidden: true
---

<section>
  <div style="float: right; width: 50%">
    <img class="plain" style="width: 100%" src="/images/11.6.j.6.secureuml.secure.png">
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .5em"><code class="java">public class Security{
  String name;
  int secret;

  Security(){
    this.reset();
  }

  int count(){
    return name.length();
  }

  void reset(){
    this.name = "test";
    this.secret = 123;
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <img class="plain" style="width: 100%" src="/images/11.6.j.6.secureuml.secure.png">
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .5em"><code class="java">public class Security{
  <mark>public</mark> String name;
  int secret;

  <mark>public</mark> Security(){
    this.reset();
  }

  <mark>public</mark> int count(){
    return name.length();
  }

  void reset(){
    this.name = "test";
    this.secret = 123;
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <img class="plain" style="width: 100%" src="/images/11.6.j.6.secureuml.secure.png">
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .5em"><code class="java">public class Security{
  public String name;
  <mark>private</mark> int secret;

  public Security(){
    this.reset();
  }

  public int count(){
    return name.length();
  }

  <mark>private</mark> void reset(){
    this.name = "test";
    this.secret = 123;
  }
}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 50%">
    <img class="plain" style="width: 100%" src="/images/11.6.j.6.secureuml.secure.png">
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .5em"><code class="java">public class Security{
  public String name;
  private int secret;

  public Security(){
    this.reset();
  }

  public int count(){
    return name.length();
  }

  private void reset(){
    this.name = "test";
    this.secret = 123;
  }
}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Main{
  public static void main(String[] args){

  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Security{
  public String name;
  private int secret;

  public Security(){
    this.reset();
  }

  public int count(){
    return name.length();
  }

  private void reset(){
    this.name = "test";
    this.secret = 123;
  }
}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Main{
  public static void main(String[] args){
    <mark>Security someSecurity = new Security();</mark>
  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Security{
  public String name;
  private int secret;

  public Security(){
    this.reset();
  }

  public int count(){
    return name.length();
  }

  private void reset(){
    this.name = "test";
    this.secret = 123;
  }
}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Main{
  public static void main(String[] args){
    Security someSecurity = new Security();
    <mark>System.out.println(someSecurity.name);</mark>
  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Security{
  public String name;
  private int secret;

  public Security(){
    this.reset();
  }

  public int count(){
    return name.length();
  }

  private void reset(){
    this.name = "test";
    this.secret = 123;
  }
}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Main{
  public static void main(String[] args){
    Security someSecurity = new Security();
    System.out.println(someSecurity.name);
    <mark>System.out.println(someSecurity.count());</mark>
  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Security{
  public String name;
  private int secret;

  public Security(){
    this.reset();
  }

  public int count(){
    return name.length();
  }

  private void reset(){
    this.name = "test";
    this.secret = 123;
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Main{
  public static void main(String[] args){
    Security someSecurity = new Security();
    System.out.println(someSecurity.name);
    System.out.println(someSecurity.count());
    <mark>System.out.println(someSecurity.secret);</mark>
  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Security{
  public String name;
  private int secret;

  public Security(){
    this.reset();
  }

  public int count(){
    return name.length();
  }

  private void reset(){
    this.name = "test";
    this.secret = 123;
  }
}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Main{
  public static void main(String[] args){
    Security someSecurity = new Security();
    System.out.println(someSecurity.name);
    System.out.println(someSecurity.count());
    <mark>System.out.println(<mark style="background-color: red">someSecurity.secret</mark>);</mark>
  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Security{
  public String name;
  private int secret;

  public Security(){
    this.reset();
  }

  public int count(){
    return name.length();
  }

  private void reset(){
    this.name = "test";
    this.secret = 123;
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Main{
  public static void main(String[] args){
    Security someSecurity = new Security();
    System.out.println(someSecurity.name);
    System.out.println(someSecurity.count());
    <s>System.out.println(someSecurity.secret);</s>
  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Security{
  public String name;
  private int secret;

  public Security(){
    this.reset();
  }

  public int count(){
    return name.length();
  }

  private void reset(){
    this.name = "test";
    this.secret = 123;
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Main{
  public static void main(String[] args){
    Security someSecurity = new Security();
    System.out.println(someSecurity.name);
    System.out.println(someSecurity.count());
    <s>System.out.println(someSecurity.secret);</s>
    <mark>someSecurity.reset();</mark>
  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Security{
  public String name;
  private int secret;

  public Security(){
    this.reset();
  }

  public int count(){
    return name.length();
  }

  private void reset(){
    this.name = "test";
    this.secret = 123;
  }
}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Main{
  public static void main(String[] args){
    Security someSecurity = new Security();
    System.out.println(someSecurity.name);
    System.out.println(someSecurity.count());
    <s>System.out.println(someSecurity.secret);</s>
    <mark style="background-color: red">someSecurity.reset();</mark>
  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Security{
  public String name;
  private int secret;

  public Security(){
    this.reset();
  }

  public int count(){
    return name.length();
  }

  private void reset(){
    this.name = "test";
    this.secret = 123;
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Main{
  public static void main(String[] args){
    Security someSecurity = new Security();
    System.out.println(someSecurity.name);
    System.out.println(someSecurity.count());
    <s>System.out.println(someSecurity.secret);</s>
    <s>someSecurity.reset();</s>
  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Security{
  public String name;
  private int secret;

  public Security(){
    this.reset();
  }

  public int count(){
    return name.length();
  }

  private void reset(){
    this.name = "test";
    this.secret = 123;
  }
}</code></pre>
  </div>
</section>
