# -*- coding-8 -*-
import json, re, requests, time, urllib
from bs4 import BeautifulSoup
from settings import headers, redisConnect
from config import SEARCH_URL


def option():
    # 这里先默认选择上海地区,注册资金在100万以内的，成立1-5年的选项
    params = {
        "base": "sh",
        "companyType": "institution"
    }
    slash = {
        "funds": "or0100",
        "establish": "oe015"
    }
    slash_uri = ""
    for v in slash.values():
        if v != list(slash.values())[-1]:
            v = v + "-"
        slash_uri += v

    param_uri = ""
    for k, v in params.items():
        if k != list(params.keys())[-1]:
            k = "?" + k
        else:
            k = "&" + k
        t_uri = k + "=" + v
        param_uri += t_uri
    url = SEARCH_URL + slash_uri + param_uri
    headers['Referer'] = "https://www.tianyancha.com/search/or0100-e015?base=sh"
    response = requests.get(url, headers=headers)
    print(response.url)
    soup = BeautifulSoup(response.text, features="html.parser")
    companys = soup.find("div", class_="result-list sv-search-container").find_all("div", class_="search-result-single")
    for company in companys:
        name = company.find("div", class_="header").find("a").text
        herf = company.find("div", class_="header").find("a").get('href')
        index_response = requests.get(herf, headers=headers)
        index_text = index_response.text
        if "<!DOCTYPE html PUBLIC" == index_text[:21]:
            index_soup = BeautifulSoup(index_text, features="html.parser")
        else:
            print(response.url)

def options():
    pass


if __name__ == '__main__':
    option()
