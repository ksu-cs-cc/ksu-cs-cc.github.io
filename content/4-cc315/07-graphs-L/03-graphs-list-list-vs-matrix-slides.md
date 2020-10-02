---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 7 <br> Graphs: Lists <br> Lists VS Matrices</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<div style="float:left;width:50%">
<h4>Matrix</h4>
<ul style="font-size:50px">
<li><b>Nodes</b>: Node Array</li>
<li><b>Edges</b>: Adjacency Matrix</li>
</ul>
</div>
<div style="float:right;width:50%">
<h4>List</h4>
<ul style="font-size:50px">
<li><b>Nodes</b>:List of Graph Nodes</li>
<li><b>Graph Node</b>: Single Node</li>
</ul>
</div>
</section>

<section>
<h3>Space</h3>
<p>For a graph with N nodes and E edges:</p>
<div style="float:left;width:50%">
<h4>Matrix</h4>
<ul style="font-size:50px">
<li><b>Nodes</b>: N-dim. array</li>
<li><b>Edges</b>: NxN array</li>
</ul>
</div>
<div style="float:right;width:50%">
<h4>List</h4>
<ul style="font-size:50px">
<li><b>Nodes</b>: N-dim. array</li>
<li><b>Graph Nodes</b>: 8xE bytes </li>
</ul>
</div>
</section>

<section>
<h3>Sparse VS Dense</h3>
<img class="stretch plain" src="/images/315_7.3_sps_vs_dns.svg">
</section>

<section>
<h3>Sparse VS Dense</h3>
<p>For a graph with N nodes <br/> and E edges if </p>
<img class="stretch plain" src="/images/315_7.3_proportion.svg">
<p>then the adjacency matrix is preferred</p>
</section>

<section>
<h3>Accessing Edges</h3>
<p> To access an edge from node I to J:</p>
<div style="float:left;width:50%">
<h4>Matrix</h4>
<ul style="font-size:50px">
<li>Go to the (I,J) entry of 'edges'</li>
</ul>
</div>
<div style="float:right;width:50%">
<h4>List</h4>
<ul style="font-size:50px">
<li>Go to the I graph node, loop through 'edges' until J is found</li>
</ul>
</div>
</section>

<section>
<h3>Summary</h3>
<div style="float:left;width:50%">
<h4>Matrix</h4>
<ul style="font-size:50px">
<li>Dense Graphs</li>
<li>Accessing Edges</li>
</ul>
</div>
<div style="float:right;width:50%">
<h4>List</h4>
<ul style="font-size:50px">
<li>Sparse Graphs</li>
</ul>
</div>
</section>