---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 3 <br> Tree Traversals <br> Relationships </h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3> Relational Functions </h3>
<ul>
<li> Is Ancestor </li>
<li> Is Descendant </li>
<li> Is Sibling </li>
<li> Lowest Common Ancestor </li>
<li> Path From Root </li>
</ul>
</section>

<section>
<h3> Is Ancestor </h3>
<pre class="" style="font-size: .38em; width: 54%"><code class="python">
function ISANCESTOR(TREE)
    if at TREE
        return true
    else if at LEAF
        return false
    else 
        for CHILD in CHILDREN
            FOUND = CHILD.ISANCESTOR(TREE)
            if FOUND
                return true
        return false
end function
 </code></pre>
</section>

<section>
<h3> Is Descendant </h3>
<pre class="" style="font-size: .38em; width: 54%"><code class="python">
function ISDESCENDANT(TREE)
    if at TREE
        return true
    else if at ROOT
        return false
    else 
        return PARENT.ISDESCENDANT(TREE)
end function
 </code></pre>
</section>


<section>
<h3> Is Sibling </h3>
<pre class="" style="font-size: .38em; width: 54%"><code class="python">
function ISSIBLING(TREE)
    if TREE in PARENT`s CHILDREN
        return true
    else 
        return false
end function
 </code></pre>
</section>

<section>
<h3> Lowest Common Ancestor </h3>
<pre class="" style="font-size: .38em; width: 54%"><code class="python">
function LOWESTANCESTOR(TREE)
    if at TREE
        return TREE
    else if ISANCESTOR(TREE)
        return instance
    else if at ROOT
        return NONE
    else
        return PARENT.LOWESTANCESTOR(TREE)
end function
 </code></pre>
</section>

<section>
<h3> Path From Root </h3>
<pre class="" style="font-size: .38em; width: 54%"><code class="python">
function PATHFROMROOT(PATH)
    if NOT ROOT
        PARENT.PATHFROMROOT(PATH)
    append ITEM to PATH
end function
 </code></pre>
</section>