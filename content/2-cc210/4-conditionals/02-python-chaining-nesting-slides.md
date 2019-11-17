---
type: "reveal"
hidden: true
---

<section>
  <img class="stretch plain" src="/images/chaining1.png">
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">
    </code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining1.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">

</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining3.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python"><mark>x = 3</mark>

</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining3.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3

</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining4.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
<mark>if x < 0:</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining4.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining5.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  <mark>print(-1)</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining5.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  print(-1)
</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining6.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  print(-1)
<mark>if x == 0:
  print(0)</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining6.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  print(-1)
if x == 0:
  print(0)
</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining7.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  print(-1)
if x == 0:
  print(0)
<mark>if x > 0:
  print(1)</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <img class="plain" src="/images/chaining7.png">
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  print(-1)
if x == 0:
  print(0)
if x > 0:
  print(1)
</code></pre>
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
    <pre class="stretch" style="font-size: 0.8em"><code class="python">
    </code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting2.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">
    </code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting3.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python"><mark>x = 3
</mark></code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting3.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting4.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
<mark>if x < 0:

else:</mark>

</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting4.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:

else:

</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting5.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  <mark>print(-1)</mark>
else:

</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting5.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  print(-1)
else:

</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting6.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  print(-1)
else:
  <mark>if x == 0:

  else:</mark>

</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting6.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  print(-1)
else:
  if x == 0:

  else:

</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting7.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  print(-1)
else:
  if x == 0:
    <mark>print(0)</mark>
  else:
    <mark>print(1)</mark></code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting7.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  print(-1)
else:
  if x == 0:
    print(0)
  else:
    print(1)</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting2.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  print(-1)
<mark>elif x == 0:
  print(0)
elif x > 0:
  print(1)</mark></code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting2.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  print(-1)
elif x == 0:
  print(0)
elif x > 0:
  print(1)
<mark>else:
  #impossible
  print("ERROR!")</mark>
</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting2.png">
  </div>
</section>
<section>
  <div style="float: right; width: 60%">
    <pre class="stretch" style="font-size: 0.8em"><code class="python">x = 3
if x < 0:
  print(-1)
elif x == 0:
  print(0)
elif x > 0:
  print(1)
else:
  #impossible
  print("ERROR!")
</code></pre>
  </div>
  <div style="width: 40%">
    <img class="plain" src="/images/nesting2.png">
  </div>
</section>