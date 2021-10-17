def handle_params(params):
    params_list=params.split('&')
    #print(params_list)
    params_dict={}
    for params_one in params_list:
        params_list2=params_one.split('=')
        params_dict[params_list2[0]]=params_list2[1]
        #print(params_list2)
    # print(params_dict)
    return params_dict




if __name__ =='__main__':
    handle_params('state=-1&page=1&count=6&keywords= ')