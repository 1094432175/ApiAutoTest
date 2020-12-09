'''
fixture 带参数
'''
import pytest
import requests

@pytest.fixture(params=[{"username":"root","pwd":"123456"},
                        {"username":"admin","pwd":"888888"},
                        {"username":"administrator","pwd":"HelloPwd"},
                        "four",
                        5])

def login_data(request):#参数request是固定的,不能写成其他
    return request.param#使用request.param返回每组数据

#测试逻辑(测试步骤)
#登录功能的测试脚本
def test_login(login_data):
    print(f"测试登录功能,测试数据为:{login_data}")

#练习:注册接口的测试代码,用这种方式来实现


url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"

@pytest.fixture(params=[{"data":{"mobilephone":"13133333310","pwd":"123456"},"expect":{"msg":"手机号码已被注册","code":"20110"}},
                        {"data":{"mobilephone":"13821111114","pwd":"123456789098765432"},"expect":{"msg":"手机号码已被注册","code":"20110"}},
                        {"data":{"mobilephone":"13821111116","pwd":"123456"},"expect":{"msg":"手机号码已被注册","code":"20110"}},
                        {"data":{"mobilephone":"13821111114","pwd":"123456789009876543"},"expect":{"msg":"手机号码已被注册","code":"20110"}}
                        ])

def register_data(request):
    return request.param

def test_register(register_data):
    r = requests.post(url, data=register_data['data'])
    print(r.text)
    print(r.json())
    print("测试数据:",register_data['data'])
    print("预期结果:",register_data['expect'])
    assert r.json()['msg'] == register_data['expect']['msg']
    assert r.json()['code'] == register_data['expect']['code']



