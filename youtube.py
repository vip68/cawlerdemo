"""
┌─┐┬ ┬ ┬┌─┐┬┌─┬ ┬┌─┐┬─┐
├┤ │ └┬┘└─┐├┴┐└┬┘├┤ ├┬┘
└  ┴─┘┴ └─┘┴ ┴ ┴ └─┘┴└─
Time    : 2022-07-18 10:24
Topic   : YouTube接口数据抓取
            https://studio.youtube.com/channel/UCHN9P-CQVBQ1ba8o1NQJVCA/videos/upload
"""

import time
import json
import requests


def get_api_response(proxies=None, page_size=100, page_token=None):
    """
    获取接口响应
    :param proxies:
    :param page_size:
    :param page_token:
    :return:
    """
    cookies = {
        'PREF': 'tz=Asia.Shanghai',
    }

    headers = {
        'authority': 'studio.youtube.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'authorization': 'SAPISIDHASH 1658110855_c998e4f5f5fd554f00c4416d191f1092a96879bd',
        'cache-control': 'no-cache',
        'origin': 'https://studio.youtube.com',
        'pragma': 'no-cache',
        'referer': 'https://studio.youtube.com/channel/UCHN9P-CQVBQ1ba8o1NQJVCA/videos/upload?c=UCHN9P-CQVBQ1ba8o1NQJVCA&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"103.0.5060.114"',
        'sec-ch-ua-full-version-list': '".Not/A)Brand";v="99.0.0.0", "Google Chrome";v="103.0.5060.114", "Chromium";v="103.0.5060.114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"14.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-client-data': 'CKa1yQEIl7bJAQimtskBCMO2yQEIqZ3KAQjq88oBCJahywEI2+/LAQjducwBCIK7zAEIirvMAQi0vMwBCM+8zAEIxb/MAQj7wMwBGKupygE=',
        'x-goog-authuser': '0',
        'x-goog-pageid': 'undefined',
        'x-goog-visitor-id': 'CgtYVlFRY3ZVMGNIMCiGh9OWBg%3D%3D',
        'x-origin': 'https://studio.youtube.com',
        'x-youtube-ad-signals': 'dt=1658110854657&flash=0&frm&u_tz=480&u_his=35&u_h=1080&u_w=1920&u_ah=1032&u_aw=1920&u_cd=24&bc=31&bih=961&biw=1143&brdim=0%2C0%2C0%2C0%2C1920%2C0%2C1920%2C1032%2C1143%2C961&vis=1&wgl=true&ca_type=image',
        'x-youtube-client-name': '62',
        'x-youtube-client-version': '1.20220711.03.00',
        'x-youtube-delegation-context': 'EhhVQ0hOOVAtQ1FWQlExYmE4bzFOUUpWQ0EqAggG',
        'x-youtube-page-cl': '460244062',
        'x-youtube-page-label': 'youtube.studio.web_20220711_03_RC00',
        'x-youtube-time-zone': 'Asia/Shanghai',
        'x-youtube-utc-offset': '480',
    }

    params = {
        'alt': 'json',
        'key': 'AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo',
    }

    json_data = {
        'filter': {
            'and': {
                'operands': [
                    {
                        'channelIdIs': {
                            'value': 'UCHN9P-CQVBQ1ba8o1NQJVCA',
                        },
                    },
                    {
                        'videoOriginIs': {
                            'value': 'VIDEO_ORIGIN_UPLOAD',
                        },
                    },
                ],
            },
        },
        'order': 'VIDEO_ORDER_DISPLAY_TIME_DESC',
        'pageSize': page_size,
        'mask': {
            'channelId': True,
            'videoId': True,
            'lengthSeconds': True,
            'premiere': {
                'all': True,
            },
            'status': True,
            'thumbnailDetails': {
                'all': True,
            },
            'title': True,
            'draftStatus': True,
            'downloadUrl': True,
            'watchUrl': True,
            'shareUrl': True,
            'permissions': {
                'all': True,
            },
            'timeCreatedSeconds': True,
            'timePublishedSeconds': True,
            'origin': True,
            'livestream': {
                'all': True,
            },
            'privacy': True,
            'contentOwnershipModelSettings': {
                'all': True,
            },
            'features': {
                'all': True,
            },
            'responseStatus': {
                'all': True,
            },
            'statusDetails': {
                'all': True,
            },
            'description': True,
            'metrics': {
                'all': True,
            },
            'publicLivestream': {
                'all': True,
            },
            'publicPremiere': {
                'all': True,
            },
            'titleFormattedString': {
                'all': True,
            },
            'descriptionFormattedString': {
                'all': True,
            },
            'audienceRestriction': {
                'all': True,
            },
            'monetization': {
                'all': True,
            },
            'selfCertification': {
                'all': True,
            },
            'allRestrictions': {
                'all': True,
            },
            'mfkSettings': {
                'all': True,
            },
            'inlineEditProcessingStatus': True,
            'videoPrechecks': {
                'all': True,
            },
            'videoStreamUrl': True,
            'videoResolutions': {
                'all': True,
            },
            'scheduledPublishingDetails': {
                'all': True,
            },
            'visibility': {
                'all': True,
            },
            'privateShare': {
                'all': True,
            },
            'sponsorsOnly': {
                'all': True,
            },
            'unlistedExpired': True,
            'videoTrailers': {
                'all': True,
            },
            'remix': {
                'isSource': True,
            },
            'shorts': {
                'all': True,
            },
        },
        'context': {
            'client': {
                'clientName': 62,
                'clientVersion': '1.20220711.03.00',
                'hl': 'zh-CN',
                'gl': 'US',
                'experimentsToken': '',
                'utcOffsetMinutes': 480,
                'screenWidthPoints': 1143,
                'screenHeightPoints': 961,
                'screenPixelDensity': 1,
                'screenDensityFloat': 1,
                'userInterfaceTheme': 'USER_INTERFACE_THEME_LIGHT',
            },
            'request': {
                'returnLogEntry': True,
                'internalExperimentFlags': [],
            },
            'user': {
                'delegationContext': {
                    'externalChannelId': 'UCHN9P-CQVBQ1ba8o1NQJVCA',
                    'roleType': {
                        'channelRoleType': 'CREATOR_CHANNEL_ROLE_TYPE_VIEWER',
                    },
                },
                'serializedDelegationContext': 'EhhVQ0hOOVAtQ1FWQlExYmE4bzFOUUpWQ0EqAggG',
            },
            'clientScreenNonce': 'MC4yNzYzMTYwOTYxMzcyMzc3Mw..',
        },
    }

    if page_token:
        json_data.update(pageToken=page_token)

    response = requests.post('https://studio.youtube.com/youtubei/v1/creator/list_creator_videos',
                             params=params, cookies=cookies, headers=headers, json=json_data, proxies=proxies)

    return response


def get_api_data(proxies):
    """
    获取接口数据
    :param proxies:
    :return:
    """
    resp = get_api_response(proxies)
    resp_data = resp.json()
    page_token = resp_data.get('nextPageToken')
    data_list = get_data(resp_data)

    page = 1

    while page_token:
        time.sleep(1)
        page += 1
        print('当前页面：%d' % page)

        resp = get_api_response(proxies, page_token=page_token)
        resp_data = resp.json()
        page_token = resp_data.get('nextPageToken')
        data_list.extend(get_data(resp_data))

    print('共 %d 条数据' % len(data_list))

    return data_list


def get_data(resp_data):
    """
    获取数据
    :param resp_data:
    :return:
    """
    data_list = []
    videos = resp_data.get('videos')

    for video in videos:
        created_seconds = int(video.get('timeCreatedSeconds', 0))
        created_date = '-' if created_seconds == 0 else time.strftime('%Y-%m-%d', time.localtime(created_seconds))

        published_seconds = int(video.get('timePublishedSeconds', 0))
        published_date = '-' if published_seconds == 0 else time.strftime('%Y-%m-%d', time.localtime(published_seconds))

        metrics = video.get('metrics', {})
        all_count = int(metrics.get('likeCount', 0)) + int(metrics.get('dislikeCount', 0))
        ratio = (int(metrics.get('likeCount', 0)) / all_count) if all_count > 0 else 0

        data_dict = {
            'videoId': video.get('videoId', ''),
            'title': video.get('title', ''),
            'created': created_date,
            'published': published_date,
            'viewCount': int(metrics.get('viewCount', 0)),
            'commentCount': int(metrics.get('commentCount', 0)),
            'likeCount': int(metrics.get('likeCount', 0)),
            'dislikeCount': int(metrics.get('dislikeCount', 0)),
            'ratio': ratio,
        }
        data_list.append(data_dict)

    return data_list


if __name__ == '__main__':
    proxies = {'https': 'http://127.0.0.1:11832'}

    data_list = get_api_data(proxies)

    with open('youtube_result.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f)
