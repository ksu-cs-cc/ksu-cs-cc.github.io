---
title: "Protocols"
pre: "12.3 "
weight: 15
date: 2020-08-28T16:27:26-05:00
---

{{< youtube SuFyXGWOkhY >}}

<!-- CIS 115: U84jB5BQeJg -->

#### Resources
* [Slides](/1-cc110/12-internettech/slides/11-How_the_Internet_Works.pdf)

#### Video Script

The topmost layer of the seven layer OSI network model is the application layer. In this video, we'll take a look at some application layer protocols and discuss what they do. These protocols are usually used to send data across two different computers using different programs. For example, there are protocols such as pop, SMTP, and eye map for sending and receiving email. We have HTTP and FTP for sending and receiving files and webpages using the World Wide Web. We have DNS and DHCP for helping us configure and set up our networks. And we can use protocols such as SSH, RDP, or telnet to remotely connect to computer systems all across the globe. So let's take a look at a few of these application layer protocols and see how they work. 

Probably the most important of the application layer protocols is DNS or the Domain Name System. You can think of DNS like the phonebook for the internet. Earlier in this module, we talked about how each computer on the is assigned a unique IP address, which is kind of like a phone number. However, just like phone numbers, IP addresses can be very confusing and hard to remember, it's just a random string of numbers that we have trouble associating to anything. So instead, DNS allows us to remember domain names, and then it will associate them with IP addresses that actually are the computers we want to talk to. For example, when we open up a web browser and type in www.ksu.edu, DNS actually looks up the value of ksu.edu in the DNS system and returns an IP address like 129.130.8.41. And it says here, you need to talk to this computer to get the ksu.edu. The same thing happens for Google.com, ibm.com. Any website that you put into your web browser, we use DNS to figure out what the IP addresses of the computer system you want to talk to. The domain namespace itself is actually a hierarchical system. At the very top level, you have the root domain name servers. And then below that you have the top level domain servers for domains such as.org.com, dotnet.edu. Each of those have their own domain name servers. Then below that you can have servers for each individual domain names such as ksu.edu, ibm.com, espn.com, they all can maintain their own servers. And they can even delegate to further sub zones. For example, the computer science department runs its own DNS server at cs.ksu.edu. So we can have our own systems. 

The process for looking up a domain name using DNS is interesting because it's recursive. In computer science. We're very familiar with recursive algorithms. So let's say we want to look up the IP address for wikipedia.org. We would start by going to a DNS for cursor, which is usually a piece of software on our computer, it would go out and try and contact the root name server and say, Where is www.wikipedia.org and the root name server would say, I don't know but I know where the .org name server is. Why don't you try there? So then our recursive would go to the.org name server and say, Hey, where is wikipedia.org? And the.org name server says, Well, I know where Wikipedia is, why don't you go try there. So then we'll go talk to the wikipedia.org name server and ask it Where is www.wikipedia.org. And that org name server will say, Aha, I am the authoritative name server for wikipedia.org. And I can tell you that it is at this IP address. So then your DNS cursor will tell your computer Oh, you want to go to wikipedia.org. It's this IP address. And usually this process happens within just a fraction of a second after you press the Enter key to load a webpage. 

The next protocol we'll discuss is the Dynamic Host Configuration Protocol or DHCP. DHCP is what allows a computer to connect to an unknown computer network and get an IP address and get connected without any other configuration needed. Before DHCP was really commonly used bringing your computer to a new office, usually required quite a lot of technical setup. And it made it very hard to have portable computers available like we do today. The Dynamic Host Configuration Protocol consists of four very simple steps that happen whenever a new computer connects to the network. Let's go through those steps really quick and see what they do. In the first step, the client will send a DHCP discover message, which is basically a shout message that goes to every single system on the network. And it says, Hi, I'm new, I need an IP address. Then, on the network, there's a DHCP server that is listening for those shout messages. And it will send back its own shot message of a DHCP offer that says Hi, I'm a DHCP server. Here's an IP address and some configuration information you can use. Then the client once it gets that information, we'll send a short message that says hey, that's great. I'd like to use that information. And finally the DHCP server will send back one final shout that acknowledges Okay, good. That's your information. Good luck. And then it will record that that IP address has been used by that particular computer. Meanwhile, the computer will use that information to configure its network settings so that it can talk to the network. So whenever you come to campus and you bring your computer and you see your wireless icon flashing for a few seconds before it goes solid, the DHCP protocol is actually what's going on. It is connecting your computer to K-State's wireless network requesting an IP address and getting connected so that you can use the internet on your mobile device. 

Another important protocol at the application layer is the hypertext transfer protocol or HTTP. HTTP was developed by Tim Berners-Lee to actually send webpages using the World Wide Web. And it was developed in the late 1980s. And it's really a revolutionary part of the internet we use today. Here's what the HTTP protocol actually looks like. It is very interestingly, a text based protocol. So at the top of this image in red, we have the request where we've connected to wikipedia.org and we've requested to get the main page. So then the web server we'll respond. And in blue, it responds with the response headers that tell us about the information we're about to receive, such as the size and different things about it. And then finally, in green, you see the body of the response, which is actually the HTML that makes up the webpage that gets sent. And so if you're really good, you can use tools such as telnet to browse the web. By typing in these HTML, HTTP requests and getting the response directly from the web server. It's a really fun activity to try if you're interested. 

To make things a little bit simpler HTTP requires several different commands. For example, there is the get command that used to request a webpage, the post command that used to send data back to a web page, the head command, which gets information about the page without actually loading the page itself. And then there are other commands that are less often used, such as put and delete to change pages and delete pages off a web server.

To further simplify things, HTTP also defines a set of status codes that the server can respond to With telling more information about the response, the sending the most common response hopefully is 200, which simply means Okay, I received it and I'm sending back data. You can also get responses like 301 moved permanently if a website has been moved, you can get 434 bitten if you try and log into a website that you don't have access to. And you can get some dreaded errors such as the 404 not found error if that web page can't be found on the server. Of course, there are other errors, such as the 500 errors, the internal server errors, that means the server itself is having a problem and can't respond right now. There's also the 503 error, which means that the service is unavailable, but it might come back soon. As you can see, there are a lot of different application layer protocols that are used on the internet today, and they all serve a variety of different purposes. I hope this has been a really interesting look into the technology behind how the internet works. In the next few modules will actually explore what it takes to build web Websites ourselves.