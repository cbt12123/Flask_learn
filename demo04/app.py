from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# MYSQL主机名
HOSTNAME = '127.0.0.1'
# MYSQL监听的端口号，默认3306
PORT = 3306
# MYSQL的用户名
USERNAME = 'root'
# MYSQL的密码
PASSWORD = '123456'
# 使用的数据库
DATABASE = 'database_learn'

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

# 在app.config设置好一些数据库的信息
# 然后使用SQLAlchemy(app)创建一个db对象
# 会自动读取app.config中连接数据库的信息

db = SQLAlchemy(app)

# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text("select 1"))
#         print(rs.fetchone())

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()