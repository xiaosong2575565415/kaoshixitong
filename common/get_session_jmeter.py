from get_cookie import *

#  打开存放用户登录信息CSV文件
zhuce_file=open('zhuce3.csv','r',encoding='utf-8')
#print(zhuce_file.readlines())
# 把登录信息，按行赋值于变量
zhuce_file_1=zhuce_file.readlines()
#print(zhuce_file_1)
# 遍历用户信息，逐行提取用户名和登录密码
for line in zhuce_file_1:
    # 修改格式，把用户名和密码单独提出来
    line1=line.split(',')
    line1[1]=line1[1].replace('\n','')
    username=str(line1[0])
    # print(username)
    password=str(line1[1])
    # 调用获取cookie函数，获取对应cookie
    cookies_new=get_cookie(username,password)
    print(cookies_new)
    # 将调好格式的cookie追加写到存放cookie的CSV文件中，方便jmeter把cookie参数化
    cookie_file=open('E:\软件测试第四阶段\\apache-jmeter-3.1\\bin\datafile\sessions.csv','a',encoding='utf-8')
    cookie_file.write('SESSION='+cookies_new+'\n')




