from flask import Flask, jsonify, request;


app = Flask(__name__);

lst=[{"name": "THARUN", "Roll": 1},{"name": "AK", "Roll": 2},{"name": "Vikky", "Roll": 3}];

@app.get("/")
def samp():
    return(jsonify(lst));


@app.delete("/del/<int:inputId>")
def deletemethod(inputId):
    for item in lst:
        if(item["Roll"] == inputId):
            lst.remove(item)
            return("deleted")

if(__name__=='__main__'):
    app.run(debug=True,port=2000) 