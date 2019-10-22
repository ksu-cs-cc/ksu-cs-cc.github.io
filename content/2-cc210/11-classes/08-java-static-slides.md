---
type: "reveal"
hidden: true
---

<section>
  <div style="float: right; width: 50%">
    <img class="plain" style="width: 100%" src="/images/11.6.j.7.staticuml.stat.png">
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public int sum(int a){
    return x + a;
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <img class="plain" style="width: 100%" src="/images/11.6.j.7.staticuml.stat.png">
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public <mark>static</mark> int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public int sum(int a){
    return x + a;
  }
}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <img class="plain" style="width: 100%" src="/images/11.6.j.7.staticuml.stat.png">
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public <mark>static</mark> int sum(int a){
    return x + a;
  }
}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 50%">
    <img class="plain" style="width: 100%" src="/images/11.6.j.7.staticuml.stat.png">
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="java">public class Main{
 public static void main(String[] args){
   Stat someStat = new Stat(7);
   Stat anotherStat = new Stat(8);

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   someStat.x = 10;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   Stat.x = 25;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);
 }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="java">public class Main{
 public static void main(String[] args){
   <mark>Stat someStat = new Stat(7);</mark>
   Stat anotherStat = new Stat(8);

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   someStat.x = 10;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   Stat.x = 25;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);
 }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  <ul>
    <li>Stat.x = 5</li>
    <li>someStat.y = 7</li>
  </ul>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="java">public class Main{
 public static void main(String[] args){
   Stat someStat = new Stat(7);
   <mark>Stat anotherStat = new Stat(8);</mark>

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   someStat.x = 10;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   Stat.x = 25;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);
 }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  <ul>
    <li>Stat.x = 5</li>
    <li>someStat.y = 7</li>
    <li>anotherStat.y = 8</li>
  </ul>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="java">public class Main{
 public static void main(String[] args){
   Stat someStat = new Stat(7);
   Stat anotherStat = new Stat(8);

   <mark>System.out.println(someStat.x);</mark>
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   someStat.x = 10;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   Stat.x = 25;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);
 }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  <ul>
    <li>Stat.x = 5</li>
    <li>someStat.y = 7</li>
    <li>anotherStat.y = 8</li>
  </ul>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="java">public class Main{
 public static void main(String[] args){
   Stat someStat = new Stat(7);
   Stat anotherStat = new Stat(8);

   <mark>System.out.println(someStat.x);</mark>
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   someStat.x = 10;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   Stat.x = 25;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);
 }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  <ul>
    <li><mark>Stat.x = 5</mark></li>
    <li>someStat.y = 7</li>
    <li>anotherStat.y = 8</li>
  </ul>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="java">public class Main{
 public static void main(String[] args){
   Stat someStat = new Stat(7);
   Stat anotherStat = new Stat(8);

   System.out.println(someStat.x);
   <mark>System.out.println(someStat.y);</mark>
   <mark>System.out.println(anotherStat.x);</mark>
   <mark>System.out.println(anotherStat.y);</mark>

   someStat.x = 10;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   Stat.x = 25;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);
 }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  <ul>
    <li>Stat.x = 5</li>
    <li>someStat.y = 7</li>
    <li>anotherStat.y = 8</li>
  </ul>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="java">public class Main{
 public static void main(String[] args){
   Stat someStat = new Stat(7);
   Stat anotherStat = new Stat(8);

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   <mark>someStat.x = 10;</mark>

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   Stat.x = 25;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);
 }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  <ul>
    <li>Stat.x = 5</li>
    <li>someStat.y = 7</li>
    <li>anotherStat.y = 8</li>
  </ul>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="java">public class Main{
 public static void main(String[] args){
   Stat someStat = new Stat(7);
   Stat anotherStat = new Stat(8);

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   <mark>someStat.x = 10;</mark>

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   Stat.x = 25;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);
 }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  <ul>
    <li><mark>Stat.x = 10</mark></li>
    <li>someStat.y = 7</li>
    <li>anotherStat.y = 8</li>
  </ul>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="java">public class Main{
 public static void main(String[] args){
   Stat someStat = new Stat(7);
   Stat anotherStat = new Stat(8);

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   someStat.x = 10;

   <mark>System.out.println(someStat.x);</mark>
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   Stat.x = 25;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);
 }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  <ul>
    <li><mark>Stat.x = 10</mark></li>
    <li>someStat.y = 7</li>
    <li>anotherStat.y = 8</li>
  </ul>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="java">public class Main{
 public static void main(String[] args){
   Stat someStat = new Stat(7);
   Stat anotherStat = new Stat(8);

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   someStat.x = 10;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   <mark>System.out.println(anotherStat.x);</mark>
   System.out.println(anotherStat.y);

   Stat.x = 25;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);
 }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  <ul>
    <li><mark>Stat.x = 10</mark></li>
    <li>someStat.y = 7</li>
    <li>anotherStat.y = 8</li>
  </ul>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="java">public class Main{
 public static void main(String[] args){
   Stat someStat = new Stat(7);
   Stat anotherStat = new Stat(8);

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   someStat.x = 10;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   <mark>Stat.x = 25;</mark>

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);
 }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  <ul>
    <li>Stat.x = 10</li>
    <li>someStat.y = 7</li>
    <li>anotherStat.y = 8</li>
  </ul>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="java">public class Main{
 public static void main(String[] args){
   Stat someStat = new Stat(7);
   Stat anotherStat = new Stat(8);

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   someStat.x = 10;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   <mark>Stat.x = 25;</mark>

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);
 }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  <ul>
    <li><mark>Stat.x = 25</mark></li>
    <li>someStat.y = 7</li>
    <li>anotherStat.y = 8</li>
  </ul>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="java">public class Main{
 public static void main(String[] args){
   Stat someStat = new Stat(7);
   Stat anotherStat = new Stat(8);

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   someStat.x = 10;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   Stat.x = 25;

   <mark>System.out.println(someStat.x);</mark>
   System.out.println(someStat.y);
   <mark>System.out.println(anotherStat.x);</mark>
   System.out.println(anotherStat.y);
 }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  <ul>
    <li><mark>Stat.x = 25</mark></li>
    <li>someStat.y = 7</li>
    <li>anotherStat.y = 8</li>
  </ul>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="java">public class Main{
 public static void main(String[] args){
   Stat someStat = new Stat(7);
   Stat anotherStat = new Stat(8);

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   someStat.x = 10;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);

   Stat.x = 25;

   System.out.println(someStat.x);
   System.out.println(someStat.y);
   System.out.println(anotherStat.x);
   System.out.println(anotherStat.y);
 }
}</code></pre>
  </div>
  <div style="width: 50%">
    <pre class="stretch" style="font-size: .49em"><code class="java">public class Stat{
  public static int x = 5;
  public int y;

  public Stat(int an_y){
    this.y = an_y;
  }

  public static int sum(int a){
    return x + a;
  }
}</code></pre>
  <ul>
    <li>Stat.x = 25</li>
    <li>someStat.y = 7</li>
    <li>anotherStat.y = 8</li>
  </ul>
  </div>
</section>
