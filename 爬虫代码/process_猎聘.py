import pandas as pd
import os

# 注意！！！
# 代码直接对csv进行修改，运行前先把源数据进行保存
# 注意！！！


# 处理猎聘的数据
# 主要处理technique，technique列有空的数据，将其替换成’无‘

# 处理technique的空值
def split_first(string):
    if isinstance(string, str):
        return string
    else:
        return '无'


# 处理函数
def handle_csv(path: str):
    data = pd.read_csv(path)
    data['technique'] = data['technique'].apply(split_first)
    data.to_csv(f'{path}', index=False)


# 寻找每个csv
# path_in为py文件同级目录下的目标文件夹名称
path_in = "猎聘_processed"
pathdir = os.listdir(path_in)
for dir in pathdir:
    csv_path = os.listdir(f"{path_in}/{dir}")
    for csv in csv_path:
        path = f"{path_in}/{dir}/{csv}"
        handle_csv(path)
