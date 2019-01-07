from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config


# 对扩展类实例化
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)                               # 创建一个程序实例
    app.config.from_object(config[config_name])         # 选择环境配置(开发、测试、生产)
    config[config_name].init_app(app)

    bootstrap.init_app(app)                             # 扩展实例对程序实例app进行包装
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
