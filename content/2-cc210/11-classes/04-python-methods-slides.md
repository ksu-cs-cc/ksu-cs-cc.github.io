---
type: "reveal"
hidden: true
---

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .4em"><code class="python">class Student:
  name = "name"
  age = 19
  student_id = "123456987"
  credits = 0
  gpa = 0.0
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .4em"><code class="python">class Student:
  name = "name"
  age = 19
  student_id = "123456987"
  credits = 0
  gpa = 0.0

  def birthday():

  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .4em"><code class="python">class Student:
  name = "name"
  age = 19
  student_id = "123456987"
  credits = 0
  gpa = 0.0

  def birthday():
    <mark>age = age + 1</mark>
  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .4em"><code class="python">class Student:
  name = "name"
  age = 19
  student_id = "123456987"
  credits = 0
  gpa = 0.0

  def birthday(<mark>self</mark>):
    <mark>age = age + 1</mark>
  </code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .4em"><code class="python">class Student:
  name = "name"
  age = 19
  student_id = "123456987"
  credits = 0
  gpa = 0.0

  def birthday(<mark>self</mark>):
    <mark>self.age = self.age + 1</mark>
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .4em"><code class="python">class Student:
  name = "name"
  age = 19
  student_id = "123456987"
  credits = 0
  gpa = 0.0

  def birthday(self):
    self.age = self.age + 1
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .4em"><code class="python">class Student:
  name = "name"
  age = 19
  student_id = "123456987"
  credits = 0
  gpa = 0.0

  def birthday(self):
    self.age = self.age + 1

  def grade(credits, grade_points):
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .4em"><code class="python">class Student:
  name = "name"
  age = 19
  student_id = "123456987"
  credits = 0
  gpa = 0.0

  def birthday(self):
    self.age = self.age + 1

  def grade(<mark>self</mark>, credits, grade_points):
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .4em"><code class="python">class Student:
  name = "name"
  age = 19
  student_id = "123456987"
  credits = 0
  gpa = 0.0

  def birthday(self):
    self.age = self.age + 1

  def grade(self, credits, grade_points):
    current_points = self.gpa * self.credits
  </code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .4em"><code class="python">class Student:
  name = "name"
  age = 19
  student_id = "123456987"
  credits = 0
  gpa = 0.0

  def birthday(self):
    self.age = self.age + 1

  def grade(self, credits, grade_points):
    current_points = <mark>int</mark>(self.gpa * self.credits)
  </code></pre>
  </div>
</section>




<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .4em"><code class="python">class Student:
  name = "name"
  age = 19
  student_id = "123456987"
  credits = 0
  gpa = 0.0

  def birthday(self):
    self.age = self.age + 1

  def grade(self, credits, grade_points):
    current_points = <mark>round</mark>(self.gpa * self.credits)
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .4em"><code class="python">class Student:
  name = "name"
  age = 19
  student_id = "123456987"
  credits = 0
  gpa = 0.0

  def birthday(self):
    self.age = self.age + 1

  def grade(self, credits, grade_points):
    current_points = round(self.gpa * self.credits)
    self.credits += credits
    current_points += grade_points
  </code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
  <pre class="stretch" style="font-size: .4em"><code class="python">class Student:
  name = "name"
  age = 19
  student_id = "123456987"
  credits = 0
  gpa = 0.0

  def birthday(self):
    self.age = self.age + 1

  def grade(self, credits, grade_points):
    current_points = round(self.gpa * self.credits)
    self.credits += credits
    current_points += grade_points
    self.gpa = current_points / self.credits
  </code></pre>
  </div>
</section>