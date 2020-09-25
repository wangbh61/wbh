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
  "changeMoney": "自动生成 数字 50000,80000"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)


def test_addProd(pub_data):
    pub_data["productCode"] = "自动生成 字符串 2,9 数字 w"
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '增加产品'  # allure报告中二级分类
    title = "全字段正常流_4"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = "创建产品成功"  # 预期结果
    json_data='''{
  "brand": "阿迪达斯",
  "colors": [
    "白色"
  ],
  "price": 688,
  "productCode": "${productCode}",
  "productName": "${productCode}",
  "sizes": [
    "37"
  ],
  "type": "服装"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_fullSku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '全量调整单个商品库存'  # allure报告中二级分类
    title = "全字段正常流_5"  # allure报告中用例名字
    uri = "/product/fullSku"  # 接口地址
    headers = {"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = "更新成功"  # 预期结果
    data={'qty': '555555555', 'skuCode': '${productCode}_白色_37'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

class dfg():
    def test_addOrder(pub_data):
        method = "POST"  #请求方法，全部大写
        feature = "订单模块"  # allure报告中一级分类
        story = '明文下单'  # allure报告中二级分类
        title = "全字段正常流_6"  # allure报告中用例名字
        uri = "/order/addOrder"  # 接口地址
        headers = {"token":"${token}"}
        status_code = 200  # 响应状态码
        expect = "下单成功"  # 预期结果
        json_data='''{
      "ordeerPrice": 6880,
      "orderLineList": [
        {
          "qty": 10,
          "skuCode": "${productCode}_白色_37"
        }
      ],
      "receiver": "李越",
      "receiverPhone": "自动生成 手机号",
      "receivingAddress": "自动生成 地址",
      "userName": "${userName}"
    }'''

        # --------------------分界线，下边的不要修改-----------------------------------------
        # method,pub_data和url为必传字段
        r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
