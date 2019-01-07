# 错误处理程序
from flask import render_template
from . import main


# 响应码为404时返回404.html页面
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# 响应码为500时返回500.html页面
@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
