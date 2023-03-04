# -*- coding: utf-8 -*-
import asyncio
import html

from fastapi import Request, Body
from fastapi.responses import HTMLResponse, Response

from zgrobot.robot import BaseRoBot


def make_view(robot: BaseRoBot):
    """
    为一个 BaseRobot 生成 FastApi View。

    Usage ::

        from zgrobot import ZgRoBot
        from zgrobot.contrib.fastapi import make_view
        from fastapi import FastAPI

        app = FastAPI()
        robot = ZgRoBot(token="qazxswedc")


        @robot.handler
        def hello():
            return "Hello World"

        app.add_route("/", make_view(robot=robot), methods=["GET", "POST"])

    :param robot: 一个 BaseRoBot 实例
    :return: 一个 FastApi Response 对象
    """
    def zgrobot_view(request: Request, body=Body()):
        timestamp = request.query_params.get("timestamp")
        nonce = request.query_params.get("nonce")
        signature = request.query_params.get("signature")

        if not robot.check_signature(
            timestamp=timestamp, nonce=nonce, signature=signature
        ):
            return HTMLResponse(
                content=robot.make_error_page(
                    html.escape(request.url.__str__()),
                ),
                status_code=403
            )
        if request.method != "POST":
            return request.path_params.get("echostr")

        message = robot.parse_message(
            body=asyncio.run(request.body()),
            timestamp=timestamp,
            nonce=nonce,
            msg_signature=request.path_params.get("msg_signature")
        )
        response = Response(
            content=robot.get_encrypted_reply(message=message),
            status_code=200,
            media_type="application/xml"
        )
        return response

    return zgrobot_view
