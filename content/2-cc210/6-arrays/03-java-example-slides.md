---
type: "reveal"
hidden: true
---

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">// Load required classes
import java.util.Scanner;
import java.io.File;

public class Example{
  public static void main(String[] args) throws Exception{
    // Scanner variable
    Scanner reader;

    // If an argument is present,
    // we are reading from a file
    // specified in args[0]
    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    // If no argument, read from System.in
    }else{
      reader = new Scanner(System.in);
    }

    <mark>/* -=-=-=-=- MORE CODE GOES HERE -=-=-=-=- */</mark>
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
    <pre class="stretch" style="font-size: .37em"><code class="java">int numAssignments = reader.nextInt();
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Handle Input</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">int numAssignments = reader.nextInt();

<mark>if(numAssignments > 0){

}else{
  System.out.println("Invalid Input!");
}</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Handle Input</p>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">int numAssignments = reader.nextInt();

if(numAssignments > 0){

  <mark>int[] scores = new int[numAssignments];
  double[] weights = new double[numAssignments];</mark>

}else{
  System.out.println("Invalid Input!");
}</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Create Arrays</p>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">int numAssignments = reader.nextInt();

if(numAssignments > 0){

  int[] scores = new int[numAssignments];
  double[] weights = new double[numAssignments];

  <mark>for(int i = 0; i < numAssignments; i++){
    scores[i] = reader.nextInt();
    weights[i] = reader.nextDouble();
  }</mark>

}else{
  System.out.println("Invalid Input!");
}</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Fill Arrays</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">int numAssignments = reader.nextInt();

if(numAssignments > 0){

  int[] scores = new int[numAssignments];
  double[] weights = new double[numAssignments];

  for(int i = 0; i < numAssignments; i++){
    scores[i] = reader.nextInt();
    weights[i] = reader.nextDouble();
  }

  <mark>double sum = 0.0;
  for(double d : weights){
    sum += d;
  }

  if(sum == 1.0){

  }else{
    System.out.println("Error! Weights do not add...");
  }</mark>

}else{
  System.out.println("Invalid Input!");
}</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Check Weights</p>
  </div>
</section>


<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">int numAssignments = reader.nextInt();

if(numAssignments > 0){

  int[] scores = new int[numAssignments];
  double[] weights = new double[numAssignments];
  for(int i = 0; i < numAssignments; i++){
    scores[i] = reader.nextInt();
    weights[i] = reader.nextDouble();
  }

  double sum = 0.0;
  for(double d : weights){
    sum += d;
  }
  if(sum == 1.0){

    <mark>double totalScore = 0.0;
    for(int j = 0; j < numAssignments; j++){
      totalScore += scores[j] * weights[j];
    }
    System.out.println(totalScore);</mark>

  }else{
    System.out.println("Error! Weights do not add...");
  }
}else{
  System.out.println("Invalid Input!");
}</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Calculate Score</p>
  </div>
</section>

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">int numAssignments = reader.nextInt();

if(numAssignments > 0){

  int[] scores = new int[numAssignments];
  double[] weights = new double[numAssignments];
  for(int i = 0; i < numAssignments; i++){
    scores[i] = reader.nextInt();
    weights[i] = reader.nextDouble();
  }

  double sum = 0.0;
  for(double d : weights){
    sum += d;
  }
  if(sum == 1.0){

    double totalScore = 0.0;
    for(int j = 0; j < numAssignments; j++){
      totalScore += scores[j] * weights[j];
    }
    System.out.println(totalScore);

  }else{
    System.out.println("Error! Weights do not add...");
  }
}else{
  System.out.println("Invalid Input!");
}</mark>
</code></pre>
  </div>
  <div style="width: 30%">
    <p>Done!</p>
  </div>
</section>
