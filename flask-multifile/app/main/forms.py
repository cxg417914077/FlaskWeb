# 创建一个form表单
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
    name = StringField('请输入你的名字（必须为英文）', validators=[Required()])
    submit = SubmitField('登录')
