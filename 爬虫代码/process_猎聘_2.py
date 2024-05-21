# 统一keyword格式和boss数据一致

import pandas as pd


df = pd.read_csv("test_data/猎聘_merge_new.csv")

# 处理函数
def handle(string):
    if string == 'c++':
        return 'C++'
    else:
        return string


df['keyword'] = df['keyword'].apply(handle)

df.to_csv("猎聘_processed/猎聘_merge_new.csv", index=False)

