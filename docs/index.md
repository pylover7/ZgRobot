<h1 align="center"> ZgRoBot </h1>

<b align="center">

</b>

`ZgRoBot` 是一个基于 [`WeRoBot`](https://github.com/offu/WeRoBot) 开发的微信公众号后台开发框架，采用MIT协议发布。

 > 我是来看【 [使用文档](https://zgrobot.readthedocs.io/zh/stable/) 】的！

## 安装
### 推荐安装
推荐使用 `pip` 进行安装：
```shell
pip install zgrobot
```
### 其他安装方法
1. 手动下载安装包
    - 下载地址1： [release](https://github.com/pylover7/ZgRobot/releases)
    - 下载地址2：[蓝奏云仓库](https://shuoshuo.lanzoui.com/b016uiu7i) 、 [蓝奏云备用地址](https://shuoshuo.lanzoux.com/b016uiu7i) 【密码：1n86】
    
2. 本地安装
```shell
pip install zgrobot-XXX.tar.gz
```

### 更新
```shell
pip install --upgrade zgrobot
```

## 使用
### Hello World
一个非常简单的 `Hello World` 微信公众号，会对收到的所有文本消息回复 `Hello World`

```python
import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')

@robot.text
def hello_world():
    return 'Hello World!'

robot.run()
```

### 高级使用
请参阅【 [使用文档](https://zgrobot.readthedocs.io/zh/stable/) 】

## Status

![Alt](https://repobeats.axiom.co/api/embed/1fb76725ce62ccf8879ab82b24b09d18f47664f2.svg "Repobeats analytics image")
