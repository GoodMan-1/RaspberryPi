# coding:utf-8
import urllib2
import json

def search_flight(dcity, acity, ddate):
    refer = 'http://flights.ctrip.com/booking/SIA-CAN-day-1.html?DDate1='+ddate
    ctrip_header = {'Accept': '*/*',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Connection': 'keep-alive',
                    'User-Agent':
                        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                    'Host': 'flights.ctrip.com',
                    'Referer': refer}

    request_url = 'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?' \
                + 'DCity1=' + dcity \
                + '&ACity1=' + acity \
                + '&SearchType=S' \
                + '&DDate1=' + ddate
    request = urllib2.Request(request_url, headers=ctrip_header)
    response = urllib2.urlopen(request)
    return_json = response.read()
    return_data = json.loads(return_json, encoding='gbk')

    flight_list = return_data['fis']
    flight_nums = len(flight_list)
    flight_dest = flight_list[0]['acn']     #目的城市
    flight_source=flight_list[0]['dcn']     #出发城市
    company=return_data['als']  # 全部航空公司字典
    print '携程',date,flight_source,'-->',flight_dest,'共有航班:', flight_nums, '趟'
    for i in range(flight_nums):
        airline = flight_list[i]['alc']         # 航空公司
        flight_no = flight_list[i]['fn']         # 航班号
        flight_airport_dest = flight_list[i]['apbn']  # 目的机场
        flight_airport_source = flight_list[i]['dpbn']  # 出发机场
        flight_start_date = flight_list[i]['dt']  # 起飞时间
        flight_final_date = flight_list[i]['at']  # 到达时间
        flight_low = flight_list[i]['lp']       #最低价
        print i+1,company[airline], flight_no,flight_airport_source,'-->',flight_airport_dest," 起飞时间:",flight_start_date,"到达时间:",flight_final_date,"最低票价:",flight_low,
        price_list = [each['p'] for each in flight_list[i]['scs'] if each['hotel'] is None]     # 非飞宿产品价格
        print "票价:",price_list


if __name__ == '__main__':
    try:
        date = raw_input("出发时间(如2018-07-03):")
        fp = open("./city.json", "r")
        all_city = fp.read()
        fp.close()
        all_city = json.loads(all_city)
        dcity = acity = ""
        while True:
            city1 = raw_input("出发城市：").decode("utf-8")
            city2 = raw_input("目的城市：").decode("utf-8")
            for i in range(len(all_city)):
                if all_city[i]['name'] == city1:
                    dcity=all_city[i]['code']
                if all_city[i]['name'] == city2:
                    acity=all_city[i]['code']
            if dcity!="" and acity!="":
                break
            else:
                print "输入城市错误(正确输入如：北京、上海)!"
        print "正在查询，请稍等..."
        search_flight(dcity, acity, date)
    except Exception as e:
        print e
