"""
┌─┐┬ ┬ ┬┌─┐┬┌─┬ ┬┌─┐┬─┐
├┤ │ └┬┘└─┐├┴┐└┬┘├┤ ├┬┘
└  ┴─┘┴ └─┘┴ ┴ ┴ └─┘┴└─
Time    : 2022-07-17 14:06
Topic   : 某博客管理后台登录破解
            https://admin.dlszyht.com/login.php
"""

import requests
from utils import download_captcha, identify_code

sess = requests.session()


def get_captcha():
    """
    获取验证码
    :return:
    """
    headers = {
        'authority': 'admin.dlszyht.com',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://admin.dlszyht.com/login.php',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36',
    }

    response = sess.get('https://admin.dlszyht.com/include/captcha/captcha.php', headers=headers)

    return response


def login(username, password, validate_code):
    """
    模拟登录
    :param validate_code:
    :return:
    """
    # 由于采用全局session，所以这里cookies不用带入
    # cookies = {
    #     'PHPSESSID': 'v3tnivo6lootvdujdilm5pnlj4',
    # }

    headers = {
        'authority': 'admin.dlszyht.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://admin.dlszyht.com',
        'pragma': 'no-cache',
        'referer': 'https://admin.dlszyht.com/login.php',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'username': username,
        # 子管理员标识
        'is_manager': '0',
        'userpwd': password,
        'validatecode': validate_code,
    }

    response = sess.post('https://admin.dlszyht.com/check_login.php', headers=headers, data=data)

    return response


if __name__ == '__main__':
    resp_captcha = get_captcha()
    captcha_path = download_captcha('dlszyht.jpg', resp_captcha.content)
    code = identify_code(captcha_path)

    if not code:
        print('验证码识别错误！')
    else:
        print('验证码：{}'.format(code))

        resp_login = login('test', '123456', code)

        print(resp_login.json())
