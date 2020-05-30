#-*- coding-8 -*-
import json, re,requests, time, urllib
from bs4 import BeautifulSoup
from settings import headers, redisConnect


def craw(url,key_word,page_now, area):
    if page_now == 0:
        reg = 'https://www.tianyancha.com/search?key={}&base={}'.format(key_word, area)
    else:
        reg = 'https://www.tianyancha.com/search/p{}?key={}&base={}'.format(page_now-1,key_word,area)

    headers['Referer'] = reg
    try:
        response = requests.get(url,headers = headers)
        if response.status_code != 200:
            response.encoding = 'utf-8'
            print(response.status_code)
            print('ERROR')
        soup = BeautifulSoup(response.text,'lxml')
    except Exception:
        print('请求都不让，这天眼查也搞事情吗？？？')
    try:
        com_all_info = soup.body.select('.mt74 .container.-top .container-left .search-block.header-block-container')[0]
        com_all_info_array = com_all_info.select('.search-item.sv-search-company')
        print('开始爬取第{}页数据'.format(page_now+1))
    except Exception:
        print('好像被拒绝访问了呢...请稍后再试叭...')

    strftime = time.strftime("%H:%M:%S", time.localtime())
    for i in range(0, len(com_all_info_array)):
        temp = dict()
        try:
            temp['name'] = com_all_info_array[i].select('.content .header .name')[0].text    #获取公司名
            temp['href'] = com_all_info_array[i].select('.content .header .name')[0].get('href')   #获取公司详细页面
        except:
            print('名字都没有就算了吧')
            continue
        try:
            temp['state'] = com_all_info_array[i].select('.content .header .tag-common.-normal-bg')[0].text  #获取公司状态
        except:
            temp['state'] = '没抓取到'
        try:
            temp['r_name'] = com_all_info_array[i].select('.content .legalPersonName.link-click')[0].text    #获取法人名
        except:
            temp['r_name'] = '没获取到'
        try:
            temp['money'] = com_all_info_array[i].select('.content .info.row.text-ellipsis div')[1].text.strip('注册资本：')    #获取注册资本
        except:
            temp['money'] = '没获取到'
        try:
            temp['date'] = com_all_info_array[i].select('.content .info.row.text-ellipsis div')[2].text.strip('成立日期：')    #获取公司注册时间
        except:
            temp['date'] = '1999-01-01'
        temp['url'] = url
        try:
            try:
                temp['r_phone'] = com_all_info_array[i].select('.content .contact.row div script')[0].text.strip('[').strip(']')    #获取法人手机号
            except Exception:
                temp['r_phone'] = com_all_info_array[i].select('.content .contact.row div')[0].select('span span')[0].text    #获取法人手机号
        except:
            temp['r_phone'] = '未找到法人手机号'
        try:
            try:
                temp['r_email'] = com_all_info_array[i].select('.content .contact.row div script')[1].text.strip('[').strip(']')    #获取法人Email
            except Exception:
                temp['r_email'] = com_all_info_array[i].select('.content .contact.row div')[1].select('span')[1].text    #获取法人Email
        except Exception:
            temp['r_email'] = '未找到法人邮箱'

        temp['xid'] = "{}_{}_{}".format(page_now+1,str(i+1).zfill(2),strftime)
        redisConnect.rpush("tianyan", json.dumps(temp,ensure_ascii=True))

if __name__ == '__main__':
    key_word_tmp = input('请输入您想搜索的关键词：')
    try:
        new_num = int(input('请输入您想从第几页检索：'))-1
    except Exception:
        new_num = 0
    try:
        area = int(input('请输入搜索的地区（请使用url中的简写,比如江苏写成js）：'))
    except Exception:
        area = 'js'
    try:
        num = new_num + int(input('请输入您想检索的页数：'))
    except Exception:
        num = new_num + 6
    try:
        sleep_time = int(input('请输入每次检索延时的秒数：'))
    except Exception:
        sleep_time = 5


    key_word = urllib.parse.quote(key_word_tmp)

    print('正在搜索，请稍后')

    for page_now in range(new_num,num):
        url = r'https://www.tianyancha.com/search/p{}?key={}&base={}'.format(page_now,key_word, area)
        s1 = craw(url,key_word,page_now, area)
        time.sleep(sleep_time)

