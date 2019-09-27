---
type: "reveal"
hidden: true
---

<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">// Load required classes
import java.util.Scanner;
import java.io.File;

public class Exercise{
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
    <pre class="stretch" style="font-size: .37em"><code class="java">int m = reader.nextInt();
int n = reader.nextInt();

if(m > 0 && n > 0){

}else{
  System.out.println("Error - Invalid Input!");
}</code></pre>
  </div>
  <div style="width: 30%">
    <p>Handle Input</p>
  </div>
</section>



<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">int m = reader.nextInt();
int n = reader.nextInt();

if(m > 0 && n > 0){
  <mark>int[][] array = new int[m][n];</mark>

}else{
  System.out.println("Error - Invalid Input!");
}</code></pre>
  </div>
  <div style="width: 30%">
    <p>Create 2D Array</p>
  </div>
</section>





<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">int m = reader.nextInt();
int n = reader.nextInt();

if(m > 0 && n > 0){
  int[][] array = new int[m][n];

  <mark>for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++){
      array[i][j] = reader.nextInt();
    }
  }</mark>

}else{
  System.out.println("Error - Invalid Input!");
}</code></pre>
  </div>
  <div style="width: 30%">
    <p>Fill Array</p>
  </div>
</section>





<section>
  <div style="float: right; width: 70%">
    <pre class="stretch" style="font-size: .37em"><code class="java">int m = reader.nextInt();
int n = reader.nextInt();

if(m > 0 && n > 0){
  int[][] array = new int[m][n];

  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++){
      array[i][j] = reader.nextInt();
    }
  }

  <mark>for(int j = 0; j < n; j++){
    for(int i = 0; i < m; i++){
      System.out.print(array[i][j] + " ");
    }
    System.out.println();
  }</mark>

}else{
  System.out.println("Error - Invalid Input!");
}</code></pre>
  </div>
  <div style="width: 30%">
    <p>Transpose</p>
  </div>
</section>
