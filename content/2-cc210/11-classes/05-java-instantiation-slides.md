---
type: "reveal"
hidden: true
---

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="java">public class Main{

  public static void main(String[] args){

  }
}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="java">public class Main{

  public static void main(String[] args){
    <mark>new Student();</mark>
  }
}</code></pre>
  </div>
</section>

<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="java">public class Main{

  public static void main(String[] args){
    <mark>Student jane =</mark> new Student();
  }
}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="java">public class Main{

  public static void main(String[] args){
    Student jane = new Student();
    System.out.println(<mark>jane.name</mark>);
  }
}</code></pre>
  </div>
</section>



<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="java">public class Main{

  public static void main(String[] args){
    Student jane = new Student();
    System.out.println(jane.name);
    <mark>jane.name = "Jane";</mark>
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="java">public class Main{

  public static void main(String[] args){
    Student jane = new Student();
    System.out.println(jane.name);
    jane.name = "Jane";
    jane.age = jane.age + 15;
    jane.student_id = "123" + "456";
    jane.credits = 45
    jane.gpa = jane.gpa - 1.1;

    System.out.println(jane.name + ": " +
                          jane.student_id);
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
	   <img class="plain" style="width: 100%" src="/images/11.3.methods.student.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .5em"><code class="java">public class Main{

  public static void main(String[] args){
    Student jane = new Student();
    System.out.println(jane.name);
    jane.name = "Jane";
    jane.age = jane.age + 15;
    jane.student_id = "123" + "456";
    jane.credits = 45
    jane.gpa = jane.gpa - 1.1;

    System.out.println(jane.name + ": " +
                          jane.student_id);

    <mark>jane.birthday();</mark>
    <mark>jane.grade(4, 12);</mark>
  }
}</code></pre>
  </div>
</section>