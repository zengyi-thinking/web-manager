from app import db

class Course(db.Model):
    __tablename__ = 'Course'
    
    # 课程编号
    Cno = db.Column(db.String(20), primary_key=True)
    # 课程名称
    Cname = db.Column(db.String(50), nullable=False)
    # 学时
    Chours = db.Column(db.String(10), nullable=False)
    # 学分
    Credit = db.Column(db.Float, nullable=False)
    # 教师编号
    Tno = db.Column(db.String(20), db.ForeignKey('Teacher.Tno', ondelete='SET NULL'), nullable=True)
    # 选课人数
    StudentCount = db.Column(db.Integer, default=0)
    
    def to_dict(self):
        return {
            'Cno': self.Cno,
            'Cname': self.Cname,
            'Chours': self.Chours,
            'Credit': self.Credit,
            'Tno': self.Tno,
            'StudentCount': self.StudentCount,
            'teacher_name': self.teacher.Tname if self.teacher else None
        } 