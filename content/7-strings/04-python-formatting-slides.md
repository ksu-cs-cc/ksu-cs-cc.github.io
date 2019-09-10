---
type: "reveal"
hidden: true
---

<section>
  <h2>Concatenation</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23

print("Sum: " + str(sum) + " Avg: " + str(avg) + ".")
 </code></pre>
</section>

<section>
  <h2>Concatenation</h2>
  <pre class="" style="font-size: .53em"><code class="python">int <mark>sum = 123</mark>;
avg = 1.23

print("Sum: " + <mark>str(sum)</mark> + " Avg: " + str(avg) + ".")
 </code></pre>
</section>

<section>
  <h2>Concatenation</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23

print("Sum: " + <mark>"123"</mark> + " Avg: " + str(avg) + ".")
 </code></pre>
</section>

<section>
  <h2>Concatenation</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
double <mark>avg = 1.23</mark>;

print("Sum: " + "123" + " Avg: " + <mark>str(avg)</mark> + ".")
 </code></pre>
</section>

<section>
  <h2>Concatenation</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23

print("Sum: " + "123" + " Avg: " + <mark>"1.23"</mark> + ".")
 </code></pre>
</section>

<section>
  <h2>Concatenation</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23

print("Sum: " + "123" + " Avg: " + "1.23" + ".")
// Sum: 123 Avg: 1.23. </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23
name = "Student"

output = "{}: Score: {:5} Average: {:8.4f}."

print(output.format(name, sum, avg))
 </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23
name = "Student"

output = "{}: Score: {:5} Average: {:8.4f}."

print(<mark>output.format(name, sum, avg)</mark>)
 </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23
name = "Student"

output = <mark>"{}: Score: {:5} Average: {:8.4f}."</mark>

print(<mark>output</mark>.format(name, sum, avg))
// <mark>"{}: Score: {:5} Average: {:8.4f}."</mark> </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23
name = "Student"

output = "{}: Score: {:5} Average: {:8.4f}."

print(output.format(<mark>name</mark>, sum, avg))
// "<mark>{}</mark>: Score: {:5} Average: {:8.4f}." </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23
name = "Student"

output = "{}: Score: {:5} Average: {:8.4f}."

print(output.format(<mark>name</mark>, sum, avg))
// "<mark>Student</mark>: Score: {:5} Average: {:8.4f}." </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23
name = "Student"

output = "{}: Score: {:5} Average: {:8.4f}."

print(output.format(name, <mark>sum</mark>, avg))
// "Student: Score: <mark>{:5}</mark> Average: {:8.4f}." </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23
name = "Student"

output = "{}: Score: {:5} Average: {:8.4f}."

print(output.format(name, <mark>sum</mark>, avg))
// "Student: Score: <mark>  123</mark> Average: {:8.4f}." </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23
name = "Student"

output = "{}: Score: {:5} Average: {:8.4f}."

print(output.format(name, sum, <mark>avg</mark>))
// "Student: Score:   123 Average: <mark>{:8.4f}</mark>." </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23
name = "Student"

output = "{}: Score: {:5} Average: {:8.4f}."

print(output.format(name, sum, <mark>avg</mark>))
// "Student: Score:   123 Average: <mark>  1.2300</mark>." </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23
name = "Student"

output = "{}: Score: {:5} Average: {:8.4f}."

print(output.format(name, sum, <mark>avg</mark>))
// <mark>"Student: Score:   123 Average:   1.2300."</mark> </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="python">sum = 123
avg = 1.23
name = "Student"

output = "{}: Score: {:5} Average: {:8.4f}."

print(output.format(name, sum, <mark>avg</mark>))
// Student: Score:   123 Average:   1.2300.</code></pre>
</section>
