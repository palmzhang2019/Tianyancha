# 基于Python的天眼查爬虫，爬取完整的公司数据（可爬需要VIP才能用的邮箱和电话等）
#### 运行前请将自己的cookie替换settings中的第42行的Cookie。

PS：<a href="https://blog.csdn.net/MuWinter/article/details/75313476" rel="nofollow">小白怎么拿到cookie？点击查看</a>

### 运行方法，
1. 本项目有两部分组成列表页面mainlist.py和详情页面DetailSpider.py。
2. 本项目用到的编程语言为python,数据库用到了Mysql和redis。所以你的电脑或者服务器中需要有这几样东西。PS：<a href="https://www.runoob.com/redis/redis-install.html" rel="nofollow">小白怎么在windows中安装redis？</a>
3. 先运行mainlist.py，如图，按照自己的需求输入<br>
![avatar](Imags/1.jpg)
4. 再运行DetailSpider.py，PS：可以在另一个窗口开<br>
![avatar](Imags/2.jpg)
5. 如果撞到了机制墙，那么爬取的页面会返给你一个验证码的页面，此时，终端会提示你需要点验证码了。<br>
![avatar](Imags/3.jpg)
6. 点击验证码，告诉天眼查你不是机器人，而是一个伪装成机器人的人类。然后再运行DetailSpider程序，这个时候程序会记得你上次停下来的位置。并从那里继续向下爬取。<br>
![avatar](Imags/4.jpg)

博客：<a href="http://zhangxiaodai.life">zhangxiaodai.life</a>