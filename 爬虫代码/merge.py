# 由于爬取的数据保存在多个文件夹，本代码用于合并爬取的数据
import pandas as pd
import os


# 创建空的DataFrame用于存储合并的数据
merge_csv = pd.DataFrame()


# 读取数据keyword为爬取时搜索的职位
def read_add_csv(path: str, keyword: str):
    global merge_csv
    data = pd.read_csv(path)
    data.insert(loc=0, column='keyword', value=keyword)
    merge_csv = pd.concat([merge_csv, data])


# path_in为要进行合并的数据的文件夹，运行时换成Boss_processed或猎聘_processed
path_in = "猎聘_processed"
pathdir = os.listdir(path_in)

for dir in pathdir:
    csv_path = os.listdir(f"{path_in}/{dir}")
    for csv in csv_path:
        path = f"{path_in}/{dir}/{csv}"
        read_add_csv(path, dir)

# 保存合并后的数据
merge_csv.to_csv(f"{path_in}/merge.csv", index=False, encoding='utf-8')
