from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
import pandas as pd

# 本地读取路径
path = "file:///mnt/hgfs/project_data/merge_all.csv"

# 记录总共有多少的keyword
def Count_keyword():

    # 创建SparkSession
    spark = SparkSession.builder.appName("count_keyword").getOrCreate()

    # 读取csv文件
    df = spark.read.csv(path, header=True, multiLine=True)

    # 统计各个关键字的结果数
    keyword_count = df.groupBy("keyword").count()

    # 按照结果从高到低进行排序
    sorted_count = keyword_count.sort(desc("count"))

    # 显示排序结果
    sorted_count.select("keyword").show()
    # 保存结果
    sorted_count.coalesce(1).write.csv("file:///mnt/hgfs/project_data/count_keyword", header=True, mode='overwrite')

    spark.stop()

# 向前端返回keyword列表
def get_count_keyword():

    # 创建SparkSession
    spark = SparkSession.builder.appName("count_keyword").getOrCreate()

    # 读取csv文件
    df = spark.read.csv(path, header=True, multiLine=True)

    # 统计各个关键字的结果数
    keyword_count = df.groupBy("keyword").count()

    # 按照结果从高到低进行排序
    sorted_count = keyword_count.sort(desc("count"))

    # 转json文件
    pd_data = sorted_count.toPandas()
    json_data = pd_data.to_json(force_ascii=False)

    # 停止spark会话
    spark.stop()
    return json_data
