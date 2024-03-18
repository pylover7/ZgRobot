# -*- coding:utf-8 -*-

import hashlib
import os
import time

import pytest

from zgrobot import ZgRoBot
from zgrobot.utils import generate_token, to_text


def _make_xml(content):
    return """
        <xml>
        <ToUserName><![CDATA[toUser]]></ToUserName>
        <FromUserName><![CDATA[fromUser]]></FromUserName>
        <CreateTime>1348831860</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[%s]]></Content>
        <MsgId>1234567890123456</MsgId>
        </xml>
    """ % content


def test_signature_checker():
    token = generate_token()

    robot = ZgRoBot(token, SESSION_STORAGE=False)

    timestamp = str(int(time.time()))
    nonce = '12345678'

    sign = [token, timestamp, nonce]
    sign.sort()
    sign = ''.join(sign)
    sign = sign.encode()
    sign = hashlib.sha1(sign).hexdigest()

    assert robot.check_signature(timestamp, nonce, sign)
    
def test_robot_config():
    robot = ZgRoBot(enable_session=False)
    assert robot.config.get('SESSION_STORAGE') == False
    
    robot = ZgRoBot(session_storage=True)
    assert robot.config.get('SESSION_STORAGE') == True
    
def test_crypto():
    from zgrobot.exceptions import ConfigError
    
    robot = ZgRoBot()
    with pytest.raises(ConfigError):
        robot.crypto()
        
    robot = ZgRoBot(app_id="xxxxxx")
    with pytest.raises(ConfigError):
        robot.crypto()
        
    robot = ZgRoBot(app_id="xxxxxx",
                    encoding_aes_key="eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHg=",
                    token="xxxxxx"
                )
    r = robot.crypto
    assert r.__class__.__name__ == "MessageCrypt"


def test_register_handlers():  # noqa: C901
    robot = ZgRoBot(SESSION_STORAGE=False)

    for type in robot.message_types:
        assert hasattr(robot,
                       type) or hasattr(robot, type.replace('_event', ''))

    @robot.text
    def text_handler():
        return "Hi"

    assert robot._handlers["text"] == [(text_handler, 0)]

    @robot.image
    def image_handler(message):
        return 'nice pic'

    assert robot._handlers["image"] == [(image_handler, 1)]

    assert robot.get_handlers("text") == [(text_handler, 0)]

    @robot.handler
    def handler(message, session):
        pass

    assert robot.get_handlers("text") == [(text_handler, 0), (handler, 2)]

    @robot.video
    def video_handler():
        pass

    assert robot._handlers["video"] == [(video_handler, 0)]
    assert robot.get_handlers("video") == [(video_handler, 0), (handler, 2)]

    @robot.shortvideo
    def shortvideo_handler():
        pass

    assert robot._handlers["shortvideo"] == [(shortvideo_handler, 0)]
    assert robot.get_handlers("shortvideo") == [
        (shortvideo_handler, 0), (handler, 2)
    ]

    @robot.location
    def location_handler():
        pass

    assert robot._handlers["location"] == [(location_handler, 0)]

    @robot.link
    def link_handler():
        pass

    assert robot._handlers["link"] == [(link_handler, 0)]

    @robot.subscribe
    def subscribe_handler():
        pass

    assert robot._handlers["subscribe_event"] == [(subscribe_handler, 0)]

    @robot.unsubscribe
    def unsubscribe_handler():
        pass

    assert robot._handlers["unsubscribe_event"] == [(unsubscribe_handler, 0)]

    @robot.voice
    def voice_handler():
        pass

    assert robot._handlers["voice"] == [(voice_handler, 0)]

    @robot.click
    def click_handler():
        pass

    assert robot._handlers["click_event"] == [(click_handler, 0)]

    @robot.key_click("MENU")
    def menu_handler():
        pass

    assert len(robot._handlers["click_event"]) == 2

    @robot.scan
    def scan_handler():
        pass

    assert robot._handlers["scan_event"] == [(scan_handler, 0)]

    @robot.scancode_push
    def scancode_push_handler():
        pass

    assert robot._handlers["scancode_push_event"] == [
        (scancode_push_handler, 0)
    ]

    @robot.scancode_waitmsg
    def scancode_waitmsg_handler():
        pass

    assert robot._handlers["scancode_waitmsg_event"] == [
        (scancode_waitmsg_handler, 0)
    ]


def test_filter():
    import re
    import zgrobot.testing
    robot = ZgRoBot(SESSION_STORAGE=False)

    @robot.filter("喵")
    def _1():
        return "喵"

    assert len(robot._handlers["text"]) == 1

    @robot.filter(re.compile(to_text(".*?呵呵.*?")))
    def _2():
        return "哼"

    assert len(robot._handlers["text"]) == 2

    @robot.text
    def _3():
        return "汪"

    assert len(robot._handlers["text"]) == 3

    tester = zgrobot.testing.WeTest(robot)

    assert tester.send_xml(_make_xml("啊"))._args['content'] == u"汪"
    assert tester.send_xml(_make_xml("啊呵呵"))._args['content'] == u"哼"
    assert tester.send_xml(_make_xml("喵"))._args['content'] == u"喵"

    try:
        os.remove(os.path.abspath("zgrobot_session"))
    except OSError:
        pass
    robot = ZgRoBot(SESSION_STORAGE=False)

    @robot.filter("帮助", "跪求帮助", re.compile("(.*?)help.*?"))
    def _(message, session, match):
        if match and match.group(1) == u"小姐姐":
            return "本小姐就帮你一下"
        return "就不帮"

    assert len(robot._handlers["text"]) == 3

    @robot.text
    def _4():
        return "哦"

    assert len(robot._handlers["text"]) == 4

    tester = zgrobot.testing.WeTest(robot)

    assert tester.send_xml(_make_xml("啊"))._args['content'] == u"哦"
    assert tester.send_xml(_make_xml("帮助"))._args['content'] == u"就不帮"
    assert tester.send_xml(_make_xml("跪求帮助"))._args['content'] == u"就不帮"
    assert tester.send_xml(_make_xml("ooohelp"))._args['content'] == u"就不帮"
    assert tester.send_xml(_make_xml("小姐姐help")
                           )._args['content'] == u"本小姐就帮你一下"


def test_register_not_callable_object():
    robot = ZgRoBot(SESSION_STORAGE=False)
    with pytest.raises(ValueError):
        robot.add_handler("s")


def test_error_page():
    robot = ZgRoBot()

    @robot.error_page
    def make_error_page(url):
        return url

    assert robot.make_error_page('喵') == '喵'


def test_config_ignore():
    from zgrobot.config import Config
    config = Config(TOKEN="token from config")
    robot = ZgRoBot(config=config, token="token2333")
    assert robot.token == "token from config"


def test_add_filter():
    import zgrobot.testing
    import re

    robot = ZgRoBot()

    def test_register():
        return "test"

    robot.add_filter(test_register, ["test", re.compile(u".*?啦.*?")])

    tester = zgrobot.testing.WeTest(robot)

    assert tester.send_xml(_make_xml("test"))._args["content"] == "test"
    assert tester.send_xml(_make_xml(u"我要测试啦"))._args["content"] == "test"
    assert tester.send_xml(_make_xml(u"我要测试")) is None

    with pytest.raises(ValueError) as e:
        robot.add_filter("test", ["test"])
    assert e.value.args[0] == "test is not callable"

    with pytest.raises(ValueError) as e:
        robot.add_filter(test_register, "test")
    assert e.value.args[0] == "test is not list"

    with pytest.raises(TypeError) as e:
        robot.add_filter(test_register, [["bazinga"]])
    assert e.value.args[0] == "[\'bazinga\'] is not a valid rule"

def test_parse_message():
    from zgrobot.messages.base import ZgRoBotMetaClass
    from zgrobot.utils import get_signature
    from zgrobot.crypto.exceptions import AppIdValidationError
    
    token = "xxxxx"
    timestamp = "xxxxxx"
    nonce = "xxxxxx"
    
    robot = ZgRoBot(app_id="xxxxxx",
                    app_secret="xxxxxx",
                    encoding_aes_key="eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHg=",
                    token=token
                )
    encrypt_msg ="""<xml>
                    <ToUserName></ToUserName>
                    <Encrypt><![CDATA[LDFAmKFr7U/RMmwRbsR676wjym90byw7+hhh226e8bu6KVYy00HheIsVER4eMgz/VBtofSaeXXQBz6fVdkN2CzBUaTtjJeTCXEIDfTBNxpw/QRLGLq
qMZHA3I+JiBxrrSzd2yXuXst7TdkVgY4lZEHQcWk85x1niT79XLaWQog+OnBV31eZbXGPPv8dZciKqGo0meTYi+fkMEJdyS8OE7NjO79vpIyIw7hMBtEXPBK/tJGN5m5SoAS
6I4rRZ8Zl8umKxXqgr7N8ZOs6DB9tokpvSl9wT9T3E62rufaKP5EL1imJUd1pngxy09EP24O8Th4bCrdUcZpJio2l11vE6bWK2s5WrLuO0cKY2GP2unQ4fDxh0L4ePmNOVFJ
wp9Hyvd0BAsleXA4jWeOMw5nH3Vn49/Q/ZAQ2HN3dB0bMA+6KJYLvIzTz/Iz6vEjk8ZkK+AbhW5eldnyRDXP/OWfZH2P3WQZUwc/G/LGmS3ekqMwQThhS2Eg5t4yHv0mAIei
07Lknip8nnwgEeF4R9hOGutE9ETsGG4CP1LHTQ4fgYchOMfB3wANOjIt9xendbhHbu51Z4OKnA0F+MlgZomiqweT1v/+LUxcsFAZ1J+Vtt0FQXElDKg+YyQnRCiLl3I+GJ/c
xSj86XwClZC3NNhAkVU11SvxcXEYh9smckV/qRP2Acsvdls0UqZVWnPtzgx8hc8QBZaeH+JeiaPQD88frNvA==]]></Encrypt>
                    </xml>"""
    signature = "1f90c73385e0ee747446c4656c7ebd71601401c7"
    with pytest.raises(AppIdValidationError):
        r =  robot.parse_message(encrypt_msg, timestamp, nonce, signature)

def test_get_encrypted_reply():
    import time
    from zgrobot.messages.messages import TextMessage
    
    robot = ZgRoBot(app_id="xxxxxx",
                    app_secret="xxxxxx",
                    encoding_aes_key="eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHg=",
                    token="token"
                )
    message = TextMessage({"type": "text", "content": "hello", "source": "xxx", "time": 1234})
    
    r = robot.get_encrypted_reply(message)
    assert r == "success"
    
    @robot.text
    def handle(message):
        return "nihao"
    r = robot.get_encrypted_reply(message)
    assert r == f"""
    <xml>
    <ToUserName><![CDATA[xxx]]></ToUserName>
    <FromUserName><![CDATA[None]]></FromUserName>
    <CreateTime>{int(time.time())}</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[nihao]]></Content>
    </xml>
    """

def test_run():
    from zgrobot.config import Config
    config = Config(
    SERVER="auto",
    HOST=None,
    PORT=8080
    )
    robot = ZgRoBot(config=config)
    with pytest.raises(ValueError):
        robot.run()
