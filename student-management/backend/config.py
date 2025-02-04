import os

class Config:
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Zhuqing5201314@localhost/sct'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 应用配置
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')  
    
    # 调试配置
    DEBUG = True