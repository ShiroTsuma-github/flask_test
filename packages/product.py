from packages import app
from flask import render_template, request, redirect, url_for
from flask import g
from flask import jsonify

@app.route('/')
def index():
    return render_template("xd.html")



@app.route('/person/')
def hello():
    #return ",418,", 420
    return jsonify({'name':'Jimit',
                    'address':'India'})

@app.route('/json_example', methods=['POST'])
def handle_json():
    data = request.json
    return jsonify({'name':data.get('name'),
                    'address':data.get('age')})

@app.route('/deletexd/<nazwa>', methods=['DELETE'])
def handle_delete(nazwa):
    uzytkownicy = ["xd1", "ddx", "mariuszek12", "dedede", "tede"]
    if nazwa in uzytkownicy:
        return "zajebiscie", 204
    return "chujowo", 500