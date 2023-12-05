---
toc: true
comments: false
layout: post
title: 4.1 - The Internet
description: Internet and basic protocols
type: tangibles
courses: { compsci: {week: 14} }
---

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title> CSP | Routing and Computing</title>
    <link rel="stylesheet" href="../assets/style/page.css">
    <link rel="stylesheet" href="../assets/style/slideAnim.css">
    <link rel="icon" type="image/x-icon" href="../assets/images/favicon.ico">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/github-dark.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>

<!-- and it's easy to individually load additional languages -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/languages/python.min.js"></script>

<script>hljs.highlightAll();</script>

  </head>
  <body>
    <div class="loadModal">
      
    </div>
    <nav id="header">
      <div class="headerDiv">
        <div id="home" onclick="window.location.href = '../index.html'">
          AP CSP Projects
        </div>
      </div>
      <div class="headerDiv" id="redMotButton" onclick="toggleMot()">
        error
      </div>
    </nav>
   
    <div class="articleParallax" style="background-image:url('../assets/images/routing.jpg'); height:100%;"><span class="artParText slideable" data-slideanim="slideOpacity" style="background-color: rgba(5, 5, 5, 0.301)">Routing and Computing</span></div>
    <article>
    <h1 data-slideanim="slideRight" class="slideable">Routing and Computing<br><span style="font-size:small">Devadharson Sasikumar, Sri Surapaneni,Soham Kulkarni, Jonathan Liu: 11/30/23</span></h1>
    <h1 data-slideanim="slideLeft" class="slideable">Fault Tolerance<br><span style="font-size:small">Sri Surapaneni</span></h1>
    <p class="slideable" data-slideanim="slideLeft">Routing, also known as Fault Tolerance is the practice of connecting devices together and the ability to share data between them.</p>
    <p>In this representation, each computer will be represented by a letter and each connection between them being a line.</p>
    <img src="../assets/images/LinktedLaptops.png" class="slideable" data-slideanim="slideRight">
    <ul>
        <li class="sildeable" data-slideanim="slideRight">Slow Network</li>
        <li class="sildeable" data-slideanim="slideRight">One path connects all computers</li>
        <li class="sildeable" data-slideanim="slideRight">Not Fault Tolerant</li>
    </ul>
    <p>
        A <b class="slideable" data-slideanim="slideOpacity">fault</b> is an obstruction of one of the lines seen in the image, in literal terms an obstruction and loss of connection and communication between the computers.<br>
        Fault tolerance is what will happen to the network if one of those lines are shut down.
    </p>
    <p>Do you know why the top image is not fault tolerant?</p>
    <button class="runButton" onclick="document.getElementById('q1').innerText = 'The computers cannot communicate for if they lose connection with each other, and the chain of communication is broken.' ">Reveal Answer</button>
    <p id="q1"></p>
    <h2 class="slideable" data-slideanim="slideRight">How Redundancy Helps Fault Tolerance </h2>
    <p>In this diagram, each computer is linked to another computer multiple times.</p>
    <img class="slideable" data-slideanim="slideLeft" src="../assets/images/complexRoute.jpg">
    <p>In this representation if one of the computer's communication lines is severed, it is more fault tolerant for it has other routes it can take to reach the same computer. <br>
    If a computer has multiple routes to the same computer it is conisdered "redundant"; however, that is not a bad thing, because with only one route the network may be slower, and it is safer.</p>
    <ul>
        <li>Fast Networking</li>
        <li>Multiple Paths</li>
    </ul>
    <p>In this diagram, is the network fault tolerant if we broke one communication line in any location?</p>
    <img src="../assets/images/routPH1.png" class="slideable" data-slideanim="slideOpacity">
    <br>
    <button class="runButton" onclick="document.getElementById('q2').innerText = 'Yes, for there is redundancy allowing for each device to remain connected'">Reveal Answer</button>
    <p id="q2"></p>
    <p>In this diagram, is the network fault tolerant if one of any of the lines break</p>
    <img class="slideable" data-slideanim="slideRight" src="../assets/images/SK2FAULT.png">
    <br>
    <button class="runButton slideable"  data-slideanim="slideOpacity" onclick="document.getElementById('q3').innerText = 'No, if line CF is severed, the network can no longer reach device F'">Reveal Answer</button>
    <p id="q3"></p>
    <p>All of this represents the network and internet, the letters represent devices such as our computers in class right now, and the wires are inside of our computer, redundancy increases reliability on the internet and scales it to more people.
      <br>
      As a matter of fact: your room probably has 2 doors to exit
      </p>
      <h1 data-slideanim="slideLeft" class="slideable">Fault Tolerance Continued<br><span style="font-size:small">Soham Kulkarni</span></h1>
    <p>
      So if you remove a line, then we know that the network breaks, and it says that if a device or connection fails, then the data will be sent through another route. We also learned that fault tolerant networks are reliable and strong. So here are hacks:
    </p>
    <h1>Which of the following is <b>NOT</b> a fault-tolerant network?</h1>
    <p>
      A. Data has more than one path to travel from one device to another.
    </p>
    <p>
      B.If part of the network fails, the network sitll functions via alternative path
    </p>
    <p>
      C.Data will only take one route from one device to another, no matter the number of routes available.
    </p>
    <p>
      D. More devices creates more connections and makes the network stronger.
    </p>
    <button class="runButton" onclick="document.getElementById('SK1').innerText = '(C because information in the wires take the fastest route possible, which makes the network strong and fast)'">Reveal Answer</button>
    <p id="SK1"></p>
    <p>Here is another example, what would make this network fault-tolerant?</p>
    <img src="../assets/images/SK2.png">
    <pre>
      A, because if you remove the wire, then there will be no connection, but if you add it, there are multiple paths and you would create a strong, fast network

Fault tolerance is a really important thing in the internet as it creates multiple paths and connects all of us to it. If a connection fails, there are multiple other paths.

    </pre>
    <h1 data-slideanim="slideLeft" class="slideable">Computing<br><span style="font-size:small">Jonathan Liu and Deva Sasikumar</span></h1>
   <h1>Parallel and Distrubuted Computing</h1>
    <p>
      What is it?
      <br>
      <ul>
        <li>Parallel computing: Using multiple processors or cores to execute a single program simultaneously.
        </li>
        <li>Distributed computing: Connecting multiple computers over a network to solve a common problem.</li>
      </ul>
      Why use it?
      <ul class="slideable" data-slideanim="slideLeft">
      <li>Faster execution time</li>
      <li>Scalability: Handle larger and more complex problems</li>
      <li>Increased efficiency: Utilize resources more effectively</li>
      </ul>
      Types of Parallelism
      <ul class="slideable" data-slideanim="slideRight">
        <li>Bit-level parallelism: Executing multiple instructions in a single clock cycle</li>
        <li>Instruction-level parallelism: Executing multiple instructions in parallel within a single processor</li>
        <li>Task-level parallelism: Distributing different tasks among multiple processors or computers</li>
        <li>Challenges of parallel computing</li>
        <li>Communication overhead: Time spent exchanging data between processors</li>
        <li>Synchronization: Ensuring that tasks are executed in the correct order</li>
        <li>Load balancing: Distributing tasks evenly among processors
        </li>

        </li>
        <li>

        </li>
      </ul>
      Challenges of parallel computing
      <img src="https://cdn.kastatic.org/ka-perseus-images/0db827a36e9287ee9c130cf17610faaed276b931.svg">
      <ul>
        <li>Communication overhead: Time spent exchanging data between processors
        </li>
      <li>Synchronization: Ensuring that tasks are executed in the correct order
      </li>
      <li>Load balancing: Distributing tasks evenly among processors</li>
    </ul>
    Applications of parllalel and distibuted computing
    <ul>
      <li>Scientific computing: Weather forecasting, molecular modeling
      </li>
      <li>Engineering simulations: Crashworthiness tests, fluid dynamic</li>
      <li>Data analysis: Gene sequencing, image processing</li>
      <li>Artificial intelligence: Machine learning, natural language processing</li>
      </ul>
      Sequential Computing
      <ul>
      <li>Executing tasks one after the other, in a single processor or core</li>
      <li>Simplicity: Easier to program and debug</li>
      <li>Limited hardware: Common in older computers or embedded systems</li>
      <li>Task dependencies: When tasks depend on the output of previous tasks</li>
      <li>Total execution time is the sum of individual task execution times</li>
      <img src="https://www.researchgate.net/publication/367162510/figure/fig3/AS:11431281113220233@1673803320022/Parallel-vs-sequential-programming.png">
      </ul>

      <pre>
        Parallel Computing:
        Code gets broken into small sequential operations performed simultaneously
        Parallel computing schedules tasks that get executed at the same time
        Done on the same computer
        Parallel consists of parallel portion and sequential portion
        Comparing efficiency = comparing the time it takes to perform the task
        <img src="https://hpc.llnl.gov/sites/default/files/shared_mem.gif">
      </pre>

      <pre>
        Why:
        Hardware driven: multiple processors
        Link hundreds of cpu together 
        Data: lot of data gets processed same way (SIMD) (Single Instruction Multiple Data)
        Solutions use parall computing scale effectively
      </pre>   
   </p>
   <h1>Quick Question:</h1>
   <pre>
    Assuming there are 4 cores,
    Core 1's task takes 45ms
    Core 2's tasks takes 50ms
    Core 3's tasks take 30ms
    Core 4's tasks take 40ms,

    How long will the program take to run?
   </pre>
   <button class="runButton" onclick="document.getElementById('DJquestion').innerText = 'The total time of the program will take 50ms because that is the longest task assuming they all start at the same time.'">Reveal Answer</button>
   <p id="DJquestion">
      
   </p>
   <pre>
Distributed computing:
Google web search: google sends request to thousands of servers
Web services: (protocols like soap rss rest)
Beowolf clusters: special software to group different computers together

Distributed:
Uses more than one computer
Needs network
Is a mix of seq and par
Takes longer based no network
   </pre>
<h1>Homework:</h1>
<pre>
  Question 1: What is parallel computing?
    Parallel computing is when 
  Question 2: If there is a computer with 3 cores that can each take one task, and the tasks are 25ms, 632ms and 100ms in run time respectively, how long will the program take to run?
  Question 3: Is sequential or parallel computing more efficient, and why?
  Question 4: What is the term called when a network has multiple paths leading up to one destination? (Used in fault-tolerant systems)
  <img src="../assets\images\ftolhw.png">
  Question 5: Using the image above, is this fault tolerant?
</pre>
Due Dec 5th (Tuesday), at 8:30 AM, submit your answers to us on Slack
  <footer class="footing">
    
    </footer>
    <script src="../assets/js/page.js"></script>
    
  </body>
</html>