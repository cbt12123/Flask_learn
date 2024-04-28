from flask import Flask
import config
from exts import db
from models import UserModule

app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)

db.init_app(app)

@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run()