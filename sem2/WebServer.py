from flask import Flask
from flask import render_template
from flask.wrappers import Request
from flask_socketio import SocketIO, disconnect
from flask_socketio import emit
import logging

# Removes useless print functions
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

socketio = SocketIO(app)
vibGraph = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
countGraph = [0]


@app.route('/')
def index():
    return render_template('indexGrpProj.html')

# Noise


@socketio.event
def BBBW1Event(RxData):
    socketio.emit('Web_BBBW1Event', RxData)
    print('Receive Data from BBBW1: ' + str(RxData))

# Number of patrons


@socketio.event
def BBBWcount(RxData):
    global countGraph
    print("Recieved Data from BBBWcount: " + str(RxData))
    if (len(countGraph) == 30):
        countGraph = countGraph[1:]
    countGraph.append(RxData["data"])
    socketio.emit('Web_BBBWcount', [RxData, countGraph])

# Light


@socketio.event
def PotEvent(RxData):
    socketio.emit('PotEvent', RxData)
    print('Receive Data from BBBWPot: ' + str(RxData))

# Running (send)


@socketio.event
def changeThreshold(RxData):
    print("Sending count data")
    socketio.emit('changeThreshold', RxData)

# Running (recieve)


@socketio.event
def changecount(RxData):
    socketio.emit('changecount', RxData)


@socketio.event
def BBBWJQEvent(RxData):
    global vibGraph
    print("Recieved Data from Running Detector: " + str(RxData))
    vibGraph = vibGraph[1:]
    vibGraph.append(RxData[0])
    if RxData[0] > RxData[1]:
        status = "Running Detected"
    elif RxData[0] == 0:
        status = "No Creature Detected"
    else:
        status = "Normal"
    socketio.emit('VibData', [RxData[0], RxData[1], status, vibGraph])


if __name__ == '__main__':
    app.run(host='192.168.137.1')
    