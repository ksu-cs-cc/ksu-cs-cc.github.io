---
type: "reveal"
hidden: true
---

<section>
  <h2>Concatenation</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;

System.out.println("Sum: " + sum + " Avg: " + avg + ".");
 </code></pre>
</section>

<section>
  <h2>Concatenation</h2>
  <pre class="" style="font-size: .53em"><code class="java">int <mark>sum = 123</mark>;
double avg = 1.23;

System.out.println("Sum: " + <mark>sum</mark> + " Avg: " + avg + ".");
 </code></pre>
</section>

<section>
  <h2>Concatenation</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;

System.out.println("Sum: " + <mark>123</mark> + " Avg: " + avg + ".");
 </code></pre>
</section>

<section>
  <h2>Concatenation</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double <mark>avg = 1.23</mark>;

System.out.println("Sum: " + 123 + " Avg: " + <mark>avg</mark> + ".");
 </code></pre>
</section>

<section>
  <h2>Concatenation</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;

System.out.println("Sum: " + 123 + " Avg: " + <mark>1.23</mark> + ".");
 </code></pre>
</section>

<section>
  <h2>Concatenation</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;

System.out.println("Sum: " + 123 + " Avg: " + 1.23 + ".");
// Sum: 123 Avg: 1.23. </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;
String name = "Student";

String output = "%s: Score: %5d Average: %8.4f.";

System.out.println(String.format(output, name, sum, avg));
 </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;
String name = "Student";

String output = "%s: Score: %5d Average: %8.4f.";

System.out.println(<mark>String.format(output, name, sum, avg)</mark>);
 </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;
String name = "Student";

String output = <mark>"%s: Score: %5d Average: %8.4f.";</mark>;

System.out.println(String.format(<mark>output</mark>, name, sum, avg));
// <mark>"%s: Score: %5d Average: %8.4f."</mark> </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;
String name = "Student";

String output = "%s: Score: %5d Average: %8.4f.";

System.out.println(String.format(output, <mark>name</mark>, sum, avg));
// "<mark>%s</mark>: Score: %5d Average: %8.4f." </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;
String name = "Student";

String output = "%s: Score: %5d Average: %8.4f.";

System.out.println(String.format(output, <mark>name</mark>, sum, avg));
// "<mark>Student</mark>: Score: %5d Average: %8.4f." </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;
String name = "Student";

String output = "%s: Score: %5d Average: %8.4f.";

System.out.println(String.format(output, name, <mark>sum</mark>, avg));
// "Student: Score: <mark>%5d</mark> Average: %8.4f." </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;
String name = "Student";

String output = "%s: Score: %5d Average: %8.4f.";

System.out.println(String.format(output, name, <mark>sum</mark>, avg));
// "Student: Score: <mark>  123</mark> Average: %8.4f." </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;
String name = "Student";

String output = "%s: Score: %5d Average: %8.4f.";

System.out.println(String.format(output, name, sum, <mark>avg</mark>));
// "Student: Score:   123 Average: <mark>%8.4f</mark>." </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;
String name = "Student";

String output = "%s: Score: %5d Average: %8.4f.";

System.out.println(String.format(output, name, sum, <mark>avg</mark>));
// "Student: Score:   123 Average: <mark>  1.2300</mark>." </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;
String name = "Student";

String output = "%s: Score: %5d Average: %8.4f.";

System.out.println(String.format(output, name, sum, avg));
// <mark>"Student: Score:   123 Average:   1.2300."</mark> </code></pre>
</section>

<section>
  <h2>Formatted Strings</h2>
  <pre class="" style="font-size: .53em"><code class="java">int sum = 123;
double avg = 1.23;
String name = "Student";

String output = "%s: Score: %5d Average: %8.4f.";

System.out.println(String.format(output, name, sum, avg));
// Student: Score:   123 Average:   1.2300.</code></pre>
</section>
