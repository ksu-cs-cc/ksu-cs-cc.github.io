---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 8 <br> Graphs Traversals <br> Depth First Traversal</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3>Depth First Traversal</h3>
<ul>
<li>Pseudocode</li>
<li>Example</li>
</ul>
</section>

<section>
<h3> Depth First Traversal </h3>
<pre class="" style="font-size: .4em; width: 65%; height: 400px"><code class="python" style="max-height: 1000px;">
function DEPTHFIRST(GRAPH,SRC)
    STACK = empty array
    DISCOVERED = empty set
    append SRC to STACK
    while STACK is not empty
        CURR = top of the stack
        if CURR not in DISCOVERED
            add CURR to DISCOVERED
            NEIGHS = neighbors of CURR
            for EDGE in NEIGHS
                NODE = first entry in EDGE
                append NODE to STACK
</code></pre>
</section>

<section>
<h3> Depth First Traversal </h3>
<pre class="" style="font-size: .4em; width: 65%; height: 400px"><code class="python" style="max-height: 1000px;">
function DEPTHFIRST(GRAPH,SRC)<mark>
    STACK = empty array
    DISCOVERED = empty set
    append SRC to STACK</mark>
    while STACK is not empty
        CURR = top of the stack
        if CURR not in DISCOVERED
            add CURR to DISCOVERED
            NEIGHS = neighbors of CURR
            for EDGE in NEIGHS
                NODE = first entry in EDGE
                append NODE to STACK
</code></pre>
</section>

<section>
<h3> Depth First Traversal </h3>
<pre class="" style="font-size: .4em; width: 65%; height: 400px"><code class="python" style="max-height: 1000px;">
function DEPTHFIRST(GRAPH,SRC)
    STACK = empty array
    DISCOVERED = empty set
    append SRC to STACK<mark>
    while STACK is not empty
        CURR = top of the stack
        if CURR not in DISCOVERED
            add CURR to DISCOVERED
            NEIGHS = neighbors of CURR
            for EDGE in NEIGHS
                NODE = first entry in EDGE
                append NODE to STACK</mark>
</code></pre>
</section>

[comment]: <> (WALK-THROUGH: Start at slide 05)
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_01.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_02.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_03.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_04.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_05.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_06.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_07.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_08.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_09.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_10.svg">
</section>

[comment]: <> (WALK-THROUGH: Slide 15 is next)

<section>
<img class="stretch plain" src="/images/315_8.2_DFS_11.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_12.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_13.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_14.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_15.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_16.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_17.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_18.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_19.svg">
</section>

[comment]: <> (WALK-THROUGH: Slide 25 is next)

<section>
<img class="stretch plain" src="/images/315_8.2_DFS_20.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_21.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_22.svg">
</section>

<section>
<h3> Depth First Traversal </h3>
<pre class="" style="font-size: .4em; width: 65%; height: 400px"><code class="python" style="max-height: 1000px;">
function DEPTHFIRST(GRAPH,SRC)
    STACK = empty array
    DISCOVERED = empty set
    append SRC to STACK
    while STACK is not empty
        CURR = top of the stack
        if CURR not in DISCOVERED
            add CURR to DISCOVERED
            NEIGHS = neighbors of CURR
            for EDGE in NEIGHS
                NODE = first entry in EDGE
                append NODE to STACK
</code></pre>
</section>


<section>
<img class="stretch plain" src="/images/315_8.2_DFS_23.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_24.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_25.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_26.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_27.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_28.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_29.svg">
</section>

[comment]: <> (WALK-THROUGH: 30)

<section>
<img class="stretch plain" src="/images/315_8.2_DFS_30.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_31.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_32.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_33.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_34.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_35.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_36.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_37.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_38.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_39.svg">
</section>

[comment]: <> (WALK-THROUGH: 40)

<section>
<img class="stretch plain" src="/images/315_8.2_DFS_40.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_41.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_42.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.2_DFS_43.svg">
</section>

<section>
<h3> We Made It! </h3>
<pre class="" style="font-size: .4em; width: 65%; height: 400px"><code class="python" style="max-height: 1000px;">
function DEPTHFIRST(GRAPH,SRC)
    STACK = empty array
    DISCOVERED = empty set
    append SRC to STACK
    while STACK is not empty
        CURR = top of the stack
        if CURR not in DISCOVERED
            add CURR to DISCOVERED
            NEIGHS = neighbors of CURR
            for EDGE in NEIGHS
                NODE = first entry in EDGE
                append NODE to STACK
</code></pre>
</section>