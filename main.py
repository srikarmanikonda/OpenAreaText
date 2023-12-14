from flask import Flask, jsonify, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from db import create_database, insert_area_code, get_all_area_codes_from_db, get_area_codes_by_state_from_db, get_states
from exceptions import StateNotFoundError
app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)



@app.route('/areacodes', methods=['GET'])
def get_all_area_codes():
    
    
  area_codes = get_all_area_codes_from_db()
  clean_data = {state: codes for state, codes in area_codes}
  return jsonify(clean_data)

@app.route('/areacodes/<string:state>', methods=['GET'])
def get_area_codes_by_state(state):
    try:
        area_codes = get_area_codes_by_state_from_db(state)
        return jsonify(area_codes)
    except StateNotFoundError: 
        abort(404, description="State not found")
    
@app.route('/states', methods=['GET'])
def get_all_states():
    return jsonify(list(area_codes_data.keys()))

@app.route('/states/<int:area_code>', methods=['GET'])
def get_state_by_area_code(area_code):
    
    if not area_code.isdigit() or len(area_code) != 3:
        abort(400, description="An area code must be exactly three digits long and contain only numbers.")
    for state, codes in area_codes_data.items():
        if area_code in codes:
            return jsonify(state)
    abort(404, description="Area code not found")


if __name__ == '__main__':
    app.run(debug=True)
