import random, redis, pymysql, logging

user_agent_list = [ \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
    "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

Cookie = r'aliyungf_tc=77e040c7af18d7b0c0f3e36d5b74ab36cc17e1fd26435f7e44d859055929751d; csrfToken=6eF-Ytq9FjQviOG1pcvatYoe; jsid=SEO-GOOGLE-ALL-SY-000001; TYCID=eb84d720816e11eca71f7f10dc15f4d6; ssuid=1794085248; sajssdk_2015_cross_new_user=1; bannerFlag=true; show_activity_id_27=27; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1643507395; _ga=GA1.2.2086516854.1643507395; _gid=GA1.2.1071553194.1643507395; tyc-user-phone=%255B%252215671044865%2522%255D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2245406%22%2C%22first_id%22%3A%2217ea8aca59dba7-0ebc00029843ca-f791b31-2073600-17ea8aca59ee50%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217ea8aca59dba7-0ebc00029843ca-f791b31-2073600-17ea8aca59ee50%22%7D; searchSessionId=1643512169.36432266; acw_tc=781bad0e16435215962076296e33fa5a481998f5ea5d72731117bacb57aeef; acw_sc__v2=61f6263ca404daecfa7591b4a2e7654dfbc80d7d; _gat_gtag_UA_123487620_1=1; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1643521726; tyc-user-info={%22isExpired%22:%220%22%2C%22mobile%22:%2215671044865%22%2C%22state%22:%227%22%2C%22vipManager%22:%220%22}; tyc-user-info-save-time=1643521743683; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTY3MTA0NDg2NSIsImlhdCI6MTY0MzUyMTc0NCwiZXhwIjoxNjQ2MTEzNzQ0fQ.Z5tV6RJrMMK7ItBmIRCM8HcCCUY3zjzFaLsTlDGF5E7zwWVWCzWp1_onMme2WISu6aRbcqWl9_joUZFpTh9XQA'
headers = {'Host': 'www.tianyancha.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1', 'User-Agent': random.choice(user_agent_list),
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cookie': Cookie}

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
redisConnect = redis.Redis(connection_pool=pool)

mysqlConnect = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='daidai',
    db='tianyancha',
    charset='utf8',
    cursorclass = pymysql.cursors.DictCursor)

logging.basicConfig(filename='log/logger.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
