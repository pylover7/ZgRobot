# -*- coding: utf-8 -*-

import io
import json
import os
import random
import re
import string
import time
from functools import wraps
from hashlib import sha1
from typing import BinaryIO

try:
    from secrets import choice
except ImportError:
    from random import choice

string_types = (str, bytes)

re_type = type(re.compile("regex_test"))


def get_signature(token, timestamp, nonce, *args):
    sign = [token, timestamp, nonce] + list(args)
    sign.sort()
    sign = to_binary(''.join(sign))
    return sha1(sign).hexdigest()


def check_signature(token, timestamp, nonce, signature):
    if not (token and timestamp and nonce and signature):
        return False
    sign = get_signature(token, timestamp, nonce)
    return sign == signature


def check_token(token):
    return re.match('^[A-Za-z0-9]{3,32}$', token)


def cached_property(method):
    prop_name = '_{}'.format(method.__name__)

    @wraps(method)
    def wrapped_func(self, *args, **kwargs):
        if not hasattr(self, prop_name):
            setattr(self, prop_name, method(self, *args, **kwargs))
        return getattr(self, prop_name)

    return property(wrapped_func)


def to_text(value, encoding="utf-8") -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, bytes):
        return value.decode(encoding)
    return str(value)


def to_binary(value, encoding="utf-8") -> bytes:
    if isinstance(value, bytes):
        return value
    if isinstance(value, str):
        return value.encode(encoding)
    return bytes(value)


def is_string(value) -> bool:
    """Check if value's type is `str` or `bytes`
    """
    return isinstance(value, string_types)


def byte2int(s, index=0):
    """Get the ASCII int value of a character in a string.

    :param s: a string
    :param index: the position of desired character

    :return: ASCII int value
    """
    return s[index]


def generate_token(length=''):
    if not length:
        length = random.randint(3, 32)
    length = int(length)
    assert 3 <= length <= 32
    letters = string.ascii_letters + string.digits
    return ''.join(choice(letters) for _ in range(length))


def json_loads(s):
    s = to_text(s)
    return json.loads(s)


def json_dumps(d):
    return json.dumps(d)


def pay_sign_dict(
    appid,
    pay_sign_key,
    add_noncestr=True,
    add_timestamp=True,
    add_appid=True,
    **kwargs
):
    """
    支付参数签名
    """
    assert pay_sign_key, "PAY SIGN KEY IS EMPTY"

    if add_appid:
        kwargs.update({'appid': appid})

    if add_noncestr:
        kwargs.update({'noncestr': generate_token()})

    if add_timestamp:
        kwargs.update({'timestamp': int(time.time())})

    params = kwargs.items()

    _params = [
        (k.lower(), v) for k, v in kwargs.items() if k.lower() != "appid"
    ]
    _params += [('appid', appid), ('appkey', pay_sign_key)]
    _params.sort()

    sign = '&'.join(["%s=%s" % (str(p[0]), str(p[1]))
                     for p in _params]).encode("utf-8")
    sign = sha1(sign).hexdigest()
    sign_type = 'SHA1'

    return dict(params), sign, sign_type


def make_error_page(url):
    with io.open(
        os.path.join(os.path.dirname(__file__), 'contrib/error.html'),
        'r',
        encoding='utf-8'
    ) as error_page:
        return error_page.read().replace('{url}', url)


def is_regex(value):
    return isinstance(value, re_type)


def check_file_type_and_size(file_type: str, file_object: BinaryIO):
    file_suffix = file_object.name.split(".")[-1]
    file_size = file_object.__sizeof__()
    file_type_dict = {
        "image": ["png", "jpg", "jpeg", "gif", "bmp", 10 * 1024 * 1024],
        "voice": ["mp3", "amr", "wma", "wav", 2 * 1024 * 1024],
        "video": ["mp4", 10 * 1024 * 1024],
        "thumb": ["jpg", 64 * 1024]
    }
    try:
        file_size_max = file_type_dict[file_type][-1] / 1024
        if file_suffix in file_type_dict[
            file_type] and file_size < file_type_dict[file_type][-1]:
            return True
        else:
            print(
                f"File Type error, Please provide the correct type {str(file_type_dict[file_type][:-1])}, "
                f"or File Size error, Please provide the correct file "
                f"size<{str(file_size_max)} Kb"
            )
    except KeyError:
        print(
            "File Type error, Please provide the correct type: image, voice, video and thumb!"
        )


def str2button(button_txt: str, reply_txt: str) -> str:
    """
    将普通文本包装为智能按钮

    :param button_txt: 想要转换为智能按钮的文本
    :param reply_txt: 按下智能按钮后回复的文本
    :return: 返回智能按钮的字符串
    """
    return f"<a href='weixin://bizmsgmenu?msgmenuid=1&msgmenucontent={button_txt}'>{reply_txt}</a>"
