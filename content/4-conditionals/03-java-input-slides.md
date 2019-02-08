---
type: "reveal"
hidden: true
---

<section>
  <pre class="stretch" style="font-size: 0.5em;"><code class="java">// Load required classes
import java.util.Scanner;
import java.io.File;

public class Conditionals{
  public static void main(String[] args) throws Exception{
    // Scanner variable
    Scanner reader;

    // If an argument is present, we are reading from a file
    // specified in args[0]
    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    // If no argument, read from System.in
    }else{
      reader = new Scanner(System.in);
    }

    int x = reader.nextInt();
    System.out.println(x);
  }
}</code></pre>
</section>
<section>
  <pre class="stretch" style="font-size: 0.5em;"><code class="java">// Load required classes
<mark>import java.util.Scanner;
import java.io.File;</mark>

public class Conditionals{
  public static void main(String[] args) throws Exception{
    // Scanner variable
    Scanner reader;

    // If an argument is present, we are reading from a file
    // specified in args[0]
    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    // If no argument, read from System.in
    }else{
      reader = new Scanner(System.in);
    }

    int x = reader.nextInt();
    System.out.println(x);
  }
}</code></pre>
</section>
<section>
  <h3>Forgot Imports?</h3>
  <pre style="font-size: 0.5em;"><code class="no-highlight">error: cannot find symbol
    Scanner reader;
    ^
  symbol:   class Scanner
  location: class Conditionals</code></pre>
</section>
<section>
  <pre class="stretch" style="font-size: 0.5em;"><code class="java">// Load required classes
import java.util.Scanner;
import java.io.File;

public class Conditionals{
  public static void main(String[] args) <mark>throws Exception</mark>{
    // Scanner variable
    Scanner reader;

    // If an argument is present, we are reading from a file
    // specified in args[0]
    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    // If no argument, read from System.in
    }else{
      reader = new Scanner(System.in);
    }

    int x = reader.nextInt();
    System.out.println(x);
  }
}</code></pre>
</section>
<section>
  <h3>Forgot Throws Exception?</h3>
  <pre style="font-size: 0.5em;"><code class="no-highlight">error: unreported exception FileNotFoundException;
       must be caught or declared to be thrown
       reader = new Scanner(new File(args[0]));
               ^</code></pre>
</section>
<section>
  <pre class="stretch" style="font-size: 0.5em;"><code class="java">// Load required classes
import java.util.Scanner;
import java.io.File;

public class Conditionals{
  public static void main(String[] args) throws Exception{
    // Scanner variable
    <mark>Scanner reader;</mark>

    // If an argument is present, we are reading from a file
    // specified in args[0]
    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    // If no argument, read from System.in
    }else{
      reader = new Scanner(System.in);
    }

    int x = reader.nextInt();
    System.out.println(x);
  }
}</code></pre>
</section>
<section>
  <pre class="stretch" style="font-size: 0.5em;"><code class="java">// Load required classes
import java.util.Scanner;
import java.io.File;

public class Conditionals{
  public static void main(String[] args) throws Exception{
    // Scanner variable
    Scanner reader;

    // If an argument is present, we are reading from a file
    // specified in args[0]
    <mark>if(args.length > 0){
      reader = new Scanner(new File(args[0]));</mark>
    // If no argument, read from System.in
    }else{
      reader = new Scanner(System.in);
    }

    int x = reader.nextInt();
    System.out.println(x);
  }
}</code></pre>
</section>
<section>
  <pre class="stretch" style="font-size: 0.5em;"><code class="java">// Load required classes
import java.util.Scanner;
import java.io.File;

public class Conditionals{
  public static void main(String[] args) throws Exception{
    // Scanner variable
    Scanner reader;

    // If an argument is present, we are reading from a file
    // specified in args[0]
    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    // If no argument, read from System.in
    <mark>}else{
      reader = new Scanner(System.in);
    }</mark>

    int x = reader.nextInt();
    System.out.println(x);
  }
}</code></pre>
</section>
<section>
  <pre class="stretch" style="font-size: 0.5em;"><code class="java">// Load required classes
import java.util.Scanner;
import java.io.File;

public class Conditionals{
  public static void main(String[] args) throws Exception{
    // Scanner variable
    Scanner reader;

    // If an argument is present, we are reading from a file
    // specified in args[0]
    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    // If no argument, read from System.in
    }else{
      reader = new Scanner(System.in);
    }

    <mark>int x = reader.nextInt();</mark>
    System.out.println(x);
  }
}</code></pre>
</section>
<section>
  <h3>Reading Primitive Data Types</h3>
  <pre class="stretch" style="font-size: 0.9em; "><code class="java">int i = reader.nextInt();
byte b = reader.nextByte();
short s = reader.nextShort();
long l = reader.nextLong();

boolean bool = reader.nextBoolean();

float f = reader.nextFloat();
double d = reader.nextDouble();</code></pre>
</section>
<section>
  <pre class="stretch" style="font-size: 0.5em;"><code class="java">// Load required classes
<mark>import java.util.Scanner;
import java.io.File;</mark>

public class Conditionals{
  public static void main(String[] args) <mark>throws Exception</mark>{
    // Scanner variable
    <mark>Scanner reader;</mark>

    // If an argument is present, we are reading from a file
    // specified in args[0]
    <mark>if(args.length > 0){
      reader = new Scanner(new File(args[0]));</mark>
    // If no argument, read from System.in
    <mark>}else{
      reader = new Scanner(System.in);
    }</mark>

    <mark>int x = reader.nextInt();</mark>
    System.out.println(x);
  }
}</code></pre>
</section>
