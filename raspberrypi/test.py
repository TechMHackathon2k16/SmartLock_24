from flask import Flask, make_response, request
import os, jsonify, json

# Create the server
app = Flask(__name__)



@app.route('/smarthome/unlock', methods=['POST'])
def unlock():
    unlock = request.json['unlock']
   
   

    if '1' in unlock:
        os.system('python unlock.py')
       
    else:
        os.system('python lock.py')
       
       
    obj={
            'message':'Door Unlocked'
            }
    return json.dumps(obj)


@app.route('/smarthome/lock', methods=['POST'])
def lock():
    os.system('python lock.py')
     
    obj={
            'message':'Door Locked'
            }
    return json.dumps(obj)



@app.route('/smarthome/led1', methods=['POST'])
def led1():
    led1 = request.json['led1']
    if '1' in led1:
        os.system('python led1on_19.py')
        obj={
            'message':'Light1 On'
            }
        return json.dumps(obj)

    else:
        os.system('python led1off_19.py')
        obj={
            'message':'Light1 Off'
            }
        return json.dumps(obj)


@app.route('/smarthome/led2', methods=['POST'])
def led2():
    led2 = request.json['led2']
    if '1' in led2:
        os.system('python led2on_29.py')
        obj={
            'message':'Light2 On'
            }
        return json.dumps(obj)

    else:
        os.system('python led2off_29.py')
        obj={
            'message':'Light2 Off'
            }
        return json.dumps(obj)

    


@app.route('/smarthome/led3', methods=['POST'])
def led3():
    led3 = request.json['led3']
    if '1' in led3:
        os.system('python led3on_31.py')
        obj={
            'message':'Light3 On'
            }
        return json.dumps(obj)

    else:
        os.system('python led3off_31.py')
        obj={
            'message':'Light3 Off'
            }
        return json.dumps(obj)

    return make_response(jsonify({'success':'success'}), 200)


@app.route('/smarthome/led4', methods=['POST'])
def led4():
    led4 = request.json['led4']
    if '1' in led4:
        os.system('python led4on_33.py')
        obj={
            'message':'Light4 On'
            }
        return json.dumps(obj)

    else:
        os.system('python led4off_33.py')
        obj={
            'message':'Light4 Off'
            }
        return json.dumps(obj)

    return make_response(jsonify({'success':'success'}), 200)


@app.route('/smarthome/led5', methods=['POST'])
def led5():
    led5 = request.json['led5']
    if '1' in led5:
        os.system('python led5on_35.py')
        obj={
            'message':'Light5 On'
            }
        return json.dumps(obj)

    else:
        os.system('python led5off_35.py')
        obj={
            'message':'Light5 Off'
            }
        return json.dumps(obj)
    
    return make_response(jsonify({'success':'success'}), 200)

@app.route('/smarthome/motor1', methods=['POST'])
def motor1():
    motor1 = request.json['motor1']
    if '1' in motor1:
        os.system('python motor1on_37.py')
        obj={
            'message':'Motor1 On'
            }
        return json.dumps(obj)

    else:
        os.system('python motor1off_37.py')
        obj={
            'message':'Motor1 Off'
            }
        return json.dumps(obj)

    return make_response(jsonify({'success':'success'}), 200)





if __name__ == '__main__':
   app.debug = True
   app.run(host="192.168.43.217")
