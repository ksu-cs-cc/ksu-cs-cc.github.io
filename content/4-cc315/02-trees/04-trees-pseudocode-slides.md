---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 2 <br> Trees <br> Pseudocode </h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<img class="stretch plain" src="/images/315trees_uml.png">
</section>

<section>
<h3> Attributes </h3>
<ul>
<li> Item </li>
<li> Parent </li>
<li> Children</li>
</ul>
</section>

<section>
<h3> Example </h3>
<div style="float:left">
<small>

| Node | parent | children | item |
| --- | --- | --- | --- |
| A | None | \{B, C\}| A |
| B | A | \{\}| B |
| C | A | \{D, E\}| C |
| D | C | \{\}| D |
| E | C | \{\}| E |
| F | None | \{\}| F |

</small>
 </div>
 <div style="width=100%">
<img class="stretch plain" src="/images/315_2.4_code_ex.svg">
<div>
</section>

<section>
<h3> Initialization </h3>
<div style="float:top">
<pre class="" style="font-size: .3em; width: 30%"><code class="java">
    MyTree foo = MyTree('13')
 </code></pre>
 </div>
<div style="float:bottom">
<img class="stretch plain" src="/images/315_2.4_code_init.svg">
<div>
</section>


<section>
<h3>Getters</h3>
<ul>
<li>getItem <br/>returns the item for that node</li>
<li>getParent <br/>returns the parent for that node</li>
<li>getChildren <br/>returns the children for that node</li>
</ul>
</section>


<section>
<h3>Basic Functions</h3>
<ul>
<li>isRoot<br/> returns true if this node is the root</li>
<li>isLeaf<br/> returns true if this node is the leaf</li>
</ul>
</section>

<section>
<h3>Basic Functions</h3>
<ul>
<li>getDegree <br/> returns the degree of the node</li>
<li>findChild(value) <br/> returns true the node is a child of this node</li>
</ul>
</section>

<section>
<img class="stretch plain" src="/images/315trees_uml.png">
</section>