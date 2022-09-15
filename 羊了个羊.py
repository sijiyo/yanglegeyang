import requests
import vthread


@vthread.pool(100) #线程
def ppp(_i):
    url = "https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time=27&rank_role=1&skin=1"

    headers = {
        'Host': 'cat-match.easygame2021.com',
        'Connection': 'keep-alive',
        't': '',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI MiniGame WindowsWechat',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx141bfb9b73c970a9/15/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-us,en',
    }

    r = requests.get(url, headers=headers)
    print(_i, r.text)


if __name__ == '__main__':
    for i in range(1):
        ppp(i)