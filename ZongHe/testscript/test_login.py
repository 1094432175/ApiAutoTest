'''
登录接口测试脚本
'''
import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.read_yaml("data_case\login_setup.yaml"),scope='module')
def setup_data(request):
    return request.param
@pytest.fixture(params=DataRead.read_yaml("data_case\login_data.yaml"),scope='module')
def login_data(request):
    return request.param

@pytest.fixture(scope='module')
def register(setup_data, url, db, baserequests):
    # 注册用户
    mobile = setup_data['casedata']['mobilephone']#获取手机号
    r = Member.register(url, baserequests, setup_data['casedata'])#下发注册请求
    print(r.text)
    # 检查结果:1:检查响应与预期结果一致
    assert r.json()['msg'] == setup_data['expect']['msg']
    assert r.json()['code'] == setup_data['expect']['code']
    assert r.json()['status'] == setup_data['expect']['status']
    # 检查结果:2:检查系统中用户注册成功
    # 查询用户,检查手机号在返回的结果
    r = Member.list(url, baserequests)
    assert mobile in r.text
    yield
    # 删除注册用户
    DbOp.delete_user(db, mobile)#也是清理环境


def test_login(register,login_data,url,baserequests):
    # 下发登录的请求
    r = Member.login(url,baserequests,login_data['casedata'])
    # 检查结果
    assert r.json()['msg'] == login_data['expect']['msg']
    assert r.json()['code'] == login_data['expect']['code']


