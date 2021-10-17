import requests

def  get_cookie(username,password):
    url_k = 'http://101.200.61.210:8087/api/user/login'
    headers_k = {'Content-Type': 'application/json'}
    params_k = {"userName": username, "password": password, "remember": False}
    result_k = requests.post(url_k, json=params_k, headers=headers_k)
    # print(result_k.cookies)
    cookie_dict = requests.utils.dict_from_cookiejar(result_k.cookies)
    # print(cookie_dict)
    return cookie_dict['SESSION']





if __name__ =='__main__':
    get_cookie('tjj001','123456')