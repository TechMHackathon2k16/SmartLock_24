
from flask import Flask, jsonify, render_template
from flask import abort
from flask import make_response,request
import requests, simplejson
import json
from pushjack import GCMClient
import sqlite3 as sql

DATABASE = 'SmartlockUser.db'
client = GCMClient(api_key='AIzaSyAG4qhcqNqkJLtBQTmljCI8ijWuBtFY_YM')

app= Flask(__name__)
app.config.from_object(__name__)


app.secret_key = 'my key'




#post the request to rasp to Turn n or Turn Off LED	
@app.route('/smartlock/led1/action', methods=['POST'])	
def call_led1():
	Action = request.json['keyword']
	url = "http://192.168.43.217:5000/smarthome/led1"
	headers = {'content-type': 'application/json'}
	msg={
                'led1':Action
                }
	obj = simplejson.dumps(msg)

	r = requests.post(url, data=obj, headers=headers)
	#r = client.send(regid,r.json['message'],collapse_key='collapse_key',delay_while_idle=True,time_to_live=604800)
	return json.dumps(r.json())
       

#post the request to rasp to Turn n or Turn Off LED	
@app.route('/smartlock/led2/action', methods=['POST'])	
def call_led2():
	Action = request.json['keyword']
	url = "http://192.168.43.217:5000/smarthome/led2"
	headers = {'content-type': 'application/json'}
	msg={
                'led2':Action
                }
	obj = simplejson.dumps(msg)

	r = requests.post(url, data=obj, headers=headers)
	#r = client.send(regid,r.json['message'],collapse_key='collapse_key',delay_while_idle=True,time_to_live=604800)
	return json.dumps(r.json())


#post the request to rasp to Turn n or Turn Off LED	
@app.route('/smartlock/led3/action', methods=['POST'])	
def call_led3():
	Action = request.json['keyword']
	url = "http://192.168.43.217:5000/smarthome/led3"
	headers = {'content-type': 'application/json'}
	msg={
                'led3':Action
                }
	obj = simplejson.dumps(msg)

	r = requests.post(url, data=obj, headers=headers)
	#r = client.send(regid,r.json['message'],collapse_key='collapse_key',delay_while_idle=True,time_to_live=604800)
	return json.dumps(r.json())
       

#post the request to rasp to Turn n or Turn Off LED	
@app.route('/smartlock/led4/action', methods=['POST'])	
def call_led4():
	Action = request.json['keyword']
	url = "http://192.168.43.217:5000/smarthome/led4"
	headers = {'content-type': 'application/json'}
	msg={
                'led4':Action
                }
	obj = simplejson.dumps(msg)

	r = requests.post(url, data=obj, headers=headers)
	#r = client.send(regid,r.json['message'],collapse_key='collapse_key',delay_while_idle=True,time_to_live=604800)
	return json.dumps(r.json())
       

#post the request to rasp to Turn n or Turn Off LED	
@app.route('/smartlock/led5/action', methods=['POST'])	
def call_led5():
	Action = request.json['keyword']
	url = "http://192.168.43.217:5000/smarthome/led5"
	headers = {'content-type': 'application/json'}
	msg={
                'led5':Action
                }
	obj = simplejson.dumps(msg)

	r = requests.post(url, data=obj, headers=headers)
	#r = client.send(regid,r.json['message'],collapse_key='collapse_key',delay_while_idle=True,time_to_live=604800)
	return json.dumps(r.json())

#post the request to rasp to Turn n or Turn Off LED	
@app.route('/smartlock/motor1/action', methods=['POST'])	
def call_motor1():
	Action = request.json['keyword']
	url = "http://192.168.43.217:5000/smarthome/motor1"
	headers = {'content-type': 'application/json'}
	msg={
                'motor1':Action
                }
	obj = simplejson.dumps(msg)

	r = requests.post(url, data=obj, headers=headers)
	#r = client.send(regid,r.json['message'],collapse_key='collapse_key',delay_while_idle=True,time_to_live=604800)
	return json.dumps(r.json())

#post the request to rasp to Turn n or Turn Off LED	
@app.route('/smartlock/lock/action', methods=['POST'])	
def call_lockdoor():
	Action = request.json['keyword']
	url = "http://192.168.43.217:5000/smarthome/lock"
	headers = {'content-type': 'application/json'}
	msg={
                'motor2':Action
                }
	obj = simplejson.dumps(msg)

	r = requests.post(url, data=obj, headers=headers)
	#r = client.send(regid,r.json['message'],collapse_key='collapse_key',delay_while_idle=True,time_to_live=604800)
	return json.dumps(r.json())
       
#post the request to rasp to Turn n or Turn Off LED	
@app.route('/smartlock/unlock/action', methods=['POST'])	
def call_unlockdoor():
	Action = request.json['keyword']
	url = "http://192.168.43.217:5000/smarthome/unlock"
	headers = {'content-type': 'application/json'}
	msg={
                'unlock':"1"
                }
	obj = simplejson.dumps(msg)

	r = requests.post(url, data=obj, headers=headers)
	#r = client.send(regid,r.json['message'],collapse_key='collapse_key',delay_while_idle=True,time_to_live=604800)
	return json.dumps(r.json())
       
       
if __name__ == '__main__':
	app.debug = True
	app.run(host="192.168.43.147")

