## Hello World
最简单的 `Hello World` 例子， 会给收到的每一条信息回复 `Hello World`

```py title="hello.py" linenums="1"
import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')

@robot.text
def hello_world(message):
    return 'Hello World!'

if __name__ == '__main__':
    # 让服务器监听在 127.0.0.1:8080
    robot.run(host='127.0.0.1', port=8080)
```

## 消息处理

**ZgRoBot** 会解析微信服务器发来的消息， 并将消息转换成成`Message` 或者是`Event` 。

`Message` 表示用户发来的消息，如文本消息、图片消息；`Event` 则表示用户触发的事件， 如关注事件、扫描二维码事件。

在消息解析、转换完成后， **ZgRoBot** 会将消息转交给`Handler` 进行处理，并将`Handler` 的返回值返回给微信服务器。

在刚才的 Hello World 中， 我们编写的：

```py title="hello.py" linenums="5"
@robot.text
def hello_world(message):
    return 'Hello World!'
```

就是一个简单的`Handler` ， ``@robot.handler`` 意味着 ``robot`` 会将所有接收到的消息（ 包括`Message` 和`Event` ） 都转交给这个`Handler` 来处理。
当然， 你也可以编写一些只能处理特定消息的`Handler`： 

```py title="handler.py"
# @robot.text 修饰的 Handler 只处理文本消息
@robot.text
def echo(message):
    return message.content

# @robot.image 修饰的 Handler 只处理图片消息
@robot.image
def img(message):
    return message.img

```

## 使用 Session 记录用户状态
**ZgRoBot** 提供了`Session` 功能， 可以让你方便的记录用户状态。
比如， 这个`Handler` 可以判断发消息的用户之前有没有发送过消息

```py title="session.py"
@robot.text
    def first(message, session):
        if 'first' in session:
            return '你之前给我发过消息'
        session['first'] = True
        return '你之前没给我发过消息'
```

!!! note 

    ``Session`` 功能默认开启， 并使用 ``SQLite`` 存储 ``Session`` 数据。 详情请参考 `session` 文档

## 创建自定义菜单
自定义菜单能够帮助公众号丰富界面，让用户更好更快地理解公众号的功能。 `Client` 封装了微信的部分 API 接口，我们可以使用 `Client.create_menu`
来创建自定义菜单。在使用 ``Client`` 之前， 我们需要先提供微信公众平台内的 ``AppID`` 和 ``AppSecret`` 

```py title="menu.py" linenums="1"
from zgrobot import ZgRoBot

robot = ZgRoBot()
robot.config["APP_ID"] = "你的 AppID"
robot.config["APP_SECRET"] = "你的 AppSecret"

client = robot.client
```

然后， 我们就可以创建自定义菜单了

```py title="menu.py" linenums="8"
client.create_menu({
    "button":[{	
         "type": "click",
         "name": "今日歌曲",
         "key": "music"
    }]
})
```


注意以上代码只需要运行一次就可以了。在创建完自定义菜单之后， 我们还需要写一个`handler` 来响应菜单的点击操作

```py title="menu.py" linenums="15"
@robot.key_click("music")
    def music(message):
        return '你点击了“今日歌曲”按钮'
```


