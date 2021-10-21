from flask import Blueprint
from app import app
from flask_cors import CORS
from models.form import Form
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
import datetime as dt


records_api_blueprint = Blueprint('records_api',
                             __name__,
                             template_folder='templates')

@records_api_blueprint.route('/', methods=['GET'])
def index():
    all_records = Form.select()
    all_records = [model_to_dict(record) for record in all_records]

    return jsonify(all_records)

@records_api_blueprint.route("/create")
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

@records_api_blueprint.route("/update")
def update():
    # Form.create(ID="1111")
    return "create"

@records_api_blueprint.route("/delete")
def delete():
    record_to_delete = Form.get(Form.id == 3)
    record_to_delete.delete_instance()
    return "deleted"


@records_api_blueprint.route("/show", methods = ["POST"])
def show():
    
    print("connected")
    user_input = request.get_json()
    print('user_input')
    print(user_input)

    record_exists = Form.get_or_none(Form.id == user_input['id'], Form.Name == user_input['Name'])

    if record_exists:
        id = record_exists.id
        Name = record_exists.Name
        Gender = record_exists.Gender
        Birthdate = record_exists.Birthdate
        Address = record_exists.Address
        Medications = record_exists.Medications
        Nameofnextkin = record_exists.Nameofnextkin
        Phoneofnextkin = record_exists.Phoneofnextkin
        Reasonforvisit = record_exists.Reasonforvisit

        record_details = []
        
        record_details.append([{'id':record_exists.id, 'Name': record_exists.Name, 
        'Gender': record_exists.Gender, 'Birthdate': record_exists.Birthdate, 
        'Address': record_exists.Address, 'Medications': record_exists.Medications, 
        'Nameofnextkin': record_exists.Nameofnextkin, 'Phoneofnextkin': record_exists.Phoneofnextkin,
        'Reasonforvisit': record_exists.Reasonforvisit }])

        print(record_details)

    return jsonify({'record_details' : record_details})
