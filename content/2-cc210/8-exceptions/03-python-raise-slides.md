---
type: "reveal"
hidden: true
---

<section>
  <h2>Custom Exceptions</h2>
</section>

<section>
	<pre class="stretch" style="font-size: .70em"><code class="python">import sys

if len(sys.argv) > 1:
  reader = open(sys.argv[1])
else:
  reader = sys.stdin

x = float(reader.readline())
y = float(reader.readline())

if y == 0:
  print("Error")
else:
  z = x / y
  print(z)
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .70em"><code class="python">import sys

if len(sys.argv) > 1:
  reader = open(sys.argv[1])
else:
  reader = sys.stdin

x = float(reader.readline())
y = float(reader.readline())

if y == 0:
  <mark>print("Error")</mark>
else:
  z = x / y
  print(z)
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .70em"><code class="python">import sys

if len(sys.argv) > 1:
  reader = open(sys.argv[1])
else:
  reader = sys.stdin

x = float(reader.readline())
y = float(reader.readline())

if y == 0:
  <mark>raise ValueError("Cannot divide by zero")</mark>
else:
  z = x / y
  print(z)
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .70em"><code class="python">import sys

if len(sys.argv) > 1:
  reader = open(sys.argv[1])
else:
  reader = sys.stdin

x = float(reader.readline())
y = float(reader.readline())

if y == 0:
  raise ValueError("Cannot divide by zero")
else:
  z = x / y
  print(z)
</code></pre>
</section>
