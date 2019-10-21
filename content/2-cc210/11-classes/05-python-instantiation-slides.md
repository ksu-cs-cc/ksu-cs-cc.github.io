---
type: "reveal"
hidden: true
---

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Student import *
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Student import *
from Teacher import *
  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Student import *
from Teacher import *

class Main:
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Student import *
from Teacher import *

class Main:

  def main():

  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Student import *
from Teacher import *

class Main:

  def main():

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Student import *
from Teacher import *

class Main:

  def main():
    <mark>Student()</mark>

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Student import *
from Teacher import *

class Main:

  def main():
    <mark>jane =</mark> Student()

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Student import *
from Teacher import *

class Main:

  def main():
    jane = Student()
    print(<mark>jane.name</mark>)

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Student import *
from Teacher import *

class Main:

  def main():
    jane = Student()
    print(jane.name)
    <mark>jane.name = "Jane"</mark>

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Student import *
from Teacher import *

class Main:

  def main():
    jane = Student()
    print(jane.name)
    jane.name = "Jane"
    jane.age = jane.age + 15
    jane.student_id = "123" + "456"
    jane.credits = 45
    jane.gpa = jane.gpa - 1.1

    print(jane.name + ": " +
                        jane.student_id)

if __name__ == "__main__":
  Main.main()
</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .5em"><code class="python">from Student import *
from Teacher import *

class Main:

  def main():
    jane = Student()
    print(jane.name)
    jane.name = "Jane"
    jane.age = jane.age + 15
    jane.student_id = "123" + "456"
    jane.credits = 45
    jane.gpa = jane.gpa - 1.1

    print(jane.name + ": " +
                        jane.student_id)

    <mark>jane.birthday()</mark>
    <mark>jane.grade(4, 12)</mark>

if __name__ == "__main__":
  Main.main()
  </code></pre>
  </div>
</section>
