---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 9 <br> Minimum Spanning Trees <br> Prims Algorithm</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3> Kruskals Algorithm</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
function PRIM(GRAPH, SRC)
    MST = GRAPH without the edges attribute(s)
    VISITED = empty set
    add SRC to VISITED
    AVAILEDGES = list of edges where CURR is the source
    sort AVAILEDGES
    while VISITED is not all of the nodes
        SMLEDGE = smallest edge in AVAILEDGES
        SRC = source of SMLEDGE
        TAR = target of SMLEDGE
        if TAR not in VISITED
            add SMLEDGE to MST as undirected edge
            add TAR to VISITED
            add the edges where TAR is the source to AVAILEDGES
        remove SMLEDGE from AVAILEDGES
        sort AVAILEDGES
    return MST
</code></pre>
</section>



<section>
<h3>Example</h3>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_01.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_02.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_03.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_04.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_05.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_06.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_07.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_08.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_09.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_10.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_11.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_12.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_13.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_14.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_15.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_16.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_17.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_18.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_19.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_20.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_21.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_22.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_23.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_24.svg">
</section>
<section>
<img class="stretch plain" style="height:600"src="/images/315_9.4_P_25.svg">
</section>
