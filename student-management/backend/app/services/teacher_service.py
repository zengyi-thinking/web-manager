from app import db
from app.models.teacher import Teacher
from app.utils.response import ApiException
from sqlalchemy import or_
import logging

class TeacherService:
    @staticmethod
    def get_all_teachers(search_params=None):
        try:
            query = Teacher.query
            
            if search_params:
                filters = []
                if search_params.get('Tno'):
                    filters.append(Teacher.Tno.like(f"%{search_params['Tno']}%"))
                if search_params.get('Tname'):
                    filters.append(Teacher.Tname.like(f"%{search_params['Tname']}%"))
                if search_params.get('Dno'):
                    filters.append(Teacher.Dno.like(f"%{search_params['Dno']}%"))
                
                if filters:
                    query = query.filter(or_(*filters))
            
            teachers = query.all()
            return [teacher.to_dict() for teacher in teachers]
        except Exception as e:
            logging.error(f"Error in get_all_teachers: {str(e)}")
            raise ApiException(f"Failed to get teachers: {str(e)}", 500)
    
    @staticmethod
    def get_teacher_by_id(tno):
        try:
            teacher = Teacher.query.get(tno)
            if not teacher:
                raise ApiException("Teacher not found", 404)
            return teacher
        except Exception as e:
            logging.error(f"Error in get_teacher_by_id: {str(e)}")
            raise ApiException(f"Failed to get teacher: {str(e)}", 500)
    
    @staticmethod
    def create_teacher(data):
        try:
            # 验证必填字段
            required_fields = ['Tno', 'Tname', 'Dno', 'Salary']
            for field in required_fields:
                if field not in data or not data[field]:
                    raise ApiException(f"Missing required field: {field}", 400)
            
            # 检查教师编号是否已存在
            existing_teacher = Teacher.query.get(data['Tno'])
            if existing_teacher:
                raise ApiException("Teacher number already exists", 400)
            
            teacher = Teacher(
                Tno=data['Tno'],
                Tname=data['Tname'],
                Dno=data['Dno'],
                Salary=float(data['Salary']),
                Tmobile=data.get('Tmobile', '')
            )
            
            db.session.add(teacher)
            db.session.commit()
            return teacher
        except ApiException:
            db.session.rollback()
            raise
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error in create_teacher: {str(e)}")
            raise ApiException(f"Failed to create teacher: {str(e)}", 500)
    
    @staticmethod
    def update_teacher(tno, data):
        try:
            teacher = TeacherService.get_teacher_by_id(tno)
            
            # 更新字段
            if 'Tname' in data:
                teacher.Tname = data['Tname']
            if 'Dno' in data:
                teacher.Dno = data['Dno']
            if 'Salary' in data:
                teacher.Salary = float(data['Salary'])
            if 'Tmobile' in data:
                teacher.Tmobile = data['Tmobile']
            
            db.session.commit()
            return teacher
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error in update_teacher: {str(e)}")
            raise ApiException(f"Failed to update teacher: {str(e)}", 500)
    
    @staticmethod
    def delete_teacher(tno):
        try:
            teacher = TeacherService.get_teacher_by_id(tno)
            db.session.delete(teacher)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error in delete_teacher: {str(e)}")
            raise ApiException(f"Failed to delete teacher: {str(e)}", 500) 