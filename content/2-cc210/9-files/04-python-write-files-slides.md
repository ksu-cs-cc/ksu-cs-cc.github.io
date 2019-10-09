---
type: "reveal"
hidden: true
---

<section>
	<pre class="stretch" style="font-size: .5em"><code class="python">import sys

try:
  with open(sys.argv[1], "w") as writer:

except Exception as e:
  # unknown exception
  print("Exception: {}".format(e))
  sys.exit()</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .5em"><code class="python">import sys

try:
  with open(sys.argv[1]<mark>, "w"</mark>) as writer:

except Exception as e:
  # unknown exception
  print("Exception: {}".format(e))
  sys.exit()</code></pre>
</section>


<section>
	<pre class="stretch" style="font-size: .5em"><code class="python">import sys

try:
  with open(sys.argv[1], "w") as writer:
    <mark>writer.write("Hello World")
    writer.write("\n")</mark>

except Exception as e:
  # unknown exception
  print("Exception: {}".format(e))
  sys.exit()</code></pre>
</section>



<section>
	<pre class="stretch" style="font-size: .5em"><code class="python">import sys

try:
  with open(<mark>sys.argv[1]</mark>, "w") as writer:
    writer.write("Hello World")
    writer.write("\n")

<mark>except IndexError as e:
  # no arguments provided
  print("IndexError: {}".format(e))
  sys.exit()</mark>
except Exception as e:
  # unknown exception
  print("Exception: {}".format(e))
  sys.exit()</code></pre>
</section>

<section>
	<pre class="stretch" style="font-size: .5em"><code class="python">import sys

try:
  with open(sys.argv[1], "w") as writer:
    <mark>writer.write("Hello World")</mark>
    writer.write("\n")

except IndexError as e:
  # no arguments provided
  print("IndexError: {}".format(e))
  sys.exit()
<mark>except IOError as e:
  # unable to write to the file
  print("IOError: {}".format(e))
  sys.exit()</mark>
except Exception as e:
  # unknown exception
  print("Exception: {}".format(e))
  sys.exit()</code></pre>
</section>



<section>
	<pre class="stretch" style="font-size: .5em"><code class="python">import sys

try:
  with open(sys.argv[1], "w") as writer:
    writer.write("Hello World")
    writer.write("\n")

except IndexError as e:
  # no arguments provided
  print("IndexError: {}".format(e))
  sys.exit()
except IOError as e:
  # unable to write to the file
  print("IOError: {}".format(e))
  sys.exit()
except Exception as e:
  # unknown exception
  print("Exception: {}".format(e))
  sys.exit()</code></pre>
</section>
