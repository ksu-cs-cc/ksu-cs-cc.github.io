---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 8 <br> Graphs Traversals <br> Breadth First Search (BFS)</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3>Breadth First Traversal</h3>
<ul>
<li>Pseudocode</li>
<li>Example</li>
</ul>
</section>

<section>
<h3> Breadth First Traversal </h3>
<pre class="" style="font-size: .4em; width: 65%; height: 400px"><code class="python" style="max-height: 1000px;">
function BREADTHFIRST(GRAPH,SRC)
    QUEUE = empty queue
    DISCOVERED = empty set
    add SRC to DISCOVERED
    add SRC to QUEUE
    while QUEUE is not empty
        CURR = first element in QUEUE
        NEIGHS = neighbors of CURR
        for EDGE in NEIGHS
            NODE = first entry in EDGE
            if NODE is not in DISCOVERED
                add NODE to DISCOVERED
                append NODE to QUEUE
</code></pre>
</section>

<section>
<h3> Breadth First Traversal </h3>
<pre class="" style="font-size: .4em; width: 65%; height: 400px"><code class="python" style="max-height: 1000px;">
function BREADTHFIRST(GRAPH,SRC)<mark>
    QUEUE = empty queue
    DISCOVERED = empty set
    add SRC to DISCOVERED
    add SRC to QUEUE</mark>
    while QUEUE is not empty
        CURR = first element in QUEUE
        NEIGHS = neighbors of CURR
        for EDGE in NEIGHS
            NODE = first entry in EDGE
            if NODE is not in DISCOVERED
                add NODE to DISCOVERED
                append NODE to QUEUE
</code></pre>
</section>

<section>
<h3> Breadth First Traversal </h3>
<pre class="" style="font-size: .4em; width: 65%; height: 400px"><code class="python" style="max-height: 1000px;">
function BREADTHFIRST(GRAPH,SRC)
    QUEUE = empty queue
    DISCOVERED = empty set
    add SRC to DISCOVERED
    add SRC to QUEUE<mark>
    while QUEUE is not empty
        CURR = first element in QUEUE
        NEIGHS = neighbors of CURR
        for EDGE in NEIGHS
            NODE = first entry in EDGE
            if NODE is not in DISCOVERED
                add NODE to DISCOVERED
                append NODE to QUEUE</mark>
</code></pre>
</section>

[comment]: <> (WALK-THROUGH: Start at slide )
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_01.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_02.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_03.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_04.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_05.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_06.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_07.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_08.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_09.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_10.svg">
</section>

[comment]: <> (WALK-THROUGH: Slide  is next)

<section>
<img class="stretch plain" src="/images/315_8.3_BFS_11.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_12.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_13.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_14.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_15.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_16.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_17.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_18.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_19.svg">
</section>

[comment]: <> (WALK-THROUGH: Slide  is next)

<section>
<img class="stretch plain" src="/images/315_8.3_BFS_20.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_21.svg">
</section>
<section>
<img class="stretch plain" src="/images/315_8.3_BFS_22.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_8.3_BFS_23.svg">
</section>
