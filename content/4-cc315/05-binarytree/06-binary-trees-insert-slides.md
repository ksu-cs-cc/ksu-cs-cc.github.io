---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 5 <br> Binary Trees <br> Insert Element </h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section> 


<section>
<h3>Example<h3>
<img class="stretch plain" src="/images/315_4.6_insBase.svg">
</section> 

<section>
<img class="stretch plain" src="/images/315_4.6_insBase1.svg">
</section> 

<section>
<img class="stretch plain" src="/images/315_4.6_insBase2.svg">
</section> 

<section>
<img class="stretch plain" src="/images/315_4.6_insBase3.svg">
</section> 

<section>
<img class="stretch plain" src="/images/315_4.6_insBase4.svg">
</section> 


<section>
<h3>Insert</h3>
<pre class="" style="font-size: .3em; width: 70%; height: 400px"><code class="python" style="max-height: 1000px;">
function INSERT(VALUE)
    if node.ITEM is VALUE
        return false
    else if node.ITEM > VALUE 
        LEFTCHILD = node`s left child
        if LEFTCHILD is NONE
            CHILD = new BINARYTREE with root.ITEM equal VALUE
            add CHILD to nodes children
            set node.LEFTCHILD equal to CHILD
        else
            LEFTCHILD.INSERT(VALUE)
    else
        RIGHTCHILD = node`s right child
        if RIGHTCHILD is NONE
            CHILD = new BINARYTREE with root.ITEM equal VALUE
            add CHILD to nodes children
            set node.RIGHTCHILD equal to CHILD
        else
            RIGHTCHILD.INSERT(VALUE)
end function
 </code></pre>
</section> 

<section>
<h3>Insert</h3>
<pre class="" style="font-size: .3em; width: 70%; height: 400px"><code class="python" style="max-height: 1000px;">
function INSERT(VALUE)
    if node.ITEM is VALUE<mark>
        return false</mark>
    else if node.ITEM > VALUE 
        LEFTCHILD = node`s left child
        if LEFTCHILD is NONE
            CHILD = new BINARYTREE with root.ITEM equal VALUE
            add CHILD to nodes children
            set node.LEFTCHILD equal to CHILD
        else
            LEFTCHILD.INSERT(VALUE)
    else
        RIGHTCHILD = node`s right child
        if RIGHTCHILD is NONE
            CHILD = new BINARYTREE with root.ITEM equal VALUE
            add CHILD to nodes children
            set node.RIGHTCHILD equal to CHILD
        else
            RIGHTCHILD.INSERT(VALUE)
end function
 </code></pre>
</section> 


<section>
<h3>Insert</h3>
<pre class="" style="font-size: .3em; width: 70%; height: 400px"><code class="python" style="max-height: 1000px;">
function INSERT(VALUE)
    if node.ITEM is VALUE
        return false
    else if node.ITEM > VALUE <mark>
        LEFTCHILD = node`s left child
        if LEFTCHILD is NONE
            CHILD = new BINARYTREE with root.ITEM equal VALUE
            add CHILD to nodes children
            set node.LEFTCHILD equal to CHILD
        else
            LEFTCHILD.INSERT(VALUE)</mark>
    else
        RIGHTCHILD = node`s right child
        if RIGHTCHILD is NONE
            CHILD = new BINARYTREE with root.ITEM equal VALUE
            add CHILD to nodes children
            set node.RIGHTCHILD equal to CHILD
        else
            RIGHTCHILD.INSERT(VALUE)
end function
 </code></pre>
</section> 

<section>
<h3>Insert</h3>
<pre class="" style="font-size: .3em; width: 70%; height: 400px"><code class="python" style="max-height: 1000px;">
function INSERT(VALUE)
    if node.ITEM is VALUE
        return false
    else if node.ITEM > VALUE 
        LEFTCHILD = node`s left child
        if LEFTCHILD is NONE
            CHILD = new BINARYTREE with root.ITEM equal VALUE
            add CHILD to nodes children
            set node.LEFTCHILD equal to CHILD
        else
            LEFTCHILD.INSERT(VALUE)
    else<mark>
        RIGHTCHILD = node`s right child
        if RIGHTCHILD is NONE
            CHILD = new BINARYTREE with root.ITEM equal VALUE
            add CHILD to nodes children
            set node.RIGHTCHILD equal to CHILD
        else
            RIGHTCHILD.INSERT(VALUE)</mark>
end function
 </code></pre>
</section> 