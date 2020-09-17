---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 6 <br> Graphs <br> Terms</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3>Vocab</h3>
<ul>
<li>Nodes: Containers</li>
<li>Edges: Connections</li>
</ul>
</section>

<section>
<h3>Edges</h3>
<ul>
<li>More than just parents and children</li>
<ul>
<li>Electrical Connections</li>
<li>Roads</li>
<li>Friendships</li>
</ul>
</ul>
</section>

<section>
<h3>Edges</h3>
<ul>
<li>Adjacent: A is adjacent to B if <br/> there is an edge from A to B </li>
<li>Neighbors: All Adjacent Nodes </li>
</ul>
</section>

<section>
<h3>Example</h3>

<img style="height:580px;width:580px;float:left" class="stretch plain" src="/images/315_6.2_graphEdges.svg" >

<small>
<table>
<tr>
<td>Node</td><td>Adjacent to</td></tr>
<tr><td>A</td><td>C</td></tr>
<tr><td>B</td><td>None</td></tr>
<tr><td>C</td><td>B, D, E</td></tr>
<tr><td>D</td><td>F</td></tr>
<tr><td>E</td><td>F</td></tr>
<tr><td>F</td><td>None</td></tr>
</table>
</small>
</section>

<section>
<h3>Example</h3>

<img style="height:580px;width:580px;float:left" class="stretch plain" src="/images/315_6.2_graphEdges.svg" >

<small>
<table>
<tr>
<td>Node</td><td>Neighbors</td></tr>
<tr><td>A</td><td>{C}</td></tr>
<tr><td>B</td><td>{}</td></tr>
<tr><td>C</td><td>{B, D, E}</td></tr>
<tr><td>D</td><td>{F}</td></tr>
<tr><td>E</td><td>{F}</td></tr>
<tr><td>F</td><td>{}</td></tr>
</table>
</small>
</section>


<section>
<h3>Graph Attributes</h3>
<ul>
<li>Size </li>
<li>Capacity </li>
</ul>
</section>


<section>
<h3>Cycles</h3>
<ul>
<li>If there is a path that <br/>starts and ends at the <br/>same node </li>
</ul>
</section>


<section>
<h3>Cycle Example</h3>
<img class="stretch plain" src="/images/315_6.2_graphCycle.svg" >
</section>

<section>
<h3>Cycle Example</h3>
<img class="stretch plain" src="/images/315_6.2_graphNoCycle.svg" >
</section>


<section>
<h3>Cycle Example</h3>

<img style="height:580px;width:580px;float:left" class="stretch plain" src="/images/315_6.2_graphNoCycle.svg" >
<small>
<table>
<tr><td>Paths</td></tr>
<tr><td>B</td></tr>
<tr><td>E</td></tr>
<tr><td>AE</td></tr>
<tr><td>AB</td></tr>
<tr><td>ACE</td></tr>
<tr><td>ACB</td></tr>
<tr><td>ACDB</td></tr>
<tr><td>ACFE</td></tr>
<tr><td>ACFDB</td></tr>
</table>
</small>
</section>

<section>
<h3>Concepts</h3>
<ul>
<li>Nodes and Edges</li>
<li>Adjacent</li>
<li>Neighbors</li>
<li>Size and Capacity</li>
<li>Cycles</li>
</ul>
</section>