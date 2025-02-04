from app import db
from app.models.student import Student
from app.utils.response import ApiException
from sqlalchemy import or_
import logging

class StudentService:
    @staticmethod
    def get_all_students(search_params=None):
        try:
            query = Student.query
            
            if search_params:
                filters = []
                if search_params.get('Sno'):
                    filters.append(Student.Sno.like(f"%{search_params['Sno']}%"))
                if search_params.get('Sname'):
                    filters.append(Student.Sname.like(f"%{search_params['Sname']}%"))
                if search_params.get('Dno'):
                    filters.append(Student.Dno.like(f"%{search_params['Dno']}%"))
                
                if filters:
                    query = query.filter(or_(*filters))
            
            students = query.all()
            logging.info(f"Found {len(students)} students")
            return [student.to_dict() for student in students]
        except Exception as e:
            logging.error(f"Error in get_all_students: {str(e)}")
            raise ApiException(f"Failed to get students: {str(e)}", 500)
    
    @staticmethod
    def get_student_by_id(sno):
        try:
            student = Student.query.get(sno)
            if not student:
                raise ApiException("Student not found", 404)
            return student
        except ApiException:
            raise
        except Exception as e:
            logging.error(f"Error in get_student_by_id: {str(e)}")
            raise ApiException(f"Failed to get student: {str(e)}", 500)
    
    @staticmethod
    def create_student(data):
        try:
            # 验证必填字段
            required_fields = ['Sno', 'Sname', 'Ssex', 'Sage', 'Dno']
            for field in required_fields:
                if field not in data or not data[field]:
                    raise ApiException(f"Missing required field: {field}", 400)
            
            # 检查学号是否已存在
            existing_student = Student.query.get(data['Sno'])
            if existing_student:
                raise ApiException("Student number already exists", 400)
            
            student = Student(**data)
            db.session.add(student)
            db.session.commit()
            logging.info(f"Created student with Sno: {student.Sno}")
            return student
        except ApiException:
            db.session.rollback()
            raise
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error in create_student: {str(e)}")
            raise ApiException(f"Failed to create student: {str(e)}", 500)
    
    @staticmethod
    def update_student(sno, data):
        try:
            student = StudentService.get_student_by_id(sno)
            
            # 更新字段
            for key, value in data.items():
                if hasattr(student, key):
                    setattr(student, key, value)
            
            db.session.commit()
            logging.info(f"Updated student with Sno: {sno}")
            return student
        except ApiException:
            db.session.rollback()
            raise
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error in update_student: {str(e)}")
            raise ApiException(f"Failed to update student: {str(e)}", 500)
    
    @staticmethod
    def delete_student(sno):
        try:
            student = StudentService.get_student_by_id(sno)
            db.session.delete(student)
            db.session.commit()
            logging.info(f"Deleted student with Sno: {sno}")
        except ApiException:
            db.session.rollback()
            raise
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error in delete_student: {str(e)}")
            raise ApiException(f"Failed to delete student: {str(e)}", 500) 