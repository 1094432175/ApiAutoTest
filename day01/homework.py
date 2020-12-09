import requests

'''注册'''

url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
#1.验证用户使用正确的手机号、6位长度的密码、注册名为空时，注册成功
# user = {
#     "mobilephone": "13821111114",
#     "pwd": "123456",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 1
# assert r['code'] == "10001"
# assert r['msg'] == "注册成功"

#2.验证用户使用正确的手机号、18位长度的密码、注册名为空时，注册成功
# user = {
#     "mobilephone": "13821111115",
#     "pwd": "123456789098765432",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 1
# assert r['code'] == "10001"
# assert r['msg'] == "注册成功"

#3.验证用户使用正确的手机号、6位的密码、正确的注册名，注册成功
# user = {
#     "mobilephone": "13821111116",
#     "pwd": "123456",
#     "regname": "乌拉"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 1
# assert r['code'] == "10001"
# assert r['msg'] == "注册成功"

#4.验证用户使用正确的手机号、18位的密码、正确的注册名，注册成功
# user = {
#     "mobilephone": "13821111117",
#     "pwd": "123456789098765432",
#     "regname": "乌拉"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 1
# assert r['code'] == "10001"
# assert r['msg'] == "注册成功"

#5.验证用户手机号为空时、输入6位长度的密码、注册名为空时，注册失败
# user = {
#     "mobilephone": "",
#     "pwd": "123456",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20103"
# assert r['msg'] == "手机号不能为空"

#6.验证用户手机号为空时、6位长度的密码、正确的注册名，注册失败
# user = {
#     "mobilephone": "",
#     "pwd": "123456",
#     "regname": "安心吧"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20103"
# assert r['msg'] == "手机号不能为空"

#7.验证用户输入过短的手机号、6位长度的密码、注册名为空时，注册失败
# user = {
#     "mobilephone": "1383333333",
#     "pwd": "123456",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20109"
# assert r['msg'] == "手机号码格式不正确"

#验证用户输入过短手机号、6位长度的密码、正确的注册名，注册失败
# user = {
#     "mobilephone": "1383333333",
#     "pwd": "123456",
#     "regname": "啊啊啊啊"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20109"
# assert r['msg'] == "手机号码格式不正确"

#验证用户输入过长的手机号、6位长度的密码、注册名为空时，注册失败
# user = {
#     "mobilephone": "138333333333",
#     "pwd": "123456",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20109"
# assert r['msg'] == "手机号码格式不正确"

#验证用户输入过长的手机号、6位长度的密码、正确的注册名，注册失败
# user = {
#     "mobilephone": "138333333333",
#     "pwd": "123456",
#     "regname": "啊啊啊啊"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20109"
# assert r['msg'] == "手机号码格式不正确"

#11.验证用户输入非法字符手机号、6位长度的密码、注册名为空时，注册失败
# user = {
#     "mobilephone": "1383333333+",
#     "pwd": "123456",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20109"
# assert r['msg'] == "手机号码格式不正确"

#12.验证用户输入非法字符手机号、6位长度的密码、正确的注册名，注册失败
# user = {
#     "mobilephone": "1383333333+",
#     "pwd": "123456",
#     "regname": "aaaaaaaa"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20109"
# assert r['msg'] == "手机号码格式不正确"

#13.验证用户输入有汉字的手机号、6位长度的密码、注册名为空时，注册失败
# user = {
#     "mobilephone": "1383333333啊",
#     "pwd": "123456",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20109"
# assert r['msg'] == "手机号码格式不正确"

#14.验证用户输入有汉字的手机号、6位长度的密码、正确的注册名，注册失败
# user = {
#     "mobilephone": "1383333333啊",
#     "pwd": "123456",
#     "regname": "啊啊"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20109"
# assert r['msg'] == "手机号码格式不正确"

#15.验证用户输入非号段手机号、6位长度的密码、正确的注册名，注册失败
# user = {
#     "mobilephone": "23833333333",
#     "pwd": "123456",
#     "regname": "啊啊"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20109"
# assert r['msg'] == "手机号码格式不正确"

#16.验证用户输入非号段手机号、6位长度的密码、注册名为空时，注册失败
# user = {
#     "mobilephone": "23833333333",
#     "pwd": "123456",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20109"
# assert r['msg'] == "手机号码格式不正确"

#17.验证用户输入正确的手机号，过短的密码、正确的注册名，注册失败
# user = {
#     "mobilephone": "13833333331",
#     "pwd": "12345",
#     "regname": "啊啊啊啊"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20108"
# assert r['msg'] == "密码长度必须为6~18"

#18.验证用户输入正确的手机号，过短的密码、注册名为空时，注册失败
# user = {
#     "mobilephone": "13833333331",
#     "pwd": "12345",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20108"
# assert r['msg'] == "密码长度必须为6~18"

#19.验证用户输入正确的手机号，过长的密码、注册名为空时，注册失败
# user = {
#     "mobilephone": "13833333331",
#     "pwd": "1234567899876543211",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20108"
# assert r['msg'] == "密码长度必须为6~18"

#20.验证用户输入正确的手机号，过长的密码、正确的注册名，注册失败
# user = {
#     "mobilephone": "13833333331",
#     "pwd": "1234567899876543211",
#     "regname": "啊啊啊啊"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20108"
# assert r['msg'] == "密码长度必须为6~18"

#21.验证用户输入正确的手机号，密码为空、正确的注册名，注册失败
# user = {
#     "mobilephone": "13833333331",
#     "pwd": "",
#     "regname": "啊啊啊啊"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20103"
# assert r['msg'] == "密码不能为空"

#22.验证用户输入正确的手机号，密码为空、注册名为空时，注册失败
# user = {
#     "mobilephone": "13821111114",
#     "pwd": "",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20110"
# assert r['msg'] == "手机号码已被注册"

#23.验证用户输入正确的手机号，正确的密码、注册名为空时，注册失败
# user = {
#     "mobilephone": "13821111114",
#     "pwd": "123456",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20110"
# assert r['msg'] == "手机号码已被注册"

#24.验证用户输入正确的手机号，正确的密码、正确的注册名时，注册失败
# user = {
#     "mobilephone": "13821111114",
#     "pwd": "123456",
#     "regname": "啊啊啊啊啊"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20110"
# assert r['msg'] == "手机号码已被注册"

#登录
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# 1.验证会员输入正确的手机号，正确的密码，登录成功
# user = {
#     "mobilephone": "13821111114",
#     "pwd": "123456",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 1
# assert r['code'] == "10001"
# assert r['msg'] == "登录成功"

#2.验证会员输入正确的手机号，输入正确的6位的密码，登录成功
# user = {
#     "mobilephone": "13821111114",
#     "pwd": "123456",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 1
# assert r['code'] == "10001"
# assert r['msg'] == "登录成功"

#3.验证会员手机号为空，输入正确18位的密码，登录失败
# user = {
#     "mobilephone": "",
#     "pwd": "123456789098765432",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20103"
# assert r['msg'] == "手机号不能为空"

#4.验证会员输入过短的手机号，输入正确的密码，登录失败
# user = {
#     "mobilephone": "13821111114",
#     "pwd": "12345",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20111"
# assert r['msg'] == "用户名或密码错误"

#5.验证会员输入过长的手机号，输入正确的密码，登录失败
# user = {
#     "mobilephone": "138211111141",
#     "pwd": "123456",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20111"
# assert r['msg'] == "用户名或密码错误"

#6.验证会员输入未注册的手机号，输入正确的密码，登录失败
# user = {
#     "mobilephone": "13821111129",
#     "pwd": "123456",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20111"
# assert r['msg'] == "用户名或密码错误"

#7.验证会员输入正确的手机号，密码为空时，登录失败
# user = {
#     "mobilephone": "13821111114",
#     "pwd": "",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20111"
# assert r['msg'] == "用户名或密码错误"

#8.验证会员输入正确的手机号，过短的密码，登录失败
# user = {
#     "mobilephone": "13821111114",
#     "pwd": "12345",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20111"
# assert r['msg'] == "用户名或密码错误"

#9.验证会员输入正确的手机号，过长的密码，登录失败
# user = {
#     "mobilephone": "13821111114",
#     "pwd": "1234567890098765432",
#     "regname": ""
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == "20111"
# assert r['msg'] == "用户名或密码错误"





