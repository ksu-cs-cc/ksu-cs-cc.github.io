---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 6 <br> Graphs <br> Node and Edge Functions</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3>UML Diagram</h3>
<img class="stretch plain" src="/images/315_6.7_graphMatUML2.svg">
</section>


<section>
<h3>Add Node</h3>
<pre class="" style="font-size: .4em; width: 55%; height: 200px"><code class="python" style="max-height: 1000px;">
function ADDNODE(VALUE)
    IDX = -1
    for NODE in NODES
        if NODE is VALUE 
            return NODE`s index
        if NODE has no entry and IDX is -1
            IDX = NODE`s index
    if IDX is not -1
        add VALUE to NODES at position IDX
        increment SIZE
    return IDX
 </code></pre>
</section>

<section>
<h3>Remove Node</h3>
<pre class="" style="font-size: .4em; width: 65%; height: 200px"><code class="python" style="max-height: 1000px;">
function REMOVENODE(IDX)
    if IDX is in the range of our indexes 
        if NODES at position IDX is not empty
            set NODES at IDX to be empty
            decrement SIZE by one
            for J in node indexes 
                set EDGES (J,IDX) equal to infinity 
                set EDGES (IDX,J) equal to infinity
            return true
        else
            return false
    else
        return false 
 </code></pre>
</section>

<section>
<h3>Add Edge</h3>
<pre class="" style="font-size: .4em; width: 85%; height: 200px"><code class="python" style="max-height: 1000px;">
function ADDEDGE(SOURCE, TARGET, WEIGHT)
    if SOURCE and TARGET are both in the range of our node indexes
        set EDGES(SOURCE, TARGET) equal to WEIGHT
        return true 
    else
        return false
 </code></pre>
</section>

<section>
<h3>Remove Edge</h3>
<pre class="" style="font-size: .4em; width: 85%; height: 200px"><code class="python" style="max-height: 1000px;">
function REMOVEEDGE(SOURCE, TARGET)
    if SOURCE and TARGET are both in the range of our node indexes
        if EDGES(SOURCE, TARGET) is not equal to infinity
            set EDGES(SOURCE, TARGET) equal to infinity
            return true 
        else
            return false
    else
        return false
 </code></pre>
</section>

<section>
<h3>Add Undirected Edge</h3>
<pre class="" style="font-size: .4em; width: 65%; height: 200px"><code class="python" style="max-height: 1000px;">
function ADDUNDIRECTEDEDGE(NODE1, NODE2, WEIGHT)
    RES = ADDEDGE(NODE1, NODE2, WEIGHT)
    RES = RES and ADDEDGE(NODE2, NODE1, WEIGHT)
    return RES
 </code></pre>
</section>

<section>
<h3>Remove Undirected Edge</h3>
<pre class="" style="font-size: .4em; width: 60%; height: 200px"><code class="python" style="max-height: 1000px;">
function REMOVEUNDIRECTEDEDGE(NODE1, NODE2)
    RES = REMOVEEDGE(NODE1, NODE2)
    RES = RES and REMOVEEDGE(NODE2, NODE1)
    return RES
 </code></pre>
</section>
