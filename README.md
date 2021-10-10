# ZgRoBot

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/pylover7/ZgRobot/tests?label=tests)](https://github.com/pylover7/ZgRobot/actions/workflows/test.yml)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/pylover7/ZgRobot/Lint?label=lint)](https://github.com/pylover7/ZgRobot/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/pylover7/ZgRobot/branch/master/graph/badge.svg?token=JGB56KZ6CU)](https://codecov.io/gh/pylover7/ZgRobot)
[![GitHub all releases](https://img.shields.io/github/downloads/pylover7/ZgRobot/total)](https://github.com/pylover7/ZgRobot/releases)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pip)](https://www.python.org/)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/pylover7/ZgRobot)](https://github.com/pylover7/ZgRobot/commits/feature-update_docs)
[![GitHub](https://img.shields.io/github/license/pylover7/ZgRobot)]()


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
[![contributors](https://opencollective.com/zgrobot/contributors.svg?width=890&button=false)](https://opencollective.com/zgrobot)

## License
```text
Copyright (c) 2013 whtsky

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
