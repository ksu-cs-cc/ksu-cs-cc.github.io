---
type: "reveal"
hidden: true
---

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.util.InputMismatchException;
import java.io.FileNotFoundException;

public class Resources{

  public static void main(String[] args){
    Scanner reader;

    try{
      reader = new Scanner(new File(args[0]))
      int x = reader.nextInt();
      System.out.println(x + 5);

    }catch(InputMismatchException e){
      System.out.println("Error: Invalid Number Format!");
    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }finally{
      reader.close();
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.util.InputMismatchException;
import java.io.FileNotFoundException;

public class Resources{

  public static void main(String[] args){
    <mark>Scanner reader;</mark>

    try{
      reader = new Scanner(new File(args[0]))
      int x = reader.nextInt();
      System.out.println(x + 5);

    }catch(InputMismatchException e){
      System.out.println("Error: Invalid Number Format!");
    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }finally{
      reader.close();
    }
  }
}</code></pre>
</section>



<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.util.InputMismatchException;
import java.io.FileNotFoundException;

public class Resources{

  public static void main(String[] args){
    <mark>Scanner reader;</mark>

    try{
      <mark>reader = new Scanner(new File(args[0]))</mark>
      int x = reader.nextInt();
      System.out.println(x + 5);

    }catch(InputMismatchException e){
      System.out.println("Error: Invalid Number Format!");
    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }finally{
      reader.close();
    }
  }
}</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.util.InputMismatchException;
import java.io.FileNotFoundException;

public class Resources{

  public static void main(String[] args){
    <mark>Scanner reader;</mark>

    try{
      <mark>reader = new Scanner(new File(args[0]))</mark>
      int x = reader.nextInt();
      System.out.println(x + 5);

    }catch(InputMismatchException e){
      System.out.println("Error: Invalid Number Format!");
    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }finally{
      <mark>reader.close();</mark>
    }
  }
}</code></pre>
</section>



<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.util.InputMismatchException;
import java.io.FileNotFoundException;

public class Resources{

  public static void main(String[] args){
    Scanner reader;

    <mark>try(
      Scanner reader = new Scanner(new File(args[0]))
    ){</mark>
      int x = reader.nextInt();
      System.out.println(x + 5);

    }catch(InputMismatchException e){
      System.out.println("Error: Invalid Number Format!");
    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }finally{
      reader.close();
    }
  }
}</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.util.InputMismatchException;
import java.io.FileNotFoundException;

public class Resources{

  public static void main(String[] args){
    <s>Scanner reader;</s>

    <mark>try(
      Scanner reader = new Scanner(new File(args[0]))
    ){</mark>
      int x = reader.nextInt();
      System.out.println(x + 5);

    }catch(InputMismatchException e){
      System.out.println("Error: Invalid Number Format!");
    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }<s>finally{
      reader.close();
    }</s>
  }
}</code></pre>
</section>



<section>
	<pre class="stretch" style="font-size: .45em"><code class="java">import java.util.Scanner;
import java.io.File;
import java.util.InputMismatchException;
import java.io.FileNotFoundException;

public class Resources{

  public static void main(String[] args){

    try(
      Scanner reader = new Scanner(new File(args[0]))
    ){
      int x = reader.nextInt();
      System.out.println(x + 5);

    }catch(InputMismatchException e){
      System.out.println("Error: Invalid Number Format!");
    }catch(FileNotFoundException e){
      System.out.println("Error: File Not Found!");
    }
  }
}</code></pre>
</section>
