import zgrobot
from zgrobot.client import Client
from zgrobot.replies import ImageReply, VoiceReply

# 导入自己的配置
import local_config

robot = zgrobot.ZgRoBot(config=local_config.config)
my_client = Client(config=local_config.config)


# 获取音频
@robot.filter("音乐")
def music_reply(message):
    with open("./media/track1.mp3", "rb") as f:
        media_id = my_client.upload_media(media_type="voice", media_file=f)["media_id"]
    return VoiceReply(message=message, media_id=media_id)



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
