import pandas as pd

# 处理文件的薪资列，取下限值

path = 'Boss_processed/Boss_merge.csv'
data = pd.read_csv(path)
data['salary'] = data['salary'].apply(lambda x: x.split('-')[0])
data.to_csv('Boss_processed/Boss_merge_new.csv', index=False)
print(data['salary'])