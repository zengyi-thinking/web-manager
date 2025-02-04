from app import db

class Student(db.Model):
    __tablename__ = 'Student'
    
    # 学号
    Sno = db.Column(db.String(20), primary_key=True)
    # 姓名
    Sname = db.Column(db.String(20), nullable=False)
    # 性别
    Ssex = db.Column(db.String(20), nullable=False)
    # 年龄
    Sage = db.Column(db.Integer, nullable=False)
    # 所属院系
    Dno = db.Column(db.String(20), nullable=False)
    # 班级
    Sclass = db.Column(db.String(20))
    # 家庭住址
    address = db.Column(db.String(255))

    def to_dict(self):
        return {
            'Sno': self.Sno,
            'Sname': self.Sname,
            'Ssex': self.Ssex,
            'Sage': self.Sage,
            'Dno': self.Dno,
            'Sclass': self.Sclass,
            'address': self.address
        } 