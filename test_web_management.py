# test_web_management.py
import unittest
from app import create_app
from flask_sqlalchemy import SQLAlchemy
import json

class SystemTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app({
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'mysql+mysqlconnector://root:@localhost/test_student_mgmt',
            'SQLALCHEMY_TRACK_MODIFICATIONS': False
        })
        self.client = self.app.test_client()
        with self.app.app_context():
            db = SQLAlchemy()
            db.init_app(self.app)
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db = SQLAlchemy()
            db.drop_all()

    def test_student_crud_flow(self):
        """测试学生管理全流程"""
        # 创建学生
        response = self.client.post('/api/students', json={
            'sno': '20230001',
            'sname': '张三',
            'ssex': '男',
            'sage': 20,
            'sdept': '计算机学院'
        })
        self.assertEqual(response.status_code, 201)

        # 查询学生
        response = self.client.get('/api/students/20230001')
        self.assertIn('计算机学院', response.get_data(as_text=True))

        # 更新学生
        response = self.client.put('/api/students/20230001', json={
            'saddress': '海淀区'
        })
        self.assertEqual(response.status_code, 200)

        # 删除学生
        response = self.client.delete('/api/students/20230001')
        self.assertEqual(response.status_code, 204)

    def test_course_management(self):
        """测试课程管理功能"""
        # 创建课程
        response = self.client.post('/api/courses', json={
            'cno': 'CS101',
            'cname': '数据结构',
            'ccredit': 4.0
        })
        self.assertEqual(response.status_code, 201)

        # 获取课程列表
        response = self.client.get('/api/courses')
        data = json.loads(response.data)
        self.assertGreaterEqual(len(data), 1)

    def test_error_handling(self):
        """测试异常处理机制"""
        # 无效请求测试
        response = self.client.post('/api/students', json={})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()