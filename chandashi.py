"""
┌─┐┬ ┬ ┬┌─┐┬┌─┬ ┬┌─┐┬─┐
├┤ │ └┬┘└─┐├┴┐└┬┘├┤ ├┬┘
└  ┴─┘┴ └─┘┴ ┴ ┴ └─┘┴└─
Time    : 2022-07-17 13:33
Topic   : 蝉大师接口数据抓取
            https://www.chandashi.com/new/android/keyword?appId=239857072
"""

import json
import requests

cookies = {
    'Hm_lvt_0cb325d7c4fd9303b6185c4f6cf36e36': '1658037713',
    'cds_session_id': 'grmrs5nmgulcuoqcvkn4kf65n2',
    'cds_asm_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'
                     'eyJ1aWQiOiIyNzIzNjEiLCJpYXQiOjE2NTgwMzc3MjksImV4cCI6MTY2MDYyOTcyOX0.'
                     'mk0cWK2CJGV5fS_-JjP8J6OEDdizYxKrLMJuMa-i_6A',
    'Hm_lpvt_0cb325d7c4fd9303b6185c4f6cf36e36': '1658037731',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://www.chandashi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.chandashi.com/new/android/keyword?appId=239857072',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'appId': '239857072',
    'country': 'cn',
    'market': 'huawei',
    'page': '1',
    'pageSize': '100',
    'keyword': '',
    'minRank': '',
    'maxRank': '',
    'minPriority': '',
    'maxPriority': '',
    'minYesterdayRank': '',
    'maxYesterdayRank': '',
    'minResult': '',
    'maxResult': '',
    'minChange': '',
    'maxChange': '',
    'order': '',
}

# 请求接口数据
response = requests.post('https://www.chandashi.com/interf/v1/android/keywordCoverList',
                         cookies=cookies, headers=headers, data=data)
# 打印请求结果
print(response.json())

# 将结果保存到文件
with open('chandashi_result.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False)
