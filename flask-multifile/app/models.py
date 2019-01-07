from . import db


class Role(db.Model):
    __tablename__ = 'roles'                                             # 表名
    id = db.Column(db.Integer, primary_key=True)                        # 主键字段， Integer型
    name = db.Column(db.String(64), unique=True)                        # name字段， String型，唯一不能重复
    users = db.relationship('User', backref='role', lazy='dynamic')     # 表与表之间的关系，Uesr为与之有关系的表backref添加反向关系

    def __repr__(self):                                                 # 返回一个可读性字符串表示模型，print(Role)时显示的内容
        return '<Role %s>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))          # 外键  存储的为表roles的主键id

    def __repr__(self):
        return '<User %s>' % self.username
