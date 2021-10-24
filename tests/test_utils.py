# -*- coding: utf-8 -*-

import re
import os
import time

from zgrobot.utils import generate_token, check_token, to_text, to_binary
from zgrobot.utils import pay_sign_dict, make_error_page, is_regex
from zgrobot.utils import check_file_type_and_size, str2button, set_timeout


def test_token_generator():
    assert not check_token('AA C')
    assert check_token(generate_token())
    assert 3 <= len(generate_token()) <= 32


def test_to_text():
    assert to_text(6) == str(6)
    assert to_text(b"aa") == "aa"
    assert to_text("cc") == "cc"
    assert to_text(u"喵") == u"喵"
    assert to_text("喵") == u"喵"


def test_to_binary():
    assert to_binary(6) == bytes(6)
    assert to_binary(b"aa") == b"aa"
    assert to_binary("cc") == b"cc"
    assert to_binary(u"喵") == b"\xe5\x96\xb5"
    assert to_binary("喵") == b"\xe5\x96\xb5"


def test_pay_sign_dict():
    appid = {"id": "nothing"}
    key = "test_key"

    pay_sign = pay_sign_dict(appid, key)

    assert "timestamp" in pay_sign[0]
    assert "noncestr" in pay_sign[0]
    assert "appid" in pay_sign[0]
    assert pay_sign[0]["appid"] == appid
    assert pay_sign[2] == u"SHA1"

    pay_sign = pay_sign_dict(
        appid, key, add_noncestr=False, add_timestamp=False, gadd_appid=False
    )

    assert "timestamp" not in pay_sign[0]
    assert "noncestr" not in pay_sign[0]
    assert "appid" in pay_sign[0]


def test_make_error_page():
    rand_string = generate_token()
    content = make_error_page(rand_string)
    assert rand_string in content


def test_is_regex():
    regex = re.compile(r"test")
    assert not is_regex("test")
    assert is_regex(regex)


def test_check_file_type_and_size():
    assert check_file_type_and_size(
        file_type="image",
        file_object=open(
            os.path.join(
                os.path.dirname(__file__), os.path.join("media", "123.png")
            ), "rb"
        )
    )
    assert not check_file_type_and_size(
        file_type="iamgea",
        file_object=open(
            os.path.join(
                os.path.dirname(__file__), os.path.join("media", "123.png")
            ), "rb"
        )
    )
    assert not check_file_type_and_size(
        file_type="image",
        file_object=open(
            os.path.join(
                os.path.dirname(__file__), os.path.join("media", "234.pngw")
            ), "rb"
        )
    )


def test_str2button():
    assert type(str2button(button_txt="123", reply_txt="456")) is str


def test_set_timeout():
    def timeout_func():
        time.sleep(5)

    assert set_timeout(timeout_func)() == "success"
