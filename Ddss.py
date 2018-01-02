import itchat
import requests
from itchat.content import *


def get_reply(info):
    data = {
        'key': 'b5940ddeb4c9444ab187ea43851c19bf',
        'info': info,
        'userid': '12345678'
    }
    s = requests.post("http://www.tuling123.com/openapi/api", data=data).json()
    print(s)
    return s['text']


@itchat.msg_register(INCOME_MSG)
def text_reply(msg):
    print(msg)
    s = get_reply(msg)
    return s


try:
    itchat.auto_login()
    myname=itchat.get_friends(update=True)[0]["UserName"]
    itchat.run
except:
    print("ddddddddddddd")
