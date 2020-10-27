---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 10 <br> Heaps and Priority Queues <br> Dijkstra's Algorithm</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3>Dijkstra's Algorithm</h3>
<p>Goal: given an input node, find the shortest path to all other nodes.</p>
</section>

<section>
<h3>Dijkstra's Algorithm</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
DIJKSTRAS(GRAPH, SRC)
    SIZE = size of GRAPH
    DISTS = array with length equal to SIZE
    PREVIOUS = array with length equal to SIZE
    set all of the entries in PREVIOUS to none
    set all of the entries in DISTS to infinity 
    DISTS[SRC] = 0 
    PQ = min-priority queue
    loop IDX starting at 0 up to SIZE
        insert (DISTS[IDX],IDX) into PQ
    while PQ is not empty
        MIN = REMOVE-MIN from PQ
        for NODE in neighbors of MIN
            WEIGHT = graph weight between MIN and NODE
            CALC = DISTS[MIN] + WEIGHT
            if CALC < DISTS[NODE]
                DISTS[NODE] = CALC
                PREVIOUS[NODE] = MIN
                PQ decrease-key (CALC, NODE)
    return DISTS and PREVIOUS
</code></pre>
</section>

<section>
<h3>Dijkstra's Algorithm</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
DIJKSTRAS(GRAPH, SRC)<mark>
    SIZE = size of GRAPH
    DISTS = array with length equal to SIZE
    PREVIOUS = array with length equal to SIZE
    set all of the entries in PREVIOUS to none
    set all of the entries in DISTS to infinity 
    DISTS[SRC] = 0 
    PQ = min-priority queue</mark>
    loop IDX starting at 0 up to SIZE
        insert (DISTS[IDX],IDX) into PQ
    while PQ is not empty
        MIN = REMOVE-MIN from PQ
        for NODE in neighbors of MIN
            WEIGHT = graph weight between MIN and NODE
            CALC = DISTS[MIN] + WEIGHT
            if CALC < DISTS[NODE]
                DISTS[NODE] = CALC
                PREVIOUS[NODE] = MIN
                PQ decrease-key (CALC, NODE)
    return DISTS and PREVIOUS
</code></pre>
</section>

<section>
<h3>Dijkstra's Algorithm</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
DIJKSTRAS(GRAPH, SRC)
    SIZE = size of GRAPH
    DISTS = array with length equal to SIZE
    PREVIOUS = array with length equal to SIZE
    set all of the entries in PREVIOUS to none
    set all of the entries in DISTS to infinity 
    DISTS[SRC] = 0 
    PQ = min-priority queue<mark>
    loop IDX starting at 0 up to SIZE
        insert (DISTS[IDX],IDX) into PQ</mark>
    while PQ is not empty
        MIN = REMOVE-MIN from PQ
        for NODE in neighbors of MIN
            WEIGHT = graph weight between MIN and NODE
            CALC = DISTS[MIN] + WEIGHT
            if CALC < DISTS[NODE]
                DISTS[NODE] = CALC
                PREVIOUS[NODE] = MIN
                PQ decrease-key (CALC, NODE)
    return DISTS and PREVIOUS
</code></pre>
</section>

<section>
<h3>Dijkstra's Algorithm</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
DIJKSTRAS(GRAPH, SRC)
    SIZE = size of GRAPH
    DISTS = array with length equal to SIZE
    PREVIOUS = array with length equal to SIZE
    set all of the entries in PREVIOUS to none
    set all of the entries in DISTS to infinity 
    DISTS[SRC] = 0 
    PQ = min-priority queue
    loop IDX starting at 0 up to SIZE
        insert (DISTS[IDX],IDX) into PQ
    while PQ is not empty
        MIN = REMOVE-MIN from PQ<mark>
        for NODE in neighbors of MIN
            WEIGHT = graph weight between MIN and NODE
            CALC = DISTS[MIN] + WEIGHT
            if CALC < DISTS[NODE]
                DISTS[NODE] = CALC
                PREVIOUS[NODE] = MIN
                PQ decrease-key (CALC, NODE)</mark>
    return DISTS and PREVIOUS
</code></pre>
</section>

<section>
<h3>Dijkstra's Algorithm</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
DIJKSTRAS(GRAPH, SRC)
    SIZE = size of GRAPH
    DISTS = array with length equal to SIZE
    PREVIOUS = array with length equal to SIZE
    set all of the entries in PREVIOUS to none
    set all of the entries in DISTS to infinity 
    DISTS[SRC] = 0 
    PQ = min-priority queue
    loop IDX starting at 0 up to SIZE
        insert (DISTS[IDX],IDX) into PQ
    while PQ is not empty
        MIN = REMOVE-MIN from PQ
        for NODE in neighbors of MIN
            WEIGHT = graph weight between MIN and NODE
            CALC = DISTS[MIN] + WEIGHT<mark>
            if CALC < DISTS[NODE]
                DISTS[NODE] = CALC
                PREVIOUS[NODE] = MIN
                PQ decrease-key (CALC, NODE)</mark>
    return DISTS and PREVIOUS
</code></pre>
</section>

<section>
<h3>Dijkstra's Algorithm</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
DIJKSTRAS(GRAPH, SRC)
    SIZE = size of GRAPH
    DISTS = array with length equal to SIZE
    PREVIOUS = array with length equal to SIZE
    set all of the entries in PREVIOUS to none
    set all of the entries in DISTS to infinity 
    DISTS[SRC] = 0 
    PQ = min-priority queue
    loop IDX starting at 0 up to SIZE
        insert (DISTS[IDX],IDX) into PQ
    while PQ is not empty
        MIN = REMOVE-MIN from PQ
        for NODE in neighbors of MIN
            WEIGHT = graph weight between MIN and NODE
            CALC = DISTS[MIN] + WEIGHT
            if CALC < DISTS[NODE]
                DISTS[NODE] = CALC
                PREVIOUS[NODE] = MIN
                PQ decrease-key (CALC, NODE)<mark>
    return DISTS and PREVIOUS<mark>
</code></pre>
</section>


<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_01.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_02.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_03.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_04.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_06.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_07.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_08.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_09.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_10.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_11.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_12.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_13.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_14.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_15.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_16.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_17.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_18.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_19.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_20.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_21.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_22.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_23.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_24.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_25.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_26.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_27.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_28.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_29.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_30.svg">
</section>

<section>
<h3>Dijkstra's Example</h3>
<img class="stretch plain" src="/images/315_10.5_Dijkstras_31.svg">
</section>