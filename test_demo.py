
# -*- coding: UTF-8 -*-
import requests
import pytest
from jsonpath import jsonpath
import pprint


# wwc9fe6fa0dd4c68c2

# CeQN7L - y8O7jXaS6lUqs9NJC - J1tovzLTDeOHhlEgqg


def get_token(uid,secret):

    url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={uid}&corpsecret={secret}"
    r=requests.get(url=url)
    # pprint.pprint(r.json())
    # print(r.json()['access_token'])
    return r.json()['access_token']

def add_num(uid,secret):
    token=get_token(uid,secret)
    url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    headers = {'content-type':'application/json'}
    num_body={
    "userid": "tianshi",
    "name": u'田十',
    "mobile":"13190909087",
    "department":"1"
    }

    r=requests.post(url=url,json=num_body,headers=headers)
    try:
        assert r.json()['errcode']==0
    except AssertionError:
        print('报错了')

def delete_num(uid,secret,userid):
    token=get_token(uid,secret)
    url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}"
    r=requests.get(url=url)
    print(r.json())


if __name__ == '__main__':
    uid='wwc9fe6fa0dd4c68c2'
    secret='CeQN7L-y8O7jXaS6lUqs9NJC-J1tovzLTDeOHhlEgqg'
    userid='tianqi'
    delete_num(uid,secret,userid)