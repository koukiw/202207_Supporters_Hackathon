from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json

REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"
CHANNEL_SECRET = "4767dec262d22735f5d4f085c7800bcd"
ACCESSTOKEN = 'BSLzDq5+3GTnn2uBODxBRI1mxDvzBsUF+mwwULR0CCF5x4MM5NlDeyOmqJdIA3Q2CR+XHqGRYV1b6FZuRTFK6HYqZkiVKXYOiXT5baAySnLLtGuQ/bPHu6KU9DIMlJJUNUgxfFyZ3BVwm2FPy/WfKwdB04t89/1O/w1cDnyilFU='
HEADER = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + ACCESSTOKEN
}

class URIMessage():
    def __init__(self, messages):
        self.messages = messages

    def reply(self, reply_token):
        body = {
                'replyToken': reply_token,
                "messages": [
                    {
                        "type": "imagemap",
                        "baseUrl": "https://1.bp.blogspot.com/--L0axHlIFJ0/X0B4RtkgVQI/AAAAAAABarM/3S2zDdrLpFo6OsoPfo3_IdYZt0RIZuFVACNcBGAsYHQ/s1600/otaku_girl_fashion_penlight.png",
                        "altText": "This is an imagemap",
                        "baseSize": {
                            "width": 1040,
                            "height": 1040
                        },   
                        "actions": [
                            {
                        "type": "uri",
                        "linkUri": "https://example.com/",
                        "area": {
                            "x": 0,
                            "y": 586,
                            "width": 520,
                            "height": 454
                                }
                            },
                        {
                            "type": "message",
                            "text": "Hello",
                            "area": {
                                "x": 520,
                                "y": 586,
                                "width": 520,
                                "height": 454
                            }
                        }
                    ]   
                    }       
                ]
        }   
        print(body)
        req = urllib.request.Request(REPLY_ENDPOINT_URL, json.dumps(body).encode(), HEADER)
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err.reason)