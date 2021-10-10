====================================
ZgRoBot
====================================

.. image:: https://github.com/pylover7/zgrobot/workflows/tests/badge.svg
    :target: https://github.com/pylover7/zgrobot/actions
.. image:: https://codecov.io/gh/pylover7/ZgRoBot/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/pylover7/ZgRoBot

ZgRoBot 是一个微信公众号开发框架，采用MIT协议发布。

文档在这里： https://zgrobot.readthedocs.org/zh_CN/latest/

安装
========

推荐使用 pip 进行安装 ::

    pip install zgrobot

Hello World
=============

一个非常简单的 Hello World 微信公众号，会对收到的所有文本消息回复 Hello World ::

    import zgrobot

    robot = zgrobot.ZgRoBot(token='tokenhere')

    @robot.text
    def hello_world():
        return 'Hello World!'

    robot.run()
    
Credits 
=======
Contributors
-----------------
Thank you to all the people who have already contributed. 
|occontributorimage|

.. |occontributorimage| image:: https://opencollective.com/zgrobot/contributors.svg?width=890&button=false
    :target: https://opencollective.com/zgrobot
    :alt: Repo Contributors
