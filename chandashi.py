"""
┌─┐┬ ┬ ┬┌─┐┬┌─┬ ┬┌─┐┬─┐
├┤ │ └┬┘└─┐├┴┐└┬┘├┤ ├┬┘
└  ┴─┘┴ └─┘┴ ┴ ┴ └─┘┴└─
Time    : 2022-07-17 13:33
Topic   : 蝉大师接口数据抓取
            https://www.chandashi.com/new/android/keyword?appId=239857072
"""

import time
import requests
from pandas import DataFrame

# 这里的cookies仅作为演示，请自行抓取替换
cookies = {
    '...': '...'
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
    # 接口未限制最大值取值范围，这里可以任意修改
    'pageSize': '20000',
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

resp = response.json()
data_list = resp['data']['list']

data_dict = {
    "关键词": [],
    "排名": [],
    "变动": [],
    "热度": [],
    "结果数": [],
    "关键词ID": [],
    "更新时间": [],
    "先前排名": [],
}

index = 0
index_dict = {
    '序号': []
}

# 通过循环来获取响应数据，并添加到字典中
for line in data_list:
    index += 1
    index_dict['序号'].append(index)
    data_dict['关键词'].append(line['keyword'])
    data_dict['排名'].append(line['rank'])
    data_dict['热度'].append(line['priority'])
    data_dict['结果数'].append(line['result'])
    data_dict['关键词ID'].append(line['keywordId'])
    data_dict['更新时间'].append(line['updateTime'])

    if line['change'] == 99999:
        data_dict['变动'].append('进榜')
    elif line['change'] == -99999:
        data_dict['变动'].append('掉榜')
    else:
        data_dict['变动'].append(line['change'])

    if line['prevRank'] == 99999:
        data_dict['先前排名'].append('进榜')
    elif line['prevRank'] == -99999:
        data_dict['先前排名'].append('掉榜')
    else:
        data_dict['先前排名'].append(line['prevRank'])

print('正在写入Excel，请稍候......')

filename = '蝉大师抓取结果-%s.xlsx' % time.strftime('%Y%m%d%H%M%S')
dataForm = DataFrame(data_dict, index=index_dict['序号'])
dataForm.to_excel(filename)

print('导出成功，文件名：%s' % filename)
