与其他 Web 框架集成
===================

**ZgRoBot** 可以作为独立服务运行，也可以集成在其他 **Web** 框架中一同运行。

Django
--------
**ZgRoBot** 支持 **Django 2.2+** 。

首先，在一个文件中写好你的微信机器人 ::

    # Filename: robot.py

    from zgrobot import ZgRoBot

    myrobot = ZgRoBot(token='token')


    @myrobot.handler
    def hello(message):
        return 'Hello World!'

然后，在你 **Django** 项目中的 ``urls.py`` 中调用 :func:`zgrobot.contrib.django.make_view` ，将 **ZgRoBot** 集成进 **Django** ::

    from django.conf.urls import patterns, include, url
    from zgrobot.contrib.django import make_view
    from robot import myrobot

    urlpatterns = patterns('',
        url(r'^robot/', make_view(myrobot)),
    )

.. module:: zgrobot.contrib.django
.. autofunction:: make_view

Flask
----------
首先, 同样在文件中写好你的微信机器人 ::

    # Filename: robot.py

    from zgrobot import ZgRoBot

    myrobot = ZgRoBot(token='token')


    @myrobot.handler
    def hello(message):
        return 'Hello World!'

然后, 在 **Flask** 项目中为 **Flask** 实例集成 **ZgRoBot** ::

    from flask import Flask
    from robot import myrobot
    from zgrobot.contrib.flask import make_view

    app = Flask(__name__)
    app.add_url_rule(rule='/robot/', # ZgRoBot 挂载地址
                     endpoint='zgrobot', # Flask 的 endpoint
                     view_func=make_view(myrobot),
                     methods=['GET', 'POST'])

.. module:: zgrobot.contrib.flask
.. autofunction:: make_view


Bottle
--------
在你的 Bottle App 中集成 ZgRoBot ::

    from zgrobot import ZgRoBot

    myrobot = ZgRoBot(token='token')

    @myrobot.handler
    def hello(message):
        return 'Hello World!'

    from bottle import Bottle
    from zgrobot.contrib.bottle import make_view

    app = Bottle()
    app.route('/robot',  # ZgRoBot 挂载地址
             ['GET', 'POST'],
             make_view(myrobot))

.. module:: zgrobot.contrib.bottle
.. autofunction:: make_view

Tornado
----------
最简单的 Hello World ::

    import tornado.ioloop
    import tornado.web
    from zgrobot import ZgRoBot
    from zgrobot.contrib.tornado import make_handler

    myrobot = ZgRoBot(token='token')


    @myrobot.handler
    def hello(message):
        return 'Hello World!'

    application = tornado.web.Application([
        (r"/robot/", make_handler(myrobot)),
    ])

    if __name__ == "__main__":
        application.listen(8888)
        tornado.ioloop.IOLoop.instance().start()

.. module:: zgrobot.contrib.tornado
.. autofunction:: make_handler
