# -*- coding: utf-8 -*-

import os
import mongomock
import mockredis
import pytest
import sqlite3

import zgrobot
import zgrobot.testing
import zgrobot.utils
from zgrobot.session import SessionStorage
from zgrobot.session import filestorage, mongodbstorage, redisstorage, saekvstorage
from zgrobot.session import sqlitestorage
from zgrobot.session import mysqlstorage
from zgrobot.session import postgresqlstorage
from zgrobot.utils import to_binary


def teardown_module():
    try:
        os.remove("zgrobot_session")
        os.remove("zgrobot_session.sqlite3")
    except:
        pass


def remove_session(session):
    try:
        del session[to_binary("fromUser")]
    except:
        pass


def test_session():
    robot = zgrobot.ZgRoBot(
        token=zgrobot.utils.generate_token(), enable_session=True
    )

    @robot.text
    def first(message, session):
        if 'last' in session:
            return
        session['last'] = message.content
        return message.content

    @robot.text
    def second(_, session):
        return session['last']

    tester = zgrobot.testing.WeTest(robot)
    xml_1 = """
        <xml>
        <ToUserName><![CDATA[toUser]]></ToUserName>
        <FromUserName><![CDATA[fromUser]]></FromUserName>
        <CreateTime>1348831860</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[ss]]></Content>
        <MsgId>1234567890123456</MsgId>
        </xml>
    """
    xml_2 = """
        <xml>
        <ToUserName><![CDATA[toUser]]></ToUserName>
        <FromUserName><![CDATA[fromUser]]></FromUserName>
        <CreateTime>1348831860</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[dd]]></Content>
        <MsgId>1234567890123456</MsgId>
        </xml>
    """

    reply_1 = tester.send_xml(xml_1)._args['content']
    assert reply_1 == 'ss'
    reply_2 = tester.send_xml(xml_2)._args['content']
    assert reply_2 == 'ss'


def test_session_storage_get():
    session = SessionStorage()
    with pytest.raises(NotImplementedError):
        session.get('s')
    with pytest.raises(NotImplementedError):
        session['s']


def test_session_storage_set():
    session = SessionStorage()
    with pytest.raises(NotImplementedError):
        session.set('s', {})
    with pytest.raises(NotImplementedError):
        session['s'] = {}


def test_session_storage_delete():
    session = SessionStorage()
    with pytest.raises(NotImplementedError):
        session.delete('s')

    with pytest.raises(NotImplementedError):
        del session['s']


class MockPyMySQL:
    def __init__(self):
        self.db = sqlite3.connect("zgrobot_session.sqlite3")
        self.db.text_factory = str
        from zgrobot.session.sqlitestorage import __CREATE_TABLE_SQL__
        self.db.execute(__CREATE_TABLE_SQL__)
        self.cache_result = None

    def cursor(self):
        return self

    def execute(self, *args, **kwargs):
        if "CREATE TABLE" not in args[0]:
            args = list(args)
            args[0] = args[0].replace('%s', '?')
            if "SELECT" in args[0]:
                self.cache_result = self.db.execute(*args, **kwargs).fetchone()
            elif "INSERT" in args[0]:
                args = [
                    "INSERT OR REPLACE INTO ZgRoBot (id, value) VALUES (?,?);",
                    (args[1][0], args[1][1])
                ]
                self.db.execute(*args, **kwargs)
            else:
                self.db.execute(*args, **kwargs)

    def fetchone(self):
        return self.cache_result

    def commit(self):
        return self.db.commit()


class MockPostgreSQL(MockPyMySQL):
    pass


@pytest.mark.parametrize(
    "storage", [
        filestorage.FileStorage(),
        mongodbstorage.MongoDBStorage(mongomock.MongoClient().t.t),
        redisstorage.RedisStorage(mockredis.mock_redis_client()),
        sqlitestorage.SQLiteStorage(),
        mysqlstorage.MySQLStorage(MockPyMySQL()),
        postgresqlstorage.PostgreSQLStorage(MockPostgreSQL())
    ]
)
def test_storage(storage):
    assert storage.get("喵") == {}
    storage.set("喵", "喵喵")
    assert storage.get("喵") == u"喵喵"
    storage.delete("喵")
    assert storage.get("喵") == {}

    assert storage["榴莲"] == {}
    storage["榴莲"] = "榴莲"
    assert storage["榴莲"] == u"榴莲"
    del storage["榴莲"]
    assert storage["榴莲"] == {}
