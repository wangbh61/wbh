import allure
import requests

@allure.feature("post请求")
@allure.story("json数据")
@allure.title("用例名1")
def test_post_json():
    # 使用requests.request发送一个post请求
    # post请求json数据
    data = {"pwd": "tjf123456","userName": "tan021643"}
    r = requests.request("POST","http://qa.yansl.com:8084/login",json=data) # json关键字发送json类型数据
    print(r.text)

@allure.feature("post请求")
@allure.story("键值对数据")
@allure.title("用例名2")
def test_post_formdata(pub_data):
    # post请求键值对数据
    data = {"userName":"tan242743"}
    h = {"token":pub_data["token"]}
    r = requests.request("POST","http://qa.yansl.com:8084/user/unLock",data=data,headers=h) # data关键字发送键值对类型数据
    print(r.text)

@allure.feature("post请求")
@allure.story("上传文件")
@allure.title("用例名3")
def test_post_upload_file(pub_data):
    # post请求上传文件
    data = {"file":open("123.xls","rb")}
    h = {"token":pub_data["token"]}
    r = requests.request("POST","http://qa.yansl.com:8084/product/uploaProdRepertory",files=data,headers=h) # files关键字发送文件类型数据
    print(r.text)


