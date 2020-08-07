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
<h3> Same Tree </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<img class="stretch plain" src="/images/315_3.5_treePre2.svg">
</div>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
<li> A.PREORDER(SB)</li>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
<li> A.PREORDER(SB)</li>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> A </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> A.PREORDER(SB)</li>
    <ul>
        <li>B.PREORDER(SB)</li>
    </ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> A </td><td> B </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> A.PREORDER(SB)</li>
    <ul>
        <li>B.PREORDER(SB)</li>
        <ul>
            <li>F.PREORDER(SB)</li>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> A </td><td> B </td><td> F </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> A.PREORDER(SB)</li>
    <ul>
        <li>B.PREORDER(SB)</li>
        <ul>
            <li>F.PREORDER(SB)</li>
            <li>G.PREORDER(SB)</li>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> A </td><td> B </td><td> F </td><td> G </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> A.PREORDER(SB)</li>
    <ul>
        <li>B.PREORDER(SB)</li>
        <li>C.PREORDER(SB)</li>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> A </td><td> B </td><td> F </td><td> G </td><td> C </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> A.PREORDER(SB)</li>
    <ul>
        <li>B.PREORDER(SB)</li>
        <li>C.PREORDER(SB)</li>
        <ul>
            <li> H.PREORDER(SB)</li>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> A </td><td> B </td><td> F </td><td> G </td><td> C </td><td> H </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> A.PREORDER(SB)</li>
    <ul>
        <li>B.PREORDER(SB)</li>
        <li>C.PREORDER(SB)</li>
        <li>D.PREORDER(SB)</li>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> A </td><td> B </td><td> F </td><td> G </td><td> C </td><td> H </td><td> D </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> A.PREORDER(SB)</li>
    <ul>
        <li>B.PREORDER(SB)</li>
        <li>C.PREORDER(SB)</li>
        <li>D.PREORDER(SB)</li>
        <ul>
            <li> I.PREORDER(SB)</li>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> A </td><td> B </td><td> F </td><td> G </td><td> C </td><td> H </td><td> D </td><td> I </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> A.PREORDER(SB)</li>
    <ul>
        <li>B.PREORDER(SB)</li>
        <li>C.PREORDER(SB)</li>
        <li>D.PREORDER(SB)</li>
        <ul>
            <li> I.PREORDER(SB)</li>
            <li> J.PREORDER(SB)</li>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> A </td><td> B </td><td> F </td><td> G </td><td> C </td><td> H </td><td> D </td><td> I </td><td> J </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> A.PREORDER(SB)</li>
    <ul>
        <li>B.PREORDER(SB)</li>
        <li>C.PREORDER(SB)</li>
        <li>D.PREORDER(SB)</li>
        <ul>
            <li> I.PREORDER(SB)</li>
            <li> J.PREORDER(SB)</li>
            <ul>
                <li> L.PREORDER(SB)</li>
            </ul>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> A </td><td> B </td><td> F </td><td> G </td><td> C </td><td> H </td><td> D </td><td> I </td><td> J </td><td> L </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> A.PREORDER(SB)</li>
    <ul>
        <li>B.PREORDER(SB)</li>
        <li>C.PREORDER(SB)</li>
        <li>D.PREORDER(SB)</li>
        <ul>
            <li> I.PREORDER(SB)</li>
            <li> J.PREORDER(SB)</li>
            <ul>
                <li> L.PREORDER(SB)</li>
                <li> M.PREORDER(SB)</li>
            </ul>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> A </td><td> B </td><td> F </td><td> G </td><td> C </td><td> H </td><td> D </td><td> I </td><td> J </td><td> L </td><td> M </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> A.PREORDER(SB)</li>
    <ul>
        <li>B.PREORDER(SB)</li>
        <li>C.PREORDER(SB)</li>
        <li>D.PREORDER(SB)</li>
        <ul>
            <li> I.PREORDER(SB)</li>
            <li> J.PREORDER(SB)</li>
            <li> K.PREORDER(SB)</li>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> A </td><td> B </td><td> F </td><td> G </td><td> C </td><td> H </td><td> D </td><td> I </td><td> J </td><td> L </td><td> M </td><td> K </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> A.PREORDER(SB)</li>
    <ul>
        <li>B.PREORDER(SB)</li>
        <li>C.PREORDER(SB)</li>
        <li>D.PREORDER(SB)</li>
        <li>E.PREORDER(SB)</li>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> A </td><td> B </td><td> F </td><td> G </td><td> C </td><td> H </td><td> D </td><td> I </td><td> J </td><td> L </td><td> M </td><td> K </td><td> E </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Examples </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> ABFGCHDIJLMKE </li>
    <li> AECHBGFDKIJML </li>
    <li> ACHBGFEDIKJLM </li>
    <li> ... </li>
</ul>
</small>
</div>
</section>

<section>
<h3> Counterexamples </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> AGFBHCDIKJLME </li>
    <li> EADIJLMKCHBFG </li>
    <li> ABCFGHEDKIJLM </li>
</ul>
</small>
</div>
</section>

<section>
<h3> Preorder Traversal </h3>
<ul>
<li> Pre: refers to the root </li>
<li> Record Root then Children </li>
</ul>
</section>