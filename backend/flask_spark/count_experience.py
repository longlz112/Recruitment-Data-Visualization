from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
import pandas as pd

# 本地读取路径
path = "file:///mnt/hgfs/project_data/merge_all.csv"

# 不含参数，用于保存结果
def Count_exp():

    # 初始化spark会话
    spark = SparkSession.builder.appName("count_exp").getOrCreate()

    # 读取文件
    df = spark.read.csv(path, header=True, multiLine=True)

    # 统计同一个keyword下，不同experience的数量
    exp_count = df.groupBy("keyword", "experience").count()

    # 排序
    sort_data = exp_count.orderBy("keyword", desc("experience"))

    # 清除小于100的值
    filter_data = sort_data.filter(sort_data['count']>100)

    # 显示结果
    filter_data.show()

    # 写入文件
    filter_data.coalesce(1).write.csv("file:///mnt/hgfs/project_data/count_exp", header=True, mode='overwrite')

    # 停止spark会话
    spark.stop()

# 含参数，用于直接向前端返回结果
def get_count_exp(keyword:str):

    # 初始化spark会话
    spark = SparkSession.builder.appName("count_exp").getOrCreate()

    # 读取文件
    df = spark.read.csv(path, header=True, multiLine=True)

    # 先筛选出对应列，减少运行时间
    df = df.filter((df["keyword"]==keyword))

    # 统计同一个keyword下，不同experience的数量
    exp_count = df.groupBy("keyword", "experience").count()

    # 清除小于100的值
    filter_data = exp_count.filter((exp_count['count'] > 100) & (exp_count["keyword"]==keyword))
    # 排序
    sort_data = filter_data.sort(desc('experience'))

    # 转json文件
    pd_data = sort_data.toPandas()
    json_data = pd_data.to_json(force_ascii=False)

    # 停止spark会话
    spark.stop()
    return json_data

