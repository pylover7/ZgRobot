====================================
ZgRoBot
====================================

.. image:: https://img.shields.io/github/workflow/status/pylover7/ZgRobot/tests?label=tests   :alt: GitHub Workflow Status
.. image:: https://img.shields.io/github/workflow/status/pylover7/ZgRobot/Lint?label=lint   :alt: GitHub Workflow Status
.. image:: https://img.shields.io/github/downloads/pylover7/ZgRobot/total   :alt: GitHub all releases

.. image:: https://codecov.io/gh/pylover7/ZgRobot/branch/master/graph/badge.svg?token=JGB56KZ6CU
    :target: https://codecov.io/gh/pylover7/ZgRobot

.. image:: https://img.shields.io/github/stars/pylover7/ZgRobot?style=social   :alt: GitHub Repo stars
.. image:: https://img.shields.io/github/v/release/pylover7/ZgRobot?include_prereleases   :alt: GitHub release (latest by date including pre-releases)
.. image:: https://img.shields.io/github/v/tag/pylover7/ZgRobot   :alt: GitHub tag (latest by date)
.. image:: https://img.shields.io/pypi/pyversions/pip   :alt: PyPI - Python Version
.. image:: https://img.shields.io/github/commit-activity/m/pylover7/ZgRobot   :alt: GitHub commit activity
.. image:: https://img.shields.io/github/last-commit/pylover7/ZgRobot   :alt: GitHub last commit

.. image:: https://img.shields.io/github/issues/pylover7/ZgRobot   :alt: GitHub issues
.. image:: https://img.shields.io/github/issues-closed/pylover7/ZgRobot   :alt: GitHub closed issues
.. image:: https://img.shields.io/github/issues-pr/pylover7/ZgRobot   :alt: GitHub pull requests
.. image:: https://img.shields.io/github/issues-pr-closed/pylover7/ZgRobot   :alt: GitHub closed pull requests


.. image:: https://img.shields.io/github/license/pylover7/ZgRobot
    :alt: GitHub

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
