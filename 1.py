import itchat
from itchat.content import *

# 不带参数注册，所有消息asdasdasd 类型都将调用该方法（包括群消息）
@itchat.msg_register(TEXT)
def text_reply(msg):
    return '我已收到您发送的消息: %s   [From FunkPythonHelper]但是我现在正在上班，无法及时回复您，有急事请拨打电话15507310090' % msg['Text']

# 带参数注册，该类消息类型将调用该方法
@itchat.msg_register([MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    itchat.send('我已收到您发送的消息：%s: %s   [From FunkPythonHelper]但是我现在正在上班，无法及时回复您，有急事请拨打电话15507310090' % (msg['Type'], msg['Text']), msg['FromUserName'])

itchat.auto_login()
itchat.run()