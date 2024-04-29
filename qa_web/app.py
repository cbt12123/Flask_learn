from flask import Flask
import config
from exts import db
from models import UserModule
from api.qa import bp as qa_bp
from api.auth import bp as auth_bp
from flask_migrate import Migrate

app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)

# blueprint：用来做模块化
# 电影，读书，音乐，xxx


if __name__ == '__main__':
    app.run()