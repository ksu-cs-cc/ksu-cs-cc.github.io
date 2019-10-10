---
type: "reveal"
hidden: true
---

<section>
	<h2>Problem Statement</h2>
</section>
<section>
	<p style="font-size: 0.5em">Write a program that accepts three files as command line arguments. The first two represent input files, and the third one represents the desired output file. If there aren't three arguments provided, either input file is not an existing file, or the output file is an existing directory, print "Invalid Arguments" and exit the program. The output file may be an existing file, since it will be overwritten. </p>
	<p style="font-size: 0.5em">The program should open each input file and read the contents. Each input file will consist of a list of whole numbers, one per line. If there are any errors parsing the contents of either file, the program should print "Invalid Input" and exit. As the input is read, the program should keep track of both the count and sum of all even inputs and odd inputs.</p>
	<p style="font-size: 0.5em">Once all input is read, the program should create the output file and print the following four items, in this order, one per line: number of even inputs, sum of even inputs, number of odd inputs, sum of odd inputs.</p>
	<p style="font-size: 0.5em">Finally, when the program is done, it should simply print "Complete" and exit. Don't forget to close any open files!</p>
</section>
<section>
  <h2>Whaaaa?</h2>
	<img class="stretch plain" src="https://media.giphy.com/media/l3q2K5jinAlChoCLS/source.gif">
  <p class="imagecredit">Image Credit: <a href="https://media.giphy.com/media/l3q2K5jinAlChoCLS/source.gif">Mashable via Giphy</a></p>
	<p>Let's break it down into smaller parts</p>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .45em"><code class="python">import sys

if len(sys.argv) != 4:
  print("Invalid Arguments")
  sys.exit()</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .7em">Write a program that accepts three files as command line arguments.</p>
    <p style="font-size: .7em">If there aren't three arguments provided, ... print "Invalid Arguments" and exit the program.</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .45em"><code class="python">import sys

if len(sys.argv) != 4:
  print("Invalid Arguments")
  sys.exit()</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">The first two represent input files, and the third one represents the desired output file.</p>
    <p style="font-size: .65em">...either input file is not an existing file, or the output file is an existing directory, print "Invalid Arguments" and exit the program</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .45em"><code class="python">import sys

if len(sys.argv) != 4:
  print("Invalid Arguments")
  sys.exit()

<mark>try:
  with open(sys.argv[1]) as scanner1, \
       open(sys.argv[2]) as scanner2, \
       open(sys.argv[3], "w") as writer:</mark>

    # -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">The first two represent input files, and the third one represents the desired output file.</p>
    <p style="font-size: .65em">...either input file is not an existing file, or the output file is an existing directory, print "Invalid Arguments" and exit the program</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .45em"><code class="python">import sys

if len(sys.argv) != 4:
  print("Invalid Arguments")
  sys.exit()

try:
  with open(sys.argv[1]) as scanner1, \
       open(sys.argv[2]) as scanner2, \
       open(sys.argv[3], "w") as writer:

    # -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-

<mark>except FileNotFoundError as e:
  print("Invalid Arguments")
  sys.exit()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">The first two represent input files, and the third one represents the desired output file.</p>
    <p style="font-size: .65em">...either <mark>input file is not an existing file</mark>, or the output file is an existing directory, print "Invalid Arguments" and exit the program</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .45em"><code class="python">import sys

if len(sys.argv) != 4:
  print("Invalid Arguments")
  sys.exit()

try:
  with open(sys.argv[1]) as scanner1, \
       open(sys.argv[2]) as scanner2, \
       open(sys.argv[3], "w") as writer:

    # -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-

except FileNotFoundError as e:
  print("Invalid Arguments")
  sys.exit()
<mark>except IOError as e:
  print("Invalid Arguments")
  sys.exit()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">The first two represent input files, and the third one represents the desired output file.</p>
    <p style="font-size: .65em">...either input file is not an existing file, or the <mark>output file is an existing directory</mark>, print "Invalid Arguments" and exit the program</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .45em"><code class="python">import sys

if len(sys.argv) != 4:
  print("Invalid Arguments")
  sys.exit()

try:
  with open(sys.argv[1]) as scanner1, \
       open(sys.argv[2]) as scanner2, \
       open(sys.argv[3], "w") as writer:

    # -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-

except FileNotFoundError as e:
  print("Invalid Arguments")
  sys.exit()
except IOError as e:
  print("Invalid Arguments")
  sys.exit()
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">The first two represent input files, and the third one represents the desired output file.</p>
    <p style="font-size: .65em">...either input file is not an existing file, or the output file is an existing directory, print "Invalid Arguments" and exit the program</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .45em"><code class="python">import sys

if len(sys.argv) != 4:
  print("Invalid Arguments")
  sys.exit()

try:
  with open(sys.argv[1]) as scanner1, \
       open(sys.argv[2]) as scanner2, \
       open(sys.argv[3], "w") as writer:

    <mark># -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-</mark>

except FileNotFoundError as e:
  print("Invalid Arguments")
  sys.exit()
except IOError as e:
  print("Invalid Arguments")
  sys.exit()
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">The first two represent input files, and the third one represents the desired output file.</p>
    <p style="font-size: .65em">...either input file is not an existing file, or the output file is an existing directory, print "Invalid Arguments" and exit the program</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .42em"><code class="python">
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">The program should open each input file and read the contents. Each input file will consist of a list of whole numbers, one per line. If there are any errors parsing the contents of either file, the program should print "Invalid Input" and exit.</p>
  </div>
</section>




<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .42em"><code class="python">for line in scanner1:
  line = line.strip()

for line in scanner2:
  line = line.strip()
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">The program should <mark>open each input file and read the contents</mark>. Each input file will consist of a list of whole numbers, one per line. If there are any errors parsing the contents of either file, the program should print "Invalid Input" and exit.</p>
  </div>
</section>




<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .42em"><code class="python">for line in scanner1:
  line = line.strip()
  <mark>input = int(line)</mark>

for line in scanner2:
  line = line.strip()
  <mark>input = int(line)</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">The program should open each input file and read the contents. Each input file will consist of a list of <mark>whole numbers</mark>, one per line. If there are any errors parsing the contents of either file, the program should print "Invalid Input" and exit.</p>
  </div>
</section>





<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .42em"><code class="python">for line in scanner1:
  line = line.strip()
  <mark>input = int(line)</mark>

for line in scanner2:
  line = line.strip()
  <mark>input = int(line)</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">The program should open each input file and read the contents. Each input file will consist of a list of whole numbers, one per line. If there are any <mark>errors parsing the contents</mark> of either file, the program should <mark>print "Invalid Input" and exit.</mark></p>
  </div>
</section>




<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .45em"><code class="python">import sys

if len(sys.argv) != 4:
  print("Invalid Arguments")
  sys.exit()

try:
  with open(sys.argv[1]) as scanner1, \
       open(sys.argv[2]) as scanner2, \
       open(sys.argv[3], "w") as writer:

    # -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-

except FileNotFoundError as e:
  print("Invalid Arguments")
  sys.exit()
except IOError as e:
  print("Invalid Arguments")
  sys.exit()
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">The program should open each input file and read the contents. Each input file will consist of a list of whole numbers, one per line. If there are any <mark>errors parsing the contents</mark> of either file, the program should <mark>print "Invalid Input" and exit.</mark></p>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .45em"><code class="python">import sys

if len(sys.argv) != 4:
  print("Invalid Arguments")
  sys.exit()

try:
  with open(sys.argv[1]) as scanner1, \
       open(sys.argv[2]) as scanner2, \
       open(sys.argv[3], "w") as writer:

    # -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-

except FileNotFoundError as e:
  print("Invalid Arguments")
  sys.exit()
except IOError as e:
  print("Invalid Arguments")
  sys.exit()
<mark>except ValueError as e:
  print("Invalid Input")
  sys.exit()</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">The program should open each input file and read the contents. Each input file will consist of a list of whole numbers, one per line. If there are any <mark>errors parsing the contents</mark> of either file, the program should <mark>print "Invalid Input" and exit.</mark></p>
  </div>
</section>




<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .42em"><code class="python">for line in scanner1:
  line = line.strip()
  input = int(line)
  <mark>if input % 2 == 0:
    # even
  else:
    # odd</mark>

for line in scanner2:
  line = line.strip()
  input = int(line)
  <mark>if input % 2 == 0:
    # even
  else:
    # odd</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">As the input is read, the program should keep track of both the count and sum of all <mark>even inputs and odd inputs.</mark></p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .42em"><code class="python"><mark>countEven = 0
countOdd = 0
sumEven = 0
sumOdd = 0</mark>

for line in scanner1:
  line = line.strip()
  input = int(line)
  if input % 2 == 0:
    <mark>countEven += 1
    sumEven += input</mark>
  else:
    <mark>countOdd += 1
    sumOdd += input</mark>

for line in scanner2:
  line = line.strip()
  input = int(line)
  if input % 2 == 0:
    <mark>countEven += 1
    sumEven += input</mark>
  else:
    <mark>countOdd += 1
    sumOdd += input</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">As the input is read, the program should <mark>keep track of both the count and sum</mark> of all even inputs and odd inputs.</p>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .42em"><code class="python">countEven = 0
countOdd = 0
sumEven = 0
sumOdd = 0

for line in scanner1:
  line = line.strip()
  input = int(line)
  if input % 2 == 0:
    countEven += 1
    sumEven += input
  else:
    countOdd += 1
    sumOdd += input

for line in scanner2:
  line = line.strip()
  input = int(line)
  if input % 2 == 0:
    countEven += 1
    sumEven += input
  else:
    countOdd += 1
    sumOdd += input

<mark># -=-=-=-=- MORE CODE GOES HERE -=-=-=-=- </mark></code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">Once all input is read, the program should create the output file and print the following four items, in this order, one per line: number of even inputs, sum of even inputs, number of odd inputs, sum of odd inputs.</p>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .45em"><code class="python">writer.write("{}\n".format(countEven))
writer.write("{}\n".format(sumEven))
writer.write("{}\n".format(countOdd))
writer.write("{}\n".format(sumOdd))</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">Once all input is read, the program should create the output file and <mark>print the following four items, in this order, one per line: number of even inputs, sum of even inputs, number of odd inputs, sum of odd inputs.</mark></p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .45em"><code class="python">writer.write("{}\n".format(countEven))
writer.write("{}\n".format(sumEven))
writer.write("{}\n".format(countOdd))
writer.write("{}\n".format(sumOdd))</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">Finally, when the program is done, it should simply print "Complete" and exit. Don't forget to close any open files!</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .45em"><code class="python">writer.write("{}\n".format(countEven))
writer.write("{}\n".format(sumEven))
writer.write("{}\n".format(countOdd))
writer.write("{}\n".format(sumOdd))

<mark>print("Complete")</mark></code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">Finally, when the program is done, <mark>it should simply print "Complete" and exit</mark>. Don't forget to close any open files!</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .45em"><code class="python">writer.write("{}\n".format(countEven))
writer.write("{}\n".format(sumEven))
writer.write("{}\n".format(countOdd))
writer.write("{}\n".format(sumOdd))

print("Complete")</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">Finally, when the program is done, it should simply print "Complete" and exit. <mark>Don't forget to close any open files!</mark></p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .45em"><code class="python">import sys

if len(sys.argv) != 4:
  print("Invalid Arguments")
  sys.exit()

try:
  <mark>with open(sys.argv[1]) as scanner1, \
       open(sys.argv[2]) as scanner2, \
       open(sys.argv[3], "w") as writer:</mark>

    # -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-

except FileNotFoundError as e:
  print("Invalid Arguments")
  sys.exit()
except IOError as e:
  print("Invalid Arguments")
  sys.exit()
except ValueError as e:
  print("Invalid Input")
  sys.exit()
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .65em">Finally, when the program is done, it should simply print "Complete" and exit. <mark>Don't forget to close any open files!</mark></p>
    <p style="font-size: .65em"><i>Already taken care of using<br>With Statement</i></p>
  </div>
</section>
