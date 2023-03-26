'''
Step 1 : Give two options
        i) Login - account already exists in SQL Database
        ii)Signup - account doesnt exist, enter new 
            username and password into SQL DB
Step 2 : Enter details into login page
Step 3 : Extract details entered in the login page
Step 4 : Validate whether username exists
        i)  If username doesnt exist don't bother 
            checking for password and give error
        ii) If username exists and password is wrong
            send a error message
        iii) Username exists and password is correct
            then redirect to success page (insurance form)
Step 5: Enter required details into medical insurance form
Step 6: Extract details from form
Step 7: Do regression on the details applied
Step 8: Print the details entered and predicted value
        into a new html 'success' page
'''

import mysql.connector as sql
from medical_model import regression
#from model2_medical import regression
from flask import Flask, request, render_template
#from model import regression
app = Flask(__name__)

''' To display the html page to choose to either sign up or login'''
@app.route("/")
def main():
    return render_template("starting.html")

#%%
'''To extract whether user wants to signup or login'''
@app.route("/choose_method", methods=['Post'])
def method_chosen():
    method = request.form['method']
    print(method)

    if method=='Login':
        return render_template("login.html")
    elif method=='Sign-Up':
        return render_template("signup.html")

#%%
'''Details entered in the signup window must be entered into the table in the database'''
@app.route("/signup",methods=['Post'])
def signing_in():
    global cursor
    mycon=sql.connect(host="localhost",user="root",passwd="themortalinstruments")
    cursor=mycon.cursor()
    client_username = request.form.get("Username")
    client_password = request.form.get("Password")
    #print(client_username, client_password)
    print()

    # if database doesn't exist --> create it and establish connection
    try :
        cursor.execute("create database ml_cia2")
        mycon = sql.connect(host = "localhost", user = "root", passwd = "themortalinstruments", database = "ml_cia2")
        cursor = mycon.cursor()
        #print("------ABCD-------\n")
        
    # if database already exists --> just establish a connection
    except sql.errors.DatabaseError:
        mycon = sql.connect(host = "localhost", user = "root", passwd = "themortalinstruments", database = "ml_cia2")
        cursor = mycon.cursor()
        print("-------EFGH------\n")
        # create a table called Account in it if it doesn't already exist,  else pass
        try :
            tablename = "create table Account (username varchar(50) NOT NULL, password varchar(30) NOT NULL, primary key(username) )"
            cursor.execute(tablename)
            #print("--------IJKL------\n")
        # if the table already exists -pass
        except sql.errors.ProgrammingError:
            #print("------MNOP-----\n")
            pass
    
    #if database didnt exist before the topmost try stmt creates it
    #(since the topmost try stmt creates a db, except clause is ignored and we create the table in finally)
    #and in it create Account table'''
    finally:
        try:
            tablename = "create table Account (username varchar(50) NOT NULL, password varchar(30) NOT NULL, primary key(username) )"
            cursor.execute(tablename)
            #print("------QRST-----\n")
        except sql.errors.ProgrammingError:
            #print("------UVWX-----\n")
            pass

    #print("------YZ-----\n")
    
    stmt="select * from account where username=%s"
    cursor.execute(stmt,(client_username,))
    data = cursor.fetchall()
    alist=[]
    for i in data:
        alist+=[i]

    if alist==[]:
        st="INSERT INTO Account(username,password) VALUES (%s, %s)"
        cursor.execute(st,(client_username,client_password))
        mycon.commit()
        print("--------123--------\n")
        return render_template("login.html")

    elif alist!=[]:
        errormsg="Username has already been taken up.Kindly choose another username"
        return render_template("signup.html",info=errormsg)

#%%
'''validate login detail appropriately'''
@app.route("/login", methods=['Post','Get'])
def login():
    global cursor
    mycon = sql.connect(host = "localhost", user = "root", passwd = "themortalinstruments", database = "ml_cia2")
    cursor = mycon.cursor()
    login_username = request.form.get("Username")
    login_password = request.form.get("Password")
    cursor.execute("select * from account")
    data = cursor.fetchall()
    username_list=[]
    password_list=[]

    for i in data:
        username_list.append(i[0])
        password_list.append(i[1])

    if login_username not in username_list:
        return render_template("login.html",info='Invalid Username. Username does not exist.Please try again')
    else:
        if login_password not in password_list:
            return render_template("login.html",info='Incorrect Password. Please try again')
        else:
            return render_template("insurance.html")

#%%
@app.route("/insurance",methods=['Post'])
def prediction():
    age=request.form.get("Age")
    gender=request.form["sex"]
    bmi=request.form.get("BMI")
    children=request.form.get("Children")
    smoker=request.form["smoker"]
    region=request.form["region"]
    print(age,gender,bmi,children,smoker,region)
    
    if gender=='female':
        gender1=1
    else:
        gender1=0

    if smoker=='yes':
        smoker2=1
    else: 
        smoker2=0
        
    if region=='northwest':
        region2=1
    elif region=='northeast':
        region2=0
    elif region=='southwest':
        region2=3
    else:
        region2=2

    predicted_charge=regression.predict( [[int(age),gender1,float(bmi), int(children),smoker2,region2]] )
    return render_template("success.html",input1=age,input2=gender,input3=bmi,input4=children,input5=smoker,input6=region,result=predicted_charge[0])

#%%
@app.route("/logout")
def logout():
    return render_template("starting.html")

#%%
if __name__=='__main__':
    app.run(host='localhost',port=5000)

