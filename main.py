from flask import Flask, request
from websocket import create_connection
import json

app = Flask(__name__)

WS_URL = 'ws://TARGET/dbconnector'

@app.route('/')
def index():
    req = {}
    req['param'] = request.args.get('param', '')

    ws = create_connection(WS_URL)
    ws.send(json.dumps(req))
    r = json.loads(ws.recv())
    ws.close()

    if r.get('error'):
        return r['error']

    return r['messages']

app.run(host='127.0.0.1', port=8000)
