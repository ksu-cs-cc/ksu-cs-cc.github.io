---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 9 <br> Minimum Spanning Trees <br> Kruskals Algorithm</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3> Kruskals Algorithm</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
function KRUSKAL(GRAPH)
    MST = GRAPH without the edges attribute(s)
    ALLSETS = an empty list which will contain the sets
    for NODE in GRAPH NODES
        SET = a set with element NODE
        add SET to ALLSETS
    EDGES = set of GRAPHs edges
    SORTEDEDGES = EDGES sorted by edge weight, smallest to largest
    for EDGE in SORTEDEDGES
        SRC = source node of EDGE
        TAR = target node of EDGE
        SRCSET = the set from SETS in which SRC is contained
        TARSET = the set form SETS in which TAR is contained
        if SRCSET not equal TARSET
            UNIONSET = SRCSET union TARSET
            add UNIONSET to ALLSETS
            remove SRCSET from ALLSETS
            remove TARSET from ALLSETS
            add EDGE to MST as undirected edge
    return MST
</code></pre>
</section>


<section>
<h3>Example</h3>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_01.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_02.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_03.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_04.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_05.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_06.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_07.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_08.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_09.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_10.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_11.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_12.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_13.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_14.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_15.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_16.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_17.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_18.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_19.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_20.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_21.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_22.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_23.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_24.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_25.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.3_K_26.svg">
</section>

<section>
<h3>Kruskal Intuition</h3>
<ul>
<li>Set MST nodes as graphs nodes</li>
<li>Order graph edges</li>
<li>Make each node their own set</li>
<li>Loop through edges</li>
<li>If source and target of edge not in same set, add the edge to MST and union the two sets</li>
</ul>
</section>
