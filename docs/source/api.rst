API
==========

.. module:: zgrobot

应用对象
------------

.. module:: zgrobot.robot
.. autoclass:: BaseRoBot
    :members:
.. autoclass:: ZgRoBot
    :members:

配置对象
------------

.. module:: zgrobot.config
.. autoclass:: Config
    :members:

Session 对象
------------
.. module:: zgrobot.session.sqlitestorage
.. autoclass:: SQLiteStorage

.. module:: zgrobot.session.filestorage
.. autoclass:: FileStorage

.. module:: zgrobot.session.mongodbstorage
.. autoclass:: MongoDBStorage

.. module:: zgrobot.session.redisstorage
.. autoclass:: RedisStorage

.. module:: zgrobot.session.saekvstorage
.. autoclass:: SaeKVDBStorage

.. module:: zgrobot.session.mysqlstorage
.. autoclass:: MySQLStorage

.. module:: zgrobot.session.postgresqlstorage
.. autoclass:: PostgreSQLStorage

log
------------
.. module:: zgrobot.logger
.. autofunction:: enable_pretty_logging
