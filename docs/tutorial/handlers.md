## 添加处理器
**ZgRoBot** 会将合法的请求发送给 ``Handlers`` 依次执行。

如果某一个 ``Handler`` 返回了非空值， **ZgRoBot** 就会根据这个值创建回复，后面的 ``handlers`` 将不会被执行。

你可以通过修饰符或`add_handler`添加 ``handler``

```py title="bot.py" hl_lines="6 13"
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
```

## 类型过滤
在大多数情况下， 一个 ``Handler`` 并不能处理所有类型的消息。幸运的是， **ZgRoBot** 可以帮你过滤收到的消息。

只想处理被新用户关注的消息？

```py title="bot.py"
import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')

@robot.subscribe
def subscribe(message):
    return 'Hello My Friend!'

robot.run()
```

或者，你的 ``Handler`` 只向用来处理文本？

```py title="bot.py"
import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')

@robot.text
def echo(message):
    return message.content

robot.run()
```

额，这个 ``handler`` 想处理文本信息和地理位置信息？ 

```py title="bot.py"
import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')

@robot.text
@robot.location
def handler(message):
    # Do what you love to do
    pass

robot.run()
```

当然，你也可以用 `add_handler` 函数添加handler，就像这样：

```py title="bot.py"
import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')

def handler(message):
    # Do what you love to do
    pass

robot.add_handler(handler, type='text')
robot.add_handler(handler, type='location')

robot.run()
```

!!!note
    通过 `add_handler` 添加的 handler 将收到所有信息，并且只有在其它 handler 没有给出返回值的情况下，通过 `add_handler` 添加的 handler 才会被调用。



在 **ZgRobot** 中我们把请求分成了 `messages` 和 `events` 两种类型,针对两种类型的请求分别有不同的 ``Handler``。

## 自定义菜单的处理器
你可以使用 `key_click` 回应自定义菜单。

`key_click` 是对 `click` 修饰符的改进。

如果你在自定义菜单中定义了一个 Key 为 ``abort`` 的菜单，响应这个菜单的 ``handler`` 可以写成这样：

```py title="bot.py"
@robot.key_click("abort")
def abort():
    return "I'm a robot"
```

当然，如果你不喜欢用 `key_click` ，也可以写成这样

```py title="bot.py"
@robot.click
def abort(message):
    if message.key == "abort":
        return "I'm a robot"
```

两者是等价的。

## 文本过滤器
你可以使用 `filter` 回应有指定文本的消息，`filter` 是对 `text` 修饰符的改进。

现在你可以写这样的代码：

```py title="bot.py"
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
```

这段代码等价于 

```py title="bot.py"
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
```

如果你想通过修饰符以外的方法添加 filter，可以使用 `add_filter` 方法：

```py title="bot.py"
def say_hello():
    return "hello!"

robot.add_filter(func=say_hello, rules=["hello", "hi", re.compile(".*?hello.*?")])
```

更多内容详见 `BaseRoBot()`
