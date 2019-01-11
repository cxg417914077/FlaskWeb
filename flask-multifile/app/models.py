from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import current_app
from flask_login import UserMixin
from . import login_manager


class Role(db.Model):
    __tablename__ = 'roles'                                             # 表名
    id = db.Column(db.Integer, primary_key=True)                        # 主键字段， Integer型
    name = db.Column(db.String(64), unique=True)                        # name字段， String型，唯一不能重复
    users = db.relationship('User', backref='role', lazy='dynamic')     # 表与表之间的关系，Uesr为与之有关系的表backref添加反向关系

    def __repr__(self):                                                 # 返回一个可读性字符串表示模型，print(Role)时显示的内容
        return '<Role %s>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))          # 外键  存储的为表roles的主键id
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)
    confirmed = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def __repr__(self):
        return '<User %s>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
