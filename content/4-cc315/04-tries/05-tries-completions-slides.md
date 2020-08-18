---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 4 <br> Tries <br> Completions</h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>


<section>
<img class="stretch plain" src="/images/completions_attempt01.png">
</section>

<section>
<img class="stretch plain" src="/images/completions_attempt02.png">
</section>
<section>
<img class="stretch plain" src="/images/completions_attempt03.png">
</section>
<section>
<img class="stretch plain" src="/images/completions_attempt04.png">
</section>
<section>
<img class="stretch plain" src="/images/completions_attempt05.png">
</section>
<section>
<img class="stretch plain" src="/images/completions_attempt06.png">
</section>
<section>
<img class="stretch plain" src="/images/completions_attempt07.png">
</section>
<section>
<img class="stretch plain" src="/images/completions_attempt08.png">
</section>
<section>
<img class="stretch plain" src="/images/completions_attempt09.png">
</section>
<section>
<img class="stretch plain" src="/images/completions_attempt10.png">
</section>
<section>
<img class="stretch plain" src="/images/completions_attempt11.png">
</section>
<section>
<img class="stretch plain" src="/images/completions_attempt12.png">
</section>
<section>
<img class="stretch plain" src="/images/completions_attempt13.png">
</section>
<section>
<img class="stretch plain" src="/images/completions_attempt14.png">
</section>
<section>
<img class="stretch plain" src="/images/completions_attempt15.png">
</section>
<section>
<img class="stretch plain" src="/images/completions_attempt16.png">
</section>

<section>
<h3> Word Completions </h3>
<pre class="" style="font-size: .18em; width: 54%"><code class="python">
function COMPLETIONS(WORD)
    if WORD length greater than 0
        FIRST = first character of WORD
        REMAIN = remainder of WORD
        CHILD = FINDCHILD(FIRST)
        if CHILD is none
            return []
        else
            COMPLETES = CHILD.COMPLETIONS(REMAIN)
            OUTPUT = []
            for COM in COMPLETES
                append CHILD.item + COM to OUTPUT
            return OUTPUT
    else
        OUTPUT = []
        if is_word
            append ITEM to OUTPUT
        for CHILD in CHILDREN
            COMPLETES = CHILD.COMPLETIONS("")
            for COM in COMPLETES
                append CHILD.item + COM to OUTPUT
        reutrn OUTPUT
end function
 </code></pre>
</section>


<section>
<h3> Word Completions </h3>
<pre class="" style="font-size: .18em; width: 54%"><code class="python">
function COMPLETIONS(WORD)
    if WORD length greater than 0<mark>
        FIRST = first character of WORD
        REMAIN = remainder of WORD
        CHILD = FINDCHILD(FIRST)
        if CHILD is none
            return []
        else
            COMPLETES = CHILD.COMPLETIONS(REMAIN)
            OUTPUT = []
            for COM in COMPLETES
                append CHILD.item + COM to OUTPUT
            return OUTPUT</mark>
    else
        OUTPUT = []
        if is_word
            append ITEM to OUTPUT
        for CHILD in CHILDREN
            COMPLETES = CHILD.COMPLETIONS("")
            for COM in COMPLETES
                append CHILD.item + COM to OUTPUT
        reutrn OUTPUT
end function
 </code></pre>
</section>

<section>
<h3> Word Completions </h3>
<pre class="" style="font-size: .18em; width: 54%"><code class="python">
function COMPLETIONS(WORD)
    if WORD length greater than 0
        FIRST = first character of WORD
        REMAIN = remainder of WORD
        CHILD = FINDCHILD(FIRST)<mark>
        if CHILD is none
            return []</mark>
        else
            COMPLETES = CHILD.COMPLETIONS(REMAIN)
            OUTPUT = []
            for COM in COMPLETES
                append CHILD.item + COM to OUTPUT
            return OUTPUT
    else
        OUTPUT = []
        if is_word
            append ITEM to OUTPUT
        for CHILD in CHILDREN
            COMPLETES = CHILD.COMPLETIONS("")
            for COM in COMPLETES
                append CHILD.item + COM to OUTPUT
        reutrn OUTPUT
end function
 </code></pre>
</section>

<section>
<h3> Word Completions </h3>
<pre class="" style="font-size: .18em; width: 54%"><code class="python">
function COMPLETIONS(WORD)
    if WORD length greater than 0
        FIRST = first character of WORD
        REMAIN = remainder of WORD
        CHILD = FINDCHILD(FIRST)
        if CHILD is none
            return []
        else
            COMPLETES = CHILD.COMPLETIONS(REMAIN)
            OUTPUT = []
            for COM in COMPLETES
                append CHILD.item + COM to OUTPUT
            return OUTPUT
    else<mark>
        OUTPUT = []
        if is_word
            append ITEM to OUTPUT
        for CHILD in CHILDREN
            COMPLETES = CHILD.COMPLETIONS("")
            for COM in COMPLETES
                append CHILD.item + COM to OUTPUT
        reutrn OUTPUT</mark>
end function
 </code></pre>
</section>

<section>
<h3> Word Completions </h3>
<pre class="" style="font-size: .18em; width: 54%"><code class="python">
function COMPLETIONS(WORD)
    if WORD length greater than 0
        FIRST = first character of WORD
        REMAIN = remainder of WORD
        CHILD = FINDCHILD(FIRST)
        if CHILD is none
            return []
        else
            COMPLETES = CHILD.COMPLETIONS(REMAIN)
            OUTPUT = []
            for COM in COMPLETES
                <mark>append CHILD.item + COM to OUTPUT</mark>
            return OUTPUT
    else
        OUTPUT = []
        if is_word
            append ITEM to OUTPUT
        for CHILD in CHILDREN
            COMPLETES = CHILD.COMPLETIONS("")
            for COM in COMPLETES
                <mark>append CHILD.item + COM to OUTPUT</mark>
        reutrn OUTPUT
end function
 </code></pre>
</section>