---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 12 <br> Performance <br> Algorithms </h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3>Algorithm Analysis</h3>
<ul>
<li>Time</li>
<li>Space</li>
</ul>
</section>

<section>
<h3> Preorder Traversal </h3>
<pre class="" style="font-size: .3em; width: 40%"><code class="python">
    function PREORDER(SB)
        append node ITEM to SB
        for CHILD in node`s CHILDREN
            CHILD.PREORDER(SB)
 </code></pre>
  <p> Time: linear w.r.t number of nodes<br/>Space: linear w.r.t number of nodes</p>
</section>


<section>
<h3> Postorder Traversal </h3>
<pre class="" style="font-size: .3em; width: 40%"><code class="python">
    function POSTORDER(SB)
        for CHILD in node`s CHILDREN
            CHILD.POSTORDER(SB)
        append node ITEM to SB
 </code></pre>
   <p> Time: linear w.r.t number of nodes<br/>Space: linear w.r.t number of nodes</p>
</section>

<section>
<h3> Postorder or Postorder on Binary Tree </h3>
<p> Time: linear w.r.t number of nodes<br/>
Space: constant</p>
</section>


<section>
<h3>In-Order Binary Tree Traversals</h3>
<pre class="" style="font-size: .3em; width: 40%"><code class="python">
    function INORDER(SB)
        LEFTCHILD.INORDER(SB)
        append node ITEM to SB
        RIGHTCHILD.INORDER(SB)
 </code></pre>
 <p> Time: linear w.r.t number of nodes<br/>
Space: constant</p>
</section>

<section>
<h3> Depth First Search Time </h3>
<pre class="" style="font-size: .38em; width: 105%; height: 400px"><code class="python" style="max-height: 1000px;">
1. function DEPTHFIRSTSEARCH(GRAPH,SRC,TAR)
2.     STACK = empty array                    
3.     DISCOVERED = empty set                 
4.     PARENT_MAP = empty dictionary          
5.     append SRC to STACK
6.     while STACK is not empty               'n'
7.         CURR = top of the stack            
8.         if CURR not in DISCOVERED
9.             if CURR is TAR
10.                 PATH = empty array        
11.                 TRACE = TAR               
12.                 while TRACE is not SRC    'n'
13.                     append TRACE to PATH
14.                     set TRACE equal to PARENT_MAP[TRACE]
15.                 append SRC to PATH
16.                 reverse the order of PATH
17.                 return PATH
18.            add CURR to DISCOVERED    
19.            NEIGHS = neighbors of CURR     
20.            for EDGE in NEIGHS             'n'
21.                NODE = first entry in EDGE 
22.                append NODE to STACK
23.                if PARENT_MAP does not have key NODE
24.                    in the PARENT_MAP dictionary set key NODE with value CURR
25.    return nothing
</code></pre>
</section>

<section>
<h3> Depth First Search Space </h3>
<pre class="" style="font-size: .38em; width: 105%; height: 400px"><code class="python" style="max-height: 1000px;">
1. function DEPTHFIRSTSEARCH(GRAPH,SRC,TAR)
2.     STACK = empty array                    'n'
3.     DISCOVERED = empty set                 'n'
4.     PARENT_MAP = empty dictionary          'n'
5.     append SRC to STACK
6.     while STACK is not empty
7.         CURR = top of the stack            '1'
8.         if CURR not in DISCOVERED
9.             if CURR is TAR
10.                 PATH = empty array        'n'
11.                 TRACE = TAR               '1'
12.                 while TRACE is not SRC
13.                     append TRACE to PATH
14.                     set TRACE equal to PARENT_MAP[TRACE]
15.                 append SRC to PATH
16.                 reverse the order of PATH
17.                 return PATH
18.            add CURR to DISCOVERED    
19.            NEIGHS = neighbors of CURR     'n'
20.            for EDGE in NEIGHS             '1'
21.                NODE = first entry in EDGE '1'
22.                append NODE to STACK
23.                if PARENT_MAP does not have key NODE
24.                    in the PARENT_MAP dictionary set key NODE with value CURR
25.    return nothing
</code></pre>
</section>

<section>
<h3> Breadth First Search Time </h3>
<pre class="" style="font-size: .38em; width: 105%; height: 500px"><code class="python" style="max-height: 1000px;">
1. function BREADTHFIRSTSEARCH(GRAPH,SRC,TAR)
2.     QUEUE = empty queue
3.     DISCOVERED = empty set
4.     PARENT_MAP = empty dictionary
5.     add SRC to DISCOVERED
6.     add SRC to QUEUE
7.     while QUEUE is not empty             'n'
8.         CURR = first element in QUEUE
9.         if CURR is TAR 
10.            PATH = empty list 
11.            TRACE = TAR
12.            while TRACE is not SRC       'n'
13.                    append TRACE to PATH
14.                    set TRACE equal to PARENT_MAP[TRACE]
15.                append SRC to PATH
16.                reverse the order of PATH
17.                return PATH
18.        NEIGHS = neighbors of CURR
19.        for EDGE in NEIGHS               'n'
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
<h3> Breadth First Search Space </h3>
<pre class="" style="font-size: .38em; width: 105%; height: 500px"><code class="python" style="max-height: 1000px;">
1. function BREADTHFIRSTSEARCH(GRAPH,SRC,TAR)
2.     QUEUE = empty queue                  'n'
3.     DISCOVERED = empty set               'n'
4.     PARENT_MAP = empty dictionary        'n'
5.     add SRC to DISCOVERED
6.     add SRC to QUEUE
7.     while QUEUE is not empty
8.         CURR = first element in QUEUE    '1'
9.         if CURR is TAR 
10.            PATH = empty list            'n'
11.            TRACE = TAR                  '1'
12.            while TRACE is not SRC
13.                    append TRACE to PATH
14.                    set TRACE equal to PARENT_MAP[TRACE]
15.                append SRC to PATH
16.                reverse the order of PATH
17.                return PATH
18.        NEIGHS = neighbors of CURR       'n'
19.        for EDGE in NEIGHS               '1'
20.            NODE = first entry in EDGE   '1'
21.            if NODE is not in DISCOVERED
22.                add NODE to DISCOVERED
23.                if PARENT_MAP does not have key NODE
24.                    in the PARENT_MAP dictionary set key NODE with value CURR
25.                append NODE to QUEUE
26.    return nothing
</code></pre>
</section>

<section>
<h3> Kruskals Time</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
function KRUSKAL(GRAPH)
    MST = GRAPH without the edges attribute(s)
    ALLSETS = an empty list which will contain the sets
    for NODE in GRAPH NODES                                   'n'
        SET = a set with element NODE
        add SET to ALLSETS
    EDGES = set of GRAPHs edges
    SORTEDEDGES = EDGES sorted by edge weight, smallest to largest
    for EDGE in SORTEDEDGES                                   'e'
        SRC = source node of EDGE
        TAR = target node of EDGE
        SRCSET = the set from SETS in which SRC is contained  'log(n)'
        TARSET = the set form SETS in which TAR is contained  'log(n)'
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
<h3> Kruskals Space</h3>
<pre class="" style="font-size: .38em; width: 100%; height: 400px"><code class="python" style="max-height: 1000px;">
function KRUSKAL(GRAPH)
    MST = GRAPH without the edges attribute(s)                      'n^2' or 'n + e'
    ALLSETS = an empty list which will contain the sets             'n'
    for NODE in GRAPH NODES                                         '1' 'n'
        SET = a set with element NODE                               '1'
        add SET to ALLSETS
    EDGES = set of GRAPHs edges                                     'e'
    SORTEDEDGES = EDGES sorted by edge weight, smallest to largest  'e'
    for EDGE in SORTEDEDGES
        SRC = source node of EDGE                                   '1'
        TAR = target node of EDGE                                   '1'
        SRCSET = the set from SETS in which SRC is contained        '1'
        TARSET = the set form SETS in which TAR is contained        '1'
        if SRCSET not equal TARSET
            UNIONSET = SRCSET union TARSET                          '1'
            add UNIONSET to ALLSETS
            remove SRCSET from ALLSETS
            remove TARSET from ALLSETS
            add EDGE to MST as undirected edge
    return MST
</code></pre>
</section>


<section>
<h3> Prims Time</h3>
<pre class="" style="font-size: .35em; width: 100%; height: 400px"><code class="python" style="max-height: 1000px;">
function PRIM(GRAPH, START)
    MST = GRAPH without the edges attribute(s)                  'n'
    VISITED = empty set
    add START to VISITED
    AVAILEDGES = list of edges where START is the source        'n' or '1'
    sort AVAILEDGES                                             'e * log(e)' or 'log(e)'            
    while VISITED is not all of the nodes                       'e'
        SMLEDGE = smallest edge in AVAILEDGES                   'log(e)' or '1'
        SRC = source of SMLEDGE
        TAR = target of SMLEDGE
        if TAR not in VISITED
            add SMLEDGE to MST as undirected edge
            add TAR to VISITED
            add the edges where TAR is the source to AVAILEDGES
        remove SMLEDGE from AVAILEDGES
        sort AVAILEDGES                                        'e * log(e)' or 'log(e)'
    return MST
</code></pre>
</section>

<section>
<h3> Prims Space</h3>
<pre class="" style="font-size: .38em; width: 100%; height: 400px"><code class="python" style="max-height: 1000px;">
function PRIM(GRAPH, START)
    MST = GRAPH without the edges attribute(s)                  'n^2' or 'n + e'
    VISITED = empty set                                         'n'
    add START to VISITED
    AVAILEDGES = list of edges where START is the source        'e'
    sort AVAILEDGES
    while VISITED is not all of the nodes
        SMLEDGE = smallest edge in AVAILEDGES                   '1'
        SRC = source of SMLEDGE                                 '1'
        TAR = target of SMLEDGE                                 '1'
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
<h3>Dijkstra's Time</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
DIJKSTRAS(GRAPH, SRC)
    SIZE = size of GRAPH
    DISTS = array with length equal to SIZE
    PREVIOUS = array with length equal to SIZE
    set all of the entries in PREVIOUS to none
    set all of the entries in DISTS to infinity 
    DISTS[SRC] = 0 
    PQ = min-priority queue
    loop IDX starting at 0 up to SIZE                   'n'
        insert (DISTS[IDX],IDX) into PQ
    while PQ is not empty                               'n'
        MIN = REMOVE-MIN from PQ
        for NODE in neighbors of MIN                    'n' 
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
<h3>Dijkstra's Space</h3>
<pre class="" style="font-size: .4em; width: 90%; height: 400px"><code class="python" style="max-height: 1000px;">
DIJKSTRAS(GRAPH, SRC)
    SIZE = size of GRAPH                                    '1'
    DISTS = array with length equal to SIZE                 'n'
    PREVIOUS = array with length equal to SIZE              'n'
    set all of the entries in PREVIOUS to none
    set all of the entries in DISTS to infinity 
    DISTS[SRC] = 0 
    PQ = min-priority queue                                 'n'
    loop IDX starting at 0 up to SIZE                       '1'
        insert (DISTS[IDX],IDX) into PQ
    while PQ is not empty
        MIN = REMOVE-MIN from PQ                            '1' 
        for NODE in neighbors of MIN                        '1' 'n'
            WEIGHT = graph weight between MIN and NODE      '1'
            CALC = DISTS[MIN] + WEIGHT                      '1'
            if CALC < DISTS[NODE]
                DISTS[NODE] = CALC
                PREVIOUS[NODE] = MIN
                PQIDX = index of NODE in PQ                 '1'
                PQ decrease-key (CALC, PQIDX)
    return DISTS and PREVIOUS
</code></pre>
</section>



<section>
<small>
<h3>Summary</h3>
<table>
  <tr>
    <th></th>
    <th>Time</th>
    <th>Space</th>
  </tr>
    <tr>
    <td>Preorder</td>
    <td>n</td>
    <td>n</td>
  </tr>
      <tr>
<td>Postorder</td>
    <td>n</td>
    <td>n</td>
  </tr>
      <tr>
    <td>Preorder (on Binary)</td>
    <td>n</td>
    <td>1</td>
  </tr>
      <tr>
<td>Postorder (on Binary)</td>
    <td>n</td>
    <td>1</td>
  </tr>
  <td>Inorder (on Binary)</td>
    <td>n</td>
    <td>1</td>
  </tr>

</table>

</small>

</section>

<section>
<small>
<h3>Summary (Continued)</h3>
<table>
  <tr>
    <th></th>
    <th>Time</th>
    <th>Space</th>
  </tr>
  <tr>
    <td>DFS</td>
    <td>n^2</td>
    <td>n</td>
  </tr>
  <tr>
    <td>BFS</td>
    <td>n^2</td>
    <td>n</td>
  </tr>
  </table>
  <table>
    <tr>
    <th></th>
    <th>Time</th>
    <th>Space</th>
  </tr>
  <tr>
    <td>Kruskal (List Graph)</td>
    <td>e * log(n)</td>
    <td>n + e</td>
  </tr>
  <tr>
    <td>Kruskal (Matrix Graph)</td>
    <td>e * log(n)</td>
    <td>n^2</td>
  </tr>
  <tr>
    <td>Prims (List Graph and PQ)</td>
    <td>e * log(n)</td>
    <td>n + e</td>
  </tr>
  <tr>
    <td>Prims (Matrix Graph and PQ)</td>
    <td>e * log(n)</td>
    <td>n^2</td>
  </tr>
    <tr>
    <td>Prims (List Graph and no PQ)</td>
    <td>e^2 * log(e)</td>
    <td>n + e</td>
  </tr>
  <tr>
    <td>Prims (Matrix Graph and no PQ)</td>
    <td>e^2 * log(e)</td>
    <td>n^2</td>
  </tr>
  </table>
  
  <table>
    <tr>
    <th></th>
    <th>Time</th>
    <th>Space</th>
  </tr>
  <tr>
    <td>Dijkstra's</td>
    <td>(n + e) * log(n)</td>
    <td>n</td>
  </tr>
</table>
</small>

</section>