---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 4 <br> Tries <br> Remove Word</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>


<section>
<h3>Removing a Word</h3>
<div style="float:left;width:60%">
<img class="stretch plain" src="/images/315_4.3_trie1.svg">
</div>
<div style="float:right">
<h4>hope</h4>
</div>
</section>

<section>
<h3>Removing a Word</h3>
<div style="float:left;width:60%">
<img class="stretch plain" src="/images/315_4.3_trie2.svg">
</div>
<div style="float:right">
<h4 style="color:black">h</h4><h4>ope</h4>
</div>
</section>

<section>
<h3>Removing a Word</h3>
<div style="float:left;width:60%">
<img class="stretch plain" src="/images/315_4.3_trie3.svg">
</div>
<div style="float:right">
<h4 style="color:black">ho</h4><h4>pe</h4>
</div>
</section>

<section>
<h3>Removing a Word</h3>
<div style="float:left;width:60%">
<img class="stretch plain" src="/images/315_4.3_trie4.svg">
</div>
<div style="float:right">
<h4 style="color:black">hop</h4><h4>e</h4>
</div>
</section>


<section>
<h3>Removing a Word</h3>
<div style="float:left;width:60%">
<img class="stretch plain" src="/images/315_4.3_trie5.svg">
</div>
<div style="float:right">
<h4 style="color:black">hope</h4>
</div>
</section>

<section>
<h3>Removing a Word</h3>
<div style="float:left;width:60%">
<img class="stretch plain" src="/images/315_4.3_trie6.svg">
</div>
<div style="float:right">
<h4 style="color:black">hope</h4>
</div>
</section>

<section>
<h3>Removing a Word</h3>
<div style="float:left;width:60%">
<img class="stretch plain" src="/images/315_4.3_trie7.svg">
</div>
<div style="float:right">
<h4 style="color:black">hope</h4>
</div>
</section>

<section>
<h3> Remove Word </h3>
<pre class="" style="font-size: .23em; width: 54%"><code class="python">
function REMOVEWORD(WORD)
    if WORD length is 0
        if already not a word
            return false
        else
            set is_word to false
            return true
    else
        FIRST = first character of WORD
        REMAIN = remainder of WORD
        CHILD = FINDCHILD(FIRST)
        if CHILD is NONE
            return false
        else
            RET = CHILD.REMOVEWORD(REMAIN)
            if CHILD is not a word AND CHILD is a leaf
                REMOVECHILD(CHILD)
            return RET
end function
 </code></pre>
</section>

<section>
<h3> Remove Word: Base Case </h3>
<pre class="" style="font-size: .23em; width: 54%"><code class="python">
function REMOVEWORD(WORD)<mark>
    if WORD length is 0
        if already not a word
            return false
        else
            set is_word to false
            return true</mark>
    else
        FIRST = first character of WORD
        REMAIN = remainder of WORD
        CHILD = FINDCHILD(FIRST)
        if CHILD is NONE
            return false
        else
            RET = CHILD.REMOVEWORD(REMAIN)
            if CHILD is not a word AND CHILD is a leaf
                REMOVECHILD(CHILD)
            return RET
end function
 </code></pre>
</section>

<section>
<h3> Remove Word: Recursive Case </h3>
<pre class="" style="font-size: .23em; width: 54%"><code class="python">
function REMOVEWORD(WORD)
    if WORD length is 0
        if already not a word
            return false
        else
            set is_word to false
            return true
    else<mark>
        FIRST = first character of WORD
        REMAIN = remainder of WORD
        CHILD = FINDCHILD(FIRST)
        if CHILD is NONE
            return false
        else
            RET = CHILD.REMOVEWORD(REMAIN)
            if CHILD is not a word AND CHILD is a leaf
                REMOVECHILD(CHILD)
            return RET</mark>
end function
 </code></pre>
</section>
