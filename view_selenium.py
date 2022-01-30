# -*- coding:UTF-8 -*-
# @Time : 2022/1/30 14:07
# @Author : Palm
# @Remark :
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


service = Service("utils/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://antirobot.tianyancha.com/captcha/verify?return_url=https%3A%2F%2Fwww.tianyancha.com%2Fsearch%2For0100-oe015%3Fbase%3Dsh%26companyType%3Dinstitution&rnd=")
