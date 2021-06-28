from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")  
# where db is the name of service specified in docker compose file
# 27017 is the default port used by mongodb
db = client.aNewDB
UserNum = db["UserNum"] #name of collection

UserNum.insert({
    'num_of_users' : 0
})

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0][ 'num_of_users' ]
        new_num = prev_num + 1 
        UserNum.update({}, {"$set":{ 'num_of_users' : new_num }})
        return str("Hello visitor number " + str(new_num))

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

api.add_resource(Visit, "/hello")


@app.route('/')
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)

    
    
# in folder say `export FLASK_APP=app.py`
# then `flask run`

# `sudo lsof -i :5000` to find running processes on port
# `kill -9 <pid>`

