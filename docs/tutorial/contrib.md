**ZgRoBot** 可以作为独立服务运行，也可以集成在其他 **Web** 框架中一同运行。

先写好你的机器人

```py title="robot.py"
from zgrobot import ZgRoBot

myrobot = ZgRoBot(token='token')

@myrobot.handler
def hello():
    return "Hello World"
```

## FastApi
**ZgRoBot** 支持 **fastapi 0.78+**

然后创建最简单的 **FastApi** 项目 ``main.py``

```py title="main.py"
from zgrobot.contrib.fastapi import make_view
from fastapi import FastAPI

from robot import myrobot

app = FastAPI()

app.add_route("/", make_view(robot=robot), methods=["GET", "POST"])
```

或者使用 **FastApi** 的中间件
```py title="main.py"
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

from robot import myrobot

app = FastAPI()

app.mount("/", WSGIMiddleware(myrobot.wsgi))
```

## Django
**ZgRoBot** 支持 **Django 2.2+** 

在你 **Django** 项目中的 ``urls.py`` 中调用 `make_view`，将 **ZgRoBot** 集成进 **Django** 

```py title="main.py"
from django.conf.urls import patterns, include, url
from zgrobot.contrib.django import make_view
from robot import myrobot

urlpatterns = patterns('',
    url(r'^robot/', make_view(myrobot)),
)
```

## Flask
在 **Flask** 项目中为 **Flask** 实例集成 **ZgRoBot**

```py title="main.py"
from flask import Flask
from robot import myrobot
from zgrobot.contrib.flask import make_view

app = Flask(__name__)
app.add_url_rule(
    rule='/robot', # ZgRoBot 挂载地址
    endpoint='zgrobot', # Flask 的 endpoint
    view_func=make_view(myrobot),
    methods=['GET', 'POST']
)
```

## Bottle
在你的 **Bottle** App 中集成 **ZgRoBot**

```py title="main.py"
from bottle import Bottle
from zgrobot.contrib.bottle import make_view
from robot import myrobot

app = Bottle()
app.route(
    '/robot',  # ZgRoBot 挂载地址
    ['GET', 'POST'],
    make_view(myrobot)
)
```

## Tornado
最简单的 Hello World

```py title="main.py"
import tornado.ioloop
import tornado.web
from zgrobot.contrib.tornado import make_handler
from robot import myrobot

application = tornado.web.Application([
    (r"/robot/", make_handler(myrobot)),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
```

