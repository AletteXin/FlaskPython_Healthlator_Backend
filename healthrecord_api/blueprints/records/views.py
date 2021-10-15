from flask import Blueprint

records_api_blueprint = Blueprint('records_api',
                             __name__,
                             template_folder='templates')

@records_api_blueprint.route('/', methods=['GET'])
def index():
    return "RECORDS API"
