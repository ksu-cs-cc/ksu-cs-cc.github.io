---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 3 <br> Tree Traversals <br> Getters </h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3> Getter Functions </h3>
<ul>
<li> Depth </li>
<li> Height </li>
<li> Root </li>
<li> Size </li>
</ul>
</section>

<section>
<h3> Get Depth </h3>
<pre class="" style="font-size: .38em; width: 54%"><code class="python">
    function GETDEPTH()
        if ROOT
            return 0
        else 
            return 1 + PARENT.GETDEPTH()
    end function
 </code></pre>
</section>

<section>
<h3> Get Height </h3>
<pre class="" style="font-size: .38em; width: 54%"><code class="python">
function GETHEIGHT()
    if LEAF
        return 0
    else 
        MAX = 0
        for CHILD in CHILDREN
            CURR_HEIGHT = CHILD.GETHEIGHT()
            if CURR_HEIGHT > MAX
                MAX = HEIGHT
        return 1 + MAX
end function
 </code></pre>
</section>

<section>
<h3> Get Root </h3>
<pre class="" style="font-size: .38em; width: 54%"><code class="python">
function GETROOT()
    if ISROOT()
        return this tree
    else
        return PARENT.GETROOT()
end function
 </code></pre>
</section>

<section>
<h3> Get Size </h3>
<pre class="" style="font-size: .38em; width: 54%"><code class="python">
function GETSIZE()
    SIZE = 1
    for CHILD in CHILDREN
        SIZE += CHILD.GETSIZE()
    return SIZE
end function
 </code></pre>
</section>