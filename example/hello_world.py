# -*- coding: utf-8 -*-

import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')


@robot.filter("帮助")
def show_help(message):
    return """
    帮助
    XXXXX
    """


@robot.text
def hello_world(message):
    return 'Hello World!'


robot.run()
