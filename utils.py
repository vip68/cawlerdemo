"""
┌─┐┬ ┬ ┬┌─┐┬┌─┬ ┬┌─┐┬─┐
├┤ │ └┬┘└─┐├┴┐└┬┘├┤ ├┬┘
└  ┴─┘┴ └─┘┴ ┴ ┴ └─┘┴└─
Time    : 2022-07-17 13:03
Topic   : 常用工具集合
"""

import random
import hashlib
import pytesseract
from PIL import Image

#################### 修改为你的tesseract安装目录 ####################
tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
#################### 修改为你的tesseract安装目录 ####################
pytesseract.pytesseract.tesseract_cmd = tesseract_cmd


def download_captcha(captcha_path, content):
    """
    下载验证码
    :param captcha_path:
    :param content:
    :return:
    """
    with open(captcha_path, 'wb') as f:
        f.write(content)

    return captcha_path


def identify_code(code_path):
    """
    识别验证码
    :param code_path:
    :return:
    """
    im = Image.open(code_path)
    code = pytesseract.image_to_string(im)

    return code.strip()


def get_random():
    """
    获取随机数
    :return:
    """
    return random.random()


def get_md5(value):
    """
    获取md5值
    :param value:
    :return:
    """
    md5_value = hashlib.md5(value.encode(encoding='utf-8')).hexdigest()

    return md5_value
