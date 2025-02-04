from flask import Blueprint, request, jsonify
from app.services.course_service import CourseService
from app.utils.response import success_response, error_response
import logging

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses', methods=['GET'])
def get_courses():
    try:
        search_params = request.args.to_dict()
        courses = CourseService.get_all_courses(search_params)
        return success_response(data={'items': courses})
    except Exception as e:
        logging.error(f"Error in get_courses: {str(e)}")
        return error_response(str(e))

@course_bp.route('/courses/<cno>', methods=['GET'])
def get_course(cno):
    try:
        course = CourseService.get_course_by_id(cno)
        return success_response(data=course.to_dict())
    except Exception as e:
        logging.error(f"Error in get_course: {str(e)}")
        return error_response(str(e))

@course_bp.route('/courses', methods=['POST'])
def create_course():
    try:
        data = request.get_json()
        course = CourseService.create_course(data)
        return success_response(data=course.to_dict(), status_code=201)
    except Exception as e:
        logging.error(f"Error in create_course: {str(e)}")
        return error_response(str(e))

@course_bp.route('/courses/<cno>', methods=['PUT'])
def update_course(cno):
    try:
        data = request.get_json()
        course = CourseService.update_course(cno, data)
        return success_response(data=course.to_dict())
    except Exception as e:
        logging.error(f"Error in update_course: {str(e)}")
        return error_response(str(e))

@course_bp.route('/courses/<cno>', methods=['DELETE'])
def delete_course(cno):
    try:
        CourseService.delete_course(cno)
        return success_response(message='Course deleted successfully')
    except Exception as e:
        logging.error(f"Error in delete_course: {str(e)}")
        return error_response(str(e)) 