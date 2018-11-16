import json
import requests
import re
def answer(ask):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    body = {
	    "reqType":0,
        "perception": {
            "inputText": {
                "text": ""
            }
        },
        "userInfo": {
            "apiKey": "#",
            "userId": "263212"
        }
    }
    body['perception']['inputText']['text'] = ask
    data = json.dumps(body)
    response = requests.post(url, data = data)
    retext = response.text
    answ = re.compile('{.*?results":.*?values.*?text":"(.*?)"}', re.S)
    text = re.findall(answ, retext)
    text = str(text[0])
    return text
