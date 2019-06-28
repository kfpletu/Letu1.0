#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 下午2:47
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : 车票查询.py
# @Software: PyCharm
import re
import ssl
import urllib, urllib.parse
from . import models
import requests
import urllib3

urllib3.disable_warnings()  # 不显示警告信息
ssl._create_default_https_context = ssl._create_unverified_context
req = requests.Session()


class TicketQuery:
    '''余票查询'''

    def __init__(self):
        self.station_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9103'
        self.headers = {
            # 'Host': 'kyfw.12306.cn',
            # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
            # 'Accept': '*/*'
            'Host': 'kyfw.12306.cn',
            'If-Modified-Since': '0',
            'Pragma': 'no-cache',
            'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

    def get_station_name(self):
        """
        '获取车站代码及其站名'
        :param station_name: 要查询的站名
        :return: 对应站名的代码
        """
        response = requests.get(self.station_url, verify=False)
        station = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
        # print(station)
        station_name_dict = dict(station)
        # print(station_name_dict)
        new_station_name_dict = dict(zip(station_name_dict.values(), station_name_dict.keys()))
        return (station_name_dict,new_station_name_dict)

    def get_station_daima(self, station_daima):
        pass

    def query(self, from_station, to_station, date):
        ticket = {}
        fromstation = self.get_station_name()[0][from_station]
        tostation = self.get_station_name()[0][to_station]
        url = f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={fromstation}&leftTicketDTO.to_station={tostation}&purpose_codes=ADULT'
        # url = f'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs={from_station_url},{fromstation}&ts={to_station_url},{tostation}&date={date}&flag=N,N,Y'
        # print(url)
        try:
            html = requests.get(url, headers=self.headers, verify=False).json()
            result = html['data']['result']
            # print(result)
            if result == []:
                print('很抱歉,没有查到符合当前条件的列车!')
                exit()
            else:
                print(date + from_station + '-' + to_station + '查询成功!')
                num = 1

                for i in result:
                    ticket_list = []
                    info = i.split("|")
                    # print(info)
                    # 判断是否还有余票
                    if info[0] != "" and info[0] != 'null':
                        print(str(num) + '.' + info[3] + "该车次还有余票!")
                        print("出发时间:" + info[8] + '到达时间:' + info[9] + '历时:' + info[10] + " ", end='')
                        seat = {21: '高级软卧', 23: '软卧', 26: '无座', 28: '硬卧', 29: '硬座', 30: '二等座', 31: '一等座', 32: '商务座',
                                33: '动卧'}
                        # from_station_no = info[16]
                        # to_station_no = info[17]
                        for j in seat.keys():
                            if info[j] != "无" and info[j] != '':
                                if info[j] == "有":
                                    print(seat[j] + ":有票", end='')
                                else:
                                    print(seat[j] + ":有" + info[j] + '张票', end='')
                        print('\n')
                    elif info[1] == "预定":
                        print(str(num) + '.' + info[3] + '车次目前没有余票')
                    elif info[1] == '列车停运':
                        print(str(num) + '.' + info[3] + '车次列车停运')
                    elif info[1] == '23:00-06:00系统维护时间':
                        print(str(num) + '.' + info[3] + '23:00-06:00系统维护时间')
                    else:
                        print(str(num) + '.' + info[3] + '车次列车运行图调整,暂停发售')
                    num += 1
                    try:
                        info1=models.Trip.objects.get(station_code=info[6])
                        info2=models.Trip.objects.get(station_code=info[7])

                    except:
                        pass
                    ticket_list.append(info[3])
                    # ticket_list.append(info[6])
                    ticket_list.append(info1.station_name)
                    # ticket_list.append(self.get_station_name()[1][info[6]])
                    ticket_list.append(info2.station_name)
                    # ticket_list.append(info[7])
                    # ticket_list.append(self.get_station_name()[1][info[7]])
                    ticket_list.append(info[8])
                    ticket_list.append(info[9])
                    ticket_list.append(info[10])
                    ticket_list.append(info[32])
                    ticket_list.append(info[31])
                    ticket_list.append(info[30])
                    ticket_list.append(info[21])
                    ticket_list.append(info[23])
                    ticket_list.append(info[27])
                    ticket_list.append(info[28])
                    ticket_list.append(info[24])
                    ticket_list.append(info[29])
                    ticket_list.append(info[26])
                    ticket_list.append(info[22])
                    ticket_list.append(info[1])
                    ticket[info[3]] = ticket_list
                    # ticket_dict["station_train_code"] = info[3]  # 获取车次信息，在3号位置
                    # ticket_dict["from_station_name"] = info[6]  # 始发站信息在6号位置
                    # ticket_dict["to_station_name"] = info[7]  # 终点站信息在7号位置
                    # ticket_dict["start_time"] = info[8]  # 出发时间在8号位置
                    # ticket_dict["arrive_time"] = info[9]  # 抵达时间在9号位置
                    # ticket_dict["lishi"] = info[10]  # 经历时间在10号位置
                    # ticket_dict["swz_num"] = info[32] or info[25]  # 特别注意，商务座在32或25位置
                    # ticket_dict["zy_num"] = info[31]  # 一等座信息在31号位置
                    # ticket_dict["ze_num"] = info[30]  # 二等座信息在30号位置
                    # ticket_dict["gr_num"] = info[21]  # 高级软卧信息在21号位置
                    # ticket_dict["rw_num"] = info[23]  # 软卧信息在23号位置
                    # ticket_dict["dw_num"] = info[27]  # 动卧信息在27号位置
                    # ticket_dict["yw_num"] = info[28]  # 硬卧信息在28号位置
                    # ticket_dict["rz_num"] = info[24]  # 软座信息在24号位置
                    # ticket_dict["yz_num"] = info[29]  # 硬座信息在29号位置
                    # ticket_dict["wz_num"] = info[26]  # 无座信息在26号位置
                    # ticket_dict["qt_num"] = info[22]  # 其他信息在22号位置
                    # ticket_dict["note_num"] = info[1]  # 备注信息在1号位置
                    # ticket.append(ticket_list)
            # return result
            return ticket
        except:
            print('查询信息有误!请重新输入!')
        exit()


if __name__ == '__main__':
    #     tt = TicketQuery()
    #     # aa = tt.get_station_name('西安')
    #     # print(aa)
    #     aa = tt.query('西安', '兰州', '2019-06-26')
    #     print(aa)
    pass
