import unittest
from unittest_kashixitong.public.get_cookie_kaoshi import *


class HouTai(unittest.TestCase):
    def test_001_login(self):
        url_k = 'http://101.200.61.210:8087/api/user/login'
        headers_k = {'Content-Type': 'application/json'}
        params_k = {"userName": "admin", "password": "123456", "remember": False}
        result_k = requests.post(url_k, json=params_k, headers=headers_k)
        print(result_k.json())
        expect_result='成功'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_002_xueshenglist(self):
        url_k = 'http://101.200.61.210:8087/api/admin/user/page/list'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie_2('admin','123456')}
        params_k = {"userName":"","role":1,"pageIndex":1,"pageSize":10}
        result_k = requests.post(url_k, json=params_k, headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_003_jinyong(self):
        url_k = 'http://101.200.61.210:8087/api/admin/user/changeStatus/100861274'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie_2('admin','123456')}
        result_k = requests.post(url_k, headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_004_qiyong(self):
        url_k = 'http://101.200.61.210:8087/api/admin/user/changeStatus/100861272'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie_2('admin','123456')}
        result_k = requests.post(url_k, headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_005_edit(self):
        url_k = 'http://101.200.61.210:8087/api/admin/user/edit'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie_2('admin','123456')}
        params_k = {"id":551,"userUuid":"3d3d1481-ddfe-4646-bb83-3be96849cfdc","userName":"mb210061050","realName":"hhh","age":"18","role":1,"sex":1,"birthDay":"2021-10-04T16:00:00.000Z","phone":"123456","lastActiveTime":"2021-06-08 20:59:22","createTime":"2021-06-08 20:59:22","modifyTime":"","status":1,"userLevel":10,"imagePath":'',"password":"123456"}
        result_k = requests.post(url_k, json=params_k, headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_006_loglist(self):
        url_k = 'http://101.200.61.210:8087/api/admin/user/event/page/list'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie_2('admin','123456')}
        params_k = {"userId":"100861272","userName":'',"pageIndex":1,"pageSize":10}
        result_k = requests.post(url_k, json=params_k, headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_007_delete(self):
        url_k = 'http://101.200.61.210:8087/api/admin/user/delete/100861278'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie_2('admin','123456')}
        result_k = requests.post(url_k, headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_008_selectstudent(self):
        url_k = 'http://101.200.61.210:8087/api/admin/user/page/list'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie_2('admin','123456')}
        params_k = {"userName":"tjj001","role":1,"pageIndex":1,"pageSize":10}
        result_k = requests.post(url_k, json=params_k, headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)

    def test_009_insertstudent(self):
        url_k = 'http://101.200.61.210:8087/api/admin/user/edit'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie_2('admin','123456')}
        params_k = {"id":27895,"userName":"xialuoke","password":"123456","realName":"夏洛克","role":1,"status":1,"age":"32","sex":1,"birthDay":"1921-07-12T16:00:00.000Z","phone":"221","userLevel":12}
        result_k = requests.post(url_k, json=params_k, headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)


    def test_010_logout(self):
        url_k = 'http://101.200.61.210:8087/api/user/logout'
        headers_k = {'Content-Type': 'application/json','Cookie' : 'SESSION=%s'%get_cookie_2('admin','123456')}
        result_k = requests.post(url_k, headers=headers_k)
        print(result_k.json())
        expect_result = '成功'
        self.assertEqual(result_k.json()['message'], expect_result)



if __name__ == '__main__':
    unittest.main()
