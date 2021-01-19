---
title: "Creating And Cloning Master Courses"
pre: "5. "
weight: 50
date: 2020-01-03T10:53:26-05:00
---

There are some intricacies related to properly setting up a Canvas course and a Codio class to act as "master" version of the material to allow for easy cloning each semester. This document will attempt to convey them in a straightforward way.

#### References

* [Codio LTI Configuration](https://codio.com/docs/classes/lti/lti1_0/canvas/)
* [Codio LTI Constant URLs](https://codio.com/docs/classes/lti/lti1_0/lticonstanturl/)
* [Codio LTI Class Fork](https://codio.com/docs/classes/lti/lti1_0/lticlassfork/)

## Set up Master Course

#### Codio Configuration

1. Create a class in Codio to act as the master class.
   1. You may also need to create a course in Codio that contains modules to be added to the class, but that is going away in Spring 2020 according to what I've been told.
1. In the class in Codio, enable the LTI Integration as well as the LTI Constant URLs and LTI Class Fork options.
   1. It is **important** to do this early in the process. Otherwise, you will have to update URLs later.

![Codio Screenshot](/images/clone1.png)

#### Canvas Configuration

1. Create a course in Canvas to act as the master course.
1. Configure the LTI integration as described in Codio documentation.
   1. Don't forget to go back and add the Canvas course URL to the Codio class so that it knows where to send the grades.
1. Also make sure you include the `codio_parent_class_id` and `codio_class_target_id` fields. This is **important**!

![Canvas Screenshot](/images/clone2.png)

#### Add Assignments in Canvas

1. Once the Codio class and Canvas course are set up and linked, add units from the Codio class as assignments in the Canvas course, either by copying the LTI Integration URL from the unit or selecting them in the Codio app on Canvas.
  1. Here's the trick! When LTI Constant URLs are disabled, the LTI Integration URL will include the Codio class ID, as in this example:<br>apollo.codio.com/lti/2c08254e-541a-4923-a9f1-224ed64b159e&#95;<b>5bec924abf0152035a329fa0</b>&#95;23w50f8t6CLA
  1. If LTI Constant URLs are enabled, then the Codio class ID is omitted from the LTI Integration URL:<br>apollo.codio.com/lti/2c08254e-541a-4923-a9f1-224ed64b159e_23w50f8t6CLA
1. If you have already added assignments to Canvas before enabling the LTI Constant URLs option in Codio, you'll need to update all of the URLs before cloning the course.

## Clone Master Canvas Course

1. At the start of a new semester, create a copy of the Canvas master course following the usual procedure
1. Once the course has been copied, **before doing anything else**, go to the LTI app configurations in Canvas and update the `codio_class_target_id` field to something unique. Do not change the `codio_parent_class_id` field, as that tells Codio which class to duplicate.
1. Then, load one of the assignments as an instructor in Canvas. It should create a new class in Codio using the new target id as a duplicate of the original course.
1. In Codio, add the LMS URL to the newly created class (it doesn't do this automatically)
1. That should do it!

![Canvas Screenshot](/images/clone3.png)

If you are using Piazza, you will also need to link the new course to Piazza and update the access code!

_If cloning from K-State Canvas to Global Campus Canvas Pro, you'll need to re-enter the LTI keys for both Piazza and Canvas, since they cannot be exported_
