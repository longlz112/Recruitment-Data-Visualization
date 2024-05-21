from pyspark.sql import SparkSession
from pyspark.sql.functions import desc

# 本地读取路径
path = "file:///mnt/hgfs/project_data/merge_all.csv"

# 不含参数，用于保存结果
def Count_area():

    # 初始化Spark会话
    spark = SparkSession.builder.appName("count_area").getOrCreate()

    # 读取CSV文件
    df = spark.read.csv(path, header=True, multiLine=True)

    # 统计同一个keyword下，不同job_area的数量
    area_counts = df.groupBy("keyword", "job_area").count()

    # 排序
    sort_data = area_counts.sort(desc('keyword'))

    # 清除count数小于100的值
    filter_data = sort_data.filter(sort_data['count'] > 100)

    # 显示结果
    filter_data.show()

    # 写入文件
    filter_data.coalesce(1).write.csv("file:///mnt/hgfs/project_data/count_area", header=True, mode='overwrite')

    # 停止Spark会话
    spark.stop()


# 含参数，用于直接向前端返回结果
def get_count_area(keyword: str):

    # 初始化Spark会话
    spark = SparkSession.builder.appName("count_area").getOrCreate()

    # 读取CSV文件
    df = spark.read.csv(path, header=True, multiLine=True)

    # 先筛选出对应列，减少运行时间
    df = df.filter((df["keyword"] == keyword))

    # 统计同一个keyword下，不同job_area的数量
    area_counts = df.groupBy("keyword", "job_area").count()

    # 清除count数小于100的值
    filter_data = area_counts.filter((area_counts['count'] > 100) & (area_counts["keyword"] == keyword))

    # 排序
    sort_data = filter_data.sort(desc('keyword'))

    # 转json文件
    pd_data = sort_data.toPandas()
    json_data = pd_data.to_json(force_ascii=False)

    # 停止Spark会话
    spark.stop()
    return json_data

