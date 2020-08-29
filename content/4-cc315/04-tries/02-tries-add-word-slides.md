---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 4 <br> Tries <br> Add Word</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3>Adding a Word</h3>
<div style="float:left;width:60%">
<img class="stretch plain" src="/images/315_4.2_trieBase.svg">
</div>
<div style="float:right">
<h4>hope</h4>
</div>
</section>

<section>
<h3>Adding a Word</h3>
<div style="float:left;width:60%">
<img class="stretch plain" src="/images/315_4.2_trie1.svg">
</div>
<div style="float:right">
<h4 style="color:black">h</h4><h4>ope</h4>
</div>
</section>

<section>
<h3>Adding a Word</h3>
<div style="float:left;width:60%">
<img class="stretch plain" src="/images/315_4.2_trie2.svg">
</div>
<div style="float:right">
<h4 style="color:black">ho</h4><h4>pe</h4>
</div>
</section>

<section>
<h3>Adding a Word</h3>
<div style="float:left;width:60%">
<img class="stretch plain" src="/images/315_4.2_trie3.svg">
</div>
<div style="float:right">
<h4 style="color:black">hop</h4><h4>e</h4>
</div>
</section>

<section>
<h3>Adding a Word</h3>
<div style="float:left;width:60%">
<img class="stretch plain" src="/images/315_4.2_trie4.svg">
</div>
<div style="float:right">
<h4 style="color:black">hope</h4>
</div>
</section>

<section>
<h3> Add Word </h3>
<pre class="" style="font-size: .23em; width: 54%"><code class="python">
function ADDWORD(WORD)
    if WORD length is 0
        if already a word
            return false
        else
            set is_word to true
            return true
    else
        FIRST = first character of WORD
        REMAIN = remainder of WORD
        CHILD = FINDCHILD(FIRST)
        if CHILD is NONE
            NODE = new MyTrie with item equal FIRST
            insert NODE into our existing trie 
        return CHILD.ADDWORD(REMAIN)
end function
 </code></pre>
</section>

<section>
<h3> Add Word: Base Case </h3>
<pre class="" style="font-size: .23em; width: 54%"><code class="python">
function ADDWORD(WORD)<mark>
    if WORD length is 0
        if already a word
            return false
        else
            set is_word to true
            return true</mark>
    else
        FIRST = first character of WORD
        REMAIN = remainder of WORD
        CHILD = FINDCHILD(FIRST)
        if CHILD is NONE
            NODE = new MyTrie with item equal FIRST
            insert NODE into our existing trie 
        return CHILD.ADDWORD(REMAIN)
end function
 </code></pre>
</section>

<section>
<h3> Add Word: Recursive Case </h3>
<pre class="" style="font-size: .23em; width: 54%"><code class="python">
function ADDWORD(WORD)
    if WORD length is 0
        if already a word
            return false
        else
            set is_word to true
            return true
    else<mark>
        FIRST = first character of WORD
        REMAIN = remainder of WORD
        CHILD = FINDCHILD(FIRST)
        if CHILD is NONE
            NODE = new MyTrie with item equal FIRST
            insert NODE into our existing trie 
        return CHILD.ADDWORD(REMAIN)</mark>
end function
 </code></pre>
</section>
