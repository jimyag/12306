import sys
import traceback

import requests

import TickerConfig


def sendSre24Push(msg: str, token: str = TickerConfig.SRE24_TOKEN, prefix: str = '[12306]'):
    try:
        if not token:
            return
        msg = prefix + msg
        rs = requests.post(url="https://push.jwks123.com/to/", json=dict(token=token, msg=msg), timeout=5).json()
        assert int(rs["code"] / 100) == 2, rs
    except:
        traceback.print_exc(file=sys.stderr)


if __name__ == '__main__':
    msg = '今晚看啥123，陪你度过好时光'
    token = 'token'
    prefix = '今晚看啥123'
    sendSre24Push(msg,token,prefix)
