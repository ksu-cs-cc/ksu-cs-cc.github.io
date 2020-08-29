---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 5 <br> Binary Trees <br> UML Diagram </h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section> 


<section>
<img class="stretch plain" src="/images/315_4.5_binUML.png">
</section> 

<section>
<h3>Initialization</h3>
<ul>
<li> Initialize a 'MyBinaryTree' using 'MyTree' init.</li>
<li> Set LEFTCHILD to NONE</li>
<li> Set RIGHTTCHILD to NONE</li>
</ul>
</section> 

<section>
<h3>Is Empty</h3>
<ul>
<li> Return True if item is NONE</li>
<li> Return False if item is not NONE</li>
</ul>
</section> 

<section>
<h3>Get Size</h3>
<ul>
<li> Return zero the tree is empty</li>
<li> Return the size from MyTree's get size</li>
</ul>
</section> 

<section>
<h3>To Sorted List</h3>
<pre class="" style="font-size: .3em; width: 50%"><code class="python">
    function TOSORTEDLIST()
        LIST = []
        if there`s LEFTCHILD
            LIST = LIST + LEFTCHILD.TOSORTEDLIST
        LIST = LIST + ITEM
        if there`s RIGHTCHILD
            LIST = LIST + RIGHTCHILD.TOSORTEDLIST
        return LIST
 </code></pre>
</section> 

<section>
<img class="stretch plain" src="/images/315_4.5_binUML.png">
</section> 