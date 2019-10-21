---
type: "reveal"
hidden: true
---

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">import java.lang.Math;

public class Student{
  String name = "name";
  int age = 19;
  String student_id = "123456987";
  int credits = 0;
  double gpa = 0.0;

  // other methods omitted
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.j.5.constructuml.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">import java.lang.Math;

public class Student{
  String name = "name";
  int age = 19;
  String student_id = "123456987";
  int credits = 0;
  double gpa = 0.0;

  // other methods omitted
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.j.5.constructuml.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">import java.lang.Math;

public class Student{
  String name = "name";
  int age = 19;
  String student_id = "123456987";
  int credits = 0;
  double gpa = 0.0;

  <mark>Student(){
    // do nothing
  }</mark>

  // other methods omitted
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.j.5.constructuml.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">import java.lang.Math;

public class Student{
  String name = "name";
  int age = 19;
  String student_id = "123456987";
  int credits = 0;
  double gpa = 0.0;

  Student(){
    // do nothing
  }

  // other methods omitted
}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.j.5.constructuml.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">import java.lang.Math;

public class Student{
  String name = <mark>"name";</mark>
  int age = <mark>19;</mark>
  String student_id = <mark>"123456987";</mark>
  int credits = <mark>0;</mark>
  double gpa = <mark>0.0;</mark>

  Student(){
    // do nothing
  }

  // other methods omitted
}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.j.5.constructuml.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">import java.lang.Math;

public class Student{
  String name = "name";
  int age = 19;
  String student_id = "123456987";
  int credits = 0;
  double gpa = 0.0;

  Student(){
    <mark>this.name = "name";
    this.age = 19;
    this.student_id = "123456987";
    this.credits = 0;
    this.gpa = 0.0;</mark>
  }

  // other methods omitted
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.j.5.constructuml.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">import java.lang.Math;

public class Student{
  String name <mark>= "name";</mark>
  int age <mark>= 19;</mark>
  String student_id <mark>= "123456987";</mark>
  int credits <mark>= 0;</mark>
  double gpa <mark>= 0.0;</mark>

  Student(){
    this.name = "name";
    this.age = 19;
    this.student_id = "123456987";
    this.credits = 0;
    this.gpa = 0.0;
  }

  // other methods omitted
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.j.5.constructuml.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">import java.lang.Math;

public class Student{
  String name;
  int age;
  String student_id;
  int credits;
  double gpa;

  Student(){
    this.name = "name";
    this.age = 19;
    this.student_id = "123456987";
    this.credits = 0;
    this.gpa = 0.0;
  }

  // other methods omitted
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.4.classes.main.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Main{

  public static void main(String[] args){
    <mark>Student someStudent = new Student();</mark>
    System.out.println(someStudent.name) // "name";
    System.out.println(someStudent.age)  // 19
  }
}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.j.5.constructuml.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">import java.lang.Math;

public class Student{
  String name;
  int age;
  String student_id;
  int credits;
  double gpa;

  Student(){
    this.name = "name";
    this.age = 19;
    this.student_id = "123456987";
    this.credits = 0;
    this.gpa = 0.0;
  }

  // other methods omitted
}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.j.5.constructuml.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">import java.lang.Math;

public class Student{
  String name;
  int age;
  String student_id;
  int credits;
  double gpa;

  Student(){
    this.name = "name";
    this.age = 19;
    this.student_id = "123456987";
    this.credits = 0;
    this.gpa = 0.0;
  }

  Student(<mark>String name, int age, String student_id,
                          int credits, double gpa</mark>){
  }

  // other methods omitted
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.j.5.constructuml.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">import java.lang.Math;

public class Student{
  String name;
  int age;
  String student_id;
  int credits;
  double gpa;

  Student(){
    this.name = "name";
    this.age = 19;
    this.student_id = "123456987";
    this.credits = 0;
    this.gpa = 0.0;
  }

  Student(String name, int age, String student_id,
                          int credits, double gpa){
    this.name = <mark>name</mark>;
    this.age = <mark>age</mark>;
    this.student_id = <mark>student_id</mark>;
    this.credits = <mark>credits</mark>;
    this.gpa = <mark>gpa</mark>;
  }

  // other methods omitted
}</code></pre>
  </div>
</section>




<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.6.j.5.constructuml.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">import java.lang.Math;

public class Student{
  String name;
  int age;
  String student_id;
  int credits;
  double gpa;

  Student(){
    this.name = "name";
    this.age = 19;
    this.student_id = "123456987";
    this.credits = 0;
    this.gpa = 0.0;
  }

  Student(String name, int age, String student_id,
                          int credits, double gpa){
    this.name = name;
    this.age = age;
    this.student_id = student_id;
    this.credits = credits;
    this.gpa = gpa;
  }

  // other methods omitted
}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.4.classes.main.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">public class Main{

  public static void main(String[] args){
    Student someStudent = new Student();
    System.out.println(someStudent.name) // "name";
    System.out.println(someStudent.age)  // 19

    <mark>Student anotherStudent = new Student("John", 25,
                                "1239873445", 4, 4.0);</mark>
    System.out.println(anotherStudent.name) // "John";
    System.out.println(anotherStudent.age)  // 25
  }
}</code></pre>
  </div>
</section>
