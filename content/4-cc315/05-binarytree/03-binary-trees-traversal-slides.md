---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 5 <br> Binary Trees <br> Traversals </h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section> 

<section>
<h3>Recall: Traversals</h3>
<ul>
<li>Preorder: Root then children</li>
<li>Postorder: Children then root</li>
</ul>
</section>

<section>
<h4>Preorder Binary Tree Traversals</h4>
<ul>
<li>Root, Left Child, Right Child</li>
</ul>
<pre class="" style="font-size: .3em; width: 40%"><code class="python">
    function PREORDER(SB)
        append node ITEM to SB
        LEFTCHILD.PREORDER(SB)
        RIGHTCHILD.PREORDER(SB)
 </code></pre>
</section>

<section>
<h4>Postorder Binary Tree Traversals</h4>
<ul>
<li>Left Child, Right Child, Root</li>
</ul>
<pre class="" style="font-size: .3em; width: 40%"><code class="python">
    function POSTORDER(SB)
        LEFTCHILD.POSTORDER(SB)
        RIGHTCHILD.POSTORDER(SB)
        append node ITEM to SB
 </code></pre>
</section>

<section>
<h3> Example </h3>
<img class="stretch plain" src="/images/315_4.3_binTrav.svg">
<small>
<table>
<tr>
<td>Preorder</td><td> 30 </td><td> 10 </td><td> 5 </td><td> 20 </td><td> 15 </td><td> 25 </td><td> 45 </td><td> 35 </td><td> 40 </td><td> 50 </td><td> 55 </td></tr>
<tr>
<td>Postorder</td><td> 5 </td><td> 15 </td><td> 25 </td><td> 20 </td><td> 10 </td><td> 40 </td><td> 35 </td><td> 55 </td><td> 50 </td><td> 45 </td><td> 30 </td>
</tr>
</table>
</small>
</section>

<section>
<h3>Binary Tree Traversals</h3>
<ul>
<li>Preorder: Root Left Right</li>
<li>Postorder: Left Right Root</li>
</ul>
</section>