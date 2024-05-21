import _csv
import sys
import requests
import csv
import time
import os
import multiprocessing

nul_times = 0  # 记录错误次数


# 代理ip
proxies = {
    "http": "",
    "https": ""
}

def lieping_spider(technique, city_name, city_num, pages, exp):
    global nul_times
    # 寻找路径
    for tech in technique:
        path = f"E:/爬虫/猎聘/{tech}"
        if not os.path.exists(path):
            os.mkdir(path)
        url = 'https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job'
        for exper in exp:
            csv_file = open(f'猎聘/{tech}/{city_name}_{exper}.csv', mode='w', encoding='utf-8', newline='')
            csv_wirter = csv.DictWriter(csv_file, fieldnames=[
                'job_name',
                'job_area',
                'salary',
                'experience',
                'degree',
                'company_info',
                'technique',
                'compIndustry',
                'compScale'
            ])
            csv_wirter.writeheader()
            for page in range(pages):
                # 配置csv
                time.sleep(1)

                headers = {
                    "Connection": "close",
                    'Cookie': '__gc_id=26311b60cc8d4c648f5e004d1bd76cdf; _ga=GA1.1.2071377551.1714664625; __uuid=1714664625635.65; XSRF-TOKEN=h_bYioklTxeeV3HRwS80pA; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1714801502,1714909897,1714982222,1714989928; acw_tc=276077db17149899271848502e2ee8c63014ac83939b649bc2de5ee2106501; __tlog=1714989927779.64%7C00000000%7CR000000035%7Cs_o_007%7Cs_o_007; __session_seq=3; __uv_seq=22; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1714989932; __tlg_event_seq=19; _ga_54YTJKWN86=GS1.1.1714989927.7.1.1714989943.0.0.0',
                    'Host': 'api-c.liepin.com',
                    'Origin': 'https://www.liepin.com',
                    'Referer': 'https://www.liepin.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
                    'X-Client-Type': 'web',
                    'X-Fscp-Bi-Stat': '{"location": "https://www.liepin.com/zhaopin/?d_sfrom=search_sub_site&key=java&imscid=R000000035"}',
                    'X-Fscp-Fe-Version': '',
                    'X-Fscp-Std-Info': '{"client_id": "40108"}',
                    'X-Fscp-Trace-Id': 'b14cc755-c071-4cd9-884a-7a95bf79be7c',
                    'X-Fscp-Version': '1.1',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-XSRF-TOKEN': 'h_bYioklTxeeV3HRwS80pA',
                    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }
                data = {
                    "data": {
                        "mainSearchPcConditionForm": {"city": f"{city_num}", "dq": f"{city_num}", "pubTime": "",
                                                      "currentPage": f"{page}",
                                                      "pageSize": 40,
                                                      "key": f"{tech}", "suggestTag": "", "workYearCode": f"{exper}",
                                                      "compId": "",
                                                      "compName": "", "compTag": "", "industry": "", "salary": "",
                                                      "jobKind": "",
                                                      "compScale": "", "compKind": "", "compStage": "", "eduLevel": ""},
                        "passThroughForm": {"scene": "condition", "skId": "zbrgqi80tvklurv7v15evc4sh9gcwfma",
                                            "fkId": "5x5sb8bf69g68hkvc2yncaody1a0jsl8",
                                            "ckId": "ykxk6ujnn8ck5h1gpbwv90105f73x2i8",
                                            "suggest": None}}
                }
                try:
                    response = requests.post(url, json=data, headers=headers, proxies=proxies)
                    res_json = response.json()
                except (requests.exceptions.ChunkedEncodingError,
                        requests.ConnectionError,
                        requests.exceptions.JSONDecodeError) as e:
                    print(response.status_code)
                    print(f"Error is :{e}")
                    continue

                if res_json['flag'] == 1:
                    try:
                        jobCardList = res_json['data']['data']['jobCardList']
                    except KeyError:
                        break

                    print(f'{city_name},{exper}年的第{page}页')
                    for index in jobCardList:
                        area_info = index['job']['dq'].split('-')
                        city = area_info[0]
                        try:
                            dit = {
                                'job_name': index['job']['title'],
                                'job_area': city,
                                'salary': index['job']['salary'],
                                'experience': index['job']['requireWorkYears'],
                                'degree': index['job']['requireEduLevel'],
                                'company_info': index['comp']['compName'],
                                'technique': '/'.join(index['job']['labels']),
                                'compIndustry': index['comp']['compIndustry'],
                                'compScale': index['comp']['compScale']
                            }
                        except KeyError:
                            continue

                        try:
                            csv_wirter.writerow(dit)
                        except _csv.Error:
                            continue

                else:
                    time.sleep(3)
                    nul_times += 1
                    continue



if __name__ == '__main__':
    # 'Java',"c++","PHP", "Python", "C#", ".NET", "Golang", "Node.js", "Hadoop", "Docker",
    #         "数据分析师", "数据挖掘", "数据架构师","前端开发", "后端开发", "全栈开发",
    #         "网络安全", "Linux",
    #         "机器学习", "深度学习",
    tec = [
        "爬虫", "算法工程师", "自然语言处理",
        "运维工程师", "网页产品设计", "移动产品设计", "UI设计", "性能测试", "硬件测试", "软件测试",
        "游戏策划", "游戏场景", "游戏特效", "UE4", "U3D"
    ]
    city_name = ['北京', '上海', '广州', '深圳', '杭州', '成都']
    city_num = ['010', '020', '050020', '050090', '070020', '280020']
    pages = 10
    exp = ['1', '1$3', '3$5', '5$10']

    processes = []  # 多进程爬虫
    for c_na, c_nu in zip(city_name, city_num):
        p = multiprocessing.Process(target=lieping_spider, args=(tec, c_na, c_nu, pages, exp))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

