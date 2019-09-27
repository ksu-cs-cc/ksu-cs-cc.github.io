---
type: "reveal"
hidden: true
---

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;

public class Throw{

  public static void main(String[] args){
    Scanner reader;

    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    }else{
      reader = new Scanner(System.in);
    }
    int x = reader.nextInt();
    System.out.println(x);

  }
}</code></pre>
</section>

<section>
  <h2>Checked Exception</h2>
	<pre class="" style="font-size: .40em">8j-except/Throw.java:11: error: unreported exception FileNotFoundException;
must be caught or declared to be thrown
      reader = new Scanner(new File(args[0]));
               ^
1 error</pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;

public class Throw{

  public static void main(String[] args){
    Scanner reader;

    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    }else{
      reader = new Scanner(System.in);
    }
    int x = reader.nextInt();
    System.out.println(x);

  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;

public class Throw{

  public static void main(String[] args) <mark>throws FileNotFoundException</mark>{
    Scanner reader;

    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    }else{
      reader = new Scanner(System.in);
    }
    int x = reader.nextInt();
    System.out.println(x);

  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
<mark>import java.io.FileNotFoundException;</mark>

public class Throw{

  public static void main(String[] args) throws FileNotFoundException{
    Scanner reader;

    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    }else{
      reader = new Scanner(System.in);
    }
    int x = reader.nextInt();
    System.out.println(x);

  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Throw{

  public static void main(String[] args) throws FileNotFoundException{
    Scanner reader;

    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    }else{
      reader = new Scanner(System.in);
    }
    int x = reader.nextInt();
    System.out.println(x);

  }
}</code></pre>
</section>

<section>
  <h2>Custom Exceptions</h2>
</section>


<section>
	<pre class="stretch" style="font-size: .43em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Throw{

  public static void main(String[] args) throws FileNotFoundException{
    Scanner reader;

    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    }else{
      reader = new Scanner(System.in);
    }
    double x = reader.nextDouble();
    double y = reader.nextDouble();

    if(y == 0.0){
      System.out.println("Error");
    }else{
      System.out.println(x / y);
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .43em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Throw{

  public static void main(String[] args) throws FileNotFoundException{
    Scanner reader;

    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    }else{
      reader = new Scanner(System.in);
    }
    double x = reader.nextDouble();
    double y = reader.nextDouble();

    if(y == 0.0){
      <mark>System.out.println("Error");</mark>
    }else{
      System.out.println(x / y);
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .43em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Throw{

  public static void main(String[] args) throws FileNotFoundException{
    Scanner reader;

    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    }else{
      reader = new Scanner(System.in);
    }
    double x = reader.nextDouble();
    double y = reader.nextDouble();

    if(y == 0.0){
      <mark>throw new ArithmeticException("Divide by Zero!");</mark>
    }else{
      System.out.println(x / y);
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .43em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
<mark>import java.lang.ArithmeticException;</mark>

public class Throw{

  public static void main(String[] args) throws FileNotFoundException{
    Scanner reader;

    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    }else{
      reader = new Scanner(System.in);
    }
    double x = reader.nextDouble();
    double y = reader.nextDouble();

    if(y == 0.0){
      <mark>throw new ArithmeticException("Divide by Zero!");</mark>
    }else{
      System.out.println(x / y);
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .43em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.lang.ArithmeticException;

public class Throw{

  public static void main(String[] args) throws FileNotFoundException{
    Scanner reader;

    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    }else{
      reader = new Scanner(System.in);
    }
    double x = reader.nextDouble();
    double y = reader.nextDouble();

    if(y == 0.0){
      throw new ArithmeticException("Divide by Zero!");
    }else{
      System.out.println(x / y);
    }
  }
}</code></pre>
</section>
