# Flask_MySQL_LinearPrediction
Here we make use of flask to create a web app framework that is connected to a login database in mysql to predict medical prices based on user input.

First you make sure you have flask and mysql installed in your system.

Since you are going to predict the charges that will be levied on you based on your inputs, first you will create a linear regression model (medical_model.py)
You will make use of the entire csv file as your training dataset and run the model on it.

Next will be creation of your web application.
For this you will have to create your app.py file and required given no.of html files.
HTML files must be saved within a folder called 'templates' within the same directory.
If you are making use of CSS files they will go under a file called 'static' within that directory.

All of the code linking your app.py to the HTML pages will be written by importing Flask library.
Here, the library mysql.connector has been used for linking python with mysql.

Following are the things that are done in the code:
1) Create a regression or classification model within your root project folder based on a kaggle dataset of your choice (here it is 'medical_model.py' on 'insurance.csv').
2)Create a database in mysql with a table that will store every user's username and password. (Since I have included creation of database within app.py using try-except-finally clause, this step has been skipped)
3) Next create your login page, user-input page and prediction_success page using HTML and CSS
4) Create an interface between python and mysql by importing mysql.connector and creating a cursor object after establishing the connection.
5) Write the code in app.py to do the following in chrome :
  
  i) Choose the option to signup if you haven't created an account before,else login if you have created one before. 
  
  ii) If you choose to signup, enter username and password of your choice. You will be given an error message if that username has already been taken by someone. Else it will be accepted and you move onto the Login Page.
  
  iii) If you choose to directly login, choose login option and enter username and password. If username or password is entered incorrectly (doesn't correspond to a value within your table in the database) you will be thrown an error message. Else, you move on to the medical insurance page.
  
  iv) In the medical insurance page, fill in the given inputs. Each input corresponds to a column from your chosen kaggle dataset. Click on submit once done.
  
  v) Extract the inputs from the form and plug into the regression model.
  
  vi) Display the prediction in a separate page along with your given inputs.
  
  vii) Click on Exit to be redirected back to the starting webpage.
  
  viii) Enter Ctrl+C in your kernel to end the program.
