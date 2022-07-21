"""
┌─┐┬ ┬ ┬┌─┐┬┌─┬ ┬┌─┐┬─┐
├┤ │ └┬┘└─┐├┴┐└┬┘├┤ ├┬┘
└  ┴─┘┴ └─┘┴ ┴ ┴ └─┘┴└─
Time    : 2022-07-17 15:16
Topic   : 宁波产权交易中心登录破解
            http://www.nbcqjy.org/portal/login.jsp
"""

import requests
from utils import download_captcha, identify_code, get_random, get_md5

sess = requests.session()


def init_login():
    """
    初始化登录
    :return:
    """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                  'q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36',
    }

    response = sess.get('http://www.nbcqjy.org/portal/login.jsp', headers=headers, verify=False)

    return response


def get_captcha():
    """
    获取验证码
    :return:
    """
    # 由于采用全局session，所以这里cookies不用带入
    # cookies = {
    #     'JSESSIONID': '8BA7F12070747514B1905DB820D47385',
    # }

    headers = {
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://www.nbcqjy.org/portal/login.jsp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36',
    }

    # 获取随机数
    rdm = get_random()
    response = sess.get('http://www.nbcqjy.org/portal/web/CheckRandCode?{}'.format(rdm), headers=headers, verify=False)

    return response


def login(username, password, validate_code):
    """
    模拟登录
    :param username: 用户名
    :param password: 密码
    :param validate_code: 验证码
    :return:
    """
    # 由于采用全局session，所以这里cookies不用带入
    # cookies = {
    #     'JSESSIONID': '8BA7F12070747514B1905DB820D47385',
    # }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://www.nbcqjy.org',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://www.nbcqjy.org/portal/login.jsp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'username': username,
        'password': password,
        'rand': validate_code,
    }

    response = sess.post('http://www.nbcqjy.org/portal/doUsers/login', headers=headers, data=data, verify=False)

    return response


if __name__ == '__main__':
    # 初始化登录
    init_login()

    # 获取验证码
    resp_captcha = get_captcha()

    # 下载验证码
    captcha_path = download_captcha('nbcqjy.jpg', resp_captcha.content)

    # 识别验证码
    code = identify_code(captcha_path)

    if not code:
        print('验证码识别错误！')
    else:
        pwd = get_md5('123456')
        print('验证码：{} | 密码MD5：{}'.format(code, pwd))

        resp_login = login('test', pwd, code)

        print(resp_login.json())
