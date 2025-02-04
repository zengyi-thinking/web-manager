from app import db

class Teacher(db.Model):
    __tablename__ = 'Teacher'
    
    # 教师编号
    Tno = db.Column(db.String(20), primary_key=True)
    # 教师姓名
    Tname = db.Column(db.String(20), nullable=False)
    # 所属院系
    Dno = db.Column(db.String(20), nullable=False)
    # 教师薪资
    Salary = db.Column(db.Float, nullable=False)
    # 联系方式
    Tmobile = db.Column(db.String(20))

    # 与课程的关系
    courses = db.relationship('Course', 
                            backref=db.backref('teacher', lazy=True),
                            lazy='dynamic')

    def to_dict(self):
        return {
            'Tno': self.Tno,
            'Tname': self.Tname,
            'Dno': self.Dno,
            'Salary': self.Salary,
            'Tmobile': self.Tmobile
        } 