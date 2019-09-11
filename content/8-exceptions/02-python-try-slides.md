---
type: "reveal"
hidden: true
---

<section>
	<img class="stretch plain" src="/images/8.4.handle.png">
</section>

<section>
	<img class="stretch plain" src="/images/8.4.try.png">
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

# If an argument is present, we are reading from a file
# specified in sys.argv[1]
if len(sys.argv) > 1:
  reader = open(sys.argv[1])

# If no argument, read from stdin
else:
  reader = sys.stdin

x = int(reader.readline())
print(x)
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

<mark>try:</mark>
# If an argument is present, we are reading from a file
# specified in sys.argv[1]
if len(sys.argv) > 1:
  reader = open(sys.argv[1])

# If no argument, read from stdin
else:
  reader = sys.stdin

x = int(reader.readline())
print(x)
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
<mark># If an argument is present, we are reading from a file
# specified in sys.argv[1]
if len(sys.argv) > 1:
  reader = open(sys.argv[1])

# If no argument, read from stdin
else:
  reader = sys.stdin

x = int(reader.readline())
print(x)</mark>
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  <mark># If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)</mark>
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)
</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

<mark>except Exception as e:</mark>

</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except <mark>Exception</mark> as e:

</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except Exception <mark>as</mark> e:

</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except Exception as e:

</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except Exception as e:
  <mark>print("Error!")</mark>
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except Exception as e:
  print("Error!")
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = <mark>open(sys.argv[1])</mark>

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except Exception as e:
  print("Error!")
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except <mark>Exception</mark> as e:
  print("Error!")
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except <mark>FileNotFoundError</mark> as e:
  print("Error!")
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except FileNotFoundError as e:
  print(<mark>"Error!"</mark>)
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except FileNotFoundError as e:
  print(<mark>"Error: File Not Found!"</mark>)
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except FileNotFoundError as e:
  print("Error: File Not Found!")
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = <mark>int(reader.readline())</mark>
  print(x)

except FileNotFoundError as e:
  print("Error: File Not Found!")
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except FileNotFoundError as e:
  print("Error: File Not Found!")
<mark>except ValueError as e:
  print("Error: Input Does Not Match Expected Format!")</mark>
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except FileNotFoundError as e:
  print("Error: File Not Found!")
except ValueError as e:
  print("Error: Input Does Not Match Expected Format!")
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(<mark>reader.readline()</mark>)
  print(x)

except FileNotFoundError as e:
  print("Error: File Not Found!")
except ValueError as e:
  print("Error: Input Does Not Match Expected Format!")
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except FileNotFoundError as e:
  print("Error: File Not Found!")
except ValueError as e:
  print("Error: Input Does Not Match Expected Format!")
<mark>except OSError as e:
  print("Error: OS Exception!")
</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except FileNotFoundError as e:
  print("Error: File Not Found!")
except ValueError as e:
  print("Error: Input Does Not Match Expected Format!")
except OSError as e:
  print("Error: OS Exception!")
</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

<mark>except OSError as e:
  print("Error: OS Exception!")
except FileNotFoundError as e:
  print("Error: File Not Found!")
except ValueError as e:
  print("Error: Input Does Not Match Expected Format!")</mark>
</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

<mark style="background-color: red">except OSError as e:
  print("Error: OS Exception!")
except FileNotFoundError as e:
  print("Error: File Not Found!")
except ValueError as e:
  print("Error: Input Does Not Match Expected Format!")</mark>
</code></pre>
</section>


<section>
	<h2>Exception Hierarchy</h2>
	<img class="stretch plain" src="/images/8.7.p.3.filenotfound.png">
</section>

<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

<mark style="background-color: red">except OSError as e:
  print("Error: OS Exception!")
except FileNotFoundError as e:
  print("Error: File Not Found!")
except ValueError as e:
  print("Error: Input Does Not Match Expected Format!")</mark>
</code></pre>
</section>



<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

<mark>except FileNotFoundError as e:
  print("Error: File Not Found!")
except ValueError as e:
  print("Error: Input Does Not Match Expected Format!")
except OSError as e:
  print("Error: OS Exception!")</mark>
</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .49em"><code class="python"># Load required modules
import sys

try:
  # If an argument is present, we are reading from a file
  # specified in sys.argv[1]
  if len(sys.argv) > 1:
    reader = open(sys.argv[1])

  # If no argument, read from stdin
  else:
    reader = sys.stdin

  x = int(reader.readline())
  print(x)

except FileNotFoundError as e:
  print("Error: File Not Found!")
except ValueError as e:
  print("Error: Input Does Not Match Expected Format!")
except OSError as e:
  print("Error: OS Exception!")
</code></pre>
</section>
