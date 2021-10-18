import zgrobot
from zgrobot.client import Client
from zgrobot.replies import ImageReply

# 导入自己的配置
import config

robot = zgrobot.ZgRoBot(config=config.config)
my_client = Client(config=config.config)


# 关注回复
@robot.subscribe
def subscribe_reply(message):
    return "感谢这位小可爱的关注~"


# 导入其他文件，创建菜单
import menu

menu.create_menu(robot, my_client)


# 图片回复，回复原图片
@robot.image
def img_reply(message):
    return ImageReply(message=message, media_id=message.media_id)


# 关键词回复
@robot.filter("你好呀")
def key_reply(message):
    return "你也好呀"


# 多次回复
@robot.filter("多次回复")
def reply_again(message):
    kf_account = my_client.get_custom_service_account_list().get("kf_list")
    my_client.send_text_message(user_id=message.source, content="这是客服发的消息", kf_account=kf_account)
    return "这是第二次回复哦"


if __name__ == '__main__':
    robot.run()
