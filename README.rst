====================================
ZgRoBot
====================================

.. image:: https://img.shields.io/github/workflow/status/pylover7/ZgRobot/tests?label=tests
    :target: https://github.com/pylover7/ZgRobot/actions/workflows/test.yml
.. image:: https://img.shields.io/github/workflow/status/pylover7/ZgRobot/Lint?label=lint
    :target: https://github.com/pylover7/ZgRobot/actions/workflows/lint.yml
.. image:: https://img.shields.io/github/downloads/pylover7/ZgRobot/total
.. image:: https://codecov.io/gh/pylover7/ZgRobot/branch/master/graph/badge.svg?token=JGB56KZ6CU
    :target:  https://codecov.io/gh/pylover7/ZgRobot
.. image:: https://img.shields.io/github/stars/pylover7/ZgRobot?style=social
.. image:: https://img.shields.io/pypi/pyversions/pip
.. image:: https://img.shields.io/github/commit-activity/m/pylover7/ZgRobot
.. image:: https://img.shields.io/github/license/pylover7/ZgRobot
    :alt: GitHub

ZgRoBot 是一个微信公众号开发框架，采用MIT协议发布。

文档在这里： https://zgrobot.readthedocs.io/zh/stable/

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

.. |occontributorimage| image:: https://opencollective.com/werobot/contributors.svg?width=890&button=false
    :target: https://opencollective.com/werobot
    :alt: Repo Contributors
