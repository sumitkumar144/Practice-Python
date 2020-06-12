"""
Created On Thu 04-JUN-2020
@author: sumit.kumar.mishra
"""
from flask import Flask, request
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/',methods=['Get'])
def welcome():
    return "Welcome to my first Flask API and Web App using Flagger/Swagger"

@app.route('/math',methods=['Get'])
def math_operation():

    """Math Calculator Using Flasgger/Swagger
    This is using docstings for specifications
    ---
    parameters:
        - name : operation
          in : query
          type : string
          enum : ['Addition', 'Substraction', 'Multiplication', 'Devision']
          default : 'Addition'
          description : "Operation that needs to be performed"
          required : true
        - name : Number1
          in : query
          type : number
          required : true
        - name : Number2
          in : query
          type : number
          required : true
    responses:
            200:
                description: The output values

    """
    operation=request.args.get("operation")
    #operation = request.json['operation']
    Number1=int(request.args.get("Number1"))
    Number2=int(request.args.get("Number2"))

    if (operation == "Addition"):
        rel = Number1+Number2
        result = "The Sum Of "+str(Number1)+" and "+str(Number2) +" is "+ str(rel)
    elif (operation == "Substraction"):
        rel = Number1 - Number2
        result = "The Difference Of "+str(Number1)+" and "+str(Number2)+" is "+str(rel)
    elif (operation == "Multiplication"):
        rel = Number1 * Number2
        result = "The product Of "+str(Number1)+" and "+str(Number2)+" is "+str(rel)
    elif (operation == "Devision"):
        rel = Number1 / Number2
        result = "The quotient Of "+str(Number1)+" and "+str(Number2)+" is "+str(rel)
    else:
        result = "Invalid Operation"

    print("Result is: ", result)

    return result

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

