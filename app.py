
#this is the 1st experiment


# from flask import Flask
# #flask is a framework or a library in python 
# from flask import  request


# app = Flask(__name__)

# #here app is an object of flask class

# @app.route("/")
# def hello_world():
#     return "Hello, World!"

# @app.route("/world1")
# def hello_world1():
#     return "Hello, World!1"

# #here we are able to access the functions using url by extending route server
# @app.route("/world2")
# def hello_world2():
#     return "Hello, World!2"

# @app.route("/test")
# def test():
#     a=100
#     return  "this is my first fun in flask {}".format(a)


# @app.route("/request")
# def request_input():
#     data= request.args.get('x')
#     return "this is my input from url{}".format(data)



# if __name__=="__main__":
#     app.run(host="0.0.0.0")


#this is the 2nd chapter of flask





from flask import Flask,request,render_template,jsonify
import math
#flask is a framework or a library in python 

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_ops():
    if(request.method=='POST'):  #  POST: if someone is sending data through a from, it is also is used to get the data from the user
        ops=request.form['operation']
        num1=request.form['num1']   #operation ,num1 ,num2 are id or class names in html code
        num2=request.form['num2']   #here we use form
        if ops=="add":
            r=int(num1)+int(num2)
            result="The sum of  "+ str(num1) + ' and ' +str(num2) + ' is ' + str(r)
        
        if ops=="subtract":
            r=int(num1)-int(num2)
            result="The stbtraction of  "+ str(num1) + ' and ' +str(num2) + ' is ' + str(r)
        if ops=="multiply":
            r=int(num1)*int(num2)
            result="The multiplication of  "+ str(num1) + ' and ' +str(num2) + ' is ' + str(r)
        if ops=="divide":
            r=int(num1)//int(num2)
            result="The division of  "+ str(num1) + ' and ' +str(num2) + ' is ' + str(r)
        if ops=="log":
            r=math.log(int(num1),int(num2))
            result="The log of  "+ str(num1) + ' and ' +str(num2) + ' is ' + str(r)
        return render_template('results.html',result=result)


@app.route('/postman_action',methods=['POST'])
def math_ops1():
    if(request.method=='POST'):  #  POST: if someone is sending data through a from, it is also is used to get the data from the user
        ops=request.json['operation']
        num1=request.json['num1']   #operation ,num1 ,num2 are id or class names in html code
        num2=request.json['num2']  #here we use json
        if ops=="add":
            r=int(num1)+int(num2)
            result="The sum of  "+ str(num1) + ' and ' +str(num2) + ' is ' + str(r)
        
        if ops=="subtract":
            r=int(num1)-int(num2)
            result="The stbtraction of  "+ str(num1) + ' and ' +str(num2) + ' is ' + str(r)
        if ops=="multiply":
            r=int(num1)*int(num2)
            result="The multiplication of  "+ str(num1) + ' and ' +str(num2) + ' is ' + str(r)
        if ops=="divide":
            r=int(num1)//int(num2)
            result="The division of  "+ str(num1) + ' and ' +str(num2) + ' is ' + str(r)
        if ops=="log":
            r=math.log(int(num1),int(num2))
            result="The log of  "+ str(num1) + ' and ' +str(num2) + ' is ' + str(r)
        return jsonify(result) 

if __name__=="__main__":
    app.run(host="0.0.0.0")



