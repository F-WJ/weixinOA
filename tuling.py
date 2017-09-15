# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = 2017 / 8 / 27
# coding=utf8
import sys, os
import requests


# 百度地图位置api
data = {
    'ip':'',
    'ak':'DpyYfGqWR10rGePKdgZqQm8CENxWWG4n',
}

res = requests.post('https://api.map.baidu.com/location/ip',data=data).json()

loc=res['content']['address']
lon=res['content']['point']['x']
lat=res['content']['point']['y']


# 图灵api，一个月只有5000次
def get_response(msg):
    url = 'http://www.tuling123.com/openapi/api'
    payloads = {
        'key': '78db6ce896154f118b89a285e540ce42',
        'info': msg,
        'userid': 'fwj',
        'loc': loc,
        'lon':lon,
        'lat':lat,
    }
    r = requests.post(url, data=payloads).json()
    if not r['code'] in (100000, 200000, 302000, 308000, 313000, 314000): return
    if r['code'] == 100000:  # 文本类
        return str(r['code'])+'\n'.join([r['text'].replace('<br>', '\n')])
    elif r['code'] == 200000:  # 果菜类和查找餐厅
        return '\n'.join([r['text'].replace('<br>', '\n'), r['url']])
    elif r['code'] == 302000:  # 新闻类
        l = [r['text'].replace('<br>', '\n')]
        for n in r['list']: l.append('%s - %s' % (n['article'], n['detailurl']))
        return '\n'.join(l)
    elif r['code'] == 308000:  # 菜谱类
        l = [r['text'].replace('<br>', '\n')]
        for n in r['list']: l.append('%s - %s' % (n['name'], n['detailurl']))
        return '\n'.join(l)
    elif r['code'] == 313000:  # 儿歌类
        return '\n'.join([r['text'].replace('<br>', '\n')])
    elif r['code'] == 314000:  # 诗词类
        return '\n'.join([r['text'].replace('<br>', '\n')])



