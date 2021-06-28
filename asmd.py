from flask import Flask, jsonify, request
from flask.typing import StatusCode
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
    if(functionName == "add" or functionName == "subtract" or functionName == "multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301      #missing atribute
        else:
            return 200
    elif(functionName == "divide"):
        if "x" not in postedData or "y" not in postedData:
            return 301      #missing atribute
        elif int(postedData["y"]) == 0:
            return 302
        else:
            return 200
        

class Add(Resource):
    def post(self):
        # If I'm here, then the resource Add was requested using the method POST
        
        # Get the posted data:
        postedData = request.get_json()
        # Verify validity of posted data 
        status_code = checkPostedData(postedData, "add")
        if(status_code!=200):
            retJson = {
                "Message" : "An error as occured",
                "Status Code" : status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        
        # Add the posted data
        ret = int(x) + int(y)
        retMap = {
            'Message' : ret,
            'Status code' : 200
        }
        return jsonify(retMap)
        
class Subtract(Resource):
    def post(self):
        # If I'm here, then the resource Subtract was requested using the method POST
        
        # Get the posted data:
        postedData = request.get_json()
        # Verify validity of posted data 
        status_code = checkPostedData(postedData, "subtract")
        if(status_code!=200):
            retJson = {
                "Message" : "An error as occured",
                "Status Code" : status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        
        # Add the posted data
        ret = int(x) - int(y)
        retMap = {
            'Message' : ret,
            'Status code' : 200
        }
        return jsonify(retMap)

    

class Divide(Resource):
    def post(self):
        # If I'm here, then the resource Divide was requested using the method POST
        
        # Get the posted data:
        postedData = request.get_json()
        # Verify validity of posted data 
        status_code = checkPostedData(postedData, "divide")
        if(status_code!=200):
            retJson = {
                "Message" : "An error as occured",
                "Status Code" : status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        
        # Add the posted data
        ret = (int(x)*1.0) / int(y)
        retMap = {
            'Message' : ret,
            'Status code' : 200
        }
        return jsonify(retMap)
    
class Multiply(Resource):
    def post(self):
        # If I'm here, then the resource Multiply was requested using the method POST
        
        # Get the posted data:
        postedData = request.get_json()
        # Verify validity of posted data 
        status_code = checkPostedData(postedData, "multiply")
        if(status_code!=200):
            retJson = {
                "Message" : "An error as occured",
                "Status Code" : status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        
        # Add the posted data
        ret = int(x) * int(y)
        retMap = {
            'Message' : ret,
            'Status code' : 200
        }
        return jsonify(retMap)

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Divide, "/divide")
api.add_resource(Multiply, "/multiply")


@app.route('/')
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
    
    
# in folder say `export FLASK_APP=app.py`
# then `flask run`

# `sudo lsof -i :5000` to find running processes on port
# `kill -9 <pid>`

