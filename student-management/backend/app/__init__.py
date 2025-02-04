from flask import Flask, send_from_directory, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import os
import logging

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_object=None):
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    app = Flask(__name__, 
                static_folder='../../frontend/static',  # 修改静态文件夹路径
                static_url_path='/static',
                template_folder='../../frontend')  # 添加模板文件夹路径
    CORS(app)
    
    # 配置数据库
    if config_object:
        app.config.from_object(config_object)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Zhuqing5201314@localhost/sct'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_ECHO'] = True  # 启用 SQL 语句日志
    
    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 注册蓝图
    from .routes.student_routes import student_bp
    from .routes.teacher_routes import teacher_bp
    from .routes.course_routes import course_bp
    
    app.register_blueprint(student_bp, url_prefix='/api')
    app.register_blueprint(teacher_bp, url_prefix='/api')
    app.register_blueprint(course_bp, url_prefix='/api')
    
    # 创建所有表（如果不存在）
    with app.app_context():
        try:
            # 导入所有模型以确保它们被正确注册
            from .models.student import Student
            from .models.teacher import Teacher
            from .models.course import Course
            
            # 只创建不存在的表
            db.create_all()
            logging.info("Database tables checked/created successfully")
        except Exception as e:
            logging.error(f"Error checking/creating database tables: {str(e)}")
            raise
    
    # 处理HTML页面
    @app.route('/')
    def index():
        return send_from_directory('../../frontend', 'index.html')
    
    @app.route('/teacher.html')
    def teacher():
        return send_from_directory('../../frontend', 'teacher.html')
    
    @app.route('/course.html')
    def course():
        return send_from_directory('../../frontend', 'course.html')
    
    # 处理404错误
    @app.errorhandler(404)
    def not_found(error):
        if request.path.startswith('/hybridaction/'):
            return '', 204  # 返回空响应
        return jsonify({'error': 'Not found'}), 404
    
    return app