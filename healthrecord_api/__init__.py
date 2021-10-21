from app import app
from flask_cors import CORS
from models.form import Form
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
import datetime as dt

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from healthrecord_api.blueprints.records.views import records_api_blueprint

app.register_blueprint(records_api_blueprint, url_prefix='/api/records')


@app.route("/")
def home():
    return "hello"


@app.route("/create")
def create():
    Form.create(Name = "Amy", Gender = "female", Birthdate = dt.date(1940, 1, 21), 
    Address = "Klang Valley", Medications = "high blood pressure pills", Nameofnextkin = "Mary",
    Phoneofnextkin = "0123456789", Reasonforvisit = "To complete a check up", Fever = False, 
    Headache = True, Nightchills = False, Sorethroat = False, Cough = False, Breathingdiff = False, 
    Diarrhoea = True, Chestpain = False, Legnumbness = False, Handnumbness = False, Facenumbness = False, 
    Diabetes = False, Highbloodpressure = True, Highcholesterol = False, Asthma = False, Kidneydisease = False,
    Arthritis = False, Pancreaticcancer = False, Livercancer = False, Colorectalcancer = False, 
    COPD = True, Depression = False, Lungcancer = False)
    return "create"

@app.route("/update")
def update():
    # Form.create(ID="1111")
    return "create"

@app.route("/delete")
def delete():
    record_to_delete = Form.get(Form.id == 3)
    record_to_delete.delete_instance()
    return "deleted"


@app.route("/show")
def show():
    all_records = Form.select()
    all_records = [model_to_dict(record) for record in all_records]

    return jsonify(all_records)
