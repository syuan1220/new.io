from linebot import LineBotApi, WebhookHandler
from flask import Flask, request, abort, render_template
from linebot.models import *


line_bot_api = LineBotApi('y+9fpI5QjnXrVEywQkcRanFwQMMkvnPZQZ6mWHelzEPcbfgXfrdCqy+EeWnQX6TmcnPdJFlq9Z7mGCMCRDS4UyoG6Azz4T2g9lg4LUyqLmQXrEcLqI/vWD2C0PkZiRzm8ygo5FzrlOzFVjYSH+W5yAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('476fb06bb0b5aa6408ca7719e48432b8')

liffid = '2000392649-rAO3LEM6'

app = Flask(__name__)


@app.route('/page')
def page():
    return render_template('new.html', liffid = liffid)



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    # if mtext == '@彈性配置':
    #     sendFlex(event)

    if mtext[:3] == '###' and len(mtext) > 3:
        manageForm(event, mtext)

    # def sendFlex(event):
    #     try:
    #         bubble = BubbleContainer(
    #             direction='ltr',
    #             header=BoxComponent(
    #                 layout='vertical',
    #             )
    #         )
    
    def manageForm(event,mtext):
        try:
            flist = mtext[3:].split('/')
            text1 = '日期' + flist[0] + '\n'
            text1 += '時間' + flist[1] + '\n'
            text1 += '收縮壓' + flist[2] + '\n'
            text1 += '舒張壓' + flist[3] + '\n'
            message = TextSendMessage(
                text = text1
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,message,
                                       TextSendMessage(text='發生錯誤!'))