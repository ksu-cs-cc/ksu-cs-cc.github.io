---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 7 <br> Graphs: Lists <br> Graph UML</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<img class="stretch plain" src="/images/315_7.5_listUML.svg">
</section>


<section>
<h3>Attributes</h3>
<ul>
<li>Nodes: array of graph nodes </li>
<li>Size: # of active nodes</li>
</ul>
</section>

<section>
<h3>Initialization</h3>
<ul>
<li>Nodes: array with <br/> length capacity </li>
<li>Size: 0</li>
</ul>
</section>

<section>
<h3>Getters</h3>
</section>

<section>
<h3> Get Nodes </h3>
<pre class="" style="font-size: .4em; width: 65%; height: 200px"><code class="python" style="max-height: 1000px;">
function GETNODES()
    LIST = []
    for NODE in NODES
        if NODE has a VALUE
            ITEM = VALUES`s ITEM
            append (ITEM, INDEX) to LIST
    return LIST
</code></pre>
</section>

<section>
<h3> Get Edges </h3>
<pre class="" style="font-size: .4em; width: 65%; height: 200px"><code class="python" style="max-height: 1000px;">
function GETEDGES()
    LIST = []
    for NODE in NODES
        if NODE is not empty
            for EDGE in NODE EDGES
                SRC = NODE index
                TAR = first entry of EDGE
                WEIGHT = second entry of EDGE
                append (SRC,TAR,WEIGHT) to LIST
    return LIST
</code></pre>
</section>

<section>
<h3> Node </h3>
<ul>
<li>Get Node: Given an index,<br/> return item </li>
<li>Find Node: Given an item,<br/>  return index</li>
</ul>
</section>

<section>
<h3> Get Edge </h3>
<pre class="" style="font-size: .4em; width: 85%; height: 200px"><code class="python" style="max-height: 1000px;">
function GETEDGE(SRC,TAR)
    if SRC and TAR are between 0 and capacity
        SRCNODE = the node at index SRC of the NODES attribute
        WEIGHT = call the graph node GETEDGE from SRCNODE on TAR
        return WEIGHT
    else
        return infinity
</code></pre>
</section>

<section>
<h3> Node </h3>
<ul>
<li>Get Capacity</li>
<li>Get Size</li>
</ul>
</section>

<section>
<h3> Get Number of Edges </h3>
<pre class="" style="font-size: .4em; width: 65%; height: 200px"><code class="python" style="max-height: 1000px;">
function NUMBEROFEDGES()
    COUNT = 0
    for NODE in NODES
        if NODE is not empty
            for EDGE in NODE EDGES
                increment COUNT by one
    return COUNT
</code></pre>
</section>

<section>
<h3> Get Neighbors </h3>
<pre class="" style="font-size: .4em; width: 75%; height: 200px"><code class="python" style="max-height: 1000px;">
function GETNEIGHBORS(IDX)
    SRCNODE = the node at index IDX of the NODES attribute
    if SRCNODE is not empty
        return SRCNODE`s edges 
    else
        return nothing
</code></pre>
</section>

<section>
<h3>Node and Edge Functions</h3>
</section>

<section>
<h3> Add Node </h3>
<pre class="" style="font-size: .4em; width: 75%; height: 200px"><code class="python" style="max-height: 1000px;">
function ADDNODE(VALUE)
    IDX = -1
    for NODE in NODES
        if NODE is VALUE 
            return NODE`s index
        if NODE has no entry and IDX is -1
            IDX = NODE`s index
    if IDX is not -1
        NEWNODE = graph node with VALUE and IDX for input
        add NEWNODE to NODES at position IDX
        increment SIZE
    return IDX
</code></pre>
</section>

<section>
<h3> Remove Node </h3>
<pre class="" style="font-size: .4em; width: 100%; height: 200px"><code class="python" style="max-height: 1000px;">
function REMOVENODE(IDX)
    if IDX is in the range of our indexes 
        if NODES at position IDX is not empty
            set NODES at IDX to be empty
            decrement SIZE by one
            for NODE in NODES
                if NODE has no entry
                    from NODE call the graph node REMOVEEDGE function on IDX
            return true
        else
            return false
    else
        return false 
</code></pre>
</section>

<section>
<h3> Add Edge </h3>
<pre class="" style="font-size: .4em; width: 85%; height: 200px"><code class="python" style="max-height: 1000px;">
function ADDEDGE(SRC, TAR, WEIGHT)
    if SOURCE and TARGET are both in the range of our node indexes
        SRCNODE = the node at index SRC of the NODES attribute
        if SRCNODE not empty
            from SRCNODE call the graph node ADDEDGE(TAR, WEIGHT)
            return true 
        else
            return false
    else
        return false
</code></pre>
</section>

<section>
<h3> Remove Edge </h3>
<pre class="" style="font-size: .4em; width: 85%; height: 200px"><code class="python" style="max-height: 1000px;">
function REMOVEEDGE(SOURCE, TARGET)
    if SOURCE and TARGET are both in the range of our node indexes
        SRCNODE = the node at index SRC of the NODES attribute
        if SRCNODE not empty
            RET = SRCNODE call the graph node REMOVEEDGE(TAR)
            return RET 
        else
            return false
    else
        return false
</code></pre>
</section>

<section>
<h3> Add/Remove Undirected Edge </h3>
<pre class="" style="font-size: .4em; width: 65%; height: 200px"><code class="python" style="max-height: 1000px;">
function ADDUNDIRECTEDEDGE(NODE1, NODE2, WEIGHT)
    RES = ADDEDGE(NODE1, NODE2, WEIGHT)
    RES = RES and ADDEDGE(NODE2, NODE1, WEIGHT)
    return RES
</code></pre>

<pre class="" style="font-size: .4em; width: 65%; height: 200px"><code class="python" style="max-height: 1000px;">
function REMOVEUNDIRECTEDEDGE(NODE1, NODE2)
    RES = REMOVEEDGE(NODE1, NODE2)
    RES = RES and REMOVEEDGE(NODE2, NODE1)
    return RES
</code></pre>
</section>


<section>
<img class="stretch plain" src="/images/315_7.5_listUML.svg">
</section>


