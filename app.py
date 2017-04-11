import datetime
import urllib
import json

from flask import Flask,request, jsonify, abort
import ymlconfig

config_file_path = 'config.yaml'

config = ymlconfig.load_file(config_file_path)
token = config.token
chat_id = config.chat_id

app = Flask(__name__)

@app.route("/", methods=['POST'])

def parse_test():

    if not request.json:
        abort(400)

    alert_name = request.json['alerts'][0]['labels']['alertname']
    alert_time = str(datetime.datetime.strptime(request.json['alerts'][0]['startsAt'], "%Y-%m-%dT%H:%M:%S.%fZ"))[0:19]
    alert_high = (request.json['alerts'][0]['labels']['severity']).upper()
    alert_inst = request.json['alerts'][0]['labels']['instance']
    alert_desc = request.json['alerts'][0]['annotations']['description']
    msg_chat = urllib.quote("[{}] {} at {}\non {} \n{}".format(alert_high, alert_name, alert_time, alert_inst, alert_desc))
    msg_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(token, chat_id, msg_chat).encode('UTF-8')
    
    get = urllib2.urlopen(msg_url)

    return jsonify(request.json), 201
