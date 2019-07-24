from django.test import TestCase

# Create your tests here.
import requests
from lxml import etree
import time
from headers import ua_list
import random
import pymysql


class LianjiaSpider(object):

    def __init__(self):
        self.url = "https://xa.lianjia.com/ershoufang/pg{}/"
        self.headers = {'User-Agent': random.choice(ua_list)}
        self.db = pymysql.connect(
            'localhost', 'root', '123456', 'spider', charset='utf8'
        )
        self.cursor = self.db.cursor()

    def get_page(self, url):
        html = requests.get(url, headers=self.headers).content.decode('utf-8')
        self.parse_page(html)

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        basic_xpath = '//ul[@class="sellListContent"]/li[@class="clear LOGCLICKDATA"] | //ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]'
        r_list = parse_html.xpath(basic_xpath)
        parse_list_list = []
        for r in r_list:
            parse_list = []
            parse_list.append(
                r.xpath('.//a[@data-el="ershoufang"]/text()')[0].strip())
            parse_list.append(r.xpath(
                './/div[@class="totalPrice"]/span/text()')[0].strip())
            parse_list.append(r.xpath(
                './/div[@class="unitPrice"]/span/text()')[0].strip())
            parse_list_list.append(parse_list)

        self.write_page(parse_list_list)

        def write_page(self, data):
            string = 'insert into lianjia2 (name,total_price,price) valuse (%s,%s,%s)'
            self.cursor.executemany(string, data)
            self.db.commit()

    def main(self):
        for i in range(1, 2):
            url = self.url.format(i)
            self.get_page(url)
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    start = time.time()
    spider = LianjiaSpider()
    spider.main()
    end = time.time()
    print('执行时间:%.2f' % (end - start))
