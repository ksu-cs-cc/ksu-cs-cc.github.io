---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 12 <br> Performance <br> Trees</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3>Performance Analysis</h3>
<ul>
<li>Insert</li>
<li>Access</li>
<li>Find</li>
<li>Delete</li>
</ul>
</section>

<section>
<h3>Generic Tree</h3>
<table>
  <tr>
    <th>Insert</th>
    <th>Access</th>
    <th>Find</th>
    <th>Delete</th>
  </tr>
  <tr>
    <td>1 or n</td>
    <td>1 or n</td>
    <td>n</td>
    <td>n</td>
  </tr>
</table>
<p>Where n is the number of nodes</p>
</section>

<section>
<h3>Tree: Insert</h3>
<h6>Running time: 1 or n</h6>
<img class="stretch plain" src="/images/315_3.3_treeEx.svg">
</section>

<section>
<h3>Tree: Access</h3>
<h6>Running time: 1 or n</h6>
<img class="stretch plain" src="/images/315_3.3_treeEx.svg">
</section>

<section>
<h3>Tree: Find</h3>
<h6>Running time: n</h6>
<img class="stretch plain" src="/images/315_3.3_treeEx.svg">
</section>

<section>
<h3> Tree: Delete</h3>
<h6>Running time: n</h6>
<img class="stretch plain" src="/images/315_3.3_treeEx.svg">
</section>

<section>
<h3>Tree: Memory</h3>
<p>Linear with respect to the number of nodes</p>
</section>

<section>
<h3>Trie</h3>
<table>
  <tr>
    <th>Insert</th>
    <th>Access</th>
    <th>Find</th>
    <th>Delete</th>
  </tr>
  <tr>
    <td>m</td>
    <td>m</td>
    <td>m</td>
    <td>m</td>
  </tr>
</table>
<p>Where m is the length of the word</p>
</section>

<section>
<h3>Trie: Insert, Access, Find, Remove</h3>
<h6>Running time: m</h6>
<img class="stretch plain" src="/images/315_4.3_trie1.svg">
</section>

<section>
<h3>Trie: Memory</h3>
<p>m * n</p>
</section>

<section>
<h3>Binary Tree</h3>
<table>
  <tr>
    <th>Insert</th>
    <th>Access</th>
    <th>Find</th>
    <th>Delete</th>
  </tr>
  <tr>
    <td>log(n) or n</td>
    <td>log(n) or n</td>
    <td>log(n) or n</td>
    <td>log(n) or n</td>
  </tr>
</table>
<p>Where n is the number of nodes</p>
</section>

<section>
<h3>Trie: Insert, Access, Find, Remove</h3>
<h6>Running time: log(n) or n</h6>
<img class="stretch plain" src="/images/315_12_bin_unbal_bal.svg">
</section>


<section>
<h3>Binary Tree: Memory</h3>
<p>Linear with respect to the number of nodes</p>
</section>

<section>
<small>
<h3>Summary</h3>
<table>
  <tr>
    <th></th>
    <th>Insert</th>
    <th>Access</th>
    <th>Find</th>
    <th>Delete</th>
    <th>Memory</th>
  </tr>
  <tr>
    <td>Trees</td>
    <td>1 or n</td>
    <td>1 or n</td>
    <td>n</td>
    <td>n</td>
    <td>n</td>
  </tr>
  <tr>
    <td>Tries</td>
    <td>m</td>
    <td>m</td>
    <td>m</td>
    <td>m</td>
    <td>m*w</td>
  </tr>
  <tr>
    <td>Binary Trees</td>
    <td>log(n) or n</td>
    <td>log(n) or n</td>
    <td>log(n) or n</td>
    <td>log(n) or n</td>
    <td>n</td>
  </tr>
</table>
<p>Where n is the number of nodes, m is the length of the longest word, and w is the number of words</p>
</small>

</section>