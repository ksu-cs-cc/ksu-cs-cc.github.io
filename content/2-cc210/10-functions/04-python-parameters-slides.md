---
type: "reveal"
hidden: true
---

<section>
	<pre class="" style="font-size: .7em"><code class="python">def foo(message):
  print("Message: {}".format(message))
</code></pre>
</section>


<section>
	<pre class="" style="font-size: .7em"><code class="python">def foo(<mark>message</mark>):
  print("Message: {}".format(message))</code></pre>
</section>

<section>
	<pre class="" style="font-size: .7em"><code class="python">def foo(<mark>message</mark>):
  print("Message: {}".format(<mark>message</mark>))</code></pre>
</section>


<section>
	<pre class="" style="font-size: .7em"><code class="python">def foo(message):
  print("Message: {}".format(message))

#somewhere in another function
foo("Hello World!")</code></pre>
</section>



<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  x = 5
  y = 10
  z = 8
  bar(x, y, z)
  foo(y, True)

def foo(output, long_message):
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def bar(a, b, c):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  main()
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  x = 5
  y = 10
  z = 8
  bar(x, y, z)
  foo(y, True)

def foo(output, long_message):
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def bar(a, b, c):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def <mark>main</mark>():
  x = 5
  y = 10
  z = 8
  bar(x, y, z)
  foo(y, True)

def foo(output, long_message):
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def bar(a, b, c):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  <mark>x = 5
  y = 10
  z = 8</mark>
  bar(x, y, z)
  foo(y, True)

def foo(output, long_message):
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def bar(a, b, c):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  <mark>x = 5
  y = 10
  z = 8</mark>
  bar(x, y, z)
  foo(y, True)

def foo(output, long_message):
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def bar(a, b, c):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>main</b><br>x = 5<br>y = 10<br>z = 8</p>
  </div>
</section>

<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  x = 5
  y = 10
  z = 8
  <mark>bar(x, y, z)</mark>
  foo(y, True)

def foo(output, long_message):
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def bar(a, b, c):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>main</b><br>x = 5<br>y = 10<br>z = 8</p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  x = 5
  y = 10
  z = 8
  <mark>bar(x, y, z)</mark>
  foo(y, True)

def foo(output, long_message):
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def <mark>bar</mark>(a, b, c):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>main</b><br>x = 5<br>y = 10<br>z = 8</p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  x = 5
  y = 10
  z = 8
  bar(<mark>x</mark>, y, z)
  foo(y, True)

def foo(output, long_message):
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def bar(<mark>a</mark>, b, c):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>main</b><br>x = 5<br>y = 10<br>z = 8</p>
  </div>
</section>

<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  x = 5
  y = 10
  z = 8
  bar(<mark>x</mark>, y, z)
  foo(y, True)

def foo(output, long_message):
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def bar(<mark>a</mark>, b, c):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>main</b><br>x = 5<br>y = 10<br>z = 8<br><br><b>bar</b><br><mark>a = 5</mark></p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  x = 5
  y = 10
  z = 8
  bar(x, <mark>y</mark>, z)
  foo(y, True)

def foo(output, long_message):
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def bar(a, <mark>b</mark>, c):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>main</b><br>x = 5<br>y = 10<br>z = 8<br><br><b>bar</b><br>a = 5<br><mark>b = 10</mark></p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  x = 5
  y = 10
  z = 8
  bar(x, y, <mark>z</mark>)
  foo(y, True)

def foo(output, long_message):
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def bar(a, b, <mark>c</mark>):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>main</b><br>x = 5<br>y = 10<br>z = 8<br><br><b>bar</b><br>a = 5<br>b = 10<br><mark>c = 8</mark></p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  x = 5
  y = 10
  z = 8
  <mark>bar(x, y, z)</mark>
  foo(y, True)

def foo(output, long_message):
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def bar(a, b, c):
  <mark>print("{}, {}, {}".format(a, b, c))</mark>

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>main</b><br>x = 5<br>y = 10<br>z = 8<br><br><b>bar</b><br>a = 5<br>b = 10<br>c = 8</p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  x = 5
  y = 10
  z = 8
  bar(x, y, z)
  <mark>foo(y, True)</mark>

def foo(output, long_message):
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def bar(a, b, c):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>main</b><br>x = 5<br>y = 10<br>z = 8</p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  x = 5
  y = 10
  z = 8
  bar(x, y, z)
  <mark>foo(y, True)</mark>

def <mark>foo(output, long_message)</mark>:
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def bar(a, b, c):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>main</b><br>x = 5<br>y = 10<br>z = 8</p>
  </div>
</section>

<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  x = 5
  y = 10
  z = 8
  bar(x, y, z)
  <mark>foo(y, True)</mark>

def <mark>foo(output, long_message)</mark>:
  if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))

def bar(a, b, c):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>main</b><br>x = 5<br>y = 10<br>z = 8<br><br><b>foo</b><br>output = 10<br>long_message = True</p>
  </div>
</section>



<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .5em"><code class="python">def main():
  x = 5
  y = 10
  z = 8
  bar(x, y, z)
  <mark>foo(y, True)</mark>

def foo(output, long_message):
  <mark>if long_message:
    print("The value was {}".format(output))
  else:
    print("Val: {}".format(output))</mark>

def bar(a, b, c):
  print("{}, {}, {}".format(a, b, c))

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>main</b><br>x = 5<br>y = 10<br>z = 8<br><br><b>foo</b><br>output = 10<br>long_message = True</p>
  </div>
</section>
