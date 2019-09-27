---
type: "reveal"
hidden: true
---

<section>
	<pre class="stretch" style="font-size: .7em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))

print("After Try")
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .7em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
<mark>finally:
  print("Finally Block")</mark>

print("After Try")
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .7em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

print("After Try")
</code></pre>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  <mark>x = int(reader.readline())</mark>
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  <mark>if x &lt; 0:</mark>
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
<mark>finally:</mark>
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  <mark>print("Finally Block")</mark>

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">Finally Block</pre>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

<mark>print("After Try")</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">Finally Block
After Try</pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  <mark>x = int(reader.readline())</mark>
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  <mark>if x &lt; 0:</mark>
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    <mark>raise ValueError("Input must be ...")</mark>
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
<mark>except ValueError as e:</mark>
  print("VE: {}".format(e))
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  <mark>print("VE: {}".format(e))</mark>
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: Input must...</pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
<mark>finally:</mark>
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: Input must...</pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  <mark>print("Finally Block")</mark>

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: Input must...
Finally Block</pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

<mark>print("After Try")</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: Input must...
Finally Block
After Try</pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">abc</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  <mark>x = int(reader.readline())</mark>
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">abc</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
<mark>except ValueError as e:</mark>
  print("VE: {}".format(e))
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">abc</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  <mark>print("VE: {}".format(e))</mark>
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">abc</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: invalid...</pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
<mark>finally:</mark>
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">abc</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: invalid...</pre>
  </div>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  <mark>print("Finally Block")</mark>

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">abc</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: invalid...
Finally Block</pre>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

<mark>print("After Try")</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">abc</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: invalid...
Finally Block
After Try</pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">abc</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: invalid...
Finally Block
After Try</pre>
  </div>
</section>


<section>
	<pre class="stretch" style="font-size: .7em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
finally:
  print("Finally Block")

print("After Try")
</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .7em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
<mark>else:
  print("No Errors!")</mark>
finally:
  print("Finally Block")

print("After Try")
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .7em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  print("Finally Block")

print("After Try")
</code></pre>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  <mark>x = int(reader.readline())</mark>
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  <mark>if x &lt; 0:</mark>
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
<mark>else:</mark>
  print("No Errors!")
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  <mark>print("No Errors!")</mark>
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">No Errors!</pre>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
<mark>finally:</mark>
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">No Errors!</pre>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  <mark>print("Finally Block")</mark>

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">No Errors!
Finally Block</pre>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  print("Finally Block")

<mark>print("After Try")</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">No Errors!
Finally Block
After Try</pre>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  <mark>x = int(reader.readline())</mark>
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  <mark>if x &lt; 0:</mark>
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  <mark>if x &lt; 0:</mark>
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    <mark>raise ValueError("Input must be ...")</mark>
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
<mark>except ValueError as e:</mark>
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em"> </pre>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  <mark>print("VE: {}".format(e))</mark>
else:
  print("No Errors!")
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: Input must...</pre>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
<mark>else:</mark>
  print("No Errors!")
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: Input must...</pre>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
<mark>finally:</mark>
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: Input must...</pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  <mark>print("Finally Block")</mark>

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: Input must...
Finally Block</pre>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  print("Finally Block")

<mark>print("After Try")</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: Input must...
Finally Block
After Try</pre>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="python">import sys

reader = sys.stdin
try:
  x = int(reader.readline())
  if x &lt; 0:
    raise ValueError("Input must be ...")
except ValueError as e:
  print("VE: {}".format(e))
else:
  print("No Errors!")
finally:
  print("Finally Block")

print("After Try")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Input:</p>
    <pre style="font-size: 1em">-5</pre>
    <p>Output:</p>
    <pre style="font-size: .5em">VE: Input must...
Finally Block
After Try</pre>
  </div>
</section>
