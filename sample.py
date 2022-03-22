import sqlite3
import table
import demo

from flask import Flask, jsonify, request;
app = Flask(__name__)

con=sqlite3.connect('demo.db',check_same_thread=False);


@app.get('/newRequest')
def getExample(): 
    data=demo.getAll();
    json_list=[];
    for item in data:
        content=();
        content={'Rollno':item[0], 'Name':item[1]};
        json_list.append(content);
    return(jsonify(json_list));


# cur = con.cursor();

# con = sqlite3.connect('demo.db');
# cur = con.cursor();

# json_data=[]
@app.route('/parcel')
def anotherFun():
    data =demo.getAll();

    return(jsonify(data))

#* This is POST
@app.post("/po")
def postfunc():
    data = request.get_json();
    print("__data__");
    print(data)
    #json_data.append(data);
    demo.Insert(data);
    return("Got Data");

@app.patch("/upd")
def updateFunc():
    data=request.get_json();
    demo.upd(data);
    return("Got updated");

@app.delete("/del/<id>")
def delFunc(id):
    demo.deletestu(id);
    return("deleted");


if __name__=='__main__':
 app.run(debug=True,port=2000)
