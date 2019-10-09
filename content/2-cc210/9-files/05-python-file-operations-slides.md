---
type: "reveal"
hidden: true
---

<section>
	<pre class="stretch" style="font-size: .55em"><code class="python">import pathlib

try:
  pathObject = pathlib.Path("/home/codio/workspace/file.txt")

  # -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-

except IOError as e:
  print("IOError: {}".format(e))</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .55em"><code class="python">import pathlib

try:
  pathObject = <mark>pathlib.Path("/home/codio/workspace/file.txt")</mark>

  # -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-

except IOError as e:
  print("IOError: {}".format(e))</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .55em"><code class="python">import pathlib

try:
  <mark>pathObject</mark> = pathlib.Path("/home/codio/workspace/file.txt")

  # -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-

except IOError as e:
  print("IOError: {}".format(e))</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .55em"><code class="python">import pathlib

try:
  pathObject = pathlib.Path("/home/codio/workspace/file.txt")

  # -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-

except <mark>IOError as e</mark>:
  print("IOError: {}".format(e))</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .55em"><code class="python"><mark>import pathlib</mark>

try:
  pathObject = pathlib.Path("/home/codio/workspace/file.txt")

  # -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-

except IOError as e:
  print("IOError: {}".format(e))</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .55em"><code class="python">import pathlib

try:
  pathObject = pathlib.Path("/home/codio/workspace/file.txt")

  <mark># -=-=-=-=- MORE CODE GOES HERE -=-=-=-=-</mark>

except IOError as e:
  print("IOError: {}".format(e))</code></pre>
</section>


<section>
  <h2>What is It?</h2>
	<pre class="stretch" style="font-size: .7em"><code class="python"># Determine if a file or directory
# exists at that path
pathObject.exists()

# Is that object a directory?
pathObject.is_dir()

# Is that object a regular file?
pathObject.is_file()
  </code></pre>
</section>



<section>
  <h2>How Big is It?</h2>
	<pre class="" style="font-size: .7em"><code class="python">pathObject.stat().st_size</code></pre>
  <p>Returns size of file in bytes</p>
  <p>Throws FileNotFoundError on a <br>missing file</p>
  <p>Results from a directory are confusing</p>
</section>



<section>
  <h2>Copy and Move</h2>
	<pre class="stretch" style="font-size: .54em"><code class="python">destination = pathlib.Path("/home/codio/workspace/file2.txt")

# Move (rename) a file
pathObject.rename(destination)

# Copy a file
# We need to add `import shutil` to the top of the script
shutil.copy2(str(pathObject), str(destination))</code></pre>
<p>Will overwrite existing files without warning!</p>
</section>



<section>
  <h2>Delete</h2>
	<pre class="" style="font-size: .7em"><code class="python"># Delete a file
pathObject.unlink()

# Delete an empty directory
pathObject.rmdir()</code></pre>
<p>Will throw OSError<br>if deleting a non-empty directory</p>
</section>


<section>
  <h2>Create</h2>
	<pre class="" style="font-size: .7em"><code class="python"># Create a directory
pathObject.mkdir()

# Create a file (by opening it)
file = pathObject.open("w")
file.close()</code></pre>
<p>Will throw FileExistsError<br>if destination directory exists</p>
</section>
