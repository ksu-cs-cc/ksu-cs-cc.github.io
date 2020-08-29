---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 5 <br> Binary Trees <br> In-Order Traversal </h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section> 

<section>
<h4>In-Order Binary Tree Traversals</h4>
<ul>
<li>Left Child, Root, Right Child</li>
</ul>
<pre class="" style="font-size: .3em; width: 40%"><code class="python">
    function INORDER(SB)
        LEFTCHILD.INORDER(SB)
        append node ITEM to SB
        RIGHTCHILD.INORDER(SB)
 </code></pre>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav1.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav2.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
    <ul>
        <li> 10.INORDER(SB)</li>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav3.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
    <ul>
        <li> 10.INORDER(SB)</li>
        <ul>
            <li> 5.INORDER(SB)</li>
        </ul>
    </ul>

</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> 5 </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav4.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
    <ul>
        <li> 10.INORDER(SB)</li>
    </ul>

</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> 5 </td><td> 10 </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>



<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav5.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
    <ul>
        <li> 10.INORDER(SB)</li>
        <ul>
            <li> 20.INORDER(SB)</li>
        </ul>
    </ul>

</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> 5 </td><td> 10 </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav6.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
    <ul>
        <li> 10.INORDER(SB)</li>
        <ul>
            <li> 20.INORDER(SB)</li>
            <ul>
                <li> 15.INORDER(SB)</li>
            </ul>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> 5 </td><td> 10 </td><td> 15 </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav7.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
    <ul>
        <li> 10.INORDER(SB)</li>
        <ul>
            <li> 20.INORDER(SB)</li>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> 5 </td><td> 10 </td><td> 15 </td><td> 20 </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav8.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
    <ul>
        <li> 10.INORDER(SB)</li>
        <ul>
            <li> 20.INORDER(SB)</li>
            <ul>
                <li> 25.INORDER(SB)</li>
            </ul>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> 5 </td><td> 10 </td><td> 15 </td><td> 20 </td><td> 25 </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav9.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> 5 </td><td> 10 </td><td> 15 </td><td> 20 </td><td> 25 </td><td> 30 </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav10.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
    <ul>
        <li> 45.INORDER(SB)</li>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> 5 </td><td> 10 </td><td> 15 </td><td> 20 </td><td> 25 </td><td> 30 </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav11.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
    <ul>
        <li> 45.INORDER(SB)</li>
        <ul>
            <li> 35.INORDER(SB)</li>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> 5 </td><td> 10 </td><td> 15 </td><td> 20 </td><td> 25 </td><td> 30 </td><td> 35 </td><td> _ </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav12.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
    <ul>
        <li> 45.INORDER(SB)</li>
        <ul>
            <li> 35.INORDER(SB)</li>
            <ul>
                <li> 40.INORDER(SB)</li>
            </ul>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> 5 </td><td> 10 </td><td> 15 </td><td> 20 </td><td> 25 </td><td> 30 </td><td> 35 </td><td> 40 </td><td> _ </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav13.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
    <ul>
        <li> 45.INORDER(SB)</li>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> 5 </td><td> 10 </td><td> 15 </td><td> 20 </td><td> 25 </td><td> 30 </td><td> 35 </td><td> 40 </td><td> 45 </td><td> _ </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav14.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
    <ul>
        <li> 45.INORDER(SB)</li>
        <ul>
            <li> 50.INORDER(SB)</li>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> 5 </td><td> 10 </td><td> 15 </td><td> 20 </td><td> 25 </td><td> 30 </td><td> 35 </td><td> 40 </td><td> 45 </td><td> 50 </td><td> _ </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav15.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
    <ul>
        <li> 45.INORDER(SB)</li>
        <ul>
            <li> 50.INORDER(SB)</li>
            <ul>
                <li> 55.INORDER(SB)</li>
            </ul>
        </ul>
    </ul>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> 5 </td><td> 10 </td><td> 15 </td><td> 20 </td><td> 25 </td><td> 30 </td><td> 35 </td><td> 40 </td><td> 45 </td><td> 50 </td><td> 55 </td>
</tr>
</table>
</small>
</section>

<section>
<h3> Example </h3>
<div style="width:700px;float:left">
<img class="stretch plain" src="/images/315_4.3_binTrav16.svg">
</div>
<div style="width:700px;float:right">
<small>
<ul>
    <li> 30.INORDER(SB)</li>
</ul>
</small>
</div>
<small>
<table>
<tr>
<td>SB=</td><td> 5 </td><td> 10 </td><td> 15 </td><td> 20 </td><td> 25 </td><td> 30 </td><td> 35 </td><td> 40 </td><td> 45 </td><td> 50 </td><td> 55 </td>
</tr>
</table>
</small>
</section>

<section>
<h4>In-Order Binary Tree Traversals</h4>
<ul>
<li>Left Child, Root, Right Child</li>
</ul>
<pre class="" style="font-size: .3em; width: 40%"><code class="python">
    function INORDER(SB)
        LEFTCHILD.INORDER(SB)
        append node ITEM to SB
        RIGHTCHILD.INORDER(SB)
 </code></pre>
</section>