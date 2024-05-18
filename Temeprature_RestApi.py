import json
import flask
from flask import Flask
from flask_restful import Resource,Api
app=Flask(__name__)
api=Api(app)

import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="weather"
)
# Create a cursor to execute SQL queries
cursor = db_connection.cursor()
select_query="""
select * from temperature
"""
cursor.execute(select_query)
records = cursor.fetchall()
print(cursor)
print(records)
temp=json.dumps(records)

app = Flask(__name__)
@app.route("/gettemp",methods=['GET'])

def gettemperature():
   return temp

@app.route("/getbyday/<string:day>", methods=['GET'])
def get_byday(day):
        cursor.execute(f"SELECT * FROM temperature WHERE day={day}")
        result = cursor.fetchall()
        print(result)
        rec=json.dumps(result)
        cursor.close()
        return rec
        # t = [r for r in records if (str(records['day']) == str(day))]
        # return flask.jsonify({'emp': t})
app.run()
