import requests


url_article='http://182.92.178.83:8081/article/all?state=-1&page=1&count=6&keywords= '
headers_a={'cookie':'JSESSIONID=38182570CCC7114AAC7AE259E6965A34','Content-Type': 'application/x-www-form-urlencoded'}
result_a=requests.get(url_article,headers=headers_a)
print(result_a.json())


# url_lanmu='http://182.92.178.83:8081/admin/category/all'
# headers_l={'cookie':'JSESSIONID=38182570CCC7114AAC7AE259E6965A34','Content-Type': 'application/x-www-form-urlencoded'}
# result_l=requests.get(url_lanmu,headers=headers_l)
# print(result_l.json())