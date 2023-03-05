import zgrobot
from zgrobot.client import Client


def create_menu(robot: zgrobot.ZgRoBot, client: Client):
    client.create_menu({
        "button": [
            {
                "type": "view",
                "name": "主页",
                "url": "https://mp.weixin.qq.com/s?__biz=Mzg3NzU1MjgxOA==&mid=100002639&idx=1&sn"
                       "=3d7e9959038e0a3d01fa3f76ba715200&chksm"
                       "=4f207e927857f78482f85af737e719c3eef35afcba6e58510bc65a6296284c2999fda51babf0#rd "
            },
            {
                "type": "click",
                "name": "帮助",
                "key": "help"
            }]
    })

    @robot.key_click("help")
    def music():
        return "现在还没有什么帮助哦~"
