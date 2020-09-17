---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 6 <br> Graphs <br> UML </h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3>UML Diagram</h3>
<img class="stretch plain" src="/images/315_6.7_graphMatUML.svg">
</section>

<section>
<h3>Attributes</h3>
<ul>
<li>Nodes: Object Array</li>
<li>Edges: Double 2D Array</li>
<li>Size: Integer</li>
</ul>
</section>

<section>
<h3>Initialization</h3>
<img class="stretch plain" src="/images/315_6.7_graphInit.svg">
</section>

<section>
<h3>Getters</h3>
</section>

<section>
<h3>Getting Nodes</h3>
<img class="stretch plain" src="/images/315_6.7_graphNodes.svg">
<pre class="" style="font-size: .4em; width: 55%; height: 200px"><code class="python" style="max-height: 1000px;">
function GETNODES()
    LIST = []
    for NODE in NODES
        if NODE has a VALUE
            append (VALUE, INDEX) to LIST
    return LIST
end function 

Expect: LIST = [(B,2),(C,3),(D,4),(F,6)]
 </code></pre>
</section>

<section>
<h3>Getting all Edges</h3>
<div style="float:left;width:30%">
<img class="stretch plain" style="height:600px" src="/images/315_6.7_graphEdges.svg">
</div>
<div style="float:right;width:70%">
<pre class="" style="font-size: .335em; width: 70%; height: 200px"><code class="python" style="max-height: 1000px;">
function GETEDGES()
    LIST = []
    for ROW in EDGES
        for COL in ROW
            VALUE = entry at (ROW,COL)
            if VALUE is not infinity
                append (ROW,COL,VALUE) to LIST
    return LIST
end function

Expect: LIST = [(1,2,13),(1,4,1),(2,1,13),
                (2,3,4),(3,5,5),(4,1,1),(4,5,1),
                (5,4,1),(5,6,7),(6,2,6)]
 </code></pre>
</div>
</section>

<section>
<h3>Get Node</h3>
<ul>
<li><b>Input:</b> An Index</li>
<li><b>Output:</b>  A Node</li>
</ul>
</section>

<section>
<h3>Find Node</h3>
<ul>
<li><b>Input:</b>  A Node</li>
<li><b>Output:</b> An Index</li>
<ul>
<li>If the node doesn't <br/> exist, return -1</li>
</ul>
</ul>
</section>

<section>
<h3>Get Edge</h3>
<ul>
<li><b>Input:</b>  Source Index and <br/>Target Index</li>
<li><b>Output:</b> A Weight</li>
<ul>
<li>If either index is <br/> out of range, return infinity</li>
</ul>
</ul>
</section>

<section>
<h3>More Getters</h3>
<ul>
<li><b>Get Size:</b> return the <br/>size attribute</li>
<li><b>Get Capacity:</b> return the <br/> dimension of the <br/>nodes attribute</li>
</ul>
</section>

<section>
<h3>Get Number of Edges</h3>
<img class="stretch plain" style="height:600px" src="/images/315_6.7_graphEdges.svg">
<p>Iterate through the edges counting how many are not infinity<p>
<p>Expect: 10<p>
</section>

<section>
<h3>Get Neighbors</h3>
<div style="float:left;width:30%">
<img class="stretch plain" style="height:600px" src="/images/315_6.7_graphEdges.svg">
</div>
<div style="float:right;width:70%">
<pre class="" style="font-size: .335em; width: 70%; height: 200px"><code class="python" style="max-height: 1000px;">
function GETNEIGHBORS(IDX)
    if IDX in range of NODES length
        LIST = []
        ROW = the IDX-th row of EDGES
        for J in range  0 to ROW length
            VALUE = J-th entry of ROW
            if VALUE is not infinity
                    append (J,VALUE) to LIST
        return LIST
end function

GETNEIGHBORS(2)
Expect: LIST = [(1,13),(3,4)]
 </code></pre>
</div>
</section>

<section>
<h3>Recap</h3>
<ul>
<li>Attributes</li>
<li>Getters</li>
</ul>
</section>