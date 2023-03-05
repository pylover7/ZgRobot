import uvicorn as uvicorn
from fastapi import FastAPI

from zgrobot import ZgRoBot
from zgrobot.contrib.fastapi import make_view

app = FastAPI()
robot = ZgRoBot(token="qazxswedc")


@robot.handler
def hello():
    return "Hello World"


# app.mount("/", WSGIMiddleware(robot.wsgi))
app.add_route("/", make_view(robot=robot), methods=["GET", "POST"])

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8077)
