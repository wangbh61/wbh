import pytest

from tools.api import request_tool
'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''

@pytest.mark.demo
def test_signup(pub_data):
    pub_data["userName"] = "自动生成 字符串 2,9 数字 w"
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户注册'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "注册成功"  # 预期结果
    json_data='''{
  "phone": "自动生成 手机号",
  "pwd": "1321dfg",
  "rePwd": "1321dfg",
  "userName": "${userName}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

@pytest.mark.demo
def test_login(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_2"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "登录成功"  # 预期结果
    json_data='''{
  "pwd": "1321dfg",
  "userName": "${userName}"
}'''
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"token": "$['data']['token']"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_recharge(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_3"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "充值成功"  # 预期结果
    json_data='''{
  "accountName": "${userName}",
  "changeMoney": "自动生成 数字 5000,8000000"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_getAccInfo(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '查询单个账户'  # allure报告中二级分类
    title = "全字段正常流_4"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'accountName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_getBills(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '查询资金流水'  # allure报告中二级分类
    title = "全字段正常流_5"  # allure报告中用例名字
    uri = "/acc/getBills"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'accountName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_charge(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '扣款'  # allure报告中二级分类
    title = "全字段正常流_6"  # allure报告中用例名字
    uri = "/acc/charge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "扣款成功"  # 预期结果
    json_data='''{
  "accountName": "${userName}",
  "changeMoney": "1"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_getAccInfo1(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '查询单个账户'  # allure报告中二级分类
    title = "全字段正常流_7"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'accountName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_getBills1(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '查询资金流水'  # allure报告中二级分类
    title = "全字段正常流_8"  # allure报告中用例名字
    uri = "/acc/getBills"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'accountName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_withdraw(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '提现'  # allure报告中二级分类
    title = "全字段正常流_9"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "提现成功"  # 预期结果
    json_data='''{
  "accountName": "${userName}",
  "cardNo": "自动生成 字符串 10,18 数字",
  "changeMoney": "1"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_getAccInfo2(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '查询单个账户'  # allure报告中二级分类
    title = "全字段正常流_10"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'accountName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_getBills2(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '查询资金流水'  # allure报告中二级分类
    title = "全字段正常流_11"  # allure报告中用例名字
    uri = "/acc/getBills"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'accountName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_accLock(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '账户冻结'  # allure报告中二级分类
    title = "全字段正常流_12"  # allure报告中用例名字
    uri = "/acc/accLock"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "账户冻结成功"  # 预期结果
    data={'accountName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_recharge1(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_13"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "该账户正处在冻结状态，无法充值"  # 预期结果
    json_data='''{
  "accountName": "${userName}",
  "changeMoney": "自动生成 数字 1,80000"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_withdraw1(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '提现'  # allure报告中二级分类
    title = "全字段正常流_14"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "该账户正处在冻结状态，无法提现"  # 预期结果
    json_data='''{
  "accountName": "${userName}",
  "cardNo": "自动生成 字符串 10,18 数字",
  "changeMoney": "100"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_charge1(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '扣款'  # allure报告中二级分类
    title = "全字段正常流_15"  # allure报告中用例名字
    uri = "/acc/charge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "扣款成功"  # 预期结果
    json_data='''{
  "accountName": "${userName}",
  "changeMoney": "1"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_accUnLock(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '账户解冻'  # allure报告中二级分类
    title = "全字段正常流_16"  # allure报告中用例名字
    uri = "/acc/accUnLock"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "账户解冻成功"  # 预期结果
    data={'accountName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_recharge2(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_17"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "充值成功"  # 预期结果
    json_data='''{
  "accountName": "${userName}",
  "changeMoney": "自动生成 数字 1,80000"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_withdraw2(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '提现'  # allure报告中二级分类
    title = "全字段正常流_18"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "提现成功"  # 预期结果
    json_data='''{
  "accountName": "${userName}",
  "cardNo": "自动生成 字符串 10,18 数字",
  "changeMoney": "100"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
