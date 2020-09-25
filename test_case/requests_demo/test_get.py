import allure
import requests

@allure.feature("get请求")
@allure.story("无参数")
@allure.title("用例名1")
def test_get_no_params():
    # 使用requests.get发送一个get请求
    # r = requests.get("https://www.baidu.com/")
    # 使用requests.request发送一个get请求
    # r = requests.request(method="GET",url="https://www.baidu.com/")
    sess = requests.session() # 使用session建立连接
    r = sess.request("GET","https://www.baidu.com/")
    print(r.text)

@allure.feature("get请求")
@allure.story("带参数")
@allure.title("用例名2")
def test_get_query():
    # get请求带参数
    par = {"accountName":"tan812826"} # 把get参数放入一个字典中
    r = requests.request("GET","http://qa.yansl.com:8084/acc/getAccInfo",params=par) # 请求时以params关键字传参

    print(r.text)

@allure.feature("get请求")
@allure.story("path参数")
@allure.title("用例名3")
def test_get_path():
    # get请求带参数在path中
    # 使用.format进行字符串格式化
    r = requests.request("GET","http://qa.yansl.com:8084/acc/getAllAccs/{pageNum}/{pageSize}".format(pageNum=2,pageSize=5))
    print(r.text)

@allure.feature("get请求")
@allure.story("下载文件")
@allure.title("用例名4")
def test_get_file(pub_data):
    # get请求下载文件
    with allure.step("第一步：准备测试数据"):pass
    p = {"pridCode":"ewhapqhs"}
    h = {"token":pub_data["token"]}
    with allure.step("第二步：发送请求"):pass
    r = requests.request("GET","http://qa.yansl.com:8084/product/downProdRepertory",params=p,headers=h)
    with allure.step("第三步：请求数据"):
        allure.attach("请求行，请求头，请求正文","请求信息",allure.attachment_type.TEXT)
    with open("123.xls","wb") as f:  # with语法 打开文件 并赋值给变量"f"
        f.write(r.content)  # write把响应的数据写入到文件中 r.content获取响应正文的字节码（二进制)
