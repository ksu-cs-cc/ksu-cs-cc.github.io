---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 4 <br> Tries <br> Contains Word</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3>Contains a Word</h3>
<div style="float:left;width:70%">
<img class="stretch plain" src="/images/315_4.4_trie1.svg">
</div>
<div style="float:right">
<h4>data</h4>
</div>
</section>

<section>
<h3>Contains a Word</h3>
<div style="float:left;width:70%">
<img class="stretch plain" src="/images/315_4.4_trie2.svg">
</div>
<div style="float:right">
<h4 style="color:black">d</h4><h4>ata</h4>
</div>
</section>

<section>
<h3>Contains a Word</h3>
<div style="float:left;width:70%">
<img class="stretch plain" src="/images/315_4.4_trie3.svg">
</div>
<div style="float:right">
<h4 style="color:black">da</h4><h4>ta</h4>
</div>
</section>

<section>
<h3>Contains a Word</h3>
<div style="float:left;width:70%">
<img class="stretch plain" src="/images/315_4.4_trie4.svg">
</div>
<div style="float:right">
<h4 style="color:black">dat</h4><h4>a</h4>
</div>
</section>

<section>
<h3>Contains a Word</h3>
<div style="float:left;width:70%">
<img class="stretch plain" src="/images/315_4.4_trie5.svg">
</div>
<div style="float:right">
<h4 style="color:black">data</h4>
</div>
</section>


<section>
<h3> Contains Word </h3>
<pre class="" style="font-size: .23em; width: 54%"><code class="python">
function CONTAINSWORD(WORD)
    if WORD length is 0
        return `is_word`
    else
        FIRST = first character of WORD
        REMAIN = remainder of WORD
        CHILD = FINDCHILD(FIRST)
        if CHILD is NONE
            return false
        else
            CHILD.CONTAINSWORD(REMAIN)
end function
 </code></pre>
</section>

<section>
<h3> Contains Word </h3>
<pre class="" style="font-size: .23em; width: 54%"><code class="python">
function CONTAINSWORD(WORD)
    if WORD length is 0 <mark>
        return `is_word`</mark>
    else
        FIRST = first character of WORD
        REMAIN = remainder of WORD
        CHILD = FINDCHILD(FIRST)
        if CHILD is NONE
            return false
        else
            CHILD.CONTAINSWORD(REMAIN)
end function
 </code></pre>
</section>

<section>
<h3> Contains Word </h3>
<pre class="" style="font-size: .23em; width: 54%"><code class="python">
function CONTAINSWORD(WORD)
    if WORD length is 0
        return `is_word`
    else<mark>
        FIRST = first character of WORD
        REMAIN = remainder of WORD
        CHILD = FINDCHILD(FIRST)
        if CHILD is NONE
            return false
        else
            CHILD.CONTAINSWORD(REMAIN) </mark>
end function
 </code></pre>
</section>
