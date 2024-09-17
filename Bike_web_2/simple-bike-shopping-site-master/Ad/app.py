import pymysql

from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql

app = Flask(__name__)
cors = CORS(app)

# To connect MySQL database
conn = pymysql.connect(host='b1hqbhdsdpvslodi5qpx-mysql.services.clever-cloud.com', user='unlm0mb2p6f4gglq', password = "Dm9BcLquvjGlGvhqdz5e", db='b1hqbhdsdpvslodi5qpx')

@app.route('/users', methods=['GET'])
def get_users():

    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("select * from users LIMIT 10")
    output = cur.fetchall()

    print(type(output)); #this will print tuple

    for rec in output:
        print(rec);


    # To close the connection
    #conn.close()

    return jsonify(output);

@app.route('/users', methods=['DELETE'])
def deleteRecord():
    cur = conn.cursor()
    id = int(request.args.get('id'));

    query = f"delete from users where id = {id}";
    #print(query)
    res = cur.execute(query);
    conn.commit();
    print(cur.rowcount, "record(s) deleted")

    return "Record deleted sussesfully"

@app.route('/users', methods=['POST'])
def insertRecord():

        #get raw json values
        raw_json = request.get_json();
        name= raw_json['name'];
        age= raw_json['age'];
        city= raw_json['city'];

        sql="INSERT INTO users (id,name,age,city) VALUES (NULL,'"+name+"','"+str(age)+"','"+city+"')";
        cur= conn.cursor()

        cur.execute(sql);
        conn.commit()
        return "Record inserted Succesfully"

@app.route('/users', methods=['PUT'])
def updateRecord():

        raw_json = request.get_json();

        #print(type(raw_json));

        id = raw_json['id'];
        name= raw_json['name'];
        age= raw_json['age'];
        city= raw_json['city'];
        sql_update_quary=("UPDATE users SET name = '"+name+"',age = '"+str(age)+"',city = '"+city+"'WHERE id = '"+str(id)+"'");
        cur= conn.cursor()
        cur.execute(sql_update_quary);
        conn.commit()
        return "Record Updated Sussecfully";


if __name__ == "__main__":
    #app.run(debug=True);
    app.run(host="0.0.0.0", port=int("1235"), debug=True)