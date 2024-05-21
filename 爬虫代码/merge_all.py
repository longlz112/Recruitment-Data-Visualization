# 合并两个网站的数据
import pandas as pd

path1 = "test_data/Boss_merge_new.csv"
path2 = "test_data/猎聘_merge_new.csv"

df1 = pd.read_csv(path1)
df2 = pd.read_csv(path2)
merge_csv = pd.DataFrame()

merge_csv = pd.concat([df1, df2])

merge_csv.to_csv("test_data/merge_all.csv", index=False, encoding="utf-8")

