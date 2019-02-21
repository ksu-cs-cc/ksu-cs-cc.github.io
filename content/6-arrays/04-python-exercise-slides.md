---
type: "reveal"
hidden: true
---

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="python"># Load required modules
import sys

# If an argument is present, we are reading from a file
# specified in sys.argv[1]
if len(sys.argv) > 1:
  reader = open(sys.argv[1])

# If no argument, read from stdin
else:
  reader = sys.stdin

<mark># -=-=-=-=- MORE CODE GOES HERE -=-=-=-=- </mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Skeleton</p>
  </div>
</section>




<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="python">m = int(reader.readline())
n = int(reader.readline())

if m > 0 and n > 0:

else:
  print("Error - Invalid Input!")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Handle Input</p>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="python">m = int(reader.readline())
n = int(reader.readline())

if m > 0 and n > 0:
  <mark>array = []</mark>
else:
  print("Error - Invalid Input!")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Create 2D List</p>
  </div>
</section>




<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="python">m = int(reader.readline())
n = int(reader.readline())

if m > 0 and n > 0:
  array = []

  <mark>for i in range(0, m):
    array.append([])
    for j in range(0, n):
      array[i].append(int(reader.readline()))</mark>

else:
  print("Error - Invalid Input!")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Fill List</p>
  </div>
</section>




<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="python">m = int(reader.readline())
n = int(reader.readline())

if m > 0 and n > 0:
  array = []

  for i in range(0, m):
    array.append([])
    for j in range(0, n):
      array[i].append(int(reader.readline()))

  <mark>for j in range(0, n):
    for i in range(0, m):
      print(str(array[i][j]) + " ", end="")
    print()</mark>

else:
  print("Error - Invalid Input!")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Transpose</p>
  </div>
</section>
