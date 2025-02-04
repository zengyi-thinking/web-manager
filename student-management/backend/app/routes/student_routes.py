from flask import Blueprint, request, jsonify
from app.services.student_service import StudentService
from app.utils.response import success_response, error_response, ApiException
import logging

student_bp = Blueprint('student', __name__)

@student_bp.route('/students', methods=['GET'])
def get_students():
    try:
        logging.info("Received request to get students")
        logging.info(f"Query parameters: {request.args}")
        
        # 获取搜索参数
        search_params = {}
        if request.args.get('Sno'):
            search_params['Sno'] = request.args.get('Sno')
        if request.args.get('Sname'):
            search_params['Sname'] = request.args.get('Sname')
        if request.args.get('Dno'):
            search_params['Dno'] = request.args.get('Dno')
        
        students = StudentService.get_all_students(search_params)
        logging.info(f"Successfully retrieved {len(students)} students")
        
        response = success_response({
            'items': students,
            'total': len(students)
        })
        logging.info(f"Sending response: {response}")
        return response
        
    except Exception as e:
        logging.error(f"Error in get_students: {str(e)}", exc_info=True)
        return error_response(str(e), 500)

@student_bp.route('/students/<sno>', methods=['GET'])
def get_student(sno):
    try:
        student = StudentService.get_student_by_id(sno)
        return success_response(student.to_dict())
    except ApiException as e:
        return error_response(e.message, e.status_code)
    except Exception as e:
        logging.error(f"Error in get_student: {str(e)}", exc_info=True)
        return error_response(str(e), 500)

@student_bp.route('/students/search', methods=['GET'])
def search_students():
    try:
        name = request.args.get('name', '')
        major = request.args.get('major', '')
        grade = request.args.get('grade', '')
        
        students = StudentService.search_students(name, major, grade)
        return success_response(students)
    except ApiException as e:
        return error_response(e.message, e.status_code)
    except Exception as e:
        return error_response(str(e), 500)

@student_bp.route('/students', methods=['POST'])
def add_student():
    try:
        logging.info(f"Received request to add student: {request.json}")
        data = request.json
        student = StudentService.create_student(data)
        return success_response(student.to_dict(), 201)
    except ApiException as e:
        return error_response(e.message, e.status_code)
    except Exception as e:
        logging.error(f"Error in add_student: {str(e)}", exc_info=True)
        return error_response(str(e), 500)

@student_bp.route('/students/<sno>', methods=['PUT'])
def update_student(sno):
    try:
        logging.info(f"Received request to update student {sno}: {request.json}")
        data = request.json
        student = StudentService.update_student(sno, data)
        return success_response(student.to_dict())
    except ApiException as e:
        return error_response(e.message, e.status_code)
    except Exception as e:
        logging.error(f"Error in update_student: {str(e)}", exc_info=True)
        return error_response(str(e), 500)

@student_bp.route('/students/<sno>', methods=['DELETE'])
def delete_student(sno):
    try:
        logging.info(f"Received request to delete student: {sno}")
        StudentService.delete_student(sno)
        return success_response(message="Student deleted successfully")
    except ApiException as e:
        return error_response(e.message, e.status_code)
    except Exception as e:
        logging.error(f"Error in delete_student: {str(e)}", exc_info=True)
        return error_response(str(e), 500)

@student_bp.route('/students/batch', methods=['DELETE'])
def batch_delete_students():
    try:
        student_ids = request.json.get('student_ids', [])
        StudentService.batch_delete_students(student_ids)
        return success_response(message="Students deleted successfully")
    except ApiException as e:
        return error_response(e.message, e.status_code)
    except Exception as e:
        return error_response(str(e), 500) 