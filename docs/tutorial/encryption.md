**ZgRoBot** 支持对消息的加解密，即微信公众号的安全模式。
在开启消息加解密功能之前，请先阅读微信官方的 [消息加解密说明](https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Message_encryption_and_decryption_instructions.html)

为 **ZgRoBot** 开启消息加密功能，首先需要安装 ``cryptography``

```bash
pip install cryptography
```

之后， 你只需要将开发者 ID( ``AppID`` ) 和微信公众平台后台设置的 ``EncodingAESKey`` 加到 **ZgRoBot** 的 `Config` 里面就可以了。

```py title="bot.py"

from zgrobot import ZgRoBot
robot = ZgRoBot()
robot.config["APP_ID"] = "Your AppID"
robot.config['ENCODING_AES_KEY'] = 'Your Encoding AES Key'
```

**ZgRoBot** 之后会自动进行消息的加解密工作。
