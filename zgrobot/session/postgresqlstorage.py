# -*- coding: utf-8 -*-

from zgrobot.session import SessionStorage
from zgrobot.utils import json_loads, json_dumps

__CREATE_TABLE_SQL__ = """
CREATE TABLE IF NOT EXISTS ZgRoBot
(
id VARCHAR(100) PRIMARY KEY,
value TEXT NOT NULL
);
"""


class PostgreSQLStorage(SessionStorage):
    """
    PostgreSQLStorage 会把你的 Session 数据储存在 PostgreSQL 中 ::

        import psycopg2  # pip install psycopg2-binary
        import zgrobot
        from zgrobot.session.postgresqlstorage import PostgreSQLStorage

        conn = psycopg2.connect(host='127.0.0.1', port='5432', dbname='zgrobot', user='nya', password='nyanya')
        session_storage = PostgreSQLStorage(conn)
        robot = zgrobot.ZgRoBot(token="token", enable_session=True,
                                session_storage=session_storage)

    你需要安装一个 ``PostgreSQL Client`` 才能使用 PostgreSQLStorage，比如 ``psycopg2``。

    理论上符合 `PEP-249 <https://www.python.org/dev/peps/pep-0249/#connection-objects>`_ 的库都可以使用，\
    测试时使用的是 ``psycopg2``。

    :param conn: `PEP-249 <https://www.python.org/dev/peps/pep-0249/#connection-objects>`_\
    定义的 Connection 对象
    """
    def __init__(self, conn):
        self.conn = conn
        self.conn.cursor().execute(__CREATE_TABLE_SQL__)

    def get(self, id):
        """
        根据 id 获取数据。

        :param id: 要获取的数据的 id
        :return: 返回取到的数据，如果是空则返回一个空的 ``dict`` 对象
        """
        cur = self.conn.cursor()
        cur.execute("SELECT value FROM ZgRoBot WHERE id=%s LIMIT 1;", (id, ))
        session_json = cur.fetchone()
        if session_json is None:
            return {}
        return json_loads(session_json[0])

    def set(self, id, value):
        """
        根据 id 写入数据。

        :param id: 要写入的 id
        :param value: 要写入的数据，可以是一个 ``dict`` 对象
        """
        value = json_dumps(value)
        self.conn.cursor().execute(
            "INSERT INTO ZgRoBot (id, value) values (%s, %s) ON CONFLICT (id) DO UPDATE SET value = %s;",
            (
                id,
                value,
                value,
            )
        )
        self.conn.commit()

    def delete(self, id):
        """
        根据 id 删除数据。

        :param id: 要删除的数据的 id
        """
        self.conn.cursor().execute("DELETE FROM ZgRoBot WHERE id=%s", (id, ))
        self.conn.commit()
