# Ex.03 Design a Website for Server Side Processing
## Date:

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
form.html
```
<html>
    <head>
    <title>
        churnrate
    </title>
    </head>
    <body>
        <h1>NETHAJISAMARAN(26015547)</h1>
        <h2> 
            Churn Rate
        </h2>
        <form method="POST">
            {%csrf_token%}
            <label>
                initcust 
            </label>
            <input type="number" name="inicust" value="{{i}}">
            <br>
            <label>
                customerlost:
            </label>
            <input type="number" name="custlost" value="{{c}}">
            <br>
            <input type="submit" value="calculate">
            <br>
            <label>
                  churnrate:
            </label>
            <input type="number" value="{{churnrate}}">


        </form>
        
    </body>
</html>
```

views.py
```
from django.shortcuts import render

def churn_rate(request):
    i=float(request.POST.get('inicust','0'))
    c=float(request.POST.get('custlost','0'))

    churnrate=(custlost/inicust)*100 if request.method=='POST' else 0 

    print("inicust =",i)
    print("custlost=",c)
    print("customer_churn_rate =",churnrate)

    return render(
        request,
        'churn/form.html',
        {'i':i,'c':c,'churnrate':churnrate})
```
urls.py
```from django.contrib import admin
from django.urls import path
from churn import views

urlpatterns=[path('',views.churn_rate,name='churn_rate'),]
```

## OUTPUT - SERVER SIDE:

![server-sidevoutput](<Screenshot 2026-11-14 181151.png>)
## OUTPUT - WEBPAGE:

![web-page output](<Screenshot 2026-11-14 174206.png>)
## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
