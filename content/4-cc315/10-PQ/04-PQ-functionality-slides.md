---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 10 <br> Heaps and Priority Queues <br> Functionality</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>


<section>
<h3>Implementation</h3>
<ul>
<li>Min-Priority Queues</li>
<li>Using Heaps</li>
</ul>
</section>

<section>
<h3>Class Attributes</h3>
<ul>
<li>Array: our heap</li>
<li>Elements of array: ordered pairs <br/> (priority, object)</li>
</ul>
</section>

<section>
<h3>Pushing Elements</h3>
<ul>
<li>PUSHUP</li>
<li>PUSHDOWN</li>
</ul>
</section>

<section>
<h3>Push Up</h3>
<ul>
<li>Base Case:</li>
<ul>
<li>A) Parent index of input <= 0</li>
<li>B) Parent's priority <= input's priority</li>
<li>Both cases, do nothing</li>
</ul>
<li>Recursive Case:</li>
<ul>
<li>Swap parent node and input node</li>
<li>Call PUSHUP on parent's index</li>
</ul>
</ul>
</section>

<section>
<h3>PUSHUP Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushup_start.svg">
</section>

<section>
<h3>PUSHUP Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushup_01.svg">
</section>

<section>
<h3>PUSHUP Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushup_02.svg">
</section>

<section>
<h3>PUSHUP Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushup_03.svg">
</section>

<section>
<h3>PUSHUP Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushup_04.svg">
</section>

<section>
<h3>PUSHUP Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushup_05.svg">
</section>

<section>
<h3>PUSHUP Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushup_06.svg">
</section>

<section>
<h3>PUSHUP Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushup_07.svg">
</section>

<section>
<h3>PUSHUP Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushup_09.svg">
</section>

<section>
<h3>PUSHUP Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushup_10.svg">
</section>

<section>
<h3>PUSHUP Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushup_end.svg">
</section>

<section>
<h3>Push Down Base</h3>
<ul>
<li>Base Case:</li>
<ul>
<li>A) Both children's indexes > heap size</li>
<li>B) Input's priority <= both children's priority</li>
<li>Both cases, do nothing</li>
</ul>
</ul>
</section>

<section>
<h3>Push Down Recursive</h3>
<ul>
<li>Recursive Case:</li>
<ul>
<li>A) Node has right child</li>
<li>B) Node only has left child</li>
</ul>
</ul>
</section>

<section>
<h3>Push Down Recursive: <br/> Right Child</h3>
<ul>
<li>If priority of left < priority of right</li>
<ul>
<li>If priority of left < priority of node</li>
<li>Swap node and left, recurse on left</li>
</ul>
<li>If priority left >= priority of right</li>
<ul>
<li>If priority of right < priority of node</li>
<li>Swap node and right, recurse on right</li>
</ul>
</ul>
</section>

<section>
<h3>Push Down Recursive: <br/>Left Child</h3>
<ul>
<li>If priority of left < priority of node</li>
<ul>
<li>Swap node and left, recurse on left</li>
</ul>
</ul>
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_start.svg">
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_02.svg">
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_03.svg">
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_04.svg">
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_05.svg">
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_06.svg">
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_07.svg">
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_08.svg">
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_09.svg">
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_10.svg">
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_11.svg">
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_12.svg">
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_13.svg">
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_14.svg">
</section>

<section>
<h3>PUSHDOWN Example</h3>
<img class="stretch plain" src="/images/315_10.4_pushdown_end.svg">
</section>


<section>
<h3>Remove the Minimum</h3>
<ul>
<li>Removes element with lowest priority</li>
<li>One element in array: delete it</li>
<li>More than one element: </li>
<ul>
<li>Delete the first element</li>
<li>Put the last element in the first spot</li>
<li>Call PUSHDOWN(1)</li>
</ul>
</ul>
</section>

<section>
<h3> Heapify</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
function HEAPIFY(RANKS, ITEMS)
    if RANKS and ITEMS are the same size
        SIZE = length of ITEMS
        loop INDEX starting at 1 to SIZE
            I_RANK = value at INDEX in RANKS
            I_ITEM = item at INDEX of ITEMS 
            append (I_RANK, I_ITEM) to priority queues array
        LASTPARENT = floor(SIZE/2) + 1
        loop NODE starting at LASTPARENT down to 1
            PUSHDOWN(NODE)
    else
        error
</code></pre>
</section>

<section>
<h3> Heapify</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
function HEAPIFY(RANKS, ITEMS)
    if RANKS and ITEMS are the same size<mark>
        SIZE = length of ITEMS
        loop INDEX starting at 1 to SIZE
            I_RANK = value at INDEX in RANKS
            I_ITEM = item at INDEX of ITEMS 
            append (I_RANK, I_ITEM) to priority queues array
        LASTPARENT = floor(SIZE/2) + 1
        loop NODE starting at LASTPARENT down to 1
            PUSHDOWN(NODE)</mark>
    else
        error
</code></pre>
</section>

<section>
<h3> Heapify</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
function HEAPIFY(RANKS, ITEMS)
    if RANKS and ITEMS are the same size
        SIZE = length of ITEMS
        loop INDEX starting at 1 to SIZE<mark>
            I_RANK = value at INDEX in RANKS
            I_ITEM = item at INDEX of ITEMS 
            append (I_RANK, I_ITEM) to priority queues array</mark>
        LASTPARENT = floor(SIZE/2) + 1
        loop NODE starting at LASTPARENT down to 1
            PUSHDOWN(NODE)
    else
        error
</code></pre>
</section>

<section>
<h3> Heapify</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
function HEAPIFY(RANKS, ITEMS)
    if RANKS and ITEMS are the same size
        SIZE = length of ITEMS
        loop INDEX starting at 1 to SIZE
            I_RANK = value at INDEX in RANKS
            I_ITEM = item at INDEX of ITEMS 
            append (I_RANK, I_ITEM) to priority queues array
       <mark> LASTPARENT = floor(SIZE/2) + 1
        loop NODE starting at LASTPARENT down to 1
            PUSHDOWN(NODE)</mark>
    else
        error
</code></pre>
</section>

<section>
<h3>Insert</h3>
<ul>
<li>Input: Priority and element</li>
<li>Append (priority, element) to queue</li>
<li>Call PUSHUP</li>
</ul>
</section>

<section>
<h3> Decrease Key</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
DECREASEKEY(IDX, PRIORITY)
    ELEMENT = entry in array at IDX
    if PRIORITY > ELEMENT[0]
        error
    ELEMENT[0] = PRIORITY 
    PUSHUP(IDX)
</code></pre>
</section>

<section>
<h3>Functions</h3>
<ul>
<li>PUSHUP</li>
<li>PUSHDOWN</li>
<li>REMOVEMIN</li>
<li>HEAPIFY</li>
<li>INSERT</li>
<li>DECREASEKEY</li>
</ul>
</section>