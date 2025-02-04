from app import db
from app.models.course import Course
from app.utils.response import ApiException
from sqlalchemy import or_
import logging

class CourseService:
    @staticmethod
    def get_all_courses(search_params=None):
        try:
            query = Course.query
            
            if search_params:
                filters = []
                if search_params.get('Cno'):
                    filters.append(Course.Cno.like(f"%{search_params['Cno']}%"))
                if search_params.get('Cname'):
                    filters.append(Course.Cname.like(f"%{search_params['Cname']}%"))
                if search_params.get('Tno'):
                    filters.append(Course.Tno.like(f"%{search_params['Tno']}%"))
                
                if filters:
                    query = query.filter(or_(*filters))
            
            courses = query.all()
            return [course.to_dict() for course in courses]
        except Exception as e:
            logging.error(f"Error in get_all_courses: {str(e)}")
            raise ApiException(f"Failed to get courses: {str(e)}", 500)
    
    @staticmethod
    def get_course_by_id(cno):
        try:
            course = Course.query.get(cno)
            if not course:
                raise ApiException("Course not found", 404)
            return course
        except Exception as e:
            logging.error(f"Error in get_course_by_id: {str(e)}")
            raise ApiException(f"Failed to get course: {str(e)}", 500)
    
    @staticmethod
    def create_course(data):
        try:
            # 验证必填字段
            required_fields = ['Cno', 'Cname', 'Chours', 'Credit', 'Tno']
            for field in required_fields:
                if field not in data or not data[field]:
                    raise ApiException(f"Missing required field: {field}", 400)
            
            # 检查课程编号是否已存在
            existing_course = Course.query.get(data['Cno'])
            if existing_course:
                raise ApiException("Course number already exists", 400)
            
            course = Course(
                Cno=data['Cno'],
                Cname=data['Cname'],
                Chours=data['Chours'],
                Credit=float(data['Credit']),
                Tno=data['Tno'],
                StudentCount=int(data.get('StudentCount', 0))
            )
            
            db.session.add(course)
            db.session.commit()
            return course
        except ApiException:
            db.session.rollback()
            raise
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error in create_course: {str(e)}")
            raise ApiException(f"Failed to create course: {str(e)}", 500)
    
    @staticmethod
    def update_course(cno, data):
        try:
            course = CourseService.get_course_by_id(cno)
            
            # 更新字段
            if 'Cname' in data:
                course.Cname = data['Cname']
            if 'Chours' in data:
                course.Chours = data['Chours']
            if 'Credit' in data:
                course.Credit = float(data['Credit'])
            if 'Tno' in data:
                course.Tno = data['Tno']
            if 'StudentCount' in data:
                course.StudentCount = int(data['StudentCount'])
            
            db.session.commit()
            return course
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error in update_course: {str(e)}")
            raise ApiException(f"Failed to update course: {str(e)}", 500)
    
    @staticmethod
    def delete_course(cno):
        try:
            course = CourseService.get_course_by_id(cno)
            db.session.delete(course)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error in delete_course: {str(e)}")
            raise ApiException(f"Failed to delete course: {str(e)}", 500) 