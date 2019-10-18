---
type: "reveal"
hidden: true
---

<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue1.png">
  <div style="float: left; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = 5
  y = addThree(x)
  print(x)
  print(y)

define addThree(x)
  x = x + 3
  return x
    </code></pre>
    </div>
</section>


<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue1.png">
  <div style="float: left; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  <mark>x = 5</mark>
  y = addThree(x)
  print(x)
  print(y)

define addThree(x)
  x = x + 3
  return x
    </code></pre>
    </div>
</section>


<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue2.png">
  <div style="float: left; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  <mark>x = 5</mark>
  y = addThree(x)
  print(x)
  print(y)

define addThree(x)
  x = x + 3
  return x
    </code></pre>
    </div>
</section>


<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue2.png">
  <div style="float: left; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = 5
  <mark>y = addThree(x)</mark>
  print(x)
  print(y)

define addThree(x)
  x = x + 3
  return x
    </code></pre>
    </div>
</section>


<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue3.png">
  <div style="float: left; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = 5
  <mark>y = addThree(x)</mark>
  print(x)
  print(y)

define addThree(x)
  x = x + 3
  return x
    </code></pre>
    </div>
</section>


<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue3.png">
  <div style="float: left; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = 5
  y = addThree(x)
  print(x)
  print(y)

<mark>define addThree(x)</mark>
  x = x + 3
  return x
    </code></pre>
    </div>
</section>



<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue4.png">
  <div style="float: left; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = 5
  y = addThree(x)
  print(x)
  print(y)

<mark>define addThree(x)</mark>
  x = x + 3
  return x
    </code></pre>
    </div>
</section>


<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue4.png">
  <div style="float: left; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = 5
  y = addThree(<mark>x</mark>)
  print(x)
  print(y)

define addThree(<mark>x</mark>)
  x = x + 3
  return x
    </code></pre>
    </div>
</section>


<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue5.png">
  <div style="float: left; width: 65%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = 5
  y = addThree(<mark>x</mark>)
  print(x)
  print(y)

define addThree(<mark>x</mark>)
  x = x + 3
  return x
    </code></pre>
    </div>
</section>



<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue5.png">
  <div style="float: left; width: 65%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = 5
  y = addThree(x)
  print(x)
  print(y)

define addThree(x)
  <mark>x = x + 3</mark>
  return x
    </code></pre>
    </div>
</section>



<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue6.png">
  <div style="float: left; width: 65%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = 5
  y = addThree(x)
  print(x)
  print(y)

define addThree(x)
  <mark>x = x + 3</mark>
  return x
    </code></pre>
    </div>
</section>



<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue6.png">
  <div style="float: left; width: 65%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = 5
  y = addThree(x)
  print(x)
  print(y)

define addThree(x)
  x = x + 3
  <mark>return x</mark>
    </code></pre>
    </div>
</section>



<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue7.png">
  <div style="float: left; width: 65%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = 5
  y = addThree(x)
  print(x)
  print(y)

define addThree(x)
  x = x + 3
  <mark>return x</mark>
    </code></pre>
    </div>
</section>


<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue7.png">
  <div style="float: left; width: 65%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = 5
  <mark>y = addThree(x)</mark>
  print(x)
  print(y)

define addThree(x)
  x = x + 3
  return x
    </code></pre>
    </div>
</section>

<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue8.png">
  <div style="float: left; width: 65%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = 5
  <mark>y = addThree(x)</mark>
  print(x)
  print(y)

define addThree(x)
  x = x + 3
  return x
    </code></pre>
    </div>
</section>


<section>
  <h3>Call by Value</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue8.png">
  <div style="float: left; width: 65%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = 5
  y = addThree(x)
  <mark>print(x)</mark>
  <mark>print(y)</mark>

define addThree(x)
  x = x + 3
  return x
    </code></pre>
    </div>
</section>



<section>
  <h3>Call by Reference</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue1.png">
  <div style="float: left; width: 65%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(x)
  print(x[0])
  print(x[1])

define changeLast(x)
  x[1] = 5
    </code></pre>
    </div>
</section>



<section>
  <h3>Call by Reference</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue1.png">
  <div style="float: left; width: 65%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  <mark>x = {1, 2}</mark>
  changeLast(x)
  print(x[0])
  print(x[1])

define changeLast(x)
  x[1] = 5
    </code></pre>
    </div>
</section>




<section>
  <h3>Call by Reference</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue9.png">
  <div style="float: left; width: 65%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  <mark>x = {1, 2}</mark>
  changeLast(x)
  print(x[0])
  print(x[1])

define changeLast(x)
  x[1] = 5
    </code></pre>
    </div>
</section>


<section>
  <h3>Call by Reference</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue10.png">
  <div style="float: left; width: 65%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  <mark>x = {1, 2}</mark>
  changeLast(x)
  print(x[0])
  print(x[1])

define changeLast(x)
  x[1] = 5
    </code></pre>
    </div>
</section>




<section>
  <h3>Call by Reference</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue10.png">
  <div style="float: left; width: 65%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  <mark>changeLast(x)</mark>
  print(x[0])
  print(x[1])

define changeLast(x)
  x[1] = 5
    </code></pre>
    </div>
</section>




<section>
  <h3>Call by Reference</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue10.png">
  <div style="float: left; width: 65%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(x)
  print(x[0])
  print(x[1])

<mark>define changeLast(x)</mark>
  x[1] = 5
    </code></pre>
    </div>
</section>



<section>
  <h3>Call by Reference</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue11.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(x)
  print(x[0])
  print(x[1])

<mark>define changeLast(x)</mark>
  x[1] = 5
    </code></pre>
    </div>
</section>


<section>
  <h3>Call by Reference</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue11.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(<mark>x</mark>)
  print(x[0])
  print(x[1])

define changeLast(<mark>x</mark>)
  x[1] = 5
    </code></pre>
    </div>
</section>



<section>
  <h3>Call by Reference</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue12.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(<mark>x</mark>)
  print(x[0])
  print(x[1])

define changeLast(<mark>x</mark>)
  x[1] = 5
    </code></pre>
    </div>
</section>



<section>
  <h3>Call by Reference</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue12.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(x)
  print(x[0])
  print(x[1])

define changeLast(x)
  <mark>x[1] = 5</mark>
    </code></pre>
    </div>
</section>

<section>
  <h3>Call by Reference</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue13.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(x)
  print(x[0])
  print(x[1])

define changeLast(x)
  <mark>x[1] = 5</mark>
    </code></pre>
    </div>
</section>


<section>
  <h3>Call by Reference</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue13.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  <mark>changeLast(x)</mark>
  print(x[0])
  print(x[1])

define changeLast(x)
  x[1] = 5
    </code></pre>
    </div>
</section>

<section>
  <h3>Call by Reference</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue14.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  <mark>changeLast(x)</mark>
  print(x[0])
  print(x[1])

define changeLast(x)
  x[1] = 5
    </code></pre>
    </div>
</section>

<section>
  <h3>Call by Reference</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue14.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(x)
  <mark>print(x[0])</mark>
  <mark>print(x[1])</mark>

define changeLast(x)
  x[1] = 5
    </code></pre>
    </div>
</section>



<section>
  <h3>Reassignment</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue1.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(x)
  print(x[0])
  print(x[1])

define changeLast(x)
  x = {3, 4}
    </code></pre>
    </div>
</section>



<section>
  <h3>Reassignment</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue1.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  <mark>x = {1, 2}</mark>
  changeLast(x)
  print(x[0])
  print(x[1])

define changeLast(x)
  x = {3, 4}
    </code></pre>
    </div>
</section>



<section>
  <h3>Reassignment</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue10.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  <mark>x = {1, 2}</mark>
  changeLast(x)
  print(x[0])
  print(x[1])

define changeLast(x)
  x = {3, 4}
    </code></pre>
    </div>
</section>


<section>
  <h3>Reassignment</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue10.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  <mark>changeLast(x)</mark>
  print(x[0])
  print(x[1])

define changeLast(x)
  x = {3, 4}
    </code></pre>
    </div>
</section>


<section>
  <h3>Reassignment</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue10.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(x)
  print(x[0])
  print(x[1])

<mark>define changeLast(x)</mark>
  x = {3, 4}
    </code></pre>
    </div>
</section>


<section>
  <h3>Reassignment</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue11.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(x)
  print(x[0])
  print(x[1])

<mark>define changeLast(x)</mark>
  x = {3, 4}
    </code></pre>
    </div>
</section>



<section>
  <h3>Reassignment</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue11.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(<mark>x</mark>)
  print(x[0])
  print(x[1])

define changeLast(<mark>x</mark>)
  x = {3, 4}
    </code></pre>
    </div>
</section>



<section>
  <h3>Reassignment</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue12.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(<mark>x</mark>)
  print(x[0])
  print(x[1])

define changeLast(<mark>x</mark>)
  x = {3, 4}
    </code></pre>
    </div>
</section>



<section>
  <h3>Reassignment</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue12.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(x)
  print(x[0])
  print(x[1])

define changeLast(x)
  <mark>x = {3, 4}</mark>
    </code></pre>
    </div>
</section>



<section>
  <h3>Reassignment</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue15.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(x)
  print(x[0])
  print(x[1])

define changeLast(x)
  <mark>x = {3, 4}</mark>
    </code></pre>
    </div>
</section>



<section>
  <h3>Reassignment</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue15.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  <mark>changeLast(x)</mark>
  print(x[0])
  print(x[1])

define changeLast(x)
  x = {3, 4}
    </code></pre>
    </div>
</section>



<section>
  <h3>Reassignment</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue16.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  <mark>changeLast(x)</mark>
  print(x[0])
  print(x[1])

define changeLast(x)
  x = {3, 4}
    </code></pre>
    </div>
</section>



<section>
  <h3>Reassignment</h3>
  <img class="plain" style="height: 800px" src="/images/callvalue16.png">
  <div style="float: left; width: 60%">
    <pre class="stretch" style="font-size: .5em"><code class="javascript">define main()
  x = {1, 2}
  changeLast(x)
  <mark>print(x[0])</mark>
  <mark>print(x[1])</mark>

define changeLast(x)
  x = {3, 4}
    </code></pre>
    </div>
</section>
