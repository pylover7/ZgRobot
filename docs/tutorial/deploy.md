!!!note "注意"

    本节所讨论的是将 **ZgRoBot** 作为独立服务运行情况下的部署操作。 如果你希望将 **ZgRoBot** 集成到其他 **Web** 框架内，请阅读[集成](../tutorial/contrib.md)

## 原生部署
你可以在`Config()` 中配置好 ZgRoBot 需要监听的地址和端口号， 然后使用你生成的 ``robot`` 调用 `ZgRoBot.run()` 方法来启动服务器：

```py title="bot.py"

import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')

@robot.handler
def echo(message):
    return 'Hello World!'

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80

robot.run()

```

!!!tip

    你需要 **root** 或管理员权限才能监听 1024 以下的端口。

你可以通过传递 ``server`` 参数来手动指定使用的服务器：

```py title="bot.py"
import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')

@robot.handler
def echo(message):
    return 'Hello World!'

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80

robot.run(server='gevent')
```

``server`` 支持以下几种：

+ cgi
+ flup
+ wsgiref
+ waitress
+ cherrypy
+ paste
+ fapws3
+ tornado
+ gae
+ twisted
+ diesel
+ meinheld
+ gunicorn
+ eventlet
+ gevent
+ rocket
+ bjoern
+ auto

当 ``server`` 为 ``auto`` 时， **ZgRoBot** 会自动依次尝试以下几种服务器：

+ Waitress
+ Paste
+ Twisted
+ CherryPy
+ WSGIRef

所以，只要你安装了相应的服务器软件，就可以使用 ``zgrobot.run`` 直接跑在生产环境下。

!!!info

    `server` 的默认值为 ``auto`` 。

!!!waring

    [WSGIRef](http://docs.python.org/library/wsgiref.html#module-wsgiref.simple_server) 的性能非常差， 仅能用于开发环境。 如果你要在生产环境下部署 **ZgRoBot** ， 请确保你在使用其他 server 。

## WSGI HTTP Server
``zgrobot.wsgi`` 暴露了一个 WSGI Application ，你可以使用任何你喜欢的 WSGI HTTP Server 来部署 ZgRoBot。

比如， 如果你想用 Gunicorn 来部署：

```py title="robot.py"
from zgrobot import ZgRoBot
robot = ZgRoBot()
```

那么你只需要在 Shell 下运行:

```bash
gunicorn robot:robot.wsgi
```

就可以了。

## Supervisor 守护进程
请注意， ``zgrobot.run`` 是跑在 **非守护进程模式下** 的，也就是说，一旦你关闭终端，进程就会自动退出。

我们建议您使用 [Supervisor](http://supervisord.org/) 来管理 **ZgRoBot** 的进程。

配置文件样例：
```conf title="supervisord.conf"
[program:wechat_robot]
command = python /home/<username>/robot.py
user = <username>
redirect_stderr = true
stdout_logfile = /home/<username>/logs/robot.log
stdout_errfile = /home/<username>/logs/robot_error.log
```

## Nginx 反向代理
微信服务器只支持80端口的机器人——显然，你的服务器上不会只跑着一个微信机器人。对于这种情况，我们建议您使用 Nginx 来进行反向代理。

!!!note

    建议新建一个子配置文件对机器人进行配置，并在主配置文件的 ``server`` 中添加 ``include xxx/*.conf;`` （配置文件的绝对路径），然后重新加载 ``nginx`` 服务。

配置文件样例：
```conf title="zgrobot.conf"
server {
    server_name example.com;
    listen 80;

    location / {
        proxy_pass_header Server;
        proxy_redirect off;
        proxy_pass http://127.0.0.1:12233;
    }
}
```

!!!note
    在这个例子中， ZgRoBot 的端口号为 12233。你应该在微信管理后台中将服务器地址设为 ``http://example.com`` 。

!!!tip
    更多的 ``Nginx`` 配置请参看 [万字长文看Nginx配置详解!](https://mp.weixin.qq.com/s/8c4EraI-X6i_o-3AxTUBLg)


