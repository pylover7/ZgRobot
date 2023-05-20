# -*- coding: utf-8 -*-

from zgrobot.messages.base import ZgRoBotMetaClass
from zgrobot.messages.entries import StringEntry, IntEntry, FloatEntry


class MessageMetaClass(ZgRoBotMetaClass):
    pass


class WeChatMessage(object, metaclass=MessageMetaClass):
    """
    用于处理微信服务器推送过来的消息

    Attributes:
        message_id: 消息id，64位整型
        target: 开发者账号（ OpenID ）
        source: 发送方账号（ OpenID ）
        time: 信息发送的时间，一个UNIX时间戳。
    """
    message_id = IntEntry('MsgId', 0)
    target = StringEntry('ToUserName')
    source = StringEntry('FromUserName')
    time = IntEntry('CreateTime', 0)

    def __init__(self, message):
        self.__dict__.update(message)


class TextMessage(WeChatMessage):
    __type__ = 'text'
    content = StringEntry('Content')


class ImageMessage(WeChatMessage):
    __type__ = 'image'
    img = StringEntry('PicUrl')
    media_id = StringEntry('MediaId')


class LocationMessage(WeChatMessage):
    __type__ = 'location'
    location_x = FloatEntry('Location_X')
    location_y = FloatEntry('Location_Y')
    label = StringEntry('Label')
    scale = IntEntry('Scale')

    @property
    def location(self):
        return self.location_x, self.location_y


class LinkMessage(WeChatMessage):
    __type__ = 'link'
    title = StringEntry('Title')
    description = StringEntry('Description')
    url = StringEntry('Url')


class VoiceMessage(WeChatMessage):
    __type__ = 'voice'
    media_id = StringEntry('MediaId')
    format = StringEntry('Format')
    recognition = StringEntry('Recognition')


class VideoMessage(WeChatMessage):
    __type__ = ['video', 'shortvideo']
    media_id = StringEntry('MediaId')
    thumb_media_id = StringEntry('ThumbMediaId')


class UnknownMessage(WeChatMessage):
    __type__ = 'unknown'


class Message(WeChatMessage):
    """
    用于处理微信服务器推送过来的消息

    Attributes:
        __type__: 消息类型
        content: 文本消息内容
        img: 图片链接
        media_id: 图片消息媒体id，可以调用多媒体文件下载接口拉取数据
        location_x: 地理位置维度
        location_y: 地理位置经度
        label: 地理位置信息
        scale: 地图缩放大小
        title: 消息标题
        description: 消息描述
        url: 消息链接
        format: 语音格式，如amr，speex等
        recognition: 语音识别结果，UTF8编码
        thumb_media_id: 视频消息缩略图的媒体id，可以调用多媒体文件下载接口拉取数据
    """
    __type__: str
    content = StringEntry('Content')
    img = StringEntry('PicUrl')
    media_id = StringEntry('MediaId')
    location_x = FloatEntry('Location_X')
    location_y = FloatEntry('Location_Y')
    label = StringEntry('Label')
    scale = IntEntry('Scale')
    title = StringEntry('Title')
    description = StringEntry('Description')
    url = StringEntry('Url')
    format = StringEntry('Format')
    recognition = StringEntry('Recognition')
    thumb_media_id = StringEntry('ThumbMediaId')
