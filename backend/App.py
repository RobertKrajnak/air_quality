from flask import Flask, jsonify, render_template, make_response
from flask import flash, redirect, render_template, request, session, abort
# from flask_socketio import SocketIO, send
from threading import Thread
import time
import json
import logging
from datetime import datetime
from firebase import firebase
import firebase_admin
from firebase_admin import credentials, db
from update_firebase import *

try:
    from prod_sensor_reading import *
    from luftdaten_post import *

    logging.info("Running on production enviroment (Raspberry Pi 3 server) and data will be send to luftdaten server")
except ImportError:
    from dev_sensor_reading import *

    logging.info("Running on development enviroment (localhost) without luftdaten")


def sensor_permanent_reading():
    update_time_firebase, update_time_luftdaten = time.time(), time.time()
    id = "raspi-" + get_serial_number()
    while True:
        now = datetime.now()
        data_dict['cpu_temperature'] = str(get_cpu_temperature())
        data_dict['temperature'] = "{:.2f}".format(get_temperature())
        data_dict['pressure'] = "{:.2f}".format(get_pressure() * 100)
        data_dict['light'] = str(get_light())
        data_dict['oxidised'] = str(get_oxidised())
        data_dict['reduced'] = str(get_reduced())
        data_dict['nh3'] = str(get_nh3())
        data_dict['pm1'] = str(get_pm1())
        data_dict['pm25'] = str(get_pm25())  # P2 - luftdaten
        data_dict['pm10'] = str(get_pm10())  # P1 - luftdaten
        data_dict['humidity'] = "{:.2f}".format(get_humidity())
        data_dict['timestamp'] = now.strftime("%d/%m/%Y %H:%M:%S")
        data_dict['active_enviroment'] = str(get_enviroment())

        data_dict_grafs['pressure'] = "{:.2f}".format(get_pressure())
        data_dict_grafs['pm10'] = str(get_pm10())

        time_since_update_firebase = time.time() - update_time_firebase
        if time_since_update_firebase > 60:
            update_firebase_skeleton()

            db.reference('grafs/push_0').update(json.loads(json.dumps(data_dict_grafs)))

            db.reference('record/push_0').update(json.loads(json.dumps(data_dict)))

            print("Updating sceleton and sending data to firebase database!")
            # print(last_10_firebase = db.reference('record').get()) # <- poslednych 10 zaznamov pre FE grafz
            # db.reference('record/push_0').get() # alebo volat jednotlivo napr. push_0
            update_time_firebase = time.time()

        luftdaten_dict = {}
        luftdaten_dict.update(temperature=data_dict["temperature"])
        luftdaten_dict.update(pressure=data_dict["pressure"])
        luftdaten_dict.update(humidity=data_dict["humidity"])
        luftdaten_dict.update(P2=data_dict["pm25"])
        luftdaten_dict.update(P1=data_dict["pm10"])

        time_since_update_luftdaten = time.time() - update_time_luftdaten
        if time_since_update_luftdaten > 100 and get_enviroment() == "production":
            resp = send_to_luftdaten(luftdaten_dict, id)
            print("Response: {}\n".format(
                "OK - Sending data to luftdaten!" if resp else "FAILED - No send data to luftdaten!"))
            update_time_luftdaten = time.time()


if __name__ == "__main__":
    app = Flask("__main__")


    # app.config['SECRET_KEY'] = 'robko25amalekrobiasocketi'
    # socketIO = SocketIO(app, cors_allowed_origins="*")
    # app.host = 'localhost'
    # app.debug = False
    # app.run(debug=True,host='0.0.0.0', port=4000)
    # @socketIO.on("message")
    # def handleMessage(msg):
    #    print(msg)
    #    send(msg, broadcast=True)
    #    return None

    @app.route("/api", methods=['GET'])
    def api():

        response = make_response(
            jsonify(
                data_dict
            ),
        )
        response.headers["Content-Type"] = "application/json"
        return response


    @app.route("/")
    def home():
        return render_template('login.html')


    @app.route('/login', methods=['POST'])
    def do_admin_login():
        if request.form['password'] == 'password' and request.form['username'] == 'admin':
            return api()
        else:
            flash('wrong password!')
            return home()


    data_dict = dict(cpu_temperature="", temperature="", pressure="", light="",
                     oxidised="", reduced="", nh3="", pm1="", pm25="",
                     pm10="", humidity="", timestamp="", active_enviroment="")

    data_dict_grafs = dict(pressure="", pm10="")

    #druhe jadro na permanentne citanie dat z RaspPi senzorov
    thread = Thread(target=sensor_permanent_reading)
    thread.daemon = True
    thread.start()

    app.run(debug=False)
    #socketIO.run(app)
