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

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # varchar, null=0
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    user_articles = db.relationship("Article", back_populates="author")

# user = User(username="法外狂徒", password='123654')
# sql: insert user(username, password) values('法外狂徒', '123654');

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # 添加作者的外键
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # backref: 会自动给User模型添加一个articles的属性，用来获取文章列表
    author = db.relationship("User", back_populates="user_articles")

article = Article(title="Flask学习大纲", content="Flaskxxxx")
# articel.author_id = user.id
# user = User.query.get(articel.author_id)
# articel.author = User.query.get(articel.author_id)
# print(articel.author)
# sqlalchemy/flask

with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/add')
def add_user():
    # 1. 创建ORM对象
    user = User(username="法外狂徒", password='123654')
    # 2. 将ORM对象添加到db.session中
    db.session.add(user)
    # 3. 将db.session中的改变同步到数据中
    db.session.commit()
    return "用户创建成功"

@app.route('/user/query')
def query_user():
    # 1. get查找
    # user = User.query.get(1)
    # print(f'{user.id}: {user.username}-{user.password}')
    # 2. filter_by查找
    # Query: 类数组
    users = User.query.filter_by(username="法外狂徒")
    for user in users:
        print(user.username)
    return "数据查找成功"

@app.route('/user/update')
def update_user():
    user = User.query.filter_by(username="法外狂徒").first()
    user.password = "23232303"
    db.session.commit()
    return "数据修改成功"

@app.route('/user/delete')
def delete_user():
    # 1. 查找
    user = User.query.get(1)
    # 2. 删除
    db.session.delete(user)
    # 3. 将db.session中的修改同步到数据库中
    db.session.commit()
    return "数据删除成功"

if __name__ == '__main__':
    app.run()