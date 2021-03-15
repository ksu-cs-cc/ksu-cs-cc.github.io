---
title: "Introduction"
pre: "1. "
weight: 10
date: 2020-03-06T00:53:26-05:00
---

{{< youtube >}}

TODO

#### Resources

* [Slides]({{< relref "5-cc410/15-releases/01-introduction-slides.md" >}})

#### Video Script

In this chapter, we're going to quickly discuss what it will take to package our application and create a release that others can easily download and use in their own applications. First, let's talk about all the steps we might want to take to prepare our software for release. First and foremost, we should thoroughly test our software and make sure it is as free of bugs and errors as we can get. Having ample unit tests is very helpful at this point, and it can also help anyone who wants to help improve the application by giving them a quick and easy way to confirm that nothing is broken. In addition, you'll want to take some time to document your code, both in code comments but also by creating some user documentation to help users understand how to best use the application. As you go through the code, you should try to clean up any unnecessary debugging or logging statements, either by commenting them out or turning them off. You can also look at the dependencies for your application and determine if you really need them or if they can be easily removed. In addition, you'll want to look at the licenses for your dependencies and make sure you understand the limitations placed on them and how that might affect your ability to publish your software. Once you are ready to publish, you'll want to take the time to test your system on multiple different platforms, operating systems, computer types, and just about anywhere you think a user might try to use it. You may also want to explore adding some easy configuration options to your application - both Java and Python include implementations of the `dotenv` library from the Ruby programming that make this really simple. You should also make sure your code doesn't contain any sensitive information such as API keys or passwords - there are lots of horror stories online of companies being compromised due to sensitive information being pushed to a GitHub repository. Finally, once you've reached the end and you're ready to publish, you'll be faced with one of the two hardest problems in computer science - naming things! You'll need to come up with a hopefully unique and catchy name for your application so others can find it easily.

Once you've done that, the next step is to choose a software license. As discussed in the previous chapter, you have a few options. First, if you don't do anything, your software will automatically be copyrighted, and it will prevent most anyone from using it legally. So, instead, you can choose to apply a public domain license to release it there, or apply a permissive license such as the MIT or Apache license to make it easy to use while protecting you from any liability. If you want to make sure any improvements or derivatives of your work are also free, you'll most likely want to use a copyleft license such as the GNU GPL. And finally, if you want to retain more restrictive rights, you'll probably want to look into a proprietary license and consulting a lawyer to help.

Next, as you prepare your application for release, you'll probably need to add a bit of metadata to the application's package. At a minimum, you'll most likely add the version and the name, as well as determine the full package path for your application. In addition, depending on where you plan to distribute the software, you may have additional requirements to meet.

At this point, you can now start to publish your content. The first and easiest thing to do is to publish your documentation. We've already shown how to create it automatically using tools such as Javadoc or pdoc, so all we really have to do is get it moved to the `docs` folder in our GitHub repository and then enable GitHub Pages on our repository. Thankfully, GitHub will take care of all of our web hosting needs just like that. Alternatively, we can choose to host it on our own website if desired.

Ok, so now we are finally ready to create a package. This process is pretty simple, but we'll cover it in the example project for this chapter. So, check that our for an interactive example of creating a JAR file in Java and a Wheel file in Python.

At long last, we've created our package and we're ready to publish. In many cases, this can be as simple as creating a new release tag on GitHub and then uploading our created packages as attachments to the release. For many developers, that's the last step. However, if we want, we can also look at what it takes to host our application on the library repository for our language. For Python developers, it is super simple and painless to upload a package to the Python Package Index! However, that means that the packages out there aren't really subjected to any rigorous review, and it is likely that someone could already be using the name we'd like to use. So, it comes with a few caveats. For Java developers, the process of uploading a package to Maven Central is pretty difficult, but that difficulty is required to make sure that the package posted on Maven Central come from trusted developers and there are no name conflicts. So, as with PyPI, there are some pros and cons to that approach. In either case, there are ample resources available online to help you with that last step if you desire.

There we go! We've learned all about creating a release for our application, and we'll get to explore some of this process in the example project for this chapter. Hopefully at some point you'll be able to put this information to use and publish your first program online!