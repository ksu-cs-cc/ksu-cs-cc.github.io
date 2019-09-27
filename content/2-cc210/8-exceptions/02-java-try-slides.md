---
type: "reveal"
hidden: true
---

<section>
	<img class="stretch plain" src="/images/8.4.handle.png">
</section>

<section>
	<img class="stretch plain" src="/images/8.4.try.png">
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;

public class Example{

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

public class Example{

  public static void main(String[] args){
    Scanner reader;

    <mark>try{</mark>

    if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    }else{
      reader = new Scanner(System.in);
    }
    int x = reader.nextInt();
    System.out.println(x);

    <mark>}</mark>
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

    <mark>if(args.length > 0){
      reader = new Scanner(new File(args[0]));
    }else{
      reader = new Scanner(System.in);
    }
    int x = reader.nextInt();
    System.out.println(x);</mark>

    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      <mark>if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);</mark>

    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }
  }
}</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }<mark>catch(Exception e){</mark>

    <mark>}</mark>
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(<mark>Exception e</mark>){

    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
<mark>import java.lang.Exception;</mark>

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(<mark>Exception e</mark>){

    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.lang.Exception;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(Exception e){

    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.lang.Exception;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(Exception e){
      <mark>System.out.println("Error!");</mark>
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.lang.Exception;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(Exception e){
      System.out.println("Error!");
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.lang.Exception;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        <mark>reader = new Scanner(new File(args[0]));</mark>
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(Exception e){
      System.out.println("Error!");
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.lang.Exception;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(<mark>Exception e</mark>){
      System.out.println("Error!");
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.lang.Exception;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(<mark>FileNotFoundException e</mark>){
      System.out.println("Error!");
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
<mark>import java.lang.Exception;</mark>

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(FileNotFoundException e){
      System.out.println(<mark>"Error!"</mark>);
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
<mark>import java.io.FileNotFoundException;</mark>

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(FileNotFoundException e){
      System.out.println(<mark>"Error: File Not Found!"</mark>);
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .40em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      <mark>int x = reader.nextInt();</mark>
      System.out.println(x);

    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .40em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
<mark>import java.io.IOException;</mark>

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }<mark>catch(IOException e){
      System.out.println("Error: IO Exception!");
    }</mark>
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .40em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }catch(IOException e){
      System.out.println("Error: IO Exception!");
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .40em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    <mark>}catch(IOException e){
      System.out.println("Error: IO Exception!");
    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }</mark>
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .40em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    <mark style="background-color: red">}catch(IOException e){
      System.out.println("Error: IO Exception!");
    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }</mark>
  }
}</code></pre>
</section>

<section>
	<h2>Exception Hierarchy</h2>
	<img class="stretch plain" src="/images/8.7.j.3.filenotfound.png">
</section>

<section>
	<pre class="stretch" style="font-size: .40em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    <mark style="background-color: red">}catch(IOException e){
      System.out.println("Error: IO Exception!");
    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }</mark>
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .40em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    <mark>}catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }catch(IOException e){
      System.out.println("Error: IO Exception!");
    }</mark>
  }
}</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .40em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }catch(IOException e){
      System.out.println("Error: IO Exception!");
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .37em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = <mark>reader.nextInt();</mark>
      System.out.println(x);

    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }catch(IOException e){
      System.out.println("Error: IO Exception!");
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .37em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
<mark>import java.util.InputMismatchException;</mark>

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }catch(IOException e){
      System.out.println("Error: IO Exception!");
    }<mark>catch(InputMismatchException e){
      System.out.println("Error: Input Does Not Match Expected Format!");
    }</mark>
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .37em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException
import java.util.InputMismatchException;

public class Example{

  public static void main(String[] args){
    Scanner reader;

    try{

      if(args.length > 0){
        reader = new Scanner(new File(args[0]));
      }else{
        reader = new Scanner(System.in);
      }
      int x = reader.nextInt();
      System.out.println(x);

    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }catch(IOException e){
      System.out.println("Error: IO Exception!");
    }catch(InputMismatchException e){
      System.out.println("Error: Input Does Not Match Expected Format!");
    }
  }
}</code></pre>
</section>
