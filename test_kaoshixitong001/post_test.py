import requests
from  common.params  import  *


# url_v='http://182.92.178.83:8081/login'
# headers_v={'Content-Type':'application/x-www-form-urlencoded'}
# params_v=handle_params('username=sang&password=123')
# result_v=requests.post(url_v,data=params_v,headers=headers_v)
# print(result_v.json())
# print(result_v.cookies)
# print(result_v.headers)

url_k='http://101.200.61.210:8087/api/user/login'
headers_k={'Content-Type':'application/json'}
params_k={"userName":"student","password":"123456","remember":False}
result_k=requests.post(url_k,json=params_k,headers=headers_k)
print(result_k.json())
print(result_k.cookies)
print(result_k.headers)