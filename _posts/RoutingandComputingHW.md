---
toc: true
comments: true
layout: post
title: Routing and Computing
description: Routing and computing student teach
type: tangibles
courses: { compsci: {week: 14} }
---

Question 1: What is parallel computing?

Parallel computing is when the computer divides tasks into subtasks, and runs these subtasks at the same time to be more efficient. This is helpful when processing large amounts of complicated data in a short amount of time. Computers that use this generally include more than one processing unit, memory, or communication infrastructure. 

Question 2: If there is a computer with 3 cores that can each take one task, and the tasks are 25ms, 632ms and 100ms in run time respectively, how long will the program take to run?

It will take a total of 100ms to run, since the tasks are run parallel, so it will take as long as the longest task takes to complete. 

Question 3: Is sequential or parallel computing more efficient, and why?


Parallel computing is generally more efficient because the data is processed faster, as more data is processed in any given moment. However, you could argue for a singular simple task, parallel computing might overcomplicate it by splitting it into multiple tasks, which would make sequential computing more efficient. 

Question 4: What is the term called when a network has multiple paths leading up to one destination? 

Multipath routing (Used in fault-tolerant systems)
  <img src="../assets\images\ftolhw.png">

Question 5: Using the image above, is this fault tolerant? Yes