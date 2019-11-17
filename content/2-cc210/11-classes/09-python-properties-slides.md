---
type: "reveal"
hidden: true
---

<section>
  <div style="float: right; width: 50%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.9.propertyuml.property.png">
  </div>
  <div style="width: 50%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Property:

  def __init__(self):
    self.__name = ""
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.9.propertyuml.property.png">
  </div>
  <div style="width: 50%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Property:

  def __init__(self):
    self.<mark>__</mark>name = ""
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.9.propertyuml.property.png">
  </div>
  <div style="width: 50%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Property:

  def __init__(self):
    self.__name = ""

  <mark>@property
  def name(self):
    return self.__name</mark>
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.9.propertyuml.property.png">
  </div>
  <div style="width: 50%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Property:

  def __init__(self):
    self.__name = ""

  <mark>@property</mark>
  def name(self):
    return self.__name
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.9.propertyuml.property.png">
  </div>
  <div style="width: 50%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Property:

  def __init__(self):
    self.__name = ""

  @property
  def name(self):
    return self.__name
  <mark>@name.setter
  def name(self, value):
    if not isinstance(value, str):
      raise ValueError(
        "Name must be a string")
    if len(value) == 0:
      raise ValueError(
        "Name cannot be an empty string")
    self.__name = value</mark>
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.9.propertyuml.property.png">
  </div>
  <div style="width: 50%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Property:

  def __init__(self):
    self.__name = ""

  @property
  def name(self):
    return self.__name
  <mark>@name.setter</mark>
  def name(self, value):
    if not isinstance(value, str):
      raise ValueError(
        "Name must be a string")
    if len(value) == 0:
      raise ValueError(
        "Name cannot be an empty string")
    self.__name = value
  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
	   <img class="plain" style="width: 100%" src="/images/11.6.p.9.propertyuml.property.png">
  </div>
  <div style="width: 50%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Property:

  def __init__(self):
    self.__name = ""

  @property
  def name(self):
    return self.__name
  @name.setter
  def name(self, value):
    if not isinstance(value, str):
      raise ValueError(
        "Name must be a string")
    if len(value) == 0:
      raise ValueError(
        "Name cannot be an empty string")
    self.__name = value
  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="python">from Property import *

class Main:

  def main():
    prop = Property()
    prop.name = "test"
    print(prop.name)

if __name__ == "__main__":
    Main.main()
    </code></pre>
  </div>
  <div style="width: 50%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Property:

  def __init__(self):
    self.__name = ""

  @property
  def name(self):
    return self.__name
  @name.setter
  def name(self, value):
    if not isinstance(value, str):
      raise ValueError(
        "Name must be a string")
    if len(value) == 0:
      raise ValueError(
        "Name cannot be an empty string")
    self.__name = value
  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="python">from Property import *

class Main:

  def main():
    prop = Property()
    <mark>prop.name = "test"</mark>
    print(prop.name)

if __name__ == "__main__":
    Main.main()
    </code></pre>
  </div>
  <div style="width: 50%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Property:

  def __init__(self):
    self.__name = ""

  @property
  def name(self):
    return self.__name
  @name.setter
  def name(self, value):
    if not isinstance(value, str):
      raise ValueError(
        "Name must be a string")
    if len(value) == 0:
      raise ValueError(
        "Name cannot be an empty string")
    self.__name = value
  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="python">from Property import *

class Main:

  def main():
    prop = Property()
    prop.name = "test"
    print(<mark>prop.name</mark>)

if __name__ == "__main__":
    Main.main()
    </code></pre>
  </div>
  <div style="width: 50%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Property:

  def __init__(self):
    self.__name = ""

  @property
  def name(self):
    return self.__name
  @name.setter
  def name(self, value):
    if not isinstance(value, str):
      raise ValueError(
        "Name must be a string")
    if len(value) == 0:
      raise ValueError(
        "Name cannot be an empty string")
    self.__name = value
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 50%">
    <pre class="stretch" style="font-size: .38em"><code class="python">from Property import *

class Main:

  def main():
    prop = Property()
    prop.name = "test"
    print(prop.name)

if __name__ == "__main__":
    Main.main()
    </code></pre>
  </div>
  <div style="width: 50%">
  <pre class="stretch" style="font-size: .37em"><code class="python">class Property:

  def __init__(self):
    self.__name = ""

  @property
  def name(self):
    return self.__name
  @name.setter
  def name(self, value):
    if not isinstance(value, str):
      raise ValueError(
        "Name must be a string")
    if len(value) == 0:
      raise ValueError(
        "Name cannot be an empty string")
    self.__name = value
  </code></pre>
  </div>
</section>