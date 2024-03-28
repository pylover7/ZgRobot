# -*- coding:utf-8 -*-

import time
from hashlib import sha256
import base64

import httpx

from zgrobot.client import Client
from zgrobot.config import Config

SIGIN_URL = '/v3/certificates'

#  hexdump -n 16 -e '4/4 "%08X" 1 "\n"' /dev/random
nonce_str = '69FEE29DB5856BF7D21ABA69D571859C'


class WeixinPayClient(Client):
    """
    微信支付
    
    Attributes:
        mchid (str): 发起请求的商户（包括直连商户、服务商或渠道商）的商户号mchid
        serial_no (str): 商户API证书序列号serial_no，用于声明所使用的证书
        config (zorobot.config.Config): 配置项
    """

    def __init__(self, mchid: str, serial_no: str, config: Config):
        super().__init__(config)
        self.mchid = mchid
        self.serial_no = serial_no

    def __get_order_code():
        """生成订单号

        Returns:
            order_code (str): 订单号，年月日时分秒+time.time()的后7位，例如：202104241949042979896
        """
        #  年月日时分秒+time.time()的后7位
        order_code = str(
            time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) +
            str(time.time()).replace('.', '')[-7:]
        )
        return order_code

    def sign(
        self,
        timestamp: str,
        nonce_str: str,
        apiclient_key_path: str,
        methon: str = 'GET',
        url: str = '/v3/certificates',
        data: dict = None
    ):
        """使用商户私钥对待签名串进行SHA256 with RSA签名，并对签名结果进行Base64编码得到签名值

        Args:
            methon (str): 请求方法，默认为：GET
            url (str): 请求地址，默认为：/v3/certificates
            timestamp (str): 时间戳
            nonce_str (str): 随机字符串
            apiclient_key_path (str): 私钥文件路径
            data (dict, optional): 请求报文主体，默认为 None.

        Returns:
            rsa_signature (str): 签名值
        """
        with open(apiclient_key_path, 'rb') as f:
            private_key = f.read()

        sign_str = methon + '\n' + url + '\n' + timestamp + '\n' + nonce_str + '\n' + data + '\n'
        signature = sha256(sign_str.encode("utf-8")).digest()
        rsa_signature = base64.b64encode(private_key.sign(signature, "sha256"))
        authorization = f'WECHATPAY2-SHA256-RSA2048 mchid="{self.mchid}",nonce_str="{nonce_str}",signature="{rsa_signature}",timestamp="{timestamp}",serial_no="{self.serial_no}"'
        result = httpx.get(
            url="https://api.mch.weixin.qq.com/v3/certificates",
            headers={'Authentication': authorization}
        )
        return result.content
