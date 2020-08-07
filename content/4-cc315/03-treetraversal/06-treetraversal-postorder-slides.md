---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 3 <br> Tree Traversals <br> Postorder </h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3> Postorder Traversal </h3>
<ul>
<li> Post: refers to the root </li>
<li> Postorder traverse children then record the root</li>
</ul>
</section>

<section>
<h3> Pseudocode </h3>
<pre class="" style="font-size: .3em; width: 40%"><code class="python">
    function POSTORDER(SB)
        for CHILD in node`s CHILDREN
            CHILD.POSTORDER(SB)
        append node ITEM to SB
 </code></pre>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_3.5_treePreO.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> A.POSTORDER(SB)</li>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
    </ul>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
        <ul>
            <li> F.POSTORDER(SB)</li>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
        <ul>
            <li> F.POSTORDER(SB)</li>
            <li> G.POSTORDER(SB)</li>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> B </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
        <li> C.POSTORDER(SB)</li>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> B </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
        <li> C.POSTORDER(SB)</li>
        <ul>
            <li> H.POSTORDER(SB)</li>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> B </td><td> H </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
        <li> C.POSTORDER(SB)</li>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> B </td><td> H </td><td> C </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
        <li> C.POSTORDER(SB)</li>
        <li> D.POSTORDER(SB)</li>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> B </td><td> H </td><td> C </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
        <li> C.POSTORDER(SB)</li>
        <li> D.POSTORDER(SB)</li>
            <ul>
                <li> I.POSTORDER(SB)</li>
            </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> B </td><td> H </td><td> C </td><td> I </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
        <li> C.POSTORDER(SB)</li>
        <li> D.POSTORDER(SB)</li>
            <ul>
                <li> I.POSTORDER(SB)</li>
                <li> J.POSTORDER(SB)</li>
            </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> B </td><td> H </td><td> C </td><td> I </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
        <li> C.POSTORDER(SB)</li>
        <li> D.POSTORDER(SB)</li>
            <ul>
                <li> I.POSTORDER(SB)</li>
                <li> J.POSTORDER(SB)</li>
                <ul>
                    <li> L.POSTORDER(SB)</li>
                </ul>
            </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> B </td><td> H </td><td> C </td><td> I </td><td> L </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
        <li> C.POSTORDER(SB)</li>
        <li> D.POSTORDER(SB)</li>
            <ul>
                <li> I.POSTORDER(SB)</li>
                <li> J.POSTORDER(SB)</li>
                <ul>
                    <li> L.POSTORDER(SB)</li>
                    <li> M.POSTORDER(SB)</li>
                </ul>
            </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> B </td><td> H </td><td> C </td><td> I </td><td> L </td><td> M </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
        <li> C.POSTORDER(SB)</li>
        <li> D.POSTORDER(SB)</li>
            <ul>
                <li> I.POSTORDER(SB)</li>
                <li> J.POSTORDER(SB)</li>
            </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> B </td><td> H </td><td> C </td><td> I </td><td> L </td><td> M </td><td> J </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
        <li> C.POSTORDER(SB)</li>
        <li> D.POSTORDER(SB)</li>
            <ul>
                <li> I.POSTORDER(SB)</li>
                <li> J.POSTORDER(SB)</li>
                <li> K.POSTORDER(SB)</li>
            </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> B </td><td> H </td><td> C </td><td> I </td><td> L </td><td> M </td><td> J </td><td> K </td><td> _ </td><td> _ </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
        <li> C.POSTORDER(SB)</li>
        <li> D.POSTORDER(SB)</li>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> B </td><td> H </td><td> C </td><td> I </td><td> L </td><td> M </td><td> J </td><td> K </td><td> D </td><td> _ </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
    <ul>
        <li> B.POSTORDER(SB)</li>
        <li> C.POSTORDER(SB)</li>
        <li> D.POSTORDER(SB)</li>
        <li> E.POSTORDER(SB)</li>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> B </td><td> H </td><td> C </td><td> I </td><td> L </td><td> M </td><td> J </td><td> K </td><td> D </td><td> E </td><td> _ </td>
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
    <li> A.POSTORDER(SB)</li>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> F </td><td> G </td><td> B </td><td> H </td><td> C </td><td> I </td><td> L </td><td> M </td><td> J </td><td> K </td><td> D </td><td> E </td><td> A </td>
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
    <li> FGBHCILMJKDEA </li>
    <li> EHCGFBLMJKIDA </li>
    <li> LMJKIDEHCFGBA </li>
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
    <li> GFBCHLMJIKDEA </li>
    <li> EHCLMKJIDGFBA </li>
    <li> ABFGCHDIJLMKE </li>
</ul>
</small>
</div>
</section>


<section>
<h3> Postorder Traversal </h3>
<ul>
<li> Post: refers to the root </li>
<li> Postorder traverse children then record the root</li>
</ul>
</section>