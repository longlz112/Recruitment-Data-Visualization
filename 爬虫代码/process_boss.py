import pandas as pd
import os


# 注意！！！
# 代码直接对csv进行修改，运行前先把源数据进行保存
# 注意！！！

# boss爬取到的数据存在许多问题，需要进行数据清洗
# 主要处理technique和job_area，technique处理多余字符，job_area_wrapper保留公司地区

# 处理technique每一列的第一个\
def split_first(string):
    if isinstance(string, str):
        return string.strip('/')
    else:
        return '无'


# 处理函数
def handle_csv(path: str):
    data = pd.read_csv(path)
    data['technique'] = data['technique'].apply(split_first)
    data['job_area_wrapper'] = data['job_area_wrapper'].apply(lambda x: x.split('·')[0])
    data.to_csv(f'{path}', index=False)

    # print(data['job_area_wrapper'])


# 寻找每个csv，
# path_in为py文件同级目录下的文件夹名称
path_in = ""
pathdir = os.listdir(path_in)
for dir in pathdir:
    csv_path = os.listdir(f"{path_in}/{dir}")
    for csv in csv_path:
        path = f"{path_in}/{dir}/{csv}"
        handle_csv(path)
