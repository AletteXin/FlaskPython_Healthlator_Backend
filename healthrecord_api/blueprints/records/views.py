from flask import Blueprint
from app import app
from flask_cors import CORS
from models.form import Form
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
import datetime as dt
import peewee as pw
import datetime
from database import db


records_api_blueprint = Blueprint('records_api',
                             __name__,
                             template_folder='templates')

@records_api_blueprint.route('/', methods=['GET'])
def index():
    all_records = Form.select()
    all_records = [model_to_dict(record) for record in all_records]

    return jsonify(all_records)

@records_api_blueprint.route("/create", methods = ["POST"])
def create():
    
    print("connected")
    new_entry = request.get_json()
    print('new_entry')
    print(new_entry)

    current_time = datetime.datetime.now
    now = print(current_time)

    create = Form.create(Name = new_entry['Name'], Gender = new_entry['Gender'], Birthdate = new_entry['Birthdate'], 
    Address = new_entry['Address'], Medications = new_entry['Medications'], Nameofnextkin = new_entry['Nameofnextkin'],
    Phoneofnextkin = new_entry['Phoneofnextkin'], Reasonforvisit = new_entry['Reasonforvisit'], Fever = False, 
    Headache = True, Nightchills = False, Sorethroat = False, Cough = False, Breathingdiff = False, 
    Diarrhoea = True, Chestpain = False, Legnumbness = False, Handnumbness = False, Facenumbness = False, 
    Diabetes = False, Highbloodpressure = True, Highcholesterol = False, Asthma = False, Kidneydisease = False,
    Arthritis = False, Pancreaticcancer = False, Livercancer = False, Colorectalcancer = False, 
    COPD = True, Depression = False, Lungcancer = False)

    message = []
    message.append(create.id)
    
    return jsonify({'message' : message})

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
    
    record_details = []
    
    if record_exists:
        record_details.append([{'id':record_exists.id, 'Name': record_exists.Name, 
        'Gender': record_exists.Gender, 'Birthdate': record_exists.Birthdate, 
        'Address': record_exists.Address, 'Medications': record_exists.Medications, 
        'Nameofnextkin': record_exists.Nameofnextkin, 'Phoneofnextkin': record_exists.Phoneofnextkin,
        'Reasonforvisit': record_exists.Reasonforvisit, 'Errormessage': "" }])

    
    else: 
        record_details.append([{'id':"", 'Name': "", 
        'Gender': "", 'Birthdate': "", 
        'Address': "", 'Medications': "", 
        'Nameofnextkin': "", 'Phoneofnextkin': "",
        'Reasonforvisit': "", 'Errormessage': "Record does not exist." }])

    print(record_details)

    return jsonify({'record_details' : record_details})
