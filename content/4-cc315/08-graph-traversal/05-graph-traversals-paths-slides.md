---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 8 <br> Graphs Traversals <br> Finding Paths</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3>Finding Paths</h3>
<p>Given two nodes, find the path that connects them</p>
<h5>Possible Cases</h5>
<ul>
<li>No Path</li>
<li>One Path</li>
<li>Multiple Paths</li>
</ul>
</section>


<section>
<h3> Depth First Search (DFS) </h3>
<pre class="" style="font-size: .38em; width: 105%; height: 400px"><code class="python" style="max-height: 1000px;">
1. function DEPTHFIRSTSEARCH(GRAPH,SRC,TAR)
2.     STACK = empty array
3.     DISCOVERED = empty set
4.     PARENT_MAP = empty dictionary
5.     append SRC to STACK
6.     while STACK is not empty
7.         CURR = top of the stack
8.         if CURR not in DISCOVERED
9.             if CURR is TAR
10.                 PATH = empty array
11.                 TRACE = TAR
12.                 while TRACE is not SRC
13.                     append TRACE to PATH
14.                     set TRACE equal to PARENT_MAP[TRACE]
15.                 append SRC to PATH
16.                 reverse the order of PATH
17.                 return PATH
18.            add CURR to DISCOVERED
19.            NEIGHS = neighbors of CURR
20.            for EDGE in NEIGHS
21.                NODE = first entry in EDGE
22.                append NODE to STACK
23.                if PARENT_MAP does not have key NODE
24.                    in the PARENT_MAP dictionary set key NODE with value CURR
25.    return nothing
</code></pre>
</section>

<section>
<h3> Depth First Search (DFS) </h3>
<pre class="" style="font-size: .38em; width: 105%; height: 400px"><code class="python" style="max-height: 1000px;">
1. function DEPTHFIRSTSEARCH(GRAPH,SRC,TAR)<mark>
2.     STACK = empty array
3.     DISCOVERED = empty set</mark>
4.     PARENT_MAP = empty dictionary<mark>
5.     append SRC to STACK
6.     while STACK is not empty
7.         CURR = top of the stack</mark>
8.         if CURR not in DISCOVERED
9.             if CURR is TAR
10.                 PATH = empty array
11.                 TRACE = TAR
12.                 while TRACE is not SRC
13.                     append TRACE to PATH
14.                     set TRACE equal to PARENT_MAP[TRACE]
15.                 append SRC to PATH
16.                 reverse the order of PATH
17.                 return PATH<mark>
18.            add CURR to DISCOVERED
19.            NEIGHS = neighbors of CURR
20.            for EDGE in NEIGHS
21.                NODE = first entry in EDGE
22.                append NODE to STACK</mark>
23.                if PARENT_MAP does not have key NODE
24.                    in the PARENT_MAP dictionary set key NODE with value CURR
25.    return nothing
</code></pre>
</section>

<section>
<h3> Depth First Search (DFS) </h3>
<pre class="" style="font-size: .38em; width: 105%; height: 400px"><code class="python" style="max-height: 1000px;">
1. function DEPTHFIRSTSEARCH(GRAPH,SRC,TAR)
2.     STACK = empty array
3.     DISCOVERED = empty set<mark>
4.     PARENT_MAP = empty dictionary</mark>
5.     append SRC to STACK
6.     while STACK is not empty
7.         CURR = top of the stack
8.         if CURR not in DISCOVERED<mark>
9.             if CURR is TAR
10.                 PATH = empty array
11.                 TRACE = TAR
12.                 while TRACE is not SRC
13.                     append TRACE to PATH
14.                     set TRACE equal to PARENT_MAP[TRACE]
15.                 append SRC to PATH
16.                 reverse the order of PATH
17.                 return PATH</mark>
18.            add CURR to DISCOVERED
19.            NEIGHS = neighbors of CURR
20.            for EDGE in NEIGHS
21.                NODE = first entry in EDGE
22.                append NODE to STACK<mark>
23.                if PARENT_MAP does not have key NODE
24.                    in the PARENT_MAP dictionary set key NODE with value CURR
25.    return nothing</mark>
</code></pre>
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_01.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_02.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_03.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_04.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_05.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_07.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_08.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_09.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_10.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_11.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_12.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_13.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_15.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_16.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_17.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_18.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_19.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_DFS_20.svg">
</section>


<section>
<h3> Breadth First Search (BFS) </h3>
<pre class="" style="font-size: .38em; width: 105%; height: 500px"><code class="python" style="max-height: 1000px;">
1. function BREADTHFIRSTSEARCH(GRAPH,SRC,TAR)
2.     QUEUE = empty queue
3.     DISCOVERED = empty set
4.     PARENT_MAP = empty dictionary
5.     add SRC to DISCOVERED
6.     add SRC to QUEUE
7.     while QUEUE is not empty
8.         CURR = first element in QUEUE
9.         if CURR is TAR 
10.            PATH = empty list 
11.            TRACE = TAR
12.            while TRACE is not SRC
13.                    append TRACE to PATH
14.                    set TRACE equal to PARENT_MAP[TRACE]
15.                append SRC to PATH
16.                reverse the order of PATH
17.                return PATH
18.        NEIGHS = neighbors of CURR
19.        for EDGE in NEIGHS
20.            NODE = first entry in EDGE
21.            if NODE is not in DISCOVERED
22.                add NODE to DISCOVERED
23.                if PARENT_MAP does not have key NODE
24.                    in the PARENT_MAP dictionary set key NODE with value CURR
25.                append NODE to QUEUE
26.    return nothing
</code></pre>
</section>


<section>
<h3> Breadth First Search (BFS) </h3>
<pre class="" style="font-size: .38em; width: 105%; height: 500px"><code class="python" style="max-height: 1000px;">
1. function BREADTHFIRSTSEARCH(GRAPH,SRC,TAR)<mark>
2.     QUEUE = empty queue
3.     DISCOVERED = empty set</mark>
4.     PARENT_MAP = empty dictionary<mark>
5.     add SRC to DISCOVERED
6.     add SRC to QUEUE
7.     while QUEUE is not empty
8.         CURR = first element in QUEUE</mark>
9.         if CURR is TAR 
10.            PATH = empty list 
11.            TRACE = TAR
12.            while TRACE is not SRC
13.                    append TRACE to PATH
14.                    set TRACE equal to PARENT_MAP[TRACE]
15.                append SRC to PATH
16.                reverse the order of PATH
17.                return PATH<mark>
18.        NEIGHS = neighbors of CURR
19.        for EDGE in NEIGHS
20.            NODE = first entry in EDGE
21.            if NODE is not in DISCOVERED
22.                add NODE to DISCOVERED</mark>
23.                if PARENT_MAP does not have key NODE
24.                    in the PARENT_MAP dictionary set key NODE with value CURR<mark>
25.                append NODE to QUEUE</mark>
26.    return nothing
</code></pre>
</section>


<section>
<h3> Breadth First Search (BFS) </h3>
<pre class="" style="font-size: .38em; width: 105%; height: 500px"><code class="python" style="max-height: 1000px;">
1. function BREADTHFIRSTSEARCH(GRAPH,SRC,TAR)
2.     QUEUE = empty queue
3.     DISCOVERED = empty set<mark>
4.     PARENT_MAP = empty dictionary</mark>
5.     add SRC to DISCOVERED
6.     add SRC to QUEUE
7.     while QUEUE is not empty
8.         CURR = first element in QUEUE<mark>
9.         if CURR is TAR 
10.            PATH = empty list 
11.            TRACE = TAR
12.            while TRACE is not SRC
13.                    append TRACE to PATH
14.                    set TRACE equal to PARENT_MAP[TRACE]
15.                append SRC to PATH
16.                reverse the order of PATH
17.                return PATH</mark>
18.        NEIGHS = neighbors of CURR
19.        for EDGE in NEIGHS
20.            NODE = first entry in EDGE
21.            if NODE is not in DISCOVERED
22.                add NODE to DISCOVERED<mark>
23.                if PARENT_MAP does not have key NODE
24.                    in the PARENT_MAP dictionary set key NODE with value CURR</mark>
25.                append NODE to QUEUE<mark>
26.    return nothing</mark>
</code></pre>
</section>


<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_01.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_02.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_03.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_04.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_05.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_06.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_08.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_09.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_10.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_11.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_12.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_13.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_14.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_15.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_16.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_17.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_18.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_19.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_20.svg">
</section><section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_8.5_BFS_21.svg">
</section>

<section>
<h3>Remarks</h3>
<ul>
<li>BFS and DFS won't<br/> always have the same result</li>
<li>Multiple Paths: will return some path</li>
<li>No Path: return nothing</li>
</ul>
</section>
