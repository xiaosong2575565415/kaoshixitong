import requests

def  get_cookie(username,password):
    url_v = 'http://182.92.178.83:8081/login'
    headers_v = {'Content-Type': 'application/x-www-form-urlencoded'}
    params_v = 'username=%s&password=%s&'%(username,password)
    result_v = requests.post(url_v, data=params_v, headers=headers_v)
    # print(result_v.cookies)
    cookie_dict = requests.utils.dict_from_cookiejar(result_v.cookies)
    # print(cookie_dict['JSESSIONID'])
    return cookie_dict['JSESSIONID']





if __name__ =='__main__':
    get_cookie('sang','123')