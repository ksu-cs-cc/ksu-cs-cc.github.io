---
title: "Searching the Web"
pre: "19.2 "
weight: 10
date: 2020-10-24T00:27:26-05:00
---

{{< youtube M_V5mL7lmyg >}}

#### Resources
* [Slides](/1-cc110/19-search-info/slides/19-InfoRetrieval.pdf)

#### Video Script

So in this video, we're going to reiterate a little bit what we talked about with our relational database, right? Because the whole point of the relational database is that we can store lots of information in a very structured way that is easily searchable. That's really important in today's world, because we have the World Wide Web, right, the internet, it's huge. Now that we know how to store data in a reasonable fashion, we have to talk about where most of the data in the world is actually stored. And for that, really is just the internet. So at the highest level, right, we can think of the internet as a very big, very big, completely unstructured database of all of the information in the world, right, because pretty much almost everything is connected to the internet anymore. Not everything, but pretty much. Some parts of it are very structured, and very well formed and easily searchable. But generally, it will never be as well structured as we'd like. And one structure might be entirely different than another. And so it's not going to be very uniform across the entire internet. However, we are pretty much constantly using tools like Google to find information and the vast amount of data that is out there on the web, and it does a pretty good job, doesn't it? When you do a Google search most of the time you find what you're looking for. So how do we go about finding information in a big giant unstructured pile of data that really is pretty much like finding a needle in a haystack, as far as Internet is concerned. So that task is the job of information retrieval specialist, and the algorithms and research  they do. In a base form, right, let's say we want to find some information on a very simple Internet, maybe this is back in the early early, early days, where there was pretty much nothing out there. 

So our internet has three pages, only three pages, and those three pages have very little amount of information. And so we want to find out some information about all this data that is on the web. So we want to run these search queries. And you can kind of imagine these being just put into a Google search box. Okay, so we want to find all the pages that have cats, dogs, dog sat, "dog stood", cat or mat, and cat and mat. But how could we do that? How could we find all of the pages that match these queries? Well, the most basic or straightforward way to do it is just to read through all the pages and find all the occurrences right. But in reality, the internet is huge, this approach works perfectly fine for what we currently have, right? We only have three pages, I can read this in like under five seconds and find all the results right. But doing that process on the actual internet is a really bad idea, because it's huge and would take forever so your searches would just never complete. And so we need a better way of looking at data in order to answer all of our questions very quickly and accurately to that. 

So the first step here, then is to try to simplify the data. So instead of scanning each character, each word, every single time we tried to run a search or query, we can actually do what we call indexing. For each word, we could create a list that a list that contains which document that word is actually listed in. This indexed collection becomes a little bit easier to search because now we don't have to look at all of the words in all of the web pages, we're just looking at this index list. So which queries that we had before? Which of these queries can be actually answered with this information? Well, we can find cat right because cat is one of the words that we have sat there. index. And if we look at cat here, you can see that cat occurs in our document 1, and then cat also occurs and document 3. But in order to find cat, we didn't have to read the entirety of one we didn't have to read two. And we didn't have to read the entirety of three that is already done for us. We just find the word in our list, and then we know already which pages that actually occurs in. But most of these can work just fine, right? Even dog sat, dog space sat, so we're trying to find any of any occurrences of dog and any occurrences of sat here so quickly. Number 3 here would return to 3. And then it would also return 1-3. So, so one, two and three would be returned entirety for that query there. But cat or matt also works. Cat and mat. So pages that have both cat and mat. 

Overall, we can answer all these queries, right? Except for "dog stood". So "dog stood" doesn't work. Why? If you ever ran a Google search before, so if you type in just a two word search query is looking for any occurrences in any position on any page. So if I search for just dog space sat, it's looking for any occurrences of dog and any occurrences of sat on that webpage. But if I use quotation marks, it's looking for position, it's looking for position, right, it's looking for the word dog, immediately followed by a space, followed by the word stood. So now we're dealing with the position of the words in the webpage. We can't answer information like that with what we have. Because all we are actually storing here is the word itself, and then if it occurs on and what page it actually occurs on on the in the web, and not the position of where that word occurs on in that page. So in order to do that, we need to modify our index algorithm a little bit. So to improve our indexing algorithm, we could store the location of the word within the document, along with the document number in our index. 

So using this information, we can answer all of our queries now, right? How would we actually do that? Well, let's skip all the rest of them, because we already know we can answer everything else. But let's look at dog stood. So first we're looking for for dog, right, so imagine what our algorithm is looking for here, we're looking for dog stood dog, followed by the word stood. So we can look at dog; dog occurs at two, two. So document two, position two, and document three, position six. So that's well and good. And so we also need to find stood. So we find stood at document two, three, and document three, three. So dog and stood occur both in both two, documents two and three. So let's look at the position of those words. So stood obviously is the second position and dog is the first position, so we need to have dog followed by stood. So if we look at the second number here, which is the position of the word, so we have dog that occurs at position two here, and stood that occurs at position three here. So since dog is immediately followed by stood, document two would be a valid page that matches that query. But if we look at document three, dog occurs at position six, and stood occurs at position three. And so since stood does not come after dog in document three, that is not a valid page that matches our search results, or our search query. So in a very, very basic way, this is what your Google search query is actually doing on the internet, it's trying to, or what Google is doing is trying to basically index the entire internet, so that when you run a search query, it knows where that text is actually occurring in the web, and you can run more intelligent queries like this to find a little bit more accurate information and narrow down your search results. 

So if we made an algorithm to actually do execute what we just did with dog stood, it would look something like this in a very formal sense. We haven't shown you any formal algorithms in this structure yet. A formal definition of an algorithm will look like this, where we have input, output and the algorithm steps itself. So this is kind of like pseudocode here. So the input or in other words, called the precondition describes what the input will actually be to this algorithm or the expected input. So in this case, we're expecting a two word phrase in the form of word one followed by word two, and this is in a quoted string. And the output or the post condition describes the expected or produced output from the algorithm. So given this this input, we're going to produce this output, and our output is going to be an answer list of all of the numbers of the webpages that contain the phrase. And then the steps that we have here are exactly what I did just before, where we are going to index the web here. So the page number position number pairs for word one, so find all the matches for word one in our index and find all the matches for word two in our index. And then we're going to go through each of those page number position pairs to see if we have a word that happens right after it. So for each pair in list one, see if there is a pair in list two such that the page number is the same as the one in list one. And the position number is immediately after the position number in the first page position pair. Looks a little bit more complicated than what I actually did before. 

So that is a big step that we're kind of making here and formalizing our algorithm definition. But you'll see this a lot in computer science, especially as you move forward in our courses. But we can't answer all of our search queries using this particular algorithm. This particular algorithm is expecting our word one word to our two word phrase here. And so it works perfectly fine for when we're trying to look up the phrase cat sat, using our indexing list or our indexed list. But cat space stood doesn't match our precondition, because it doesn't have the quotation marks around it. We could answer cat stood, but we couldn't answer cat or stood. 

So how could we modify our algorithm in order to handle the other different types of queries? And so there's a lot of things that we would have to think about when we did that, we would have to make sure we're modifying our precondition for it to accept different types of search queries. And then we're going to also have to modify our algorithm itself in order to handle those different types of search queries. So this is just some more complexities of actually formalizing an algorithm definition to make sure and one of the reasons why we would actually do that is to make sure our to make sure to verify that our input and output is correct. So making sure our algorithm does what we want it to actually do. 