---
type: "reveal"
hidden: true
---

<section>
  <pre class="stretch" style="font-size: .75em"><code class="python"># Load required modules
import sys

# If an argument is present,
# we are reading from a file
# specified in sys.argv[1]
if len(sys.argv) > 1:
  reader = open(sys.argv[1])

# If no argument, read from stdin
else:
  reader = sys.stdin

<mark># -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-</mark>
</code></pre>
</section>

<section>
  <h2>Reader Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(reader.readline())
s1 = reader.readline()
d = float(reader.readline())
s2 = reader.readline()</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em">1
This
2.0
is true</pre>
  </div>
</section>

<section>
  <h2>Reader Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python"><mark>x = int(reader.readline())</mark>
s1 = reader.readline()
d = float(reader.readline())
s2 = reader.readline()</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em">1
This
2.0
is true</pre>
  </div>
</section>

<section>
  <h2>Reader Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(<mark>reader.readline()</mark>)
s1 = reader.readline()
d = float(reader.readline())
s2 = reader.readline()</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><mark>1</mark>
This
2.0
is true</pre>
  </div>
</section>

<section>
  <h2>Reader Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python"><mark>x = int("1")</mark>
s1 = reader.readline()
d = float(reader.readline())
s2 = reader.readline()</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><s>1</s>
This
2.0
is true</pre>
  </div>
</section>

<section>
  <h2>Reader Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(reader.readline()) # x = 1
s1 = reader.readline()
d = float(reader.readline())
s2 = reader.readline()</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><s>1</s>
This
2.0
is true</pre>
  </div>
</section>

<section>
  <h2>Reader Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(reader.readline()) # x = 1
<mark>s1 = reader.readline()</mark>
d = float(reader.readline())
s2 = reader.readline()</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><s>1</s>
<mark>This</mark>
2.0
is true</pre>
  </div>
</section>

<section>
  <h2>Reader Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(reader.readline()) # x = 1
s1 = reader.readline()     # s1 = "This"
d = float(reader.readline())
s2 = reader.readline()</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><s>1</s>
<s>This</s>
2.0
is true</pre>
  </div>
</section>

<section>
  <h2>Reader Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(reader.readline()) # x = 1
s1 = reader.readline()     # s1 = "This"
<mark>d = float(reader.readline())</mark>
s2 = reader.readline()</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><s>1</s>
<s>This</s>
2.0
is true</pre>
  </div>
</section>

<section>
  <h2>Reader Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(reader.readline()) # x = 1
s1 = reader.readline()     # s1 = "This"
d = float(<mark>reader.readline()</mark>)
s2 = reader.readline()</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><s>1</s>
<s>This</s>
<mark>2.0</mark>
is true</pre>
  </div>
</section>

<section>
  <h2>Reader Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(reader.readline()) # x = 1
s1 = reader.readline()     # s1 = "This"
<mark>d = float("2.0")</mark>
s2 = reader.readline()</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><s>1</s>
<s>This</s>
<s>2.0</s>
is true</pre>
  </div>
</section>

<section>
  <h2>Reader Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(reader.readline()) # x = 1
s1 = reader.readline()     # s1 = "This"
d = float(reader.readline()) # d = 2.0
s2 = reader.readline()</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><s>1</s>
<s>This</s>
<s>2.0</s>
is true</pre>
  </div>
</section>

<section>
  <h2>Reader Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(reader.readline()) # x = 1
s1 = reader.readline()     # s1 = "This"
d = float(reader.readline()) # d = 2.0
<mark>s2 = reader.readline()</mark></code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><s>1</s>
<s>This</s>
<s>2.0</s>
<mark>is true</mark></pre>
  </div>
</section>

<section>
  <h2>Reader Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(reader.readline()) # x = 1
s1 = reader.readline()     # s1 = "This"
d = float(reader.readline()) # d = 2.0
s2 = reader.readline()  # s2 = "is true"</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><s>1</s>
<s>This</s>
<s>2.0</s>
<s>is true</s></pre>
  </div>
</section>


<section>
  <h2>Incorrect Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(reader.readline()) # x = 1
s1 = reader.readline()     # s1 = "This"
<mark>d = float(reader.readline())</mark>
s2 = reader.readline()</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><s>1</s>
<s>This</s>
is
2.0</pre>
  </div>
</section>

<section>
  <h2>Incorrect Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(reader.readline()) # x = 1
s1 = reader.readline()     # s1 = "This"
d = float(<mark>reader.readline()</mark>)
s2 = reader.readline()</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><s>1</s>
<s>This</s>
<mark>is</mark>
2.0</pre>
  </div>
</section>

<section>
  <h2>Incorrect Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(reader.readline()) # x = 1
s1 = reader.readline()     # s1 = "This"
<mark>d = float("is")</mark>
s2 = reader.readline()</code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><s>1</s>
<s>This</s>
<s>is</s>
2.0</pre>
  </div>
</section>

<section>
  <h2>Incorrect Input</h2>
  <div style="float: right; width: 75%">
    <p>Code:</p>
    <pre class="stretch" style="font-size: .58em"><code class="python">x = int(reader.readline()) # x = 1
s1 = reader.readline()     # s1 = "This"
<mark>d = float("is")</mark>
<mark style="background-color: red"> ValueError </mark></code></pre>
  </div>
  <div style="width: 25%">
    <p>Input:</p>
    <pre style="font-size: 1em"><s>1</s>
<s>This</s>
<s>is</s>
2.0</pre>
  </div>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em">This 1
2.0 true</pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()
line1Parts = line1.split(" ")
s1 = line1Parts[0]
x = int(line1Parts[1])

line2 = reader.readline()
line2Parts = line2.split(" ")
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><mark>This 1</mark>
2.0 true</pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python"><mark>line1 = reader.readline()</mark>
line1Parts = line1.split(" ")
s1 = line1Parts[0]
x = int(line1Parts[1])

line2 = reader.readline()
line2Parts = line2.split(" ")
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
2.0 true</pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")
s1 = line1Parts[0]
x = int(line1Parts[1])

line2 = reader.readline()
line2Parts = line2.split(" ")
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
2.0 true</pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
<mark>line1Parts = line1.split(" ")</mark>
s1 = line1Parts[0]
x = int(line1Parts[1])

line2 = reader.readline()
line2Parts = line2.split(" ")
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
2.0 true</pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # <mark>"This 1"</mark>
<mark>line1Parts = line1.split(" ")</mark>
s1 = line1Parts[0]
x = int(line1Parts[1])

line2 = reader.readline()
line2Parts = line2.split(" ")
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
2.0 true</pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
s1 = line1Parts[0]
x = int(line1Parts[1])

line2 = reader.readline()
line2Parts = line2.split(" ")
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
2.0 true</pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
<mark>s1 = line1Parts[0]</mark>
x = int(line1Parts[1])

line2 = reader.readline()
line2Parts = line2.split(" ")
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
2.0 true</pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # [<mark>"This"</mark>, "1"]
<mark>s1 = line1Parts[0]</mark>
x = int(line1Parts[1])

line2 = reader.readline()
line2Parts = line2.split(" ")
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
2.0 true</pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
s1 = line1Parts[0]             # "This"
x = int(line1Parts[1])

line2 = reader.readline()
line2Parts = line2.split(" ")
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
2.0 true</pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
s1 = line1Parts[0]             # "This"
<mark>x = int(line1Parts[1])</mark>

line2 = reader.readline()
line2Parts = line2.split(" ")
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
2.0 true</pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", <mark>"1"</mark>]
s1 = line1Parts[0]             # "This"
x = int(<mark>line1Parts[1]</mark>)

line2 = reader.readline()
line2Parts = line2.split(" ")
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
2.0 true</pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", <mark>"1"</mark>]
s1 = line1Parts[0]             # "This"
x = <mark>int("1")</mark>

line2 = reader.readline()
line2Parts = line2.split(" ")
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
2.0 true</pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
s1 = line1Parts[0]             # "This"
x = int(line1Parts[1])         # 1

line2 = reader.readline()
line2Parts = line2.split(" ")
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
<mark>2.0 true</mark></pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
s1 = line1Parts[0]             # "This"
x = int(line1Parts[1])         # 1

<mark>line2 = reader.readline()
line2Parts = line2.split(" ")</mark>
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
<s>2.0 true</s></pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
s1 = line1Parts[0]             # "This"
x = int(line1Parts[1])         # 1

line2 = reader.readline()      # "2.0 true"
line2Parts = line2.split(" ")  # ["2.0", "true"]
f = float(line2Parts[0])
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
<s>2.0 true</s></pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
s1 = line1Parts[0]             # "This"
x = int(line1Parts[1])         # 1

line2 = reader.readline()      # "2.0 true"
line2Parts = line2.split(" ")  # ["2.0", "true"]
<mark>f = float(line2Parts[0])</mark>
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
<s>2.0 true</s></pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
s1 = line1Parts[0]             # "This"
x = int(line1Parts[1])         # 1

line2 = reader.readline()      # "2.0 true"
line2Parts = line2.split(" ")  # [<mark>"2.0"</mark>, "true"]
f = float(<mark>line2Parts[0]</mark>)
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
<s>2.0 true</s></pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
s1 = line1Parts[0]             # "This"
x = int(line1Parts[1])         # 1

line2 = reader.readline()      # "2.0 true"
line2Parts = line2.split(" ")  # ["2.0", "true"]
f = <mark>float("2.0")</mark>
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
<s>2.0 true</s></pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
s1 = line1Parts[0]             # "This"
x = int(line1Parts[1])         # 1

line2 = reader.readline()      # "2.0 true"
line2Parts = line2.split(" ")  # ["2.0", "true"]
f = float(line2Parts[0])       # 2.0
b = bool(line2Parts[1])</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
<s>2.0 true</s></pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
s1 = line1Parts[0]             # "This"
x = int(line1Parts[1])         # 1

line2 = reader.readline()      # "2.0 true"
line2Parts = line2.split(" ")  # ["2.0", "true"]
f = float(line2Parts[0])       # 2.0
<mark>b = bool(line2Parts[1])</mark></code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
<s>2.0 true</s></pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
s1 = line1Parts[0]             # "This"
x = int(line1Parts[1])         # 1

line2 = reader.readline()      # "2.0 true"
line2Parts = line2.split(" ")  # ["2.0", <mark>"true"</mark>]
f = float(line2Parts[0])       # 2.0
b = bool(<mark>line2Parts[1]</mark>)</code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
<s>2.0 true</s></pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
s1 = line1Parts[0]             # "This"
x = int(line1Parts[1])         # 1

line2 = reader.readline()      # "2.0 true"
line2Parts = line2.split(" ")  # ["2.0", "true"]
f = float(line2Parts[0])       # 2.0
b = <mark>bool("true")</mark></code></pre>
</section>

<section>
  <h2>Split & Parse Input</h2>
  <pre style="font-size: 1em"><s>This 1</s>
<s>2.0 true</s></pre>
  <p>Code:</p>
  <pre class="stretch" style="font-size: .58em"><code class="python">line1 = reader.readline()      # "This 1"
line1Parts = line1.split(" ")  # ["This", "1"]
s1 = line1Parts[0]             # "This"
x = int(line1Parts[1])         # 1

line2 = reader.readline()      # "2.0 true"
line2Parts = line2.split(" ")  # ["2.0", "true"]
f = float(line2Parts[0])       # 2.0
b = bool(line2Parts[1])        # True</code></pre>
</section>