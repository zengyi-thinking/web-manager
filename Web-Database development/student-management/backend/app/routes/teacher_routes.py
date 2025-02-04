from flask import Blueprint, request
from app.services.teacher_service import TeacherService
from app.utils.response import success_response, error_response, ApiException

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers', methods=['GET'])
def get_teachers():
    try:
        # 获取搜索参数
        search_params = {}
        if request.args.get('Tno'):
            search_params['Tno'] = request.args.get('Tno')
        if request.args.get('Tname'):
            search_params['Tname'] = request.args.get('Tname')
        if request.args.get('Dno'):
            search_params['Dno'] = request.args.get('Dno')
        
        teachers = TeacherService.get_all_teachers(search_params)
        return success_response({
            'items': teachers,
            'total': len(teachers)
        })
    except ApiException as e:
        return error_response(e.message, e.status_code)
    except Exception as e:
        return error_response(str(e), 500)

@teacher_bp.route('/teachers/<tno>', methods=['GET'])
def get_teacher(tno):
    try:
        teacher = TeacherService.get_teacher_by_id(tno)
        return success_response(teacher.to_dict())
    except ApiException as e:
        return error_response(e.message, e.status_code)
    except Exception as e:
        return error_response(str(e), 500)

@teacher_bp.route('/teachers', methods=['POST'])
def add_teacher():
    try:
        data = request.json
        teacher = TeacherService.create_teacher(data)
        return success_response(teacher.to_dict(), 201)
    except ApiException as e:
        return error_response(e.message, e.status_code)
    except Exception as e:
        return error_response(str(e), 500)

@teacher_bp.route('/teachers/<tno>', methods=['PUT'])
def update_teacher(tno):
    try:
        data = request.json
        teacher = TeacherService.update_teacher(tno, data)
        return success_response(teacher.to_dict())
    except ApiException as e:
        return error_response(e.message, e.status_code)
    except Exception as e:
        return error_response(str(e), 500)

@teacher_bp.route('/teachers/<tno>', methods=['DELETE'])
def delete_teacher(tno):
    try:
        TeacherService.delete_teacher(tno)
        return success_response(message="Teacher deleted successfully")
    except ApiException as e:
        return error_response(e.message, e.status_code)
    except Exception as e:
        return error_response(str(e), 500) 