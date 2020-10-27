---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 10 <br> Heaps and Priority Queues <br> Node Relationships</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3>Heaps in Code</h3>
<ul>
<li>Heaps are trees (and graphs)</li>
<li>Don't use those structures</li>
</ul>
</section>

<section>
<h3>Why Not Trees?</h3>
<p>Trees have too much variance and possibilities for configuration. A tree with 5 nodes can look very different.</p>
<img class="stretch plain" src="/images/315_10.2_tree.svg">
</section>

<section>
<h3>Mapping</h3>
<img class="stretch plain" src="/images/315_10.2_map_tree.svg">
</section>

<section>
<h3>Mapping</h3>
<img class="stretch plain" src="/images/315_10.2_map_array.svg">
</section>

<section>
<h3>Relationships</h3>
<img class="stretch plain" src="/images/315_10.2_array.svg">
</section>

<section>
<h3>Relationships</h3>
<ul>
<li>For node i</li>
<ul>
<li>Parent of i: floor(i/2)</li>
<li>Left child of i: 2*i</li>
<li>Right child of i: 2*i + 1</li>
</ul>
</ul>
</section>


<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_10.2_array.svg">

| Node | Parent | Left | Right |
| --- | --- | --- | --- |
| 7 | floor(7/2) <br/>=  3 | 2*7 <br/>= 14 | 2*7 + 1 <br/>= 15 |

</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_10.2_array.svg">

| Node | Parent | Left | Right |
| --- | --- | --- | --- |
| 7 | floor(7/2) <br/>=  3 | 2*7 <br/>= 14 | 2*7 + 1 <br/>= 15 |
| 9 | floor(9/2) <br/>=  4 | 2*9 <br/>= 18 | 2*9 + 1 <br/>= 19 |
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_10.2_map_tree.svg">
<small>

| Node | Parent | Left | Right |
| --- | --- | --- | --- |
| 7 | floor(7/2) <br/>=  3 | 2*7 <br/>= 14 | 2*7 + 1 <br/>= 15 |
| 9 | floor(9/2) <br/>=  4 | 2*9 <br/>= 18 | 2*9 + 1 <br/>= 19 |

</small>
</section>

<section>
<h3>Useful Fact</h3>
<p>For a heap with n nodes, the nodes floor(n/2)+1 through n, will always be leaves</p>
<img class="stretch plain" src="/images/315_10.2_map_array.svg">
</section>

<section>
<h3>Relationships</h3>
<ul>
<li>For node i</li>
<ul>
<li>Parent of i: floor(i/2)</li>
<li>Left child of i: 2*i</li>
<li>Right child of i: 2*i + 1</li>
</ul>
<li>For heap with n nodes:</li>
<ul>
<li>floor(n/2)+1 through n <br/>will be leaves</li>
</ul>
</ul>
</section>