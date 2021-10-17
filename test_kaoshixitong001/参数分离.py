import requests
from common.params import *


# url_article='http://182.92.178.83:8081/article/all'
# headers_a={'cookie':'JSESSIONID=D06A3AE78266308F6805843F8B232513','Content-Type': 'application/x-www-form-urlencoded'}
# params_a=handle_params('state=-1&page=1&count=6&keywords= ')
# result_a=requests.get(url_article,headers=headers_a,params=params_a)
# print(result_a.json())
# print(result_a.url)
#
# url_article = 'http://182.92.178.83:8081/article/all'
# headers_a = {'cookie': 'JSESSIONID=D06A3AE78266308F6805843F8B232513',
#                  'Content-Type': 'application/x-www-form-urlencoded'}
# params_a = handle_params('state=-1&page=1&count=6&keywords= ')
# keywords_list=['test','222','好消息']
# state_list=['-1','0']
# for key in keywords_list:
#     params_a['keywords']=key
#     for state in state_list:
#         params_a['state']=state
#         result_a = requests.get(url_article, headers=headers_a, params=params_a)
#         print(result_a.json())
#         print(result_a.url)


url_article = 'http://182.92.178.83:8081/article/all'
headers_a = {'cookie': 'JSESSIONID=D06A3AE78266308F6805843F8B232513',
                 'Content-Type': 'application/x-www-form-urlencoded'}
params_a = handle_params('state=-1&page=2&count=2&keywords= ')
params_a['keywords']='t'
result_a = requests.get(url_article, headers=headers_a, params=params_a)
# print(result_a.json())
for line in result_a.json()['articles']:
    print(line['title'])
    print(result_a.url)
# keywords_list=['t']
# # state_list=['-1','0']
# for key in keywords_list:
#     params_a['keywords']=key
#     # params_a['state'] = state
#     result_a = requests.get(url_article, headers=headers_a, params=params_a)
#     print(result_a.json()['articles'][0]['title'])
#     print(result_a.url)
#     # for state in state_list:
#     #     params_a['state']=state
#     #     result_a = requests.get(url_article, headers=headers_a, params=params_a)
#     #     print(result_a.json())
#     #     print(result_a.url)
