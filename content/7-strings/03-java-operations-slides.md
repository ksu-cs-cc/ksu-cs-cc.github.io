---
type: "reveal"
hidden: true
---

<section>
  <h2>String Length</h2>
  <pre class="" style="font-size: .8em"><code class="java">String s = "This";
System.out.println(s.length());

String t = "This \"is\" that";
System.out.println(t.length());</code></pre>
</section>

<section>
  <h2>String Length</h2>
  <pre class="" style="font-size: .8em"><code class="java">String s = "<mark>T</mark>h<mark>i</mark>s";
System.out.println(s.length());

String t = "This \"is\" that";
System.out.println(t.length());</code></pre>
</section>

<section>
  <h2>String Length</h2>
  <pre class="" style="font-size: .8em"><code class="java">String s = "This";
System.out.println(s.length());  // 4

String t = "This \"is\" that";
System.out.println(t.length());</code></pre>
</section>

<section>
  <h2>String Length</h2>
  <pre class="" style="font-size: .8em"><code class="java">String s = "This";
System.out.println(s.length());  // 4

String t = "<mark>T</mark>h<mark>i</mark>s<mark> </mark>\"<mark>i</mark>s<mark>\"</mark> <mark>t</mark>h<mark>a</mark>t";
System.out.println(t.length());</code></pre>
</section>

<section>
  <h2>String Length</h2>
  <pre class="" style="font-size: .8em"><code class="java">String s = "This";
System.out.println(s.length());  // 4

String t = "This \"is\" that";
System.out.println(t.length());  // 14</code></pre>
</section>

<section>
  <h2>String Comparison</h2>
  <pre class="stretch" style="font-size: .79em"><code class="java">String s1 = "This";
String s2 = "This";
String s3 = "this";

System.out.println(s1 == s2);
System.out.println(s1 == s3);</code></pre>
</section>

<section>
  <h2>String Comparison</h2>
  <pre class="stretch" style="font-size: .79em"><code class="java">String s1 = "This";
String s2 = "This";
String s3 = "this";

System.out.println(s1 == s2); // false
System.out.println(s1 == s3); // false</code></pre>
</section>

<section>
  <h2>String Comparison</h2>
  <pre class="stretch" style="font-size: .79em"><code class="java">String s1 = "This";
String s2 = "This";
String s3 = "this";

<s>System.out.println(s1 == s2); // false</s>
<s>System.out.println(s1 == s3); // false</s>

System.out.println(s1.equals(s2));
System.out.println(s1.equals(s3)); </code></pre>
</section>

<section>
  <h2>String Comparison</h2>
  <pre class="stretch" style="font-size: .79em"><code class="java">String s1 = "This";
String s2 = "This";
String s3 = "this";

<s>System.out.println(s1 == s2); // false</s>
<s>System.out.println(s1 == s3); // false</s>

System.out.println(s1.equals(s2)); // true
System.out.println(s1.equals(s3)); // false</code></pre>
</section>

<section>
  <h2>String Comparison</h2>
  <pre class="stretch" style="font-size: .79em"><code class="java">String s1 = "This";
String s2 = "That";

if(s1 &lt; s2){
  System.out.println("s1 comes first");
}else{
  System.out.println("s2 comes first");
}</code></pre>
</section>

<section>
  <h2>String Comparison</h2>
  <pre class="stretch" style="font-size: .79em"><code class="java">String s1 = "This";
String s2 = "That";

if(<mark>s1 &lt; s2</mark>){
  System.out.println("s1 comes first");
}else{
  System.out.println("s2 comes first");
}</code></pre>
</section>

<section>
  <h2>String Comparison</h2>
  <pre class="stretch" style="font-size: .79em"><code class="java">String s1 = "This";
String s2 = "That";

if(<mark style="background-color: red">s1 &lt; s2</mark>){
  System.out.println("s1 comes first");
}else{
  System.out.println("s2 comes first");
}</code></pre>
</section>

<section>
  <h2>String Comparison</h2>
  <pre class="stretch" style="font-size: .79em"><code class="java">String s1 = "This";
String s2 = "That";

if(s1.compareTo(s2) &lt; 0){
  System.out.println("s1 comes first");
}else{
  System.out.println("s2 comes first");
}</code></pre>
</section>

<section>
  <h2>String Concatenation</h2>
  <pre class="stretch" style="font-size: .79em"><code class="java">String s1 = "This";
String s2 = "That";
int x = 42;

String s3 = s1 + s2;
String s4 = "" + x;

System.out.println(s3);
System.out.println(s4);</code></pre>
</section>

<section>
  <h2>String Concatenation</h2>
  <pre class="stretch" style="font-size: .79em"><code class="java">String s1 = <mark>"This"</mark>;
String s2 = <mark>"That"</mark>;
int x = 42;

String s3 = <mark>s1 + s2</mark>;
String s4 = "" + x;

System.out.println(s3);
System.out.println(s4);</code></pre>
</section>

<section>
  <h2>String Concatenation</h2>
  <pre class="stretch" style="font-size: .79em"><code class="java">String s1 = "This";
String s2 = "That";
int x = 42;

String s3 = s1 + s2;
String s4 = "" + x;

System.out.println(s3);  // "ThisThat"
System.out.println(s4);</code></pre>
</section>

<section>
  <h2>String Concatenation</h2>
  <pre class="stretch" style="font-size: .79em"><code class="java">String s1 = "This";
String s2 = "That";
int x = 42;

String s3 = s1 + s2;
String s4 = "" + x;

System.out.println(s3);  // "ThisThat"
System.out.println(s4);  // "42"</code></pre>
</section>

<section>
  <h2>Searching Strings</h2>
  <ul style="font-family: monospace">
    <li>contains</li>
    <li>indexOf</li>
    <li>lastIndexOf</li>
    <li>startsWith</li>
    <li>endsWith</li>
  </ul>
</section>

<section>
  <h2>Manipulating Strings</h2>
  <ul style="font-family: monospace">
    <li>replace</li>
    <li>substring</li>
    <li>toLowerCase</li>
    <li>toUppercase</li>
    <li>trim</li>
    <li>charAt</li>
  </ul>
</section>