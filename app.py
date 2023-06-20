import requests
import string
from random import choice as ci
SS=string.ascii_letters+string.digits
url="https://api.zhtwinkle.cn/v1/chat/completions"
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
while True:
    Key="sk-"+g20()+"T3BlbkFJ"+g20()
    if f(Key):
        print(Key)
    else:
        print(Key+"  ：不合法")
