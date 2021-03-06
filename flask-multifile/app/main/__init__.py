# 创建蓝本
from flask import Blueprint

main = Blueprint('main', __name__)          # 实例化，创建蓝本，指定蓝本名字和所在的包和模块

from . import views, errors
from ..models import Permission

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
