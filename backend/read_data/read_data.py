import pandas as pd
import pprint

def get_count_keyword():
    df = pd.read_csv('read_data/processed_data/count_keyword.csv')
    json_data = df.to_json(force_ascii=False)
    return json_data

def get_count_data(keyword:str, type:str):
    df = pd.read_csv(f'read_data/processed_data/count_{type}.csv')
    df_filter = df[df['keyword']==keyword]
    json_data = df_filter.to_json(force_ascii=False)
    return json_data


def get_skill(keyword:str):
    df = pd.read_csv('read_data/processed_data/count_skill_top20.csv')
    df_filter = df[df['keyword']==keyword]
    json_data = df_filter.to_json(force_ascii=False)
    return json_data

