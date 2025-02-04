from flask import jsonify

class ApiException(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

def success_response(data=None, message="Success", status_code=200):
    response = {
        "code": status_code,
        "message": message,
        "data": data
    }
    return jsonify(response)

def error_response(message, status_code=400):
    return jsonify({
        "code": status_code,
        "message": message,
        "data": None
    }), status_code 