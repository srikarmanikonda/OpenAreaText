from flask import Flask, jsonify, abort
from db import get_all_area_codes_from_db, get_area_codes_by_state_from_db, get_states, get_states, insert_area_code,create_database,get_state_by_area_code_from_db
from flasgger import Swagger
from exceptions import StateNotFoundError
app = Flask(__name__)
Swagger(app)

CSV_FILE_PATH = 'area_codes.csv'

create_database()

insert_area_code(CSV_FILE_PATH)


@app.route('/areacodes', methods=['GET'])
def get_all_area_codes():
    
    """  Get all area codes in a list.
    ---
    tags:
        - Area Codes

    responses:
        200:
            description: Returns a list of area codes for the specified state.
   
    """
    area_codes = get_all_area_codes_from_db()
    return jsonify(area_codes)

@app.route('/areacodes/<string:state>', methods=['GET'])
def get_area_codes_by_state(state):
    """
Get area codes for a specific state.
---
tags:
  - Area Codes
parameters:
  - name: state
    in: path
    type: string
    required: true
    description: The state for which to look up area codes
responses:
  200:
    description: Returns a list of area codes for the specified state.
    examples:
      application/json: [205, 251, 256, 334, 659, 938]
  404:
    description: State not found.
"""

    try:
        area_codes = get_area_codes_by_state_from_db(state.lower())
        return jsonify(area_codes)
    except StateNotFoundError: 
        abort(404, description="State not found")
    
@app.route('/states', methods=['GET'])
def get_all_states():
    """
    Get a list of all states.
    ---
    tags:
        - States
    responses:
        200:
            description: Returns a list of all states.
    """
    states = get_states()  
    return jsonify(states)  



@app.route('/states/<int:area_code>', methods=['GET'])
def get_state_by_area_code(area_code):
    """
    Get the state corresponding to an area code.
    ---
    tags:
        - States
    parameters:
      - name: area_code
        in: path
        type: integer
        required: true
        description: The area code to lookup
    responses:
        200:
            description: Returns the state corresponding to the area code.
        400:
            description: Invalid area code format.
        404:
            description: Area code not found.
    """
    
    if not isinstance(area_code, int):
        abort(400, description="Invalid area code format")

    state = get_state_by_area_code_from_db(area_code)  
    if state:
        return jsonify(state)
    else:
        abort(404, description="Area code not found")


if __name__ == '__main__':
    app.run(debug=True)
