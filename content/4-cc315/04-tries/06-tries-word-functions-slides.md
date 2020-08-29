---
type: "reveal"
hidden: true
---

<section>
<img class="stretch plain" src="/images/core-logo-on-white.png">
<h3> Module 4 <br> Tries <br> Word Functions </h3>
<hr style="height:15px;color:512888;background-color:512888;">
<h4>CC315 Fall 2020</h4>
</section>

<section>
<h3>Remaining Functions </h3>
<ul>
<li>Maximum Word Length</li>
<li>Word Count</li>
</ul>
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase1.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase2.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase3.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase4.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase5.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase6.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase7.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase8.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase9.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase10.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase11.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase12.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase13.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase14.svg">
</section>

<section>
<h3>Example</h3>
<img class="stretch plain" src="/images/315_4.6_trieBase15.svg">
</section>

<section>
<h3> Maximum Word Length </h3>
<pre class="" style="font-size: .23em; width: 54%"><code class="python">
function MAXWORD()
    if LEAF and is_word
        return 0
    else
        MAX = -1
        for CHILD in CHILDREN
            COUNT = CHILD.MAXWORD()
            if COUNT greater than MAX
                MAX = COUNT
        return MAX + 1
end function
 </code></pre>
</section>

<section>
<h3> Word Count </h3>
<pre class="" style="font-size: .23em; width: 54%"><code class="python">
function WORDCOUNT()
    COUNT = 0
    if is_word
        COUNT = 1
    for CHILD in CHILDREN
        COUNT += CHILD.WORDCOUNT()
    return COUNT
end function
 </code></pre>
</section>