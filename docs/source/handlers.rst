Handler
=========


**ZgRoBot** 会将合法的请求发送给 ``Handlers`` 依次执行。

如果某一个 ``Handler`` 返回了非空值， **ZgRoBot** 就会根据这个值创建回复，后面的 ``handlers`` 将不会被执行。

你可以通过修饰符或 :meth:`~zgrobot.robot.BaseRoBot.add_handler` 添加 ``handler`` ::

    import zgrobot

    robot = zgrobot.ZgRoBot(token='tokenhere')

    # 通过修饰符添加handler
    @robot.handler
    def echo(message):
        return 'Hello World!'

    # 通过`add_handler`添加handler
    def echo(message):
        return 'Hello World!'
    robot.add_handler(echo)

类型过滤
------------

在大多数情况下， 一个 ``Handler`` 并不能处理所有类型的消息。幸运的是， **ZgRoBot** 可以帮你过滤收到的消息。

只想处理被新用户关注的消息？ ::

    import zgrobot

    robot = zgrobot.ZgRoBot(token='tokenhere')

    @robot.subscribe
    def subscribe(message):
        return 'Hello My Friend!'

    robot.run()

或者，你的 ``Handler`` 只能处理文本？ ::

    import zgrobot

    robot = zgrobot.ZgRoBot(token='tokenhere')

    @robot.text
    def echo(message):
        return message.content

    robot.run()

在 **ZgRobot** 中我们把请求分成了 :doc:`messages` 和 :doc:`events` 两种类型,针对两种类型的请求分别有不同的 ``Handler``。

========================================================================================================  =========================================
修饰符                                                                                                       类型
========================================================================================================  =========================================
:func:`robot.text <zgrobot.robot.BaseRoBot.text>`                                                           文本 (Message)
:func:`robot.image <zgrobot.robot.BaseRoBot.image>`                                                         图像 (Message)
:func:`robot.location <zgrobot.robot.BaseRoBot.location>`                                                   位置 (Message)
:func:`robot.link <zgrobot.robot.BaseRoBot.link>`                                                           链接 (Message)
:func:`robot.voice <zgrobot.robot.BaseRoBot.voice>`                                                         语音 (Message)
:func:`robot.unknown <zgrobot.robot.BaseRoBot.unknown>`                                                     未知类型 (Message)
:func:`robot.subscribe <zgrobot.robot.BaseRoBot.subscribe>`                                                 被关注 (Event)
:func:`robot.unsubscribe <zgrobot.robot.BaseRoBot.unsubscribe>`                                             被取消关注 (Event)
:func:`robot.click <zgrobot.robot.BaseRoBot.click>`                                                         自定义菜单事件 (Event)
:func:`robot.view <zgrobot.robot.BaseRoBot.view>`                                                           链接 (Event)
:func:`robot.scancode_push <zgrobot.robot.BaseRoBot.scancode_push>`                                         扫描推送 (Event)
:func:`robot.scancode_waitmsg <zgrobot.robot.BaseRoBot.scancode_waitmsg>`                                   扫描弹消息 (Event)
:func:`robot.pic_sysphoto <zgrobot.robot.BaseRoBot.pic_sysphoto>`                                           弹出系统拍照发图（Event）
:func:`robot.pic_photo_or_album <zgrobot.robot.BaseRoBot.pic_photo_or_album>`                               弹出拍照或者相册发图（Event）
:func:`robot.pic_weixin <zgrobot.robot.BaseRoBot.pic_weixin>`                                               弹出微信相册发图器（Event）
:func:`robot.location_select <zgrobot.robot.BaseRoBot.location_select>`                                     弹出地理位置选择器（Event）
:func:`robot.scan <zgrobot.robot.BaseRoBot.scan>`                                                           已关注扫描二维码（Event）
:func:`robot.user_scan_product <zgrobot.robot.BaseRoBot.user_scan_product>`                                 打开商品主页事件推送（Event）
:func:`robot.user_scan_product_enter_session <zgrobot.robot.BaseRoBot.user_scan_product_enter_session>`     进入公众号事件推送（Event）
:func:`robot.user_scan_product_async <zgrobot.robot.BaseRoBot.user_scan_product_async>`                     地理位置信息异步推送（Event)
:func:`robot.user_scan_product_verify_action <zgrobot.robot.BaseRoBot.user_scan_product_verify_action>`     商品审核结果推送（Event）
:func:`robot.card_pass_check <zgrobot.robot.BaseRoBot.card_pass_check>`                                     卡券通过审核 (Event)
:func:`robot.card_not_pass_check <zgrobot.robot.BaseRoBot.card_not_pass_check>`                             卡券未通过审核 (Event)
:func:`robot.user_get_card <zgrobot.robot.BaseRoBot.user_get_card>`                                         用户领取卡券 (Event)
:func:`robot.user_gifting_card <zgrobot.robot.BaseRoBot.user_gifting_card>`                                 用户转赠卡券 (Event)
:func:`robot.user_del_card <zgrobot.robot.BaseRoBot.user_del_card>`                                         用户删除卡券 (Event)
:func:`robot.user_consume_card <zgrobot.robot.BaseRoBot.user_consume_card>`                                 卡券被核销 (Event)
:func:`robot.user_pay_from_pay_cell <zgrobot.robot.BaseRoBot.user_pay_from_pay_cell>`                       微信买单完成 (Event)
:func:`robot.user_view_card <zgrobot.robot.BaseRoBot.user_view_card>`                                       用户进入会员卡 (Event)
:func:`robot.user_enter_session_from_card <zgrobot.robot.BaseRoBot.user_enter_session_from_card>`           用户卡券里点击查看公众号进入会话 (Event)
:func:`robot.update_member_card <zgrobot.robot.BaseRoBot.update_member_card>`                               会员卡积分余额发生变动 (Event)
:func:`robot.card_sku_remind <zgrobot.robot.BaseRoBot.card_sku_remind>`                                     库存警告 (Event)
:func:`robot.card_pay_order <zgrobot.robot.BaseRoBot.card_pay_order>`                                       券点发生变动 (Event)
:func:`robot.templatesendjobfinish_event <zgrobot.robot.BaseRoBot.templatesendjobfinish_event>`             模板信息推送事件 (Event)
:func:`robot.submit_membercard_user_info <zgrobot.robot.BaseRoBot.submit_membercard_user_info>`             激活卡券 (Event)
:func:`robot.location_event <zgrobot.robot.BaseRoBot.location_event>`                                       上报位置 (Event)
:func:`robot.unknown_event <zgrobot.robot.BaseRoBot.unknown_event>`                                         未知类型 (Event)
========================================================================================================  =========================================

额，这个 ``handler`` 想处理文本信息和地理位置信息？ ::

    import zgrobot

    robot = zgrobot.ZgRoBot(token='tokenhere')

    @robot.text
    @robot.location
    def handler(message):
        # Do what you love to do
        pass

    robot.run()

当然，你也可以用 :meth:`~zgrobot.robot.BaseRoBot.add_handler` 函数添加handler，就像这样::

    import zgrobot

    robot = zgrobot.ZgRoBot(token='tokenhere')

    def handler(message):
        # Do what you love to do
        pass

    robot.add_handler(handler, type='text')
    robot.add_handler(handler, type='location')

    robot.run()

.. note:: 通过 :meth:`~zgrobot.robot.BaseRoBot.add_handler` 添加的 handler 将收到所有信息，并且只有在其它 handler 没有给出返回值的情况下， \
          通过 :meth:`~zgrobot.robot.BaseRoBot.add_handler` 添加的 handler 才会被调用。

robot.key_click()
---------------------------------

你可以使用 :meth:`~zgrobot.robot.BaseRoBot.key_click` 回应自定义菜单。

:meth:`~zgrobot.robot.BaseRoBot.key_click` 是对 :meth:`~zgrobot.robot.BaseRoBot.click` 修饰符的改进。

如果你在自定义菜单中定义了一个 Key 为 ``abort`` 的菜单，响应这个菜单的 ``handler`` 可以写成这样 ::

    @robot.key_click("abort")
    def abort():
        return "I'm a robot"

当然，如果你不喜欢用 :meth:`~zgrobot.robot.BaseRoBot.key_click` ，也可以写成这样 ::

    @robot.click
    def abort(message):
        if message.key == "abort":
            return "I'm a robot"

两者是等价的。

robot.filter()
-------------------------------------

你可以使用 :meth:`~zgrobot.robot.BaseRoBot.filter` 回应有指定文本的消息

:meth:`~zgrobot.robot.BaseRoBot.filter` 是对 :meth:`~zgrobot.robot.BaseRoBot.text` 修饰符的改进。

现在你可以写这样的代码 ::

    @robot.filter("a")
    def a():
        return "正文为 a "

    import re


    @robot.filter(re.compile(".*?bb.*?"))
    def b():
        return "正文中含有 bb "

    @robot.filter(re.compile(".*?c.*?"), "d")
    def c():
        return "正文中含有 c 或正文为 d"

    @robot.filter(re.compile("(.*)?e(.*)?"), "f")
    def d(message, session, match):
        if match:
            return "正文为 " + match.group(1) + "e" + match.group(2)
        return "正文为 f"

这段代码等价于 ::

    @robot.text
    def a(message):
        if message.content == "a":
            return "正文为 a "
    import re


    @robot.text
    def b(message):
        if re.compile(".*?bb.*?").match(message.content):
            return "正文中含有 b "

    @robot.text
    def c(message):
        if re.compile(".*?c.*?").match(message.content) or message.content == "d":
            return "正文中含有 c 或正文为 d"

    @robot.text
    def d(message):
        match = re.compile("(.*)?e(.*)?").match(message.content)
        if match:
            return "正文为 " + match.group(1) + "e" + match.group(2)
        if  message.content == "f":
            return "正文为 f"

如果你想通过修饰符以外的方法添加 filter，可以使用 :func:`~zgrobot.robot.BaseRoBot.add_filter` 方法 ::

    def say_hello():
        return "hello!"

    robot.add_filter(func=say_hello, rules=["hello", "hi", re.compile(".*?hello.*?")])

更多内容详见 :class:`~zgrobot.robot.BaseRoBot()`
