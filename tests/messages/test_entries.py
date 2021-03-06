# -*- coding: utf-8 -*-

from zgrobot.messages.entries import get_value, StringEntry, FloatEntry, IntEntry
from zgrobot.utils import to_text


class NoNameMessage(object):
    test_int = IntEntry("TestInt")
    test_string_to_int = IntEntry("TestStringToInt")
    test_float_to_int = IntEntry("TestFloatToInt")
    test_int_none = IntEntry("MIAOMIAOMIAO")

    test_float = FloatEntry("TestFloat")
    test_string_to_float = FloatEntry("TestStringToFloat")
    test_float_none = FloatEntry("WANGWANG")

    test_string = StringEntry("TestString")
    test_int_to_string = StringEntry("TestIntToString")
    test_float_to_string = StringEntry("TestFloatToString")
    test_chinese = StringEntry("TestChinese")
    test_string_none = StringEntry("HAHAHA")

    def __init__(self):
        message = {
            "TestInt": 123,
            "TestFloat": 0.00001,
            "TestString": "hello",
            "TestStringToInt": "123",
            "TestFloatToInt": 123.000,
            "TestStringToFloat": "0.00001",
            "TestIntToString": 123,
            "TestFloatToString": 0.00001,
            "TestChinese": "喵",
        }
        self.__dict__.update(message)


t = NoNameMessage()


def test_int_entry():
    assert isinstance(t.test_int, int)
    assert t.test_int == 123
    assert isinstance(t.test_string_to_int, int)
    assert t.test_string_to_int == 123
    assert isinstance(t.test_float_to_int, int)
    assert t.test_float_to_int == 123
    assert t.test_int_none is None


def test_float_entry():
    assert isinstance(t.test_float, float)
    assert t.test_float == 0.00001
    assert isinstance(t.test_string_to_float, float)
    assert t.test_string_to_float == 0.00001
    assert t.test_float_none is None


def test_string_entry():
    assert isinstance(t.test_string, str)
    assert t.test_string == "hello"
    assert isinstance(t.test_int_to_string, str)
    assert t.test_int_to_string == "123"
    assert isinstance(t.test_float_to_string, str)
    assert t.test_float_to_string == "1e-05"
    assert isinstance(t.test_chinese, str)
    assert t.test_chinese == to_text("喵")
    assert t.test_string_none is None


class FakeIntance:
    pass


def test_get_value():
    instance = FakeIntance()
    instance.b = 6
    instance.a = {'c': 'd'}
    assert get_value(instance, 'd', 'default') == 'default'
    assert get_value(instance, 'b', 'default') == 6
    assert get_value(instance, 'a.c') == 'd'
