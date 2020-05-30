import requests, json
from bs4 import BeautifulSoup
from pymysql import IntegrityError
from settings import redisConnect, headers, mysqlConnect, logging

while True:
    newObj = redisConnect.lpop('tianyan')
    if newObj == None:
        break
    info = json.loads(newObj)
    detailhref = info.get('href')
    headers['Referer'] = info.get('url')
    try:
        response = requests.get(detailhref,headers = headers)
        if response.status_code != 200:
            response.encoding = 'utf-8'
            if response.status_code == 404:
                print('ERROR:出验证码了，您该打开网页瞧瞧了{}'.format(detailhref))
                print('后期这里会加打码识别功能，敬请期待^。^')
                redisConnect.rpush("tianyan", json.dumps(info,ensure_ascii=True))
                redisConnect.close()
                break
        soup = BeautifulSoup(response.text, 'lxml')
    except Exception:
        print('请求都不让，这天眼查也搞事情吗？？？')

    try:
        # 公司地址
        info['company_address'] = soup.body.select("#company_base_info_address")[0].text.strip()
    except:
        info['company_address'] = '没有抓到'
    try:
        # 注册地址
        info['registe_address'] = soup.body.find(text="注册地址").find_parent().find_next_sibling().text.strip()
    except:
        info['registe_address'] = '没有抓到'
    try:
        # 行业
        info['industry'] = soup.body.find(text="行业").find_parent().find_next_sibling().text.strip()
    except:
        info['industry'] = '没有抓到'
    try:
        # 公司类型
        info['company_type'] = soup.body.find(text="公司类型").find_parent().find_next_sibling().text.strip()
    except:
        info['company_type'] = '没有抓到'
    try:
        # 经营范围
        info['business_scope'] = soup.body.find(text="经营范围").find_parent().find_next_sibling().text.strip()
    except:
        info['business_scope'] = '没有抓到'
    try:
        # 人员规模
        info['staff_size'] = soup.body.find(text="人员规模").find_parent().find_next_sibling().text.strip()
    except:
        info['staff_size'] = '没有抓到'

    href = info.pop('href')
    url = info.pop('url')

    table = 'company0529'
    keys = ','.join(info.keys())
    values = ','.join(['%s'] *len(info))
    sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=table, keys=keys, values=values)
    cursor = mysqlConnect.cursor()
    try:
        if cursor.execute(sql, tuple(info.values())):
            mysqlConnect.commit()
            print('{}插入成功'.format(info.get('name')))
    except IntegrityError as ie:
        mysqlConnect.rollback()
        logging.error(info.get('name')+str(ie))
        print('{}插入失败'.format(info.get('name')))
    except Exception as e:
        mysqlConnect.rollback()
        logging.error(info.get('name') + str(e))
        info['href'] = href
        info['url'] = url
        redisConnect.rpush("ti"
                           "anyan", json.dumps(info,ensure_ascii=True))
        print('{}数据库插入失败,尝试加入队列重新抓取'.format(info.get('name')))