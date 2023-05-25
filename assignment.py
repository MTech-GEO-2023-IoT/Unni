  GNU nano 6.2                                         new.py                                                  
import paho.mqtt.client as paho
import pymysql
global mqttclient;
global broker;
global port;
broker = "localhost";
port = 1883;
client_uniq = "pubclient_123"
mqttclient = paho.Client(client_uniq, True) 
def storeData(mesg,t):
 #Create a connection to MySQL Database 
 conn =pymysql.connect(database="sampledata",user="unninarayanan",password="unni",host="localhost")
 #Create a MySQL Cursor to that executes the SQLs
 cur=conn.cursor()
 #Create a dictonary containing the fields, name, age and place
 data={'topic':t,'data':mesg}
 #Execute the SQL to write data to the database
 cur.execute("INSERT INTO measurements(topic , data)VALUES(%(topic)s,%(data)s);",data)
 print("Data added")
 #Close the cursor
 cur.close()
 #Commit the data to the database
 conn.commit()
 #Close the connection to the database
 conn.close()
def test(client, userdata, message):
 print("client:"+ str(client))
 print("userdata:"+ str(userdata))
 print("message:"+ str(message.payload.decode()))
 storeData(message.payload.decode(),message.topic)
def _on_message(client, userdata, msg):
# print("Received: Topic: %s Body: %s", msg.topic, msg.payload)
 print(msg.topic+" "+str(msg.payload))
