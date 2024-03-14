import zgrobot

robot = zgrobot.ZgRoBot(token='tokenhere')

@robot.text
def hello_world(message):
    return 'Hello World!'

if __name__ == '__main__':
    # 让服务器监听在 127.0.0.1:8080
    robot.run(host='127.0.0.1', port=8080)
