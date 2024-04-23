from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# 1. debug模式：
# 热加载，修改代码之后保存就可以重新加载
# 如果开发的时候出现bug，如果开发了debug模式，在浏览器上就可以看到出错信息
# app -> Edit Configurations -> FLASK_DEBUG True
# app.run(debug=True)

# 2. 修改host
# 主要的作用：让其他电脑能访问到我的项目
# app -> Edit Configurations -> Additional options --host=0.0.0.0 --port=8000
# app.run(host='0.0.0.0')

# 3.修改port端口号
# app -> Edit Configurations -> Additional options --port=8000
# app.run(port=8000)

if __name__ == '__main__':
    app.run()
