import requests
from test_Vbuluo.public.get_cookie import *

# url_create_lanmu='http://182.92.178.83:8081/admin/category/'
# headers_create_lanmu={'Content-Type': 'application/x-www-form-urlencoded','Cookie':'JSESSIONID=%s'%get_cookie('sang','123')}
# params_create_lanmu='cateName=test_t_005&'
# result_create=requests.post(url_create_lanmu,headers=headers_create_lanmu,data=params_create_lanmu)
# print(result_create.json())

# url_eidt='http://182.92.178.83:8081/admin/category/'
# headers_eidt={'Content-Type': 'application/x-www-form-urlencoded','Cookie':'JSESSIONID=%s'%get_cookie('sang','123')}
# params_eidt='id=21375&cateName=test_t_063&'
# result_eidt=requests.put(url_eidt,headers=headers_eidt,data=params_eidt)
# print(result_eidt.json())

url_delete='http://182.92.178.83:8081/admin/category/21376'
headers={'Content-Type': 'application/x-www-form-urlencoded','Cookie':'JSESSIONID=%s'%get_cookie('sang','123')}
result_delete=requests.delete(url_delete,headers=headers)
print(result_delete.json())

