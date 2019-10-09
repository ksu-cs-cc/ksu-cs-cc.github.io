---
type: "reveal"
hidden: true
---

<section>
	<pre class="stretch" style="font-size: .44em"><code class="java">import java.nio.file.Paths;
import java.nio.file.Path;
import java.nio.file.Files;
import java.nio.file.InvalidPathException;
import java.io.IOException;

public class Manipulate{
  public static void main(String[] args){

    try{
      Path pathObject = Paths.get("/home/codio/workspace/file.txt");

      /* -=-=-=-=- MORE CODE GOES HERE -=-=-=-=- */

    }catch(InvalidPathException e){
      //cannot convert string to path
      System.out.println("Error: Invalid Path");
      return;
    }catch(IOException e){
      //file system error
      System.out.println("Error: IOException");
      return;
    }
  }
}</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .44em"><code class="java">import java.nio.file.Paths;
import java.nio.file.Path;
import java.nio.file.Files;
import java.nio.file.InvalidPathException;
import java.io.IOException;

public class Manipulate{
  public static void main(String[] args){

    try{
      Path pathObject = <mark>Paths.get("/home/codio/workspace/file.txt");</mark>

      /* -=-=-=-=- MORE CODE GOES HERE -=-=-=-=- */

    }catch(InvalidPathException e){
      //cannot convert string to path
      System.out.println("Error: Invalid Path");
      return;
    }catch(IOException e){
      //file system error
      System.out.println("Error: IOException");
      return;
    }
  }
}</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .44em"><code class="java">import java.nio.file.Paths;
import java.nio.file.Path;
import java.nio.file.Files;
import java.nio.file.InvalidPathException;
import java.io.IOException;

public class Manipulate{
  public static void main(String[] args){

    try{
      <mark>Path pathObject</mark> = Paths.get("/home/codio/workspace/file.txt");

      /* -=-=-=-=- MORE CODE GOES HERE -=-=-=-=- */

    }catch(InvalidPathException e){
      //cannot convert string to path
      System.out.println("Error: Invalid Path");
      return;
    }catch(IOException e){
      //file system error
      System.out.println("Error: IOException");
      return;
    }
  }
}</code></pre>
</section>



<section>
	<pre class="stretch" style="font-size: .44em"><code class="java">import java.nio.file.Paths;
import java.nio.file.Path;
import java.nio.file.Files;
import java.nio.file.InvalidPathException;
import java.io.IOException;

public class Manipulate{
  public static void main(String[] args){

    try{
      Path pathObject = Paths.get("/home/codio/workspace/file.txt");

      /* -=-=-=-=- MORE CODE GOES HERE -=-=-=-=- */

    }catch(<mark>InvalidPathException e</mark>){
      //cannot convert string to path
      System.out.println("Error: Invalid Path");
      return;
    }catch(<mark>IOException e</mark>){
      //file system error
      System.out.println("Error: IOException");
      return;
    }
  }
}</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .44em"><code class="java">import java.nio.file.Paths;
import java.nio.file.Path;
<mark>import java.nio.file.Files;</mark>
import java.nio.file.InvalidPathException;
import java.io.IOException;

public class Manipulate{
  public static void main(String[] args){

    try{
      Path pathObject = Paths.get("/home/codio/workspace/file.txt");

      /* -=-=-=-=- MORE CODE GOES HERE -=-=-=-=- */

    }catch(InvalidPathException e){
      //cannot convert string to path
      System.out.println("Error: Invalid Path");
      return;
    }catch(IOException e){
      //file system error
      System.out.println("Error: IOException");
      return;
    }
  }
}</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .44em"><code class="java">import java.nio.file.Paths;
import java.nio.file.Path;
import java.nio.file.Files;
import java.nio.file.InvalidPathException;
import java.io.IOException;

public class Manipulate{
  public static void main(String[] args){

    try{
      Path pathObject = Paths.get("/home/codio/workspace/file.txt");

      <mark>/* -=-=-=-=- MORE CODE GOES HERE -=-=-=-=- */</mark>

    }catch(InvalidPathException e){
      //cannot convert string to path
      System.out.println("Error: Invalid Path");
      return;
    }catch(IOException e){
      //file system error
      System.out.println("Error: IOException");
      return;
    }
  }
}</code></pre>
</section>


<section>
  <h2>What is It?</h2>
	<pre class="stretch" style="font-size: .7em"><code class="java">//Determine if a file or directory
//exists at that path
Files.exists(pathObject);

//Is that object a directory?
Files.isDirectory(pathObject);

//Is that object a regular file?
Files.isRegularFile(pathObject);
  </code></pre>
</section>



<section>
  <h2>How Big is It?</h2>
	<pre class="" style="font-size: .7em"><code class="java">Files.size(pathObject);  </code></pre>
  <p>Returns size of file in bytes</p>
  <p>Throws IOException on a directory<br>or missing file</p>
</section>



<section>
  <h2>Copy and Move</h2>
	<pre class="stretch" style="font-size: .54em"><code class="java">Path source = Paths.get("/home/codio/workspace/dir1/file1.txt");
Path dest = Paths.get("/home/codio/workspace/dir2/file2.txt");

//copy file
Files.copy(source, dest);
//move (rename) file
Files.move(source, dest);</code></pre>
<p>Will throw FileAlreadyExistsException<br>if destination exists</p>
<p>We can tell it to overwrite<br>(see documentation)</p>
</section>



<section>
  <h2>Delete</h2>
	<pre class="" style="font-size: .7em"><code class="java">Files.delete(pathObject);</code></pre>
<p>Will throw DirectoryNotEmptyException<br>if deleting a non-empty directory</p>
</section>


<section>
  <h2>Create</h2>
	<pre class="" style="font-size: .7em"><code class="java">Files.createFile(pathObject);
Files.createDirectory(pathObject);</code></pre>
<p>Will throw FileAlreadyExistsException<br>if destination exists</p>
</section>
