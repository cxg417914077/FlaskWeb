# 创建一个form表单
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
    name = StringField("你叫什么名字?", validators=[Required()])        # 该项为必填项
    submit = SubmitField('提交')
