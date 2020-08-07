---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 3 <br> Tree Traversals <br> Preorder </h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3> Preorder Traversal </h3>
<ul>
<li> Pre: refers to the root </li>
<li> Record Root then Children </li>
</ul>
</section>

<section>
<h3> Pseudocode </h3>
<pre class="" style="font-size: .3em; width: 40%"><code class="python">
    function PREORDER(SB)
        append node ITEM to SB
        for CHILD in node`s CHILDREN
            CHILD.PREORDER(SB)
 </code></pre>
</section>

<section>
<h3> Example </h3>
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</section>