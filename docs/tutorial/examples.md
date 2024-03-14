## HelloWorld
```py title="helloworld.py"
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
```

## 关注回复
```py title="fork.py"
import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')

# 关注回复
@robot.subscribe
def subscribe_reply(message):
    return "感谢这位小可爱的关注~"

robot.run()
```

## 快速回复图片
```py title="image.py"
import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')

# 图片回复，回复原图片
@robot.image
def img_reply(message):
    return ImageReply(message=message, media_id=message.media_id)

robot.run()
```

## 关键词回复
```py title="keyword.py"
import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')

# 关键词回复
@robot.filter("你好呀")
def key_reply(message):
    return "你也好呀"

robot.run()
```

## 多次回复
```py title="keyword.py"
import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')
my_client = robot.client

# 多次回复
@robot.filter("多次回复")
def reply_again(message):
    kf_account = my_client.get_custom_service_account_list().get("kf_list")
    my_client.send_text_message(user_id=message.source, content="这是客服发的消息", kf_account=kf_account)
    return "这是第二次回复哦"

robot.run()
```

## 导入其他文件
如果你为了保证你的 ``bot.py`` （或者其他）文件的干净整洁，或者不想将所有的功能都写到一个文件里面，那么就可以将其他的功能写到其他的文件内，只在执行文件内进行机器人的创建、配置和功能的导入，你可以向下面一样：

```py title="bot.py"
import zgrobot
import menu

robot = zgrobot.ZgRoBot(token='tokenhere')
my_client = robot.client

menu.create_menu(robot, my_client)

robot.run()
```

```py title="menut.py"
import zgrobot
from zgrobot.client import Client


def create_menu(robot: zgrobot.ZgRoBot, client: Client):
    client.create_menu({
        "button": [
            {
                "type": "miniprogram",
                "name": "打卡",
                "url": "https://www.dengtadaka.com/website/index.html",
                "appid": "wxf3ca7ea27608450c",
                "pagepath": "/pages/supervise/groupDetail?id=10025"
            },
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
```
