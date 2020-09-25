import random

from tools.api import request_tool


def test_get_params(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询单个用户'  # allure报告中二级分类
    title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/getCustomer"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"phone":'18103909786'}
    headers={"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_get_all(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询所有用户'  # allure报告中二级分类
    title = "查询所有用户_全字段正常流_2"  # allure报告中用例名字
    uri = "/cst/getAll/{}/{}" .format(1,9) # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = None
    headers={"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_get_file(pub_data,db):
    file_name = "d:\\sku.xlsx" # 下载文件地址
    method = "GET"  #请求方法，全部大写
    feature = "库存模块"  # allure报告中一级分类
    story = '下载某产品的库存信息'  # allure报告中二级分类
    title = "下载某产品的库存信息_全字段正常流_3"  # allure报告中用例名字
    uri = "/product/downProdRepertory"  # 接口地址
    r = db.select_execute("SELECT product_code FROM t_prod_product")
    print (r)
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"pridCode":random.choices(r)[0]}
    headers= {"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
    with open(file_name,"wb") as f :
        f.write(r.content)

def test_post_file(pub_data):
    file_name = "d:\\sku.xlsx" # 上传文件地址
    method = "POST"  #请求方法，全部大写
    feature = "库存模块"  # allure报告中一级分类
    story = '盘点库存'  # allure报告中二级分类
    title = "盘点库存_全字段正常流_4"  # allure报告中用例名字
    uri = "/product/uploaProdRepertory"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    files = {"file":open(file_name,'rb')}
    headers={"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,files=files,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

import pytest
from tools.data import excel_tool

data = excel_tool.get_test_case("d:\\充值接口测试数据.xlsx")
@pytest.mark.parametrize("account_Name,change_Money,expect_",data[1],ids=data[0])
def test_recharge(pub_data,account_Name,change_Money,expect_):
    pub_data["account_Name"] = account_Name
    pub_data["change_Money"] = change_Money
    method = "POST"  #请求方法，全部大写
    feature = "账户管理"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "None_全字段正常流_5"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    json_data='''{
  "accountName": "${account_Name}",
  "changeMoney": "${change_Money}"
}'''
    status_code = 200  # 响应状态码
    expect = expect_  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
