import multiprocessing
import csv
import time
import random
import os
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def spider(tech, n, c, c_n, exp_y, exp):
    service = Service('E:/爬虫/venv/Scripts/chromedriver.exe')
    # 代理设置
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=')


    for tec in tech:
        driver = webdriver.Chrome(options=chrome_options, service=service)
        path = f"E:/爬虫/{tec}"
        if not os.path.exists(path):
            os.mkdir(path)

        # 定义csv
        for exp_year, exp_num in zip(exp_y, exp):
            f = open(f'{tec}/{c}_{tec}_{exp_year}.csv', mode='w', encoding='utf-8', newline='')

            fieldnames = ['job_name',
                          'job_area_wrapper',
                          'salary',
                          'experience',
                          'degree',
                          'company_info',
                          'technique',
                          'info_desc']
            csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
            csv_writer.writeheader()

            for page in range(1, n + 1):
                print(f'{tec}现在是{c}的{exp_year}第{page}页')
                # 处理异常，如果当前页没有数据，就跳出循环
                try:
                    driver.get(
                        f"https://www.zhipin.com/web/geek/job?query={tec}&city={c_n}&experience={exp_num}&page={page}")

                    WebDriverWait(driver, 10, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'job-list-box')))

                    lis = driver.find_element(By.CLASS_NAME, 'job-list-box').find_elements(By.CLASS_NAME,
                                                                                           'job-card-wrapper')

                    for li in lis:
                        job_name = li.find_element(By.CLASS_NAME, 'job-name').text
                        job_area_wrapper = li.find_element(By.CLASS_NAME, 'job-area-wrapper').text
                        salary = li.find_element(By.CLASS_NAME, 'salary').text
                        experience = li.find_element(By.CLASS_NAME, 'job-info').find_element(By.CSS_SELECTOR,
                                                                                             'li:first-child').text
                        degree = li.find_element(By.CLASS_NAME, 'job-info').find_element(By.CSS_SELECTOR,
                                                                                         'li:nth-child(2)').text
                        company_info = li.find_element(By.CLASS_NAME, "company-info").text
                        technique_li = li.find_element(By.CLASS_NAME, 'job-card-footer').find_elements(By.CSS_SELECTOR,
                                                                                                       'li')
                        technique = ''
                        for item in technique_li:
                            if item.text != '':
                                technique = '{a}/{b}'.format(a=technique, b=item.text)
                        info_desc = li.find_element(By.CLASS_NAME, 'info-desc').text
                        dit = {
                            'job_name': job_name,
                            'job_area_wrapper': job_area_wrapper,
                            'salary': salary,
                            'experience': experience,
                            'degree': degree,
                            'company_info': company_info,
                            'technique': technique,
                            'info_desc': info_desc
                        }
                        csv_writer.writerow(dit)

                # 处理异常，如果当前页没有数据，就跳出循环
                except TimeoutException:
                    time.sleep(4)
                    break
                    # try:
                    #     # 如果是验证页面，就退出程序
                    #     erro = driver.find_element(By.CLASS_NAME,'error-content')
                    #     infom = erro.find_element(By.CLASS_NAME,'btn').text
                    #     if infom == '点击进行验证':
                    #         print(f'程序停止在{c},{tec}的{exp_year}第{page}页')
                    #         return
                    # except NoSuchElementException:
                    #     break
                finally:
                    time.sleep(random.randint(1, 2))
            f.close()
        driver.close()


if __name__ == '__main__':
    tech_positions = [
        "Java", "c%2B%2B", "PHP", "Python",
        "C%23", ".NET", "Golang", "Node.js", "Hadoop",
        "语音视频图形开发",
        "GIS工程师", "区块链工程师",
        "全栈工程师","前端开发工程师",
        "Android", "iOS",
        "U3D", "UE4", "Cocos",
        "技术美术", "JavaScript",

        "Docker", "Linux",
        # "测试工程师", "软件测试",
        # "自动化测试", "功能测试",
        "网页产品设计", "移动产品设计",
        "测试开发", "硬件测试", "游戏测试", "游戏策划",
        # "性能测试", "渗透测试",
        # "测试经理",
        "运维工程师",
        # "IT技术支持", "网络工程师",
        "网络安全",
        # "系统工程师", "运维开发工程师", "系统管理员", "DBA",
        # "系统安全", "技术文档工程师",
        # "图像算法",
        "自然语言处理", "大模型算法", "数据挖掘",
        # "规控算法", "SLAM算法", "推荐算法", "搜索算法",
        # "语音算法", "风控算法", "算法研究员",
        "算法工程师", "机器学习", "深度学习",
        # "自动驾驶系统工程师", "AI训练师",
        # "售前技术支持", "售后技术支持", "销售技术支持", "客户成功",
        "数据分析师", "数据开发",
        "数据仓库", "ETL工程师", "数据挖掘", "数据架构师", "爬虫", "数据采集",
        # "项目经理", "项目助理", "项目专员", "实施工程师", "实施顾问", "需求分析工程师", "硬件项目经理",
        # "技术经理", "架构师", "技术总监", "CTO", "技术合伙人", "运维总监",
        # "其他技术职位"
    ]
    city_name = ['上海'

                # '北京',
                # '广州', '深圳'
                # '杭州', '成都'
                 ]
    city_num = [101020100

                #101010100,
                # 101280100, 101280600
                # 101210100, 101270100
                ]
    ex_year = ['应届', '1-3年', '3-5年', '5-10年']
    ex_num = [102, 104, 105, 106]

    num_processes = len(city_name)

    processes = []  # 多进程爬虫

    for c_na, c_nu in zip(city_name, city_num):
        p = multiprocessing.Process(target=spider, args=(tech_positions, 10, c_na, c_nu, ex_year, ex_num))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
