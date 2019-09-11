---
type: "reveal"
hidden: true
---

<section>
	<pre class="stretch" style="font-size: .61em"><code class="python">import sys

try:
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except ValueError as e:
  print("ValueError: {}".format(e))
except FileNotFoundError as e:
  print("FileNotFoundError: {}".format(e))
finally:
  reader.close()
</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .61em"><code class="python">import sys

try:
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])
  else:
    reader = sys.stdin

  <mark>x = int(reader.readline())
  print(x)</mark>

except ValueError as e:
  print("ValueError: {}".format(e))
except FileNotFoundError as e:
  print("FileNotFoundError: {}".format(e))
finally:
  reader.close()
</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .61em"><code class="python">import sys

try:
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])
  else:
    reader = sys.stdin

  <mark>x = int(reader.readline())
  print(x)</mark>

except ValueError as e:
  print("ValueError: {}".format(e))
except FileNotFoundError as e:
  print("FileNotFoundError: {}".format(e))
<mark>finally:
  reader.close()</mark>
</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .61em"><code class="python">import sys

try:
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])
  else:
    reader = sys.stdin

  <mark>with reader:</mark>
  x = int(reader.readline())
  print(x)

except ValueError as e:
  print("ValueError: {}".format(e))
except FileNotFoundError as e:
  print("FileNotFoundError: {}".format(e))
finally:
  reader.close()
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .61em"><code class="python">import sys

try:
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])
  else:
    reader = sys.stdin

  with reader:
  <mark>x = int(reader.readline())
  print(x)</mark>

except ValueError as e:
  print("ValueError: {}".format(e))
except FileNotFoundError as e:
  print("FileNotFoundError: {}".format(e))
finally:
  reader.close()
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .61em"><code class="python">import sys

try:
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])
  else:
    reader = sys.stdin

  with reader:
    <mark>x = int(reader.readline())
    print(x)</mark>

except ValueError as e:
  print("ValueError: {}".format(e))
except FileNotFoundError as e:
  print("FileNotFoundError: {}".format(e))
finally:
  reader.close()
</code></pre>
</section>



<section>
	<pre class="stretch" style="font-size: .61em"><code class="python">import sys

try:
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])
  else:
    reader = sys.stdin

  with reader:
    x = int(reader.readline())
    print(x)

except ValueError as e:
  print("ValueError: {}".format(e))
except FileNotFoundError as e:
  print("FileNotFoundError: {}".format(e))
<s>finally:
  reader.close()</s>
</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .61em"><code class="python">import sys

try:
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])
  else:
    reader = sys.stdin

  with reader:
    x = int(reader.readline())
    print(x)

except ValueError as e:
  print("ValueError: {}".format(e))
except FileNotFoundError as e:
  print("FileNotFoundError: {}".format(e))
</code></pre>
</section>
