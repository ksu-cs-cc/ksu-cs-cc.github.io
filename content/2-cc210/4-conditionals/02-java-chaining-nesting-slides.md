---
type: "reveal"
hidden: true
---

<section>
  <img class="stretch plain" src="/images/chaining1.png">
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch"><code class="java">
    </code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining1.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch"><code class="java">
    </code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining2.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch"><code class="java"><mark>public static void main(String[] args){

}</mark></code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining2.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch"><code class="java">public static void main(String[] args){

}</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining3.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch"><code class="java">public static void main(String[] args){
  <mark>int x = 3;</mark>
}</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining3.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch"><code class="java">public static void main(String[] args){
  int x = 3;
}</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining4.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch"><code class="java">public static void main(String[] args){
  int x = 3;
  <mark>if(x < 0){

  }</mark>
}</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining4.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){

  }
}</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining5.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    <mark>System.out.println(-1);</mark>
  }
}</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining5.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    System.out.println(-1);
  }
}</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining6.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    System.out.println(-1);
  }
  <mark>if(x == 0){
    System.out.println(0);
  }</mark>
}</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining6.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    System.out.println(-1);
  }
  if(x == 0){
    System.out.println(0);
  }
}</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining7.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    System.out.println(-1);
  }
  if(x == 0){
    System.out.println(0);
  }
  <mark>if(x > 0){
    System.out.println(1);
  }</mark>
}</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining7.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    System.out.println(-1);
  }
  if(x == 0){
    System.out.println(0);
  }
  if(x > 0){
    System.out.println(1);
  }
}</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining1.png">
  </div>
</section>
<section>
  <img class="stretch plain" src="/images/nesting1.png">
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch"><code class="java">
    </code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting2.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch"><code class="java">
    </code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting3.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.45em"><code class="java"><mark>public static void main(String[] args){
  int x = 3;
}</mark></code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting3.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.45em"><code class="java">public static void main(String[] args){
  int x = 3;
}</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting4.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.45em"><code class="java">public static void main(String[] args){
  int x = 3;
  <mark>if(x < 0){

  }else{

  }</mark>
}</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting4.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.45em"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){

  }else{

  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting5.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.45em"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    <mark>System.out.println(-1);</mark>
  }else{

  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting5.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.45em"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    System.out.println(-1);
  }else{

  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting6.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.45em"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    System.out.println(-1);
  }else{
    <mark>if(x == 0){

    }else{

    }</mark>
  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting6.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.45em"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    System.out.println(-1);
  }else{
    if(x == 0){

    }else{

    }
  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting7.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.45em"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    System.out.println(-1);
  }else{
    if(x == 0){
      <mark>System.out.println(0);</mark>
    }else{
      <mark>System.out.println(1);</mark>
    }
  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting7.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.45em"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    System.out.println(-1);
  }else{
    if(x == 0){
      System.out.println(0);
    }else{
      System.out.println(1);
    }
  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting2.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.45em"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    System.out.println(-1);
  }else <mark>if(x == 0){
    System.out.println(0);
  }else if(x > 0){
    System.out.println(1);
  }</mark>
}</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting2.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.45em"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    System.out.println(-1);
  }else if(x == 0){
    System.out.println(0);
  }else if(x > 0){
    System.out.println(1);
  }<mark>else{
    //this should never happen
    System.out.println("ERROR!");
  }</mark>
}</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting2.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.45em"><code class="java">public static void main(String[] args){
  int x = 3;
  if(x < 0){
    System.out.println(-1);
  }else if(x == 0){
    System.out.println(0);
  }else if(x > 0){
    System.out.println(1);
  }else{
    //this should never happen
    System.out.println("ERROR!");
  }
}</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting2.png">
  </div>
</section>
