import requests, json
from bs4 import BeautifulSoup
from settings import headers
from settings import redisConnect, mysqlConnect
# #
# #
# # reg = 'https://www.tianyancha.com/search?key=%E5%8C%BA%E5%9D%97%E9%93%BE&base=js'
# # headers['reg'] = reg
# # url = 'https://www.tianyancha.com/search/p1?key=%E5%8C%BA%E5%9D%97%E9%93%BE&base=js'
# # new_num = 1
# # #
# # #
# # try:
# #     response = requests.get(url, headers=headers)
# #     if response.status_code != 200:
# #         response.encoding = 'utf-8'
# #         print(response.status_code)
# #         print('ERROR')
# #     soup = BeautifulSoup(response.text, 'lxml')
# # except Exception:
# #     print('请求都不让，这天眼查也搞事情吗？？？')
# # try:
# #     com_all_info = soup.body.select('.mt74 .container.-top .container-left .search-block.header-block-container')[0]
# #     com_all_info_array = com_all_info.select('.search-item.sv-search-company')
# #     print('开始爬取数据，请勿打开excel')
# # except Exception:
# #     print('好像被拒绝访问了呢...请稍后再试叭...')
# # for i in range(new_num, len(com_all_info_array)):
# #     temp_g_name = com_all_info_array[i].select('.content .header .name')[0].text  # 获取公司名
# #     href = com_all_info_array[i].select('.content .header .name')[0].get('href')
# #     print(href)
#     # temp_g_state = com_all_info_array[i].select('.content .header .tag-common.-normal-bg')[0].text  # 获取公司状态
#     # temp_r_name = com_all_info_array[i].select('.content .legalPersonName.link-click')[0].text  # 获取法人名
#     # temp_g_money = com_all_info_array[i].select('.content .info.row.text-ellipsis div')[1].text.strip('注册资本：')  # 获取注册资本
#     # temp_g_date = com_all_info_array[i].select('.content .info.row.text-ellipsis div')[2].text.strip('成立日期：')  # 获取公司注册时间
#     # print(temp_g_name, temp_g_state, temp_r_name, temp_g_money, temp_g_date)
#     # try:
#     #     try:
#     #         temp_r_phone = com_all_info_array[i].select('.content .contact.row div script')[0].text.strip('[').strip(']')  # 获取法人手机号
#     #     except Exception:
#     #         temp_r_phone = com_all_info_array[i].select('.content .contact.row div')[0].select('span span')[0].text  # 获取法人手机号
#     # except:
#     #     temp_r_phone = '未找到法人手机号'
#     # try:
#     #     try:
#     #         temp_r_email = com_all_info_array[i].select('.content .contact.row div script')[1].text.strip('[').strip(']')  # 获取法人Email
#     #     except Exception:
#     #         temp_r_email = com_all_info_array[i].select('.content .contact.row div')[1].select('span')[1].text  # 获取法人Email
#     # except Exception:
#     #     temp_r_email = '未找到法人邮箱'
#
#
# # attr_dict = {
# #     "name": "常成功",
# #     "alias": "常城",
# #     "sex": "male",
# #     "height": 175,
# #     "postal code": 100086,
# #     "Tel": 'None',
# # }
# #
# # redisConnect.hmset("123456", attr_dict)
# info = {
#     'name':'星系区块链技术服务（江苏）有限公司',
#     'href':'https://www.tianyancha.com/company/3276469146',
#     'state':'在业',
#     'r_name':'粟术英',
#     'money':'10000万人民币',
#     'date':'2018-10-06',
#     'url':'https://www.tianyancha.com/search/p0?key=%E5%8C%BA%E5%9D%97%E9%93%BE&base=js',
#     'r_phone':'18665116886',
#     'r_email':'37538731@qq.com',
#     'xid':'1_01_22:48:47',
#     'company_address':'淮安市盱眙县经济开发区企业服务大厦1403室',
#     'registe_address':'淮安市盱眙县经济开发区企 业服务大厦1403室附近公司',
#     'industry':'软件和信息技术服务业',
#     'company_type':'其他有限责任公司',
#     'business_scope':'区块链领域内的技术开发、技术咨询、技术服务、技术转让；从事广告业务。（依法须经批准的项目，经相关部门批准后方可开展 经营活动）',
#     'staff_size':'-'
# }
# info.pop('href')
# info.pop('url')
#
# table = 'company0529'
# keys = ','.join(info.keys())
# values = ','.join(['%s'] *len(info))
# sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=table, keys=keys, values=values)
#
# cursor = mysqlConnect.cursor()
# if cursor.execute(sql, tuple(info.values())):
#     mysqlConnect.commit()
#
url = 'https://www.tianyancha.com/company/3151061924'
response = requests.get(url, headers = headers)
if response.status_code == 200:
    print("yes")