---
type: "reveal"
hidden: true
---

<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .43em"><code class="python">def main():
  max(2, 3)
  max(3, 4, 5)

def max(x, y, z=None):
  if z is not None:
    if x >= y:
      if x >= z:
        print(x)
      else:
        print(z)
    else:
      if y >= z:
        print(y)
      else:
        print(z)
  else:
    if x >= y:
      print(x)
    else:
      print(y)

# main guard
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
    <pre class="stretch" style="font-size: .43em"><code class="python">def main():
  max(2, 3)
  max(3, 4, 5)

def max(x, y, z=None):
  if z is not None:
    if x >= y:
      if x >= z:
        print(x)
      else:
        print(z)
    else:
      if y >= z:
        print(y)
      else:
        print(z)
  else:
    if x >= y:
      print(x)
    else:
      print(y)

# main guard
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
    <pre class="stretch" style="font-size: .43em"><code class="python">def <mark>main</mark>():
  max(2, 3)
  max(3, 4, 5)

def max(x, y, z=None):
  if z is not None:
    if x >= y:
      if x >= z:
        print(x)
      else:
        print(z)
    else:
      if y >= z:
        print(y)
      else:
        print(z)
  else:
    if x >= y:
      print(x)
    else:
      print(y)

# main guard
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
    <pre class="stretch" style="font-size: .43em"><code class="python">def main():
  <mark>max(2, 3)</mark>
  max(3, 4, 5)

def max(x, y, z=None):
  if z is not None:
    if x >= y:
      if x >= z:
        print(x)
      else:
        print(z)
    else:
      if y >= z:
        print(y)
      else:
        print(z)
  else:
    if x >= y:
      print(x)
    else:
      print(y)

# main guard
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
    <pre class="stretch" style="font-size: .43em"><code class="python">def main():
  <mark>max(2, 3)</mark>
  max(3, 4, 5)

def <mark>max</mark>(x, y, z=None):
  if z is not None:
    if x >= y:
      if x >= z:
        print(x)
      else:
        print(z)
    else:
      if y >= z:
        print(y)
      else:
        print(z)
  else:
    if x >= y:
      print(x)
    else:
      print(y)

# main guard
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
    <pre class="stretch" style="font-size: .43em"><code class="python">def main():
  <mark>max(2, 3)</mark>
  max(3, 4, 5)

def <mark>max(x, y, z=None):</mark>
  if z is not None:
    if x >= y:
      if x >= z:
        print(x)
      else:
        print(z)
    else:
      if y >= z:
        print(y)
      else:
        print(z)
  else:
    if x >= y:
      print(x)
    else:
      print(y)

# main guard
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
    <pre class="stretch" style="font-size: .43em"><code class="python">def main():
  <mark>max(2, 3)</mark>
  max(3, 4, 5)

def <mark>max(x, y, z=None):</mark>
  if z is not None:
    if x >= y:
      if x >= z:
        print(x)
      else:
        print(z)
    else:
      if y >= z:
        print(y)
      else:
        print(z)
  else:
    if x >= y:
      print(x)
    else:
      print(y)

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>max</b><br>x = 2<br>y = 3<br>z = None</p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .43em"><code class="python">def main():
  <mark>max(2, 3)</mark>
  max(3, 4, 5)

def max(x, y, z=None):
  <mark>if z is not None:
    if x >= y:
      if x >= z:
        print(x)
      else:
        print(z)
    else:
      if y >= z:
        print(y)
      else:
        print(z)
  else:
    if x >= y:
      print(x)
    else:
      print(y)</mark>

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>max</b><br>x = 2<br>y = 3<br>z = None</p>
  </div>
</section>

<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .43em"><code class="python">def main():
  max(2, 3)
  <mark>max(3, 4, 5)</mark>

def max(x, y, z=None):
  if z is not None:
    if x >= y:
      if x >= z:
        print(x)
      else:
        print(z)
    else:
      if y >= z:
        print(y)
      else:
        print(z)
  else:
    if x >= y:
      print(x)
    else:
      print(y)

# main guard
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
    <pre class="stretch" style="font-size: .43em"><code class="python">def main():
  max(2, 3)
  <mark>max(3, 4, 5)</mark>

def <mark>max(x, y, z=None):</mark>
  if z is not None:
    if x >= y:
      if x >= z:
        print(x)
      else:
        print(z)
    else:
      if y >= z:
        print(y)
      else:
        print(z)
  else:
    if x >= y:
      print(x)
    else:
      print(y)

# main guard
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
    <pre class="stretch" style="font-size: .43em"><code class="python">def main():
  max(2, 3)
  <mark>max(3, 4, 5)</mark>

def <mark>max(x, y, z=None):</mark>
  if z is not None:
    if x >= y:
      if x >= z:
        print(x)
      else:
        print(z)
    else:
      if y >= z:
        print(y)
      else:
        print(z)
  else:
    if x >= y:
      print(x)
    else:
      print(y)

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>max</b><br>x = 3<br>y = 4<br>z = 5</p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .43em"><code class="python">def main():
  max(2, 3)
  <mark>max(3, 4, 5)</mark>

def max(x, y, z=None):
  <mark>if z is not None:
    if x >= y:
      if x >= z:
        print(x)
      else:
        print(z)
    else:
      if y >= z:
        print(y)
      else:
        print(z)
  else:
    if x >= y:
      print(x)
    else:
      print(y)</mark>

# main guard
if __name__ == "__main__":
  <mark>main()</mark>
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>max</b><br>x = 3<br>y = 4<br>z = 5</p>
  </div>
</section>



<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  max(2, 3)
  max(3, 4, 5)
  max(5, 6, 7, 8)
  max(10, 11, 12, 13, 14, 15, 16)

def max(*values):
  if len(values) > 0:
    max = values[0]
    for value in values:
      if value > max:
        max = value
    print(max)

# main guard
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
  <mark>max(2, 3)</mark>
  max(3, 4, 5)
  max(5, 6, 7, 8)
  max(10, 11, 12, 13, 14, 15, 16)

def max(*values):
  if len(values) > 0:
    max = values[0]
    for value in values:
      if value > max:
        max = value
    print(max)

# main guard
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
  <mark>max(2, 3)</mark>
  max(3, 4, 5)
  max(5, 6, 7, 8)
  max(10, 11, 12, 13, 14, 15, 16)

def <mark>max(*values):</mark>
  if len(values) > 0:
    max = values[0]
    for value in values:
      if value > max:
        max = value
    print(max)

# main guard
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
  <mark>max(2, 3)</mark>
  max(3, 4, 5)
  max(5, 6, 7, 8)
  max(10, 11, 12, 13, 14, 15, 16)

def <mark>max(*values):</mark>
  if len(values) > 0:
    max = values[0]
    for value in values:
      if value > max:
        max = value
    print(max)

# main guard
if __name__ == "__main__":
  main()
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>max</b><br>values =<br>[2, 3]</p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  <mark>max(2, 3)</mark>
  max(3, 4, 5)
  max(5, 6, 7, 8)
  max(10, 11, 12, 13, 14, 15, 16)

def max(*values):
  <mark>if len(values) > 0:
    max = values[0]
    for value in values:
      if value > max:
        max = value
    print(max)</mark>

# main guard
if __name__ == "__main__":
  main()
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>max</b><br>values =<br>[2, 3]</p>
  </div>
</section>



<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  max(2, 3)
  <mark>max(3, 4, 5)</mark>
  max(5, 6, 7, 8)
  max(10, 11, 12, 13, 14, 15, 16)

def max(*values):
  if len(values) > 0:
    max = values[0]
    for value in values:
      if value > max:
        max = value
    print(max)

# main guard
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
  max(2, 3)
  <mark>max(3, 4, 5)</mark>
  max(5, 6, 7, 8)
  max(10, 11, 12, 13, 14, 15, 16)

def <mark>max(*values)</mark>:
  if len(values) > 0:
    max = values[0]
    for value in values:
      if value > max:
        max = value
    print(max)

# main guard
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
  max(2, 3)
  <mark>max(3, 4, 5)</mark>
  max(5, 6, 7, 8)
  max(10, 11, 12, 13, 14, 15, 16)

def <mark>max(*values)</mark>:
  if len(values) > 0:
    max = values[0]
    for value in values:
      if value > max:
        max = value
    print(max)

# main guard
if __name__ == "__main__":
  main()
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>max</b><br>values =<br>[3, 4, 5]</p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  max(2, 3)
  max(3, 4, 5)
  <mark>max(5, 6, 7, 8)</mark>
  max(10, 11, 12, 13, 14, 15, 16)

def <mark>max(*values)</mark>:
  if len(values) > 0:
    max = values[0]
    for value in values:
      if value > max:
        max = value
    print(max)

# main guard
if __name__ == "__main__":
  main()
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>max</b><br>values =<br>[5, 6, 7, 8]</p>
  </div>
</section>


<section>
  <div style="float: right; width: 75%">
    <pre class="stretch" style="font-size: .6em"><code class="python">def main():
  max(2, 3)
  max(3, 4, 5)
  max(5, 6, 7, 8)
  <mark>max(10, 11, 12, 13, 14, 15, 16)</mark>

def <mark>max(*values)</mark>:
  if len(values) > 0:
    max = values[0]
    for value in values:
      if value > max:
        max = value
    print(max)

# main guard
if __name__ == "__main__":
  main()
</code></pre>
  </div>
  <div style="width: 25%">
    <h4>Variables</h4>
    <p style="font-size: .7em"><b>max</b><br>values =<br>[10, 11, 12, 13, 14, 15, 16]</p>
  </div>
</section>
