---
type: "reveal"
hidden: true
---

<section>
	<h2>Problem Statement</h2>
</section>
<section>
	<p style="font-size: 0.5em">Write a program that will calculate weighted grades for students in a college course. The input will be given in a comma-delimited format. The first line will contain a number of weights as floating-point numbers, separated by commas. The first entry should be ignored.</p>
	<p style="font-size: 0.5em">Each subsequent line of input will contain information for a student. The first entry on that line will contain that student’s name. The rest of the line will contain that student’s scores on each assignment as an integer value, separated by commas. Input will be terminated by the end of the input file, or by a blank line when input is provided via the terminal.</p>
	<p style="font-size: 0.5em">It is guaranteed that at least two lines of input will be provided, the first containing the weights and at least one additional line containing data for a student. In addition, it is guaranteed that each line of input will contain the same number of parts.</p>
	<p style="font-size: 0.5em">The program should output the student’s name, followed by a colon, and a space, and then the student’s score. The score should be formatted to be exactly 5 characters wide, with exactly two characters after the decimal point.</p>
</section>
<section>
	<h2>Yikes!</h2>
	<p>Let's break it down into smaller parts</p>
</section>
<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">// Load required classes
import java.util.Scanner;
import java.io.File;

public class Example{

  public static void main(String[] args) throws Exception{
    // Scanner variable
    Scanner reader;

    // If an argument is present, read from a file
    // specified in args[0]
    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    // If no argument, read from System.in
    }else{
      reader = new Scanner(System.in);
    }

    /* -=-=-=-=- MORE CODE GOES HERE -=-=-=-=- */

  }
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Skeleton</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first line will contain a number of weights as floating-point numbers, separated by commas. The first entry should be ignored.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em"><mark>The first line</mark> will contain a number of weights as floating-point numbers, separated by commas. The first entry should be ignored.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java"><mark>String weightLine = reader.nextLine();</mark>

</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em"><mark>The first line</mark> will contain a number of weights as floating-point numbers, separated by commas. The first entry should be ignored.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">String weightLine = reader.nextLine();

</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first line <mark>will contain a number of weights</mark> as floating-point numbers, <mark>separated by commas</mark>. The first entry should be ignored.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">String weightLine = reader.nextLine();
<mark>String[] weightParts = weightLine.split(",");</mark>

</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first line <mark>will contain a number of weights</mark> as floating-point numbers, <mark>separated by commas</mark>. The first entry should be ignored.</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">String weightLine = reader.nextLine();
String[] weightParts = weightLine.split(",");

</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first line will contain <mark>a number of weights as floating-point numbers</mark>, separated by commas. The first entry should be ignored.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">String weightLine = reader.nextLine();
String[] weightParts = weightLine.split(",");

<mark>double[] weights = new double[weightParts.length];</mark>

</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first line will contain <mark>a number of weights as floating-point numbers</mark>, separated by commas. The first entry should be ignored.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">String weightLine = reader.nextLine();
String[] weightParts = weightLine.split(",");

double[] weights = new double[weightParts.length];

</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first line will contain <mark>a number of weights</mark> as floating-point numbers, separated by commas. The first entry should be ignored.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">String weightLine = reader.nextLine();
String[] weightParts = weightLine.split(",");

double[] weights = new double[weightParts.length];

<mark>for(int i = 0; i &lt; weights.length; i++){
  weights[i] = weightParts[i];
}</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first line will contain <mark>a number of weights</mark> as floating-point numbers, separated by commas. The first entry should be ignored.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">String weightLine = reader.nextLine();
String[] weightParts = weightLine.split(",");

double[] weights = new double[weightParts.length];

for(int i = 0; i &lt; weights.length; i++){
  weights[i] = <mark>weightParts[i];</mark>
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first line will contain a number of weights as <mark>floating-point numbers</mark>, separated by commas. The first entry should be ignored.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">String weightLine = reader.nextLine();
String[] weightParts = weightLine.split(",");

double[] weights = new double[weightParts.length];

for(int i = 0; i &lt; weights.length; i++){
  weights[i] = <mark>Double.parseDouble(weightParts[i]);</mark>
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first line will contain a number of weights as <mark>floating-point numbers</mark>, separated by commas. The first entry should be ignored.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">String weightLine = reader.nextLine();
String[] weightParts = weightLine.split(",");

double[] weights = new double[weightParts.length];

for(int i = 0; i &lt; weights.length; i++){
  weights[i] = Double.parseDouble(weightParts[i]);
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first line will contain a number of weights as floating-point numbers, separated by commas. <mark>The first entry should be ignored.</mark></p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">String weightLine = reader.nextLine();
String[] weightParts = weightLine.split(",");

double[] weights = new double[weightParts.length];

for(int i = <mark>0</mark>; i &lt; weights.length; i++){
  weights[i] = Double.parseDouble(weightParts[i]);
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first line will contain a number of weights as floating-point numbers, separated by commas. <mark>The first entry should be ignored.</mark></p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">String weightLine = reader.nextLine();
String[] weightParts = weightLine.split(",");

double[] weights = new double[weightParts.length];

for(int i = <mark>1</mark>; i &lt; weights.length; i++){
  weights[i] = Double.parseDouble(weightParts[i]);
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first line will contain a number of weights as floating-point numbers, separated by commas. <mark>The first entry should be ignored.</mark></p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">String weightLine = reader.nextLine();
String[] weightParts = weightLine.split(",");

double[] weights = new double[weightParts.length];

for(int i = 1; i &lt; weights.length; i++){
  weights[i] = Double.parseDouble(weightParts[i]);
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first line will contain a number of weights as floating-point numbers, separated by commas. The first entry should be ignored.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">

</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">Each subsequent line of input will contain information for a student. ... Input will be terminated by the end of the input file, or by a blank line when input is provided via the terminal.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">

</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em"><mark>Each subsequent line of input</mark> will contain information for a student. ... Input will be terminated by the end of the input file, or by a blank line when input is provided via the terminal.</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java"><mark>while(reader.hasNext()){

}</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em"><mark>Each subsequent line of input</mark> will contain information for a student. ... Input will be terminated by the end of the input file, or by a blank line when input is provided via the terminal.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">Each subsequent <mark>line of input will contain information for a student</mark>. ... Input will be terminated by the end of the input file, or by a blank line when input is provided via the terminal.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  <mark>String line = reader.nextLine();</mark>

  <mark>// parse the input</mark>
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">Each subsequent <mark>line of input will contain information for a student</mark>. ... Input will be terminated by the end of the input file, or by a blank line when input is provided via the terminal.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();

  // parse the input
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">Each subsequent line of input will contain information for a student. ... Input will be terminated by the end of the input file, <mark>or by a blank line when input is provided via the terminal.</mark></p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  <mark>if(line.length() == 0){</mark>
    <mark>break;</mark>
  <mark>}</mark>

  // parse the input
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">Each subsequent line of input will contain information for a student. ... Input will be terminated by the end of the input file, <mark>or by a blank line when input is provided via the terminal.</mark></p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  // parse the input
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">Each subsequent line of input will contain information for a student. ... Input will be terminated by the end of the input file, or by a blank line when input is provided via the terminal.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  // parse the input
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first entry on that line will contain that student’s name. The rest of the line will contain that student’s scores on each assignment as an integer value, separated by commas.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  // parse the input
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first entry on that line will contain that student’s name. The rest of the line will contain that student’s scores on each assignment as an integer value, <mark>separated by commas.</mark></p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  <mark>String[] parts = line.split(",");</mark>
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first entry on that line will contain that student’s name. The rest of the line will contain that student’s scores on each assignment as an integer value, <mark>separated by commas.</mark></p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");
}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first entry on that line will contain that student’s name. <mark>The rest of the line will contain that student’s scores on each assignment as an integer value</mark>, separated by commas.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  <mark>for(int j = 1; j &lt; parts.length; j++){
    parts[j];
  }</mark>

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first entry on that line will contain that student’s name. <mark>The rest of the line will contain that student’s scores on each assignment as an integer value</mark>, separated by commas.</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  for(int j = 1; j &lt; parts.length; j++){
    parts[j];
  }

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first entry on that line will contain that student’s name. The rest of the line will contain that student’s scores on each assignment as an <mark>integer value</mark>, separated by commas.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  for(int j = 1; j &lt; parts.length; j++){
    <mark>Integer.parseInt(parts[j]);</mark>
  }

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The first entry on that line will contain that student’s name. The rest of the line will contain that student’s scores on each assignment as an <mark>integer value</mark>, separated by commas.</p>
  </div>
</section>







<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  for(int j = 1; j &lt; parts.length; j++){
    Integer.parseInt(parts[j]);
  }

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">Write a program that will calculate weighted grades for students in a college course.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  for(int j = 1; j &lt; parts.length; j++){
    Integer.parseInt(parts[j]);
  }

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">Write a program that will calculate <mark>weighted grades</mark> for students in a college course.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  for(int j = 1; j &lt; parts.length; j++){
    Integer.parseInt(parts[j]);
  }

}
</code></pre>
  </div>
	<div style="width: 30%">
    <p style="font-size: .5em">Write a program that will calculate <mark>weighted grades</mark> for students in a college course.<p>
		<p style="font-size: .5em; font-family: monospace">Total =<br>Sum(Score[i] * Weight[i])</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  for(int j = 1; j &lt; parts.length; j++){
    <mark>weights[j] * Integer.parseInt(parts[j]);</mark>
  }

}
</code></pre>
  </div>
	<div style="width: 30%">
    <p style="font-size: .5em">Write a program that will calculate <mark>weighted grades</mark> for students in a college course.<p>
		<p style="font-size: .5em; font-family: monospace">Total =<br>Sum(Score[i] * Weight[i])</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  <mark>double totalScore = 0.0;</mark>
  for(int j = 1; j &lt; parts.length; j++){
    <mark>totalScore += </mark>weights[j] * Integer.parseInt(parts[j]);
  }

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">Write a program that will calculate <mark>weighted grades</mark> for students in a college course.<p>
		<p style="font-size: .5em; font-family: monospace">Total =<br>Sum(Score[i] * Weight[i])</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  double totalScore = 0.0;
  for(int j = 1; j &lt; parts.length; j++){
    totalScore += weights[j] * Integer.parseInt(parts[j]);
  }

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The program should output the student’s name, followed by a colon, and a space, and then the student’s score. The score should be formatted to be exactly 5 characters wide, with exactly two characters after the decimal point.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  double totalScore = 0.0;
  for(int j = 1; j &lt; parts.length; j++){
    totalScore += weights[j] * Integer.parseInt(parts[j]);
  }

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em"><mark>The program should output</mark> the student’s name, followed by a colon, and a space, and then the student’s score. The score should be formatted to be exactly 5 characters wide, with exactly two characters after the decimal point.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  double totalScore = 0.0;
  for(int j = 1; j &lt; parts.length; j++){
    totalScore += weights[j] * Integer.parseInt(parts[j]);
  }

  <mark>System.out.println();</mark>

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em"><mark>The program should output</mark> the student’s name, followed by a colon, and a space, and then the student’s score. The score should be formatted to be exactly 5 characters wide, with exactly two characters after the decimal point.</p>
  </div>
</section>




<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  double totalScore = 0.0;
  for(int j = 1; j &lt; parts.length; j++){
    totalScore += weights[j] * Integer.parseInt(parts[j]);
  }

  <mark>...();</mark>

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The program should output the student’s name, followed by a colon, and a space, and then the student’s score. The score should be formatted to be exactly 5 characters wide, with exactly two characters after the decimal point.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  double totalScore = 0.0;
  for(int j = 1; j &lt; parts.length; j++){
    totalScore += weights[j] * Integer.parseInt(parts[j]);
  }

  ...();

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The program should output the student’s name, followed by a colon, and a space, and then the student’s score. The score should be <mark>formatted to be exactly 5 characters wide</mark>, with exactly two characters after the decimal point.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  double totalScore = 0.0;
  for(int j = 1; j &lt; parts.length; j++){
    totalScore += weights[j] * Integer.parseInt(parts[j]);
  }

  ...(<mark>String.format()</mark>);

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The program should output the student’s name, followed by a colon, and a space, and then the student’s score. The score should be <mark>formatted to be exactly 5 characters wide</mark>, with exactly two characters after the decimal point.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  double totalScore = 0.0;
  for(int j = 1; j &lt; parts.length; j++){
    totalScore += weights[j] * Integer.parseInt(parts[j]);
  }

  ...(String.format());

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The program should output the <mark>student’s name, followed by a colon, and a space,</mark> and then the student’s score. The score should be formatted to be exactly 5 characters wide, with exactly two characters after the decimal point.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  double totalScore = 0.0;
  for(int j = 1; j &lt; parts.length; j++){
    totalScore += weights[j] * Integer.parseInt(parts[j]);
  }

  ...(String.format("<mark>%s: </mark>", <mark>parts[0]</mark>));

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The program should output the <mark>student’s name, followed by a colon, and a space,</mark> and then the student’s score. The score should be formatted to be exactly 5 characters wide, with exactly two characters after the decimal point.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  double totalScore = 0.0;
  for(int j = 1; j &lt; parts.length; j++){
    totalScore += weights[j] * Integer.parseInt(parts[j]);
  }

  ...(String.format("%s: ", parts[0]));

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The program should output the student’s name, followed by a colon, and a space, <mark>and then the student’s score.</mark> The score should be formatted to be exactly 5 characters wide, with exactly two characters after the decimal point.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  double totalScore = 0.0;
  for(int j = 1; j &lt; parts.length; j++){
    totalScore += weights[j] * Integer.parseInt(parts[j]);
  }

  ...(String.format("%s: <mark>%f</mark>", parts[0], <mark>totalScore</mark>));

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The program should output the student’s name, followed by a colon, and a space, <mark>and then the student’s score.</mark> The score should be formatted to be exactly 5 characters wide, with exactly two characters after the decimal point.</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  double totalScore = 0.0;
  for(int j = 1; j &lt; parts.length; j++){
    totalScore += weights[j] * Integer.parseInt(parts[j]);
  }

  ...(String.format("%s: %f", parts[0], totalScore));

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The program should output the student’s name, followed by a colon, and a space, and then the student’s score. <mark>The score should be formatted to be exactly 5 characters wide, with exactly two characters after the decimal point.</mark></p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  double totalScore = 0.0;
  for(int j = 1; j &lt; parts.length; j++){
    totalScore += weights[j] * Integer.parseInt(parts[j]);
  }

  ...(String.format("%s: <mark>%5.2f</mark>", parts[0], totalScore));

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The program should output the student’s name, followed by a colon, and a space, and then the student’s score. <mark>The score should be formatted to be exactly 5 characters wide, with exactly two characters after the decimal point.</mark></p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  double totalScore = 0.0;
  for(int j = 1; j &lt; parts.length; j++){
    totalScore += weights[j] * Integer.parseInt(parts[j]);
  }

  ...(String.format("%s: %5.2f", parts[0], totalScore));

}
</code></pre>
  </div>
  <div style="width: 30%">
    <p style="font-size: .5em">The program should output the student’s name, followed by a colon, and a space, and then the student’s score. The score should be formatted to be exactly 5 characters wide, with exactly two characters after the decimal point.</p>
  </div>
</section>

<section>
    <pre class="stretch" style="font-size: .44em"><code class="java">String weightLine = reader.nextLine();
String[] weightParts = weightLine.split(",");

double[] weights = new double[weightParts.length];

for(int i = 1; i &lt; weights.length; i++){
  weights[i] = Double.parseDouble(weightParts[i]);
}

while(reader.hasNext()){
  String line = reader.nextLine();
  if(line.length() == 0){
    break;
  }

  String[] parts = line.split(",");

  double totalScore = 0.0;
  for(int j = 1; j &lt; parts.length; j++){
    totalScore += weights[j] * Integer.parseInt(parts[j]);
  }

  System.out.println(String.format("%s: %5.2f", parts[0], totalScore));

}</code></pre>
</section>
