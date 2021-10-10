Session
==========

你可以通过 Session 实现用户状态的记录。

一个简单的使用 Session 的 Demo ::

    from zgrobot import ZgRoBot
    robot = ZgRoBot(token=zgrobot.utils.generate_token())

    @robot.text
    def first(message, session):
        if 'last' in session:
            return
        session['last'] = message.content
        return message.content

    robot.run()

开启/关闭 Session
-----------------

Session 在 ZgRoBot 中默认开启， 并使用 :class:`zgrobot.session.sqlitestorage.SQLiteStorage` 作为存储后端。 如果想要更换存储后端， 可以修改 :doc:`config` 中的 ``SESSION_STORAGE`` ::

    from zgrobot import ZgRoBot
    from zgrobot.session.filestorage import FileStorage
    robot = ZgRoBot(token="token")
    robot.config['SESSION_STORAGE'] = FileStorage()


如果想要关闭 Session 功能， 只需把 ``SESSION_STORAGE`` 设为 False 即可 ::

    from zgrobot import ZgRoBot
    robot = ZgRoBot(token="token")
    robot.config['SESSION_STORAGE'] = False

修改 Handler 以使用 Session
--------------------------------

没有打开 Session 的时候，一个标准的 ZgRoBot Handler 应该是这样的 ::

    @robot.text
    def hello(message):
        return "Hello!"

而在打开 Session 之后， 如果你的 handler 不需要使用 Session ，可以保持不变； 如果需要使用 Session ，则这个 Handler 需要修改为接受第二个参数： ``session`` ::

    @robot.subscribe_event
    def intro(message):
        return "Hello!"

    @robot.text
    def hello(message, session):
        count = session.get("count", 0) + 1
        session["count"] = count
        return "Hello! You have sent %s messages to me" % count

传入的 ``session`` 参数是一个标准的 Python 字典。

更多可用的 Session Storage 详见 :ref:`Session 对象`。
