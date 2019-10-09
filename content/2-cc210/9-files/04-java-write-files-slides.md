---
type: "reveal"
hidden: true
---

<section>
	<pre class="stretch" style="font-size: .276em"><code class="java">public class Write{
  public static void main(String[] args){

  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .276em"><code class="java">public class Write{
  public static void main(String[] args){
    <mark>try(
      BufferedWriter writer = Files.newBufferedWriter(Paths.get(args[0]));
    ){</mark>


    <mark>}catch(Exception e){
      //something went wrong
      System.out.println("Error: unknown error!");
      return;
    }</mark>
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .276em"><code class="java">public class Write{
  public static void main(String[] args){
    try(
      BufferedWriter writer = Files.newBufferedWriter(Paths.get(args[0]));
    ){


    }catch(Exception e){
      //something went wrong
      System.out.println("Error: unknown error!");
      return;
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .276em"><code class="java"><mark>import java.io.BufferedWriter;</mark>

public class Write{
  public static void main(String[] args){
    try(
      <mark>BufferedWriter</mark> writer = Files.newBufferedWriter(Paths.get(args[0]));
    ){


    }catch(Exception e){
      //something went wrong
      System.out.println("Error: unknown error!");
      return;
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .276em"><code class="java">import java.io.BufferedWriter;
<mark>import java.nio.file.Files;</mark>

public class Write{
  public static void main(String[] args){
    try(
      BufferedWriter writer = <mark>Files</mark>.newBufferedWriter(Paths.get(args[0]));
    ){


    }catch(Exception e){
      //something went wrong
      System.out.println("Error: unknown error!");
      return;
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .276em"><code class="java">import java.io.BufferedWriter;
import java.nio.file.Files;
<mark>import java.nio.file.Paths;</mark>

public class Write{
  public static void main(String[] args){
    try(
      BufferedWriter writer = Files.newBufferedWriter(<mark>Paths</mark>.get(args[0]));
    ){


    }catch(Exception e){
      //something went wrong
      System.out.println("Error: unknown error!");
      return;
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .276em"><code class="java">import java.io.BufferedWriter;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Write{
  public static void main(String[] args){
    try(
      BufferedWriter writer = Files.newBufferedWriter(Paths.get(args[0]));
    ){


    }catch(Exception e){
      //something went wrong
      System.out.println("Error: unknown error!");
      return;
    }
  }
}</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .276em"><code class="java">import java.io.BufferedWriter;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Write{
  public static void main(String[] args){
    try(
      BufferedWriter writer = Files.newBufferedWriter(Paths.get(args[0]));
    ){

      <mark>writer.write("Hello World");
      writer.newLine();</mark>

    }catch(Exception e){
      //something went wrong
      System.out.println("Error: unknown error!");
      return;
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .276em"><code class="java">import java.io.BufferedWriter;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Write{
  public static void main(String[] args){
    try(
      BufferedWriter writer = Files.newBufferedWriter(Paths.get(args[0]));
    ){

      writer.write("Hello World");
      writer.newLine();

    }catch(Exception e){
      //something went wrong
      System.out.println("Error: unknown error!");
      return;
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .276em"><code class="java">import java.io.BufferedWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
<mark>import java.lang.ArrayIndexOutOfBoundsException;</mark>

public class Write{
  public static void main(String[] args){
    try(
      BufferedWriter writer = Files.newBufferedWriter(Paths.get(<mark>args[0]</mark>));
    ){

      writer.write("Hello World");
      writer.newLine();

    <mark>}catch(ArrayIndexOutOfBoundsException e){
      //no arguments provided
      System.out.println("Error: no arguments provided!");
      return;</mark>
    }catch(Exception e){
      //something went wrong
      System.out.println("Error: unknown error!");
      return;
    }
  }
}</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .276em"><code class="java">import java.io.BufferedWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.lang.ArrayIndexOutOfBoundsException;
<mark>import java.nio.file.InvalidPathException;</mark>

public class Write{
  public static void main(String[] args){
    try(
      BufferedWriter writer = Files.newBufferedWriter(<mark>Paths.get(args[0])</mark>);
    ){

      writer.write("Hello World");
      writer.newLine();

    }catch(ArrayIndexOutOfBoundsException e){
      //no arguments provided
      System.out.println("Error: no arguments provided!");
      return;
    <mark>}catch(InvalidPathException e){
      //path is invalid
      System.out.println("Error: invalid file path!");
      return;</mark>
    }catch(Exception e){
      //something went wrong
      System.out.println("Error: unknown error!");
      return;
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .276em"><code class="java">import java.io.BufferedWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.lang.ArrayIndexOutOfBoundsException;
import java.nio.file.InvalidPathException;
<mark>import java.io.IOException;</mark>

public class Write{
  public static void main(String[] args){
    try(
      BufferedWriter writer = Files.newBufferedWriter(Paths.get(args[0]));
    ){

      <mark>writer.write("Hello World");</mark>
      writer.newLine();

    }catch(ArrayIndexOutOfBoundsException e){
      //no arguments provided
      System.out.println("Error: no arguments provided!");
      return;
    }catch(InvalidPathException e){
      //path is invalid
      System.out.println("Error: invalid file path!");
      return;
    <mark>}catch(IOException e){
      //cannot open file or error while writing
      System.out.println("Error: I/O error!");
      return;</mark>
    }catch(Exception e){
      //something went wrong
      System.out.println("Error: unknown error!");
      return;
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .276em"><code class="java">import java.io.BufferedWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.lang.ArrayIndexOutOfBoundsException;
import java.nio.file.InvalidPathException;
import java.io.IOException;
<mark>import java.lang.UnsupportedOperationException;</mark>

public class Write{
  public static void main(String[] args){
    try(
      BufferedWriter writer = <mark>Files.newBufferedWriter(Paths.get(args[0]));</mark>
    ){

      writer.write("Hello World");
      writer.newLine();

    }catch(ArrayIndexOutOfBoundsException e){
      //no arguments provided
      System.out.println("Error: no arguments provided!");
      return;
    }catch(InvalidPathException e){
      //path is invalid
      System.out.println("Error: invalid file path!");
      return;
    }catch(IOException e){
      //cannot open file or error while writing
      System.out.println("Error: I/O error!");
      return;
    <mark>}catch(UnsupportedOperationException e){
      //unable to open the file for writing
      System.out.println("Error: unable to open file for writing!");
      return;</mark>
    }catch(Exception e){
      //something went wrong
      System.out.println("Error: unknown error!");
      return;
    }
  }
}</code></pre>
</section>



<section>
	<pre class="stretch" style="font-size: .276em"><code class="java">import java.io.BufferedWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.lang.ArrayIndexOutOfBoundsException;
import java.nio.file.InvalidPathException;
import java.io.IOException;
import java.lang.UnsupportedOperationException;

public class Write{
  public static void main(String[] args){
    try(
      BufferedWriter writer = Files.newBufferedWriter(Paths.get(args[0]));
    ){

      writer.write("Hello World");
      writer.newLine();

    }catch(ArrayIndexOutOfBoundsException e){
      //no arguments provided
      System.out.println("Error: no arguments provided!");
      return;
    }catch(InvalidPathException e){
      //path is invalid
      System.out.println("Error: invalid file path!");
      return;
    }catch(IOException e){
      //cannot open file or error while writing
      System.out.println("Error: I/O error!");
      return;
    }catch(UnsupportedOperationException e){
      //unable to open the file for writing
      System.out.println("Error: unable to open file for writing!");
      return;
    }catch(Exception e){
      //something went wrong
      System.out.println("Error: unknown error!");
      return;
    }
  }
}</code></pre>
</section>
