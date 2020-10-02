---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 7 <br> Graphs: Lists <br> Graph Node UML</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<img class="stretch plain" src="/images/315_7.4_gnodeUML.svg">
</section>


<section>
<h3>Attributes</h3>
<ul>
<li>Item: Object (what the <br/>node contains)</li>
<li>Index: Nodes position in array</li>
<li>Edges: Outgoing edges for <br/> the node</li>
<ul>
<li>List of ordered pairs: <br/>(Target, Weight)</li>
</ul>
</ul>
</section>

<section>
<h3>Getters</h3>
<ul>
<li> get item: Returns item</li>
<li> get index: Returns index</li>
<li> get edges: Returns edges</li>
</ul>
</section>

<section>
<h3> Get Edge </h3>
<pre class="" style="font-size: .4em; width: 65%; height: 200px"><code class="python" style="max-height: 1000px;">
function GETEDGE(TARINDEX)
    for EDGE in nodes EDGES
        if the first element in EDGE is TARINDEX
            return the second element in EDGE
    return infinity 
 </code></pre>

</section>

<section>
<h3>Add Edge</h3>
<pre class="" style="font-size: .4em; width: 65%; height: 200px"><code class="python" style="max-height: 1000px;">
function ADDEDGE(TARINDEX, WEIGHT)
    call REMOVEEDGE(TARINDEX) on this node
    append (TARINDEX, WEIGHT) to this nodes EDGES 
 </code></pre>
</section>

<section>
<h3>Remove Edge</h3>
<pre class="" style="font-size: .4em; width: 65%; height: 200px"><code class="python" style="max-height: 1000px;">
function REMOVEEDGE(TARINDEX)
    for EDGE in nodes EDGES
        if the first element in EDGE is TARINDEX
            remove EDGE from EDGES
            return true
    return false 
 </code></pre>
</section>

<section>
<img class="stretch plain" src="/images/315_7.4_gnodeUML.svg">
</section>
