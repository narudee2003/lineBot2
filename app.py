from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    return "นฤดั สุขะ เลขที่ 17 ชั้นม.4/3"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded['originalDetectlntentRequest]['payload']['data']['replyToken']
    userText = decoded['queryReSult']['intent']['displayName']
    if(j == 'สวัสดี)
    print('ดีด้วยจ้าา'
     elif (j == 'สบายดีไหม') :
     print('ยังไม่ตายค่ะ')
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
   print('ว่าอะไรค่ะ')

    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': os.environ['Authorization']    # ตั้ง Config vars ใน heroku พร้อมค่า Access token
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
