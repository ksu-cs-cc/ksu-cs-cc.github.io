---
type: "reveal"
hidden: true
---

<section>
	<pre class="" style="font-size: .8em"><code class="python">def foo():
  print("Foo")
  return
</code></pre>
</section>


<section>
	<pre class="" style="font-size: .8em"><code class="python"><mark>def</mark> foo():
  print("Foo")
  return
</code></pre>
</section>


<section>
	<pre class="" style="font-size: .8em"><code class="python">def <mark>foo</mark>():
  print("Foo")
  return
</code></pre>
</section>


<section>
	<pre class="" style="font-size: .8em"><code class="python">def foo<mark>()</mark>:
  print("Foo")
  return
</code></pre>
</section>


<section>
	<pre class="" style="font-size: .8em"><code class="python">def foo():<mark>
  print("Foo")
  return</mark>
</code></pre>
</section>


<section>
	<pre class="" style="font-size: .8em"><code class="python">def foo:
  print("Foo")
  <mark>return</mark>
</code></pre>
</section>


<section>
	<pre class="" style="font-size: .8em"><code class="python">def foo:
  print("Foo")
  return
</code></pre>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  foo()
  print("Main 2")
  foo()
  print("Main 3")

def foo():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  main()
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python"><mark>def main():
  print("Main 1")
  foo()
  print("Main 2")
  foo()
  print("Main 3")</mark>

def foo():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  main()
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  foo()
  print("Main 2")
  foo()
  print("Main 3")

<mark>def foo():
  print("Foo 1")
  return</mark>

# main guard
if __name__ == "__main__":
  main()
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  foo()
  print("Main 2")
  foo()
  print("Main 3")

def foo():
  print("Foo 1")
  return

# main guard
<mark>if __name__ == "__main__":</mark>
  main()
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  foo()
  print("Main 2")
  foo()
  print("Main 3")

def foo():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def <mark>main</mark>():
  print("Main 1")
  foo()
  print("Main 2")
  foo()
  print("Main 3")

def foo():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  <mark>print("Main 1")</mark>
  foo()
  print("Main 2")
  foo()
  print("Main 3")

def foo():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  <mark>print("Main 1")</mark>
  foo()
  print("Main 2")
  foo()
  print("Main 3")

def foo():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em"><mark>Main 1</mark></p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  <mark>foo()</mark>
  print("Main 2")
  foo()
  print("Main 3")

def foo():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em">Main 1</p>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  <mark>foo()</mark>
  print("Main 2")
  foo()
  print("Main 3")

def <mark>foo</mark>():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em">Main 1</p>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  <mark>foo()</mark>
  print("Main 2")
  foo()
  print("Main 3")

def foo():
  <mark>print("Foo 1")</mark>
  return

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em">Main 1</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  <mark>foo()</mark>
  print("Main 2")
  foo()
  print("Main 3")

def foo():
  <mark>print("Foo 1")</mark>
  return

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em">Main 1<br><mark>Foo 1</mark></p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  <mark>foo()</mark>
  print("Main 2")
  foo()
  print("Main 3")

def foo():
  print("Foo 1")
  <mark>return</mark>

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em">Main 1<br>Foo 1</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  foo()
  <mark>print("Main 2")</mark>
  foo()
  print("Main 3")

def foo():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em">Main 1<br>Foo 1</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  foo()
  <mark>print("Main 2")</mark>
  foo()
  print("Main 3")

def foo():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em">Main 1<br>Foo 1<br><mark>Main 2</mark></p>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  foo()
  print("Main 2")
  <mark>foo()</mark>
  print("Main 3")

def foo():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em">Main 1<br>Foo 1<br>Main 2</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  foo()
  print("Main 2")
  <mark>foo()</mark>
  print("Main 3")

<mark>def foo():
  print("Foo 1")
  return</mark>

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em">Main 1<br>Foo 1<br>Main 2</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  foo()
  print("Main 2")
  <mark>foo()</mark>
  print("Main 3")

<mark>def foo():
  print("Foo 1")
  return</mark>

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em">Main 1<br>Foo 1<br>Main 2<br><mark>Foo 1</mark></p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  foo()
  print("Main 2")
  foo()
  <mark>print("Main 3")</mark>

def foo():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em">Main 1<br>Foo 1<br>Main 2<br>Foo 1</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  foo()
  print("Main 2")
  foo()
  <mark>print("Main 3")</mark>

def foo():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em">Main 1<br>Foo 1<br>Main 2<br>Foo 1<br><mark>Main 3</mark></p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  foo()
  print("Main 2")
  foo()
  print("Main 3")

def foo():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em">Main 1<br>Foo 1<br>Main 2<br>Foo 1<br>Main 3</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  print("Main 1")
  foo()
  print("Main 2")
  foo()
  print("Main 3")

def foo():
  print("Foo 1")
  return

# main guard
if __name__ == "__main__":
  main()
</code></pre>
  </div>
  <div style="width: 30%">
    <h4>Output:</h4>
    <p style="font-size: .7em">Main 1<br>Foo 1<br>Main 2<br>Foo 1<br>Main 3</p>
  </div>
</section>
