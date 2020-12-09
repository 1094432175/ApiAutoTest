''''
发送post请求
'''

import requests
#登录的接口:
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user ={
    "mobilephone":"13821111111",
    "pwd":"123456"
}
#用data传表单参数,content-type:application/x-www-form-urlencoded
r = requests.post(url,data=user)
print(r.text)

#用data传表单
url = "http://www.httpbin.org/post"
user = {
    "mobilephone":"13821111111",
    "psd":"123456"
}
r = requests.post(url,data=user)
print(r.text)
print("*" *50) #分隔线
#用json传参数 content-type:application/json
r = requests.post(url,json=user)
print(r.text)

#练习:充值接口,给注册的用户充值
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/recharge"
user = {
    "mobilephone":"13821111111",
    "amount":300000.00
}
r = requests.post(url,data=user) #使用data还是json传参,要看接口实现的是哪个
print(r.text)
r = requests.post(url,json=user)
print(r.text)












