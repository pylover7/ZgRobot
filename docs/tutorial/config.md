## 说明
ZgRoBot 使用 ``ZgRoBot.Config`` 类来存储配置信息。  ``ZgRoBot`` 类实例的 ``config`` 属性是一个 [Config()][zgrobot.config.Config] 实例。

[Config()][zgrobot.config.Config] 继承自 [dict](https://docs.python.org/zh-cn/3.7/library/stdtypes.html?highlight=dict#mapping-types-dict)
因此， 你可以像使用普通 ``dict`` 一样使用它

```py title="bot.py"
from zgrobot import ZgRoBot
robot = ZgRoBot(token='2333')

robot.config.update(
    HOST='0.0.0.0',
    PORT=80
)
```

当然， 你也可以先创建一个 ``Config`` ，然后在初始化 ``ZgRobot`` 的时候传入自己的 ``Config`` ::


```py title="bot.py"
from zgrobot.config import Config
config = Config(
    TOKEN="token from config!"
)
robot = ZgRoBot(config=config, token="token from init")
assert robot.token == "token from config!"
```

!!!note
    如果你在初始化 ``ZgRoBot`` 时传入了 ``config`` 参数， ``ZgRoBot`` 会忽略除 ``logger`` 外其他所有的初始化参数。 如果你需要对 ``ZgRoBot`` 进行一些配置操作， 请修改 ``Config`` 。

与普通 ``dict`` 不同的是， 你可以先把配置文件保存在一个对象或是文件中， 然后在 [Config()][zgrobot.config.Config] 中导入配置

```py title="bot.py"
from zgrobot import ZgRoBot
robot = ZgRoBot(token='2333')

class MyConfig(object):
    HOST = '0.0.0.0'
    PORT = 80

robot.config.from_object(MyConfig)
robot.config.from_pyfile("config.py")
```

## 默认配置

```py
dict(
    TOKEN=None,
    SERVER="auto",
    HOST="127.0.0.1",
    PORT="8888",
    SESSION_STORAGE=None,
    APP_ID=None,
    APP_SECRET=None,
    ENCODING_AES_KEY=None
)
```


