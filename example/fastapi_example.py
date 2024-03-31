import time
import uvicorn as uvicorn
from fastapi import FastAPI, Request, Response

from zgrobot import ZgRoBot
from zgrobot.contrib.fastapi import make_view
from zgrobot.contrib import fastapi_router

app = FastAPI()
robot = ZgRoBot(token="qazxswedc")


@robot.handler
def hello():
    return "Hello World"

# 关键词回复
@robot.filter("3")
def key_reply(message):
    time.sleep(3)
    return "你也好呀"


# app.mount("/", WSGIMiddleware(robot.wsgi))
@app.get("/")
@app.post("/")
async def index(request: Request):
    return await (await fastapi_router.make_view(robot=robot))(request)

@app.get("/pay")
async def pay_code(response: Response):
    print(response.body, response.status_code)


# app.add_route("/", make_view(robot=robot), methods=["GET", "POST"])

if __name__ == '__main__':
    uvicorn.run('fastapi_example:app', host="127.0.0.1", port=8077, reload=True)
