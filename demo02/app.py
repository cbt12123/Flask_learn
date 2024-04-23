from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

def datetime_formate(value, format="%Y-%d-%m %H:%M"):
    return value.strftime(format)

app.add_template_filter(datetime_formate, "dformat")

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

@app.route('/')
def hello_world():  # put application's code here
    user = User(username="Noah", email="1318053457@qq.com")
    person = {
        "username": "张三",
        "email": "zhangsan@qq.com"
    }
    return render_template("index.html", user=user, person=person)

@app.route('/profile')
def profile():
    return "我是个人中心！"

# 带参数的URL
@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    return render_template("blog_detail.html", blog_id=blog_id, username="Noah")

@app.route('/filter')
def filter_demo():
    user = User(username="aa", email="xx@qq.com")
    mytime = datetime.now()
    return render_template("filter.html", user=user, mytime=mytime)

@app.route('/control')
def control_statement():
    age = 17
    books = [{
        "name": "三国演义",
        "author": "罗贯中"
    },
    {
        "name": "水浒传",
        "author": "施耐庵"
    }
    ]
    return render_template("control.html", age=age, books=books)

@app.route("/child1")
def child1():
    return render_template("child1.html")

@app.route("/child2")
def child2():
    return render_template("child2.html")

@app.route('/blog/list')
def book_list():
    # request.args 类字典类型
    page = request.args.get("page", default=1, type=int)
    return f"您获取的是第{page}的图书列表！"
if __name__ == '__main__':
    app.run(debug=True)
