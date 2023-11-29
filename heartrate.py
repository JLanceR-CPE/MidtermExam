from flask import Flask, jsonify, request
app = Flask(__name__)
heart_data = [
 {
       "heart_id": 1,
       "date": "2023-11-29",
       "heart_rate":75 
    },
    {
        "heart_id": 2,
       "date": "2023-11-29",
       "heart_rate":90 
    }
]
@app.route('/heart', methods=['POST'])
def insert_heart_record():
    try:
        new_record = request.get_json()
        heart_data.append(new_record)
        return jsonify(message='Heart record added successfully'), 201
    except Exception as e:
            return jsonify(message=f'Error: {str(e)}'), 500

@app.route('/heart', methods=['GET'])
def read_all_heart_information():
    return jsonify(heart_data)

@app.route('/heart/<int:heart_id>', methods=['GET'])
def read_heart_information_by_id(heart_id):
    try:
        heart_record = next((record for record in heart_data if record['heart_id'] == heart_id), None)
        return jsonify(heart_record) if heart_record else jsonify(message='Heart record not found'), 404
    except Exception as e:
            return jsonify(message=f'Error: {str(e)}'), 500

@app.route('/heart/<int:heart_id>', methods=['PUT'])
def update_heart_record(heart_id):
    try:
        for i, record in enumerate(heart_data):
            if record['heart_id'] == heart_id: heart_data[i] = request.get_json()
            return jsonify(message='Heart record updated successfully')
            return jsonify(message='Heart record not found'), 404
    except Exception as e:
        return jsonify(message=f'Error: {str(e)}'), 500

@app.route('/heart/<int:heart_id>', methods=['DELETE'])
def delete_heart_record(heart_id):
    try:
        global heart_data
        updated_data = [record for record in heart_data if record['heart_id'] != heart_id]
        if len(updated_data) < len(heart_data):
            heart_data = updated_data
            return jsonify(message='Heart record deleted successfully')
            return jsonify(message='Heart record not found'), 404
    except Exception as e:
        return jsonify(message=f'Error: {str(e)}'), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)