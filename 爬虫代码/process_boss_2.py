# boss爬取的数据分类有错误，如：
# c++和c#被替换成了c%2B%2B和C%23

import pandas as pd

df = pd.read_csv("Boss_processed/Boss_merge_new.csv")

# 处理函数
def handle(string):
    if string == 'c%2B%2B':
        return 'C++'
    elif string == 'C%23':
        return 'C#'
    elif string == 'java':
        return 'Java'
    else:
        return string


df['keyword'] = df['keyword'].apply(handle)

df.to_csv("Boss_processed/Boss_merge_new.csv", index=False)