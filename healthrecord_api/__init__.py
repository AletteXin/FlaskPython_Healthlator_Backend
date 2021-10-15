from app import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from healthrecord_api.blueprints.records.views import records_api_blueprint


app.register_blueprint(records_api_blueprint, url_prefix='/api/records')


@app.route("/")
def home():
    return "hello"