# 创建一个form表单
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('保持登录')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64), Email()])
    username  = StringField('用户名', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                      'Username must have only letters, '
                                                                                      'number, dots or underscores')])
    password = PasswordField('密码', validators=[Required(), EqualTo('password2', message='Password must match.')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册')

    def validate_name(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[Required()])
    password = PasswordField('新密码', validators=[
        Required(), EqualTo('password2', message='两次密码必需一致')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('更改密码')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64), Email()])
    submit = SubmitField('重置密码')


class PasswordResetForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('新密码', validators=[
        Required(), EqualTo('password2', message='两次密码必需一致')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('重置密码')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('邮箱不存在')


class ChangeEmailForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[Required()])
    submit = SubmitField('修改邮箱')

    def validate_email(self, firld):
        if User.query.filter_by(email=firld.data).first():
            raise ValidationError('邮箱已被注册')
