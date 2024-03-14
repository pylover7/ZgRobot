# coding=utf-8
# @FileName  :fastapi_router.py
# @Time      :2023/5/19 22:18
# @Author    :Pylover
import html

from fastapi import Request
from fastapi.responses import HTMLResponse, Response, PlainTextResponse

from zgrobot.robot import BaseRoBot


async def make_view(robot: BaseRoBot):
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

        @app.get("/")
        @app.post("/")
        async def index(request: Request):
            return await (await fastapi_router.make_view(robot=robot))(request)

    :param robot: 一个 BaseRoBot 实例
    :return: 一个 FastApi Response 对象
    """

    async def zgrobot_view(request: Request):
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
            return PlainTextResponse(request.query_params.get("echostr"))

        body = await request.body()
        message = robot.parse_message(
            body=body,
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
