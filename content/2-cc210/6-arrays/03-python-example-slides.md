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
    <pre class="stretch" style="font-size: .37em"><code class="python">numAssignments = int(reader.readline())
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Handle Input</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="python">numAssignments = int(reader.readline())

<mark>if numAssignments > 0:

else:
  print("Invalid Input!")</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Handle Input</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="python">numAssignments = int(reader.readline())

if numAssignments > 0:

  <mark>scores = []
  weights = []</mark>

else:
  print("Invalid Input!")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Create Lists</p>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="python">numAssignments = int(reader.readline())

if numAssignments > 0:

  scores = []
  weights = []

  <mark>for i in range(0, numAssignments):
    scores.append(int(reader.readline()))
    weights.append(float(reader.readline()))</mark>

else:
  print("Invalid Input!")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Fill Lists</p>
  </div>
</section>




<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="python">numAssignments = int(reader.readline())

if numAssignments > 0:

  scores = []
  weights = []

  for i in range(0, numAssignments):
    scores.append(int(reader.readline()))
    weights.append(float(reader.readline()))

  <mark>sum = 0.0
  for d in weights:
    sum += d

  if sum == 1.0:

  else:
    print("Error! Weights do not add to 1.0!")</mark>

else:
  print("Invalid Input!")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Check Weights</p>
  </div>
</section>




<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="python">numAssignments = int(reader.readline())

if numAssignments > 0:

  scores = []
  weights = []

  for i in range(0, numAssignments):
    scores.append(int(reader.readline()))
    weights.append(float(reader.readline()))

  sum = 0.0
  for d in weights:
    sum += d

  if sum == 1.0:

    <mark>totalScore = 0.0
    for j in range(0, numAssignments):
      totalScore += scores[j] * weights[j]
    print(totalScore)</mark>

  else:
    print("Error! Weights do not add to 1.0!")

else:
  print("Invalid Input!")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Calculate Score</p>
  </div>
</section>




<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="python">numAssignments = int(reader.readline())

if numAssignments > 0:

  scores = []
  weights = []

  for i in range(0, numAssignments):
    scores.append(int(reader.readline()))
    weights.append(float(reader.readline()))

  sum = 0.0
  for d in weights:
    sum += d

  if sum == 1.0:

    totalScore = 0.0
    for j in range(0, numAssignments):
      totalScore += scores[j] * weights[j]
    print(totalScore)

  else:
    print("Error! Weights do not add to 1.0!")

else:
  print("Invalid Input!")
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Done!</p>
  </div>
</section>
