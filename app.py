from flask import Flask

app = Flask(__name__)

@app.route('/')

def hell():
    return "<h1>hello Flask    hohohoho <h1>"


@app.route("/test")

def test():
    return"<h1>test<h1>"

@app.route("/money")


import os
import sys
import urllib.request
import datetime
import time
import json
import xml
import math


def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % (datetime.datetime.now()))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


# 1번
def getCurrencyRate(yyyymmdd, data):
    end_point = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON"

    parameters = "?authkey=KcTDwzxQUTFN7NJCmMCybJELXORrCfXa"
    parameters += "&searchdate=" + yyyymmdd
    parameters += "&data=" + data

    url = end_point + parameters

    retData = get_request_url(url)

    if (retData == None):
        return None
    else:
        return json.loads(retData)


def main1():
    yyyymmdd = ""
    data = "AP01"

    keys = []
    new_keys = ['조회 결과', '통화코드', '받으실때', '보내실때', '매매 기준율', '장부가격', '년환가료율', '10일환가료율', '서울외국환중개 매매기준율', '서울외국환중개 장부가격',
                '국가/통화명']
    result = []

    json_data = getCurrencyRate(yyyymmdd, data)
    new_data = {}

    for i in json_data:
        values = i.values()
        valuelist = list(values)  # 벨류 값을 리스트 형으로 바꾸는 구문
        for j in range(0, len(i)):
            new_data[new_keys[j]] = valuelist[j]
        result.append(new_data)
        new_data = {}

    print(result)


if __name__ == '__main__':
    main1()

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)

