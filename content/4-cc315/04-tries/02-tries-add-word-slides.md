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
<h3> Get Depth </h3>
<pre class="" style="font-size: .3em; width: 54%"><code class="python">
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