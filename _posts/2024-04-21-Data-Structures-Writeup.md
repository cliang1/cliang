---
toc: True
comments: True
layout: post
title: Data Structures Writeup
description: 
type: tangibles
courses: {'compsci': {'week': 29}}
---

# Collections - Total ___ / 3, Grade __/1
 - [ ] Blog Python Model code and SQLite Database.
 Stated with sleep.csv file and then created initialization and SQL schema. Used Python model code to send the SQL sleep data into frontend. Each user has inputs for duration of sleep, quality of sleep, or any sleep disorders. 
![image](https://github.com/cliang1/cliang/assets/142470304/28256356-5b36-4d4a-954a-82fbb79645dc)

 - [ ] From VSCode using SQLite3 Editor, show your unique collection/table in database, display rows and columns in the table of the SQLite database.
 
![image](https://github.com/cliang1/cliang/assets/142470304/1d1e12e2-f832-4eb4-b102-fe45f40203a3)

 - [ ] From VSCode model, show your unique code that was created to initialize table and create test data.

Defines the init_sleep function that initializes the database. The db.create.all funciton helps create the SQL table if it doesn't exist already. There is tester data underneath, and the code under it initializes the data to populate the table.  

![image](https://github.com/cliang1/cliang/assets/142470304/0ab87344-1b3b-48e1-9eb5-541cb4231d06)
![image](https://github.com/cliang1/cliang/assets/142470304/20fd6a31-e220-41b5-977b-968602b95185)

Lists and Dictionaries
Displays code to initalize the sleep.db database.
![image](https://github.com/cliang1/cliang/assets/142470304/634928e0-22a2-4bcf-874d-326ba5279167)
# Lists and Dictionaries - Total __/3, Grade __/1
 - [ ] Blog Python API code and use of List and Dictionaries.
 
![image](https://github.com/cliang1/cliang/assets/142470304/3461b09b-80fa-4213-9ab7-e392c1dd5b17)
![image](https://github.com/cliang1/cliang/assets/142470304/27e11fd7-1a4f-4309-8685-7fd9e2911ffc)

 - [ ] In VSCode using Debugger, show a list as extracted from database as Python objects.
 
![image](https://github.com/cliang1/cliang/assets/142470304/cb676161-62b2-48b8-8fb9-02d9ab571744)

 - [ ] In VSCode use Debugger and list, show two distinct example examples of dictionaries, show Keys/Values using debugger.
APIs and JSON
The first one is an example with the sleep data, which gets all the SQL data related to sleep. By adding a breakpoint there, we can see the query that gets all the data and the post function that requests the json data. 
![image](https://github.com/cliang1/cliang/assets/142470304/bc105fc4-98af-47fa-b63f-28bc2988fed4)
![image](https://github.com/cliang1/cliang/assets/142470304/fafb392e-9bd5-4d6c-804b-a007c0d3053b)

# APIs and JSON - Total __/7, Grade __/1
 - [ ] Blog Python API code and use of Postman to request and respond with JSON.
 The python code creates an ednpoint that requires a input from the body
![image](https://github.com/cliang1/cliang/assets/142470304/9d9884d7-2e5a-4a6c-935b-d23b13ec7099)

 - [ ] In VSCode, show Python API code definition for request and response using GET, POST, UPDATE methods. Discuss algorithmic condition used to direct request to appropriate Python method based on request method.

 
![image](https://github.com/cliang1/cliang/assets/142470304/5e309e26-a42d-419d-83c3-4b22075c4a1b)
![image](https://github.com/cliang1/cliang/assets/142470304/ddf5c4ac-653a-45f1-9619-4368ea3c8adb)

 - [ ] In VSCode, show algorithmic conditions used to validate data on a POST condition.
The 400 error shows up if the user doesnt' provide a body for the API to use to predict calorie count. 

 ![image](https://github.com/cliang1/cliang/assets/142470304/55f1affc-dbbb-4411-a4c8-1d7d9880fa17)
 
![image](https://github.com/cliang1/cliang/assets/142470304/498f448f-0ab6-4f41-a387-1cc16e39c1d4)

![image](https://github.com/cliang1/cliang/assets/142470304/03ec00b6-0437-441d-823b-082659ad8dd1)

 - [ ] In Postman, show URL request and Body requirements for GET, POST, and UPDATE methods.
 
![image](https://github.com/cliang1/cliang/assets/142470304/a608f506-279a-4b6d-b329-b150dcaa3354)

 - [ ] In Postman, show the JSON response data for 200 success conditions on GET, POST, and UPDATE methods.

![image](https://github.com/cliang1/cliang/assets/142470304/e21e8507-f1e4-442f-b90f-5236eb633d18)

 - [ ] In Postman, show the JSON response for error for 400 when missing body on a POST request.
 ![image](https://github.com/cliang1/cliang/assets/142470304/3ce78daf-f495-42f4-9edc-8330db52f9f7)

 
# Frontend - Total __/8, Grade __/1
 - [ ] Blog JavaScript API fetch code and formatting code to display JSON.
 The fetch code connects to the API specified in the backend, and displays the sleep data in a table, and the fitness data as a number rounded to 2 decimals. 
![image](https://github.com/cliang1/cliang/assets/142470304/2de812dd-e471-4aa5-b8d0-110f8529537b)
![image](https://github.com/cliang1/cliang/assets/142470304/437c9fc7-7cd9-4734-81db-f9a484cb5e1c)

 - [ ] In Chrome inspect, show response of JSON objects from fetch of GET, POST, and UPDATE methods.
 
![image](https://github.com/cliang1/cliang/assets/142470304/82bb1093-f71c-412b-a510-5870484759a3)

 - [ ] In the Chrome browser, show a demo (GET) of obtaining an Array of JSON objects that are formatted into the browsers screen.
 
![image](https://github.com/cliang1/cliang/assets/142470304/a019033d-9051-4b8b-adfb-27a1a651d334)

 - [ ] In JavaScript code, describe fetch and method that obtained the Array of JSON objects.
 The code gets all the records from the database, formats it as a json object, and presents it in postman when the API is called.  
 
![image](https://github.com/cliang1/cliang/assets/142470304/d6b002df-ed5f-420c-afc3-a3923fce6a04)
![image](https://github.com/cliang1/cliang/assets/142470304/7b806b6f-3936-4d26-b040-8b9d3652e266)

 - [ ] In JavaScript code, show code that performs iteration and formatting of data into HTML.
 Iterates over each row of the sleep data and then uses the displayitems function to format it as a table. 

![image](https://github.com/cliang1/cliang/assets/142470304/83a868f7-3635-450e-a799-b8c845bfe08c)

 
 - [ ] In JavaScript code, show and describe code that handles success. Describe how code shows success to the user in the Chrome Browser screen.
Sucess will print a bolded sentence telling the user their predicted calorie burn as well as a fact abotu fitness to encourage the user to continue exerciseing. 
![image](https://github.com/cliang1/cliang/assets/142470304/490d8cf5-f860-46b1-89d7-77e5a23d5af8)
![image](https://github.com/cliang1/cliang/assets/142470304/ea99377a-1df0-4a11-bffc-67c42fdb2d22)

 - [ ] In JavaScript code, show and describe code that handles failure. Describe how the code shows failure to the user in the Chrome Browser screen.
 The error message appears when there are issues with the API, and the frontend is unable to get a predicted calorie count from the backend. This can come from not running backend, forgetting to input certain values, etc. 
 ![image](https://github.com/cliang1/cliang/assets/142470304/52d296f8-e36e-4abb-bb80-725ecf10d496)
 ![image](https://github.com/cliang1/cliang/assets/142470304/6177572e-d246-41a0-b524-be462b4f2492)


# Optional/Extra, ML Algorithm Analysis - Total __/5, Grade __/1
 - [ ] In the ML projects, there is a great deal of algorithm analysis. Think about preparing data and predictions.

 - [ ] Show algorithms and preparation of data for analysis. This includes cleaning, encoding, and one-hot encoding.
 
 - [ ] Show algorithms and preparation for predictions.
 
![image](https://github.com/cliang1/cliang/assets/142470304/31a97304-76c0-40fd-aef5-1593d15f6d4b)

 - [ ] Discuss concepts and understanding of Linear Regression algorithms.
 
![image](https://github.com/cliang1/cliang/assets/142470304/3a4b4e57-1a4e-4148-a7ce-9d7a283d93dc)

 - [ ] Discuss concepts and understanding of Decision Tree analysis algorithms.
 
![image](https://github.com/cliang1/cliang/assets/142470304/d38596c8-444f-4ef2-b05b-08ace2c410c2)
