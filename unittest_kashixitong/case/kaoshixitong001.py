import unittest
from unittest_kashixitong.public.get_cookie_kaoshi import *


class MyTestCase(unittest.TestCase):
    def test_001_login(self):
        url_k = 'http://101.200.61.210:8087/api/user/login'
        headers_k = {'Content-Type': 'application/json'}
        params_k = {"userName": "student", "password": "123456", "remember": False}
        result_k = requests.post(url_k, json=params_k, headers=headers_k)
        print(result_k.json())
        expect_result='成功'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_002_register(self):
        url_k = 'http://101.200.61.210:8087/api/student/user/register'
        headers_k = {'Content-Type': 'application/json'}
        params_k = {"userName":"t006","password":"123456","userLevel":1}
        result_k = requests.post(url_k, json=params_k, headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_003_register(self):
        url_k = 'http://101.200.61.210:8087/api/student/user/register'
        headers_k = {'Content-Type': 'application/json'}
        params_k = {"userName":"t002","password":"123456","userLevel":1}
        result_k = requests.post(url_k, json=params_k, headers=headers_k)
        print(result_k.json())
        expect_result = '用户已存在'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_004_pagelist(self):
        url_k = 'http://101.200.61.210:8087/api/student/exam/paper/pageList'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie('tjj001','123456')}
        params_k = {"paperType":1,"subjectId":"256","pageIndex":1,"pageSize":10}
        result_k = requests.post(url_k, json=params_k, headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_005_kaoshijilu(self):
        url_k = 'http://101.200.61.210:8087/api/student/exampaper/answer/pageList'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie('tjj001','123456')}
        params_k = {"pageIndex":1,"pageSize":10}
        result_k = requests.post(url_k, json=params_k, headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)


    def test_006_cuotiben(self):
        url_k = 'http://101.200.61.210:8087/api/student/question/answer/page'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie('tjj001','123456')}
        params_k = {"pageIndex":1,"pageSize":10}
        result_k = requests.post(url_k, json=params_k, headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_007_gerenzhongxin(self):
        url_k = 'http://101.200.61.210:8087/api/student/user/current'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie('tjj001','123456')}
        # params_k = {"pageIndex":1,"pageSize":10}
        result_k = requests.post(url_k,  headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_008_yonghudongtai(self):
        url_k = 'http://101.200.61.210:8087/api/student/user/log'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie('tjj001','123456')}

        result_k = requests.post(url_k,  headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)


    def test_009_gerenxinxixiugai(self):
        url_k = 'http://101.200.61.210:8087/api/student/user/update'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie('tjj001','123456')}
        params_k = {"id":54538,"userUuid":"afff393b-07fb-4d2f-8e2d-8a5c81ac80f0","userName":"tjj001","realName":"tjj","age":"19","role":1,"sex":1,"birthDay":"2014-10-09T16:00:00.000Z","phone":"1001245657","lastActiveTime":"2021-10-10 19:05:57","createTime":"2021-10-10 19:05:57","modifyTime":"","status":1,"userLevel":1,"imagePath":''}
        result_k = requests.post(url_k, json=params_k, headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_010_logout(self):
        url_k = 'http://101.200.61.210:8087/api/user/logout'
        headers_k = {'Content-Type': 'application/json', 'Cookie': 'SESSION=%s' % get_cookie('tjj001', '123456')}
        # params_k = {"pageIndex": 1, "pageSize": 10}
        result_k = requests.post(url_k,  headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)












if __name__ == '__main__':
    unittest.main()
