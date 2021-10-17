import requests

r=requests.get(url="https://www.toutiao.com/article/v2/tab_comments/?aid=24&app_name=toutiao_web&offset"
                   "=0&count=20&group_id=7018327911971226149&item_id=7018327911971226149&_signature"
                   "=_02B4Z6wo00f01cK3AJAAAIDD8ablMj1TsSXCkgQAABHNLXPKj7NQA4hmW.-EDiV7G4Imih3mahN9uVYdY2kuI6-6a2nWqnY5-"
                   "hezLepJKMTNAOwSM5h3Dl9JmoXkRwTCM9rpKxEqd05X21Iwc2")
json_result=r.json()
# print(json_result['data'][0]['comment']['text'])
for line in json_result['data']:
    print(line['comment']['text'])