---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 5 <br> Binary Trees <br> Remove Element </h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section> 

<section>
<h3>Motivation</h3>
When we need to remove a node, we will replace it with its smallest right descendant
</section>

<section>
<h3>Types of Removal</h3>
<ul>
<li>Leaf</li>
<li>No Right Child</li>
<li>Right Child</li>
</ul>
</section>


<!--------------------------- START: REMOVING LEAF ------------------------>

<section>
<h3>Removing a Leaf </h3>
<img class="stretch plain" src="/images/315_4.6_binDel.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLeaf1.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLeaf2.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLeaf3.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLeaf4.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLeaf5.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLeaf6.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLeaf7.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLeaf8.svg">
</section>

<!--------------------------- END: REMOVING LEAF ------------------------>

<!--------------------- START: REMOVING RIGHTCHILDLESS ------------------>
<section>
<h3>Removing a Node with No Right Child </h3>
<img class="stretch plain" src="/images/315_4.6_binDelLC01.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLC02.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLC04.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLC05.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLC06.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLC07.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLC08.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLC09.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLC10a.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLC11.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDelLC12.svg">
</section>

<!--------------------- END: REMOVING RIGHTCHILDLESS ------------------>

<!--------------------- START: REMOVING FULL -------------------------->
<section>
<h3>Removing a Node with<br> Right Child</h3>
<img class="stretch plain" src="/images/315_4.6_binDel2Kids1.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDel2Kids2.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDel2Kids3.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDel2Kids4.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDel2Kids5.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDel2Kids6.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDel2Kids7.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDel2Kids8.svg">
</section>

<section>
<img class="stretch plain" src="/images/315_4.6_binDel2Kids9.svg">
</section>
<!--------------------- END: REMOVING FULL -------------------------->
<section>
<h3>Needed Functions</h3>
<ul>
<li>Remove</li>
<li>Remove Smallest</li>
<li>Prune (Left and Right)</li>
</ul>
</section> 




<section>
<h3>Pruning</h3>
<pre class="" style="font-size: .3em; width: 70%"><code class="python">
    function PRUNERIGHT()
        if RIGHTCHILD has no value
            REMOVECHILD(RIGHTCHILD)
            set this nodes RIGHTCHILD former RIGHTCHILDs RIGHTCHILD
            if RIGHTCHLID is not none
                ADDCHILD(RIGHTCHILD)
 </code></pre>

 <pre class="" style="font-size: .3em; width: 70%"><code class="python">
    function PRUNELEFT()
        if LEFTCHILD has no value
            REMOVECHILD(LEFTCHILD)
            set this nodes LEFTCHILD former LEFTCHILDs RIGHTCHILD
            if LEFTCHILD is not none
                ADDCHILD(LEFTCHILD)
 </code></pre>
</section> 

<section>
<h3>Remove Smallest</h3>
<pre class="" style="font-size: .22em; width: 45%"><code class="python">
function REMOVESMALLEST()
    if node has left child
        REPLACEMENT = LEFTCHILD.REMOVESMALLEST
        prune left-side
        return REPLACEMENT
    else
        REPLACEMENT = node.ITEM
        if node has right child
            node.ITEM = RIGHTCHILD.REMOVESMALLEST()
            prune right-side
        else
            node.ITEM = NONE
        return REPLACEMENT
end function
 </code></pre>
</section> 

<section>
<h3>Remove Smallest</h3>
<pre class="" style="font-size: .22em; width: 45%"><code class="python">
function REMOVESMALLEST()
    if node has left child<mark>
        REPLACEMENT = LEFTCHILD.REMOVESMALLEST
        prune left-side
        return REPLACEMENT</mark>
    else
        REPLACEMENT = node.ITEM
        if node has right child
            node.ITEM = RIGHTCHILD.REMOVESMALLEST()
            prune right-side
        else
            node.ITEM = NONE
        return REPLACEMENT
end function
 </code></pre>
</section> 

<section>
<h3>Remove Smallest</h3>
<pre class="" style="font-size: .22em; width: 45%"><code class="python">
function REMOVESMALLEST()
    if node has left child
        REPLACEMENT = LEFTCHILD.REMOVESMALLEST()
        prune left-side
        return REPLACEMENT
    else<mark>
        REPLACEMENT = node.ITEM
        if node has right child
            node.ITEM = RIGHTCHILD.REMOVESMALLEST()
            prune right-side
        else
            node.ITEM = NONE
        return REPLACEMENT</mark>
end function
 </code></pre>
</section> 

<section>
<h3>Remove</h3>
<pre class="" style="font-size: .3em; width: 50%; height: 800px"><code class="python" style="max-height: 1000px;">
function REMOVE(VALUE)
    if node.ITEM is VALUE
        if node is a leaf
            set node.ITEM to none
            return TRUE
        else if node has no right child
            node.ITEM = LEFTCHILD.REMOVESMALLEST()
            prune left-side
            switch left child to right child
            return TRUE
        else
            node.ITEM = LEFTCHILD.REMOVESMALLEST()
            prune right-side
            return TRUE
    else
        if node.ITEM > VALUE
            if node has LEFTCHILD
                SUCCESS = LEFTCHILD.REMOVE(VALUE)
                prune left-side
                return SUCCESS
            else
                return FALSE
        else
            if node has RIGHTCHILD
                SUCCESS = RIGHTCHILD.REMOVE(VALUE)
                prune right-side
                return SUCCESS
            else
                return FALSE
end function
 </code></pre>
</section> 

<section>
<h3>Remove</h3>
<pre class="" style="font-size: .3em; width: 50%; height: 800px"><code class="python" style="max-height: 1000px;">
function REMOVE(VALUE)
    if node.ITEM is VALUE
        if node is a leaf
            set node.ITEM to none
            return TRUE
        else if node has no right child
            node.ITEM = LEFTCHILD.REMOVESMALLEST()
            prune left-side
            switch left child to right child
            return TRUE
        else
            node.ITEM = LEFTCHILD.REMOVESMALLEST()
            prune right-side
            return TRUE
    else<mark>
        if node.ITEM > VALUE
            if node has LEFTCHILD
                SUCCESS = LEFTCHILD.REMOVE(VALUE)
                prune left-side
                return SUCCESS
            else
                return FALSE
        else
            if node has RIGHTCHILD
                SUCCESS = RIGHTCHILD.REMOVE(VALUE)
                prune right-side
                return SUCCESS
            else
                return FALSE</mark>
end function
 </code></pre>
</section> 

<section>
<h3>Remove</h3>
<pre class="" style="font-size: .3em; width: 50%; height: 800px"><code class="python" style="max-height: 1000px;">
function REMOVE(VALUE)
    if node.ITEM is VALUE
        if node is a leaf<mark>
            set node.ITEM to none
            return TRUE</mark>
        else if node has no right child
            node.ITEM = LEFTCHILD.REMOVESMALLEST()
            prune left-side
            switch left child to right child
            return TRUE
        else
            node.ITEM = LEFTCHILD.REMOVESMALLEST()
            prune right-side
            return TRUE
    else
        if node.ITEM > VALUE
            if node has LEFTCHILD
                SUCCESS = LEFTCHILD.REMOVE(VALUE)
                prune left-side
                return SUCCESS
            else
                return FALSE
        else
            if node has RIGHTCHILD
                SUCCESS = RIGHTCHILD.REMOVE(VALUE)
                prune right-side
                return SUCCESS
            else
                return FALSE
end function
 </code></pre>
</section> 

<section>
<h3>Remove</h3>
<pre class="" style="font-size: .3em; width: 50%; height: 800px"><code class="python" style="max-height: 1000px;">
function REMOVE(VALUE)
    if node.ITEM is VALUE
        if node is a leaf
            set node.ITEM to none
            return TRUE
        else if node has no right child<mark>
            node.ITEM = LEFTCHILD.REMOVESMALLEST()
            prune left-side
            switch left child to right child
            return TRUE</mark>
        else
            node.ITEM = LEFTCHILD.REMOVESMALLEST()
            prune right-side
            return TRUE
    else
        if node.ITEM > VALUE
            if node has LEFTCHILD
                SUCCESS = LEFTCHILD.REMOVE(VALUE)
                prune left-side
                return SUCCESS
            else
                return FALSE
        else
            if node has RIGHTCHILD
                SUCCESS = RIGHTCHILD.REMOVE(VALUE)
                prune right-side
                return SUCCESS
            else
                return FALSE
end function
 </code></pre>
</section> 

<section>
<h3>Remove</h3>
<pre class="" style="font-size: .3em; width: 50%; height: 800px"><code class="python" style="max-height: 1000px;">
function REMOVE(VALUE)
    if node.ITEM is VALUE
        if node is a leaf
            set node.ITEM to none
            return TRUE
        else if node has no right child
            node.ITEM = LEFTCHILD.REMOVESMALLEST()
            prune left-side
            switch left child to right child
            return TRUE
        else<mark>
            node.ITEM = LEFTCHILD.REMOVESMALLEST()
            prune right-side
            return TRUE</mark>
    else
        if node.ITEM > VALUE
            if node has LEFTCHILD
                SUCCESS = LEFTCHILD.REMOVE(VALUE)
                prune left-side
                return SUCCESS
            else
                return FALSE
        else
            if node has RIGHTCHILD
                SUCCESS = RIGHTCHILD.REMOVE(VALUE)
                prune right-side
                return SUCCESS
            else
                return FALSE
end function
 </code></pre>
</section> 