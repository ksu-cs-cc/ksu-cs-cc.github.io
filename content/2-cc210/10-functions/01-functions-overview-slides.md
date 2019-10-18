---
type: "reveal"
hidden: true
---

<section>
  <h2>Function</h2>
  <p><i>A piece of code that can be executed as part of a program, which may return a value.</i></p>
</section>
<section>
  <pre class="stretch" style="font-size: .65em"><code class="javascript">define main()
  name = read("Enter your name")
  print("*=*=*=*=*=*=*=*=*")
  print(name)
  print("*=*=*=*=*=*=*=*=*")

  nickname = read("Enter your nickname")
  print("*=*=*=*=*=*=*=*=*")
  print(nickname)
  print("*=*=*=*=*=*=*=*=*")

  userID = read("Enter your user ID")
  print("*=*=*=*=*=*=*=*=*")
  print(userID)
  print("*=*=*=*=*=*=*=*=*")

  </code></pre>
</section>


<section>
  <h2>Repetative Code</h2>
  <pre class="stretch" style="font-size: .62em"><code class="javascript">define main()
  <mark>name = read("Enter your name")
  print("*=*=*=*=*=*=*=*=*")
  print(name)
  print("*=*=*=*=*=*=*=*=*")</mark>

  <mark>nickname = read("Enter your nickname")
  print("*=*=*=*=*=*=*=*=*")
  print(nickname)
  print("*=*=*=*=*=*=*=*=*")</mark>

  <mark>userID = read("Enter your user ID")
  print("*=*=*=*=*=*=*=*=*")
  print(userID)
  print("*=*=*=*=*=*=*=*=*")</mark></code></pre>
</section>



<section>
  <h2>Use Loops</h2>
  <pre class="stretch" style="font-size: .62em"><code class="javascript">define main()
  for i from 0 to 2
    if i == 0
     input = read("Enter your name")
    if i == 1
      input = read("Enter your nickname")
    if i == 2
      input = read("Enter your user ID")

    print("*=*=*=*=*=*=*=*=*")
    print(input)
    print("*=*=*=*=*=*=*=*=*")
  </code></pre>
</section>

<section>
  <h2>Use Functions?</h2>
  <pre class="stretch" style="font-size: .42em"><code class="javascript">define main()
  getName()
  getNickname()
  getUserID()

define getName()
  name = read("Enter your name")
  print("*=*=*=*=*=*=*=*=*")
  print(name)
  print("*=*=*=*=*=*=*=*=*")

define getNickname()
  nickname = read("Enter your nickname")
  print("*=*=*=*=*=*=*=*=*")
  print(nickname)
  print("*=*=*=*=*=*=*=*=*")

define getUserID()
  userID = read("Enter your user ID")
  print("*=*=*=*=*=*=*=*=*")
  print(userID)
  print("*=*=*=*=*=*=*=*=*")</code></pre>
</section>

<section>
  <h3>Use Function<br>with Parameter</h3>
  <pre class="stretch" style="font-size: .65em"><code class="javascript">define main()
  name = read("Enter your name")
  prettyPrint(name)
  nickname = read("Enter your nickname")
  prettyPrint(nickname)
  userID = read("Enter your user ID")
  prettyPrint(userID)

define prettyPrint(input)
  print("*=*=*=*=*=*=*=*=*")
  print(input)
  print("*=*=*=*=*=*=*=*=*")
</code></pre>
</section>


<section>
  <h3>Use Function<br>with Parameter</h3>
  <pre class="stretch" style="font-size: .65em"><code class="javascript">define main()
  getInputAndPrint("Enter your name")
  getInputAndPrint("Enter your nickname")
  getInputAndPrint("Enter your user ID")

define getInputAndPrint(prompt)
  input = read(prompt)
  print("*=*=*=*=*=*=*=*=*")
  print(input)
  print("*=*=*=*=*=*=*=*=*")
</code></pre>
</section>

<section>
  <h3>Use Function<br>with Parameter & Return</h3>
  <pre class="stretch" style="font-size: .65em"><code class="javascript">define main()
  name = getInputAndPrint("Enter your name")
  nickname = getInputAndPrint("Enter your nickname")
  userID = getInputAndPrint("Enter your user ID")

define getInputAndPrint(prompt)
  input = read(prompt)
  print("*=*=*=*=*=*=*=*=*")
  print(input)
  print("*=*=*=*=*=*=*=*=*")
  return input
</code></pre>
</section>
