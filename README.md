<h1 align="center"> ZgRoBot </h1>

<b align="center">

[![GitHub Workflow Status](https://github.com/pylover7/zgrobot/workflows/tests/badge.svg)](https://github.com/pylover7/ZgRobot/actions)
[![codecov](https://codecov.io/gh/pylover7/ZgRobot/branch/master/graph/badge.svg?token=JGB56KZ6CU)](https://codecov.io/gh/pylover7/ZgRobot)
[![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/pylover7/ZgRobot?include_prereleases&sort=semver)](https://github.com/pylover7/ZgRobot/releases)
[![GitHub all releases](https://img.shields.io/github/downloads/pylover7/ZgRobot/total)](https://github.com/pylover7/ZgRobot/releases)
[![GitHub](https://img.shields.io/github/license/pylover7/ZgRobot)](https://github.com/pylover7/ZgRobot/blob/master/LICENSE)

[![Documentation Status](https://readthedocs.org/projects/zgrobot/badge/?version=latest)](https://zgrobot.readthedocs.io/zh/latest/?badge=latest)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zgrobot)](https://pypi.org/project/zgrobot/)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/pylover7/ZgRobot)](https://github.com/pylover7/ZgRobot/commits/feature-update_docs)
[![wakatime](https://wakatime.com/badge/user/1d39df6a-cef0-41f7-a903-ef4b9dd13fb0.svg)](https://wakatime.com/@1d39df6a-cef0-41f7-a903-ef4b9dd13fb0)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://pylover7-upgraded-space-chainsaw-pwgxxw54w6ph6jj.github.dev/)

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

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=pylover7/ZgRobot&type=Date)](https://star-history.com/#pylover7/ZgRobot&Date)
