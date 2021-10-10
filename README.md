# ZgRoBot

`ZgRoBot` 是一个基于 [`WeRoBot`](https://github.com/offu/WeRoBot) 开发微信公众号开发框架，采用MIT协议发布。

【 [阅读文档](https://zgrobot.readthedocs.io/zh/stable/) 】

## 安装

推荐使用 `pip` 进行安装：
```shell
pip install zgrobot
```

## Hello World
一个非常简单的 `Hello World` 微信公众号，会对收到的所有文本消息回复 `Hello World`

```python
import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')

@robot.text
def hello_world():
    return 'Hello World!'

robot.run()
```

## Credits
[![](https://opencollective.com/zgrobot/contributors.svg?width=890&button=false)](https://opencollective.com/zgrobot)
