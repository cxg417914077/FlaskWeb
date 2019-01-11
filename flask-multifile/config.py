# 配置文件
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KET') or 'hard to guess string'     # CSRF通用秘钥
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True                                    # SQLAlchemy自动commit
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'                                 # 邮件主题前缀
    FLASKY_MAIL_SENDER = 'Flasky Admin <cxg417914077@163.com>'              # 邮件发件人的信息和地址  地址要用<>括起来
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')                           # 从环境变量中获取邮件接收人

    @staticmethod
    def init_app(app):
        pass


# 开发环境配置
class DevelopmentConfig(Config):
    DEBUG = True                                                            # 调试模式
    MAIL_SERVER = 'smtp.163.com'                                            # 邮箱服务器
    MAIL_PORT = 25                                                         # 邮箱端口
    MAIL_USE_TLS = False                                                    # 关闭TLS安全协议
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')                         # 从环境变量获取邮件发件人账号
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')                         # 从环境变量获取邮件发件人密码(动态口令)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')         # 从环境变量获取数据库的地址或使用默认的


# 测试环境配置
class TestingConfig(Config):
    TESTING = True                                                          # 测试模式
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'data-text.sqlite')


# 生产环境配置
class ProdectionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join('data.sqlite')

config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'prodection': ProdectionConfig,


        'default': DevelopmentConfig
        }
