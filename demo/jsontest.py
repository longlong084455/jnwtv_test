# coding:utf-8
import json


def load_json(path):
    f = open(path) # 设置以utf - 8
    data = json.load(f)
    return data


def set_key_value(key, value, path='userinfo.json'):
    d = load_json(path=path)
    d[key] = value
    with open('userinfo.json', 'w') as f:
        json.dump(d, f)
        f.close()


def get_value(key, path='userinfo.json'):
    d = load_json(path=path)
    return d[key]


def get_all_keys(path='userinfo.json'):
    d = load_json(path)
    keys = dict(d).keys()
    return keys
