---
type: "reveal"
hidden: true
---

<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  return_value = last(1, 3, 5, 7, 9)
  print(return_value)

def last(*items):
  if len(items) > 0:
    return items[-1]
  return -1

if __name__ == "__main__":
  main()
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>



<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  return_value = last(1, 3, 5, 7, 9)
  print(return_value)

def last(*items):
  if len(items) > 0:
    return items[-1]
  return -1

if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>



<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def <mark>main</mark>():
  return_value = last(1, 3, 5, 7, 9)
  print(return_value)

def last(*items):
  if len(items) > 0:
    return items[-1]
  return -1

if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  <mark>return_value = last(1, 3, 5, 7, 9)</mark>
  print(return_value)

def last(*items):
  if len(items) > 0:
    return items[-1]
  return -1

if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  return_value = <mark>last(1, 3, 5, 7, 9)</mark>
  print(return_value)

def last(*items):
  if len(items) > 0:
    return items[-1]
  return -1

if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>



<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  return_value = <mark>last(1, 3, 5, 7, 9)</mark>
  print(return_value)

def <mark>last(*items)</mark>:
  if len(items) > 0:
    return items[-1]
  return -1

if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  return_value = <mark>last(1, 3, 5, 7, 9)</mark>
  print(return_value)

def <mark>last(*items)</mark>:
  if len(items) > 0:
    return items[-1]
  return -1

if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>last</b><br>items =<br>[1, 3, 5, 7, 9]</p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  return_value = <mark>last(1, 3, 5, 7, 9)</mark>
  print(return_value)

def last(*items):
  <mark>if len(items) > 0:</mark>
    return items[-1]
  return -1

if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>last</b><br>items =<br>[1, 3, 5, 7, 9]</p>
  </div>
</section>



<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  return_value = <mark>last(1, 3, 5, 7, 9)</mark>
  print(return_value)

def last(*items):
  if len(items) > 0:
    <mark>return items[-1]</mark>
  return -1

if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>last</b><br>items =<br>[1, 3, 5, 7, 9]</p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  return_value = <mark>last(1, 3, 5, 7, 9)</mark>
  print(return_value)

def last(*items):
  if len(items) > 0:
    <mark>return items[-1]</mark>
  return -1

if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>last</b><br>items =<br>[1, 3, 5, 7, <mark>9</mark>]</p>
  </div>
</section>



<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  return_value = <mark>9</mark>
  print(return_value)

def last(*items):
  if len(items) > 0:
    <mark>return items[-1]</mark>
  return -1

if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>last</b><br>items =<br>[1, 3, 5, 7, <mark>9</mark>]</p>
  </div>
</section>



<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  <mark>return_value = 9</mark>
  print(return_value)

def last(*items):
  if len(items) > 0:
    return items[-1]
  return -1

if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>main</b><br>returnValue = 9</p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  return_value = last(1, 3, 5, 7, 9)
  <mark>print(return_value)</mark>

def last(*items):
  if len(items) > 0:
    return items[-1]
  return -1

if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>main</b><br>returnValue = 9</p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  return_value = last(1, 3, 5, 7, 9)
  print(return_value)

def last(*items):
  if len(items) > 0:
    return items[-1]
  <mark>return -1</mark>

if __name__ == "__main__":
  main()
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"></p>
  </div>
</section>
