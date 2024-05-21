from pyspark.sql import SparkSession
from pyspark.sql.functions import asc, col

# 本地读取路径
path = "file:///mnt/hgfs/project_data/merge_all.csv"
# 不含参数，用于保存结果
def Count_salary():

    # 初始化spark会话
    spark = SparkSession.builder.appName("count_salary").getOrCreate()

    # 读取文件
    df = spark.read.csv(path, header=True, multiLine=True)

    # 统计同一个keyword下，不同experience的数量
    salary_count = df.groupBy("keyword", "salary").count()
    salary_count = salary_count.withColumn("salary", col("salary").cast("int"))

    # 清除格式不对的薪资
    filter_data = salary_count.filter(salary_count['salary'] <= 100)

    # 分组排序
    sort_data = filter_data.orderBy("keyword", asc("salary"))

    # 显示结果
    sort_data.show()

    # 写入文件
    sort_data.coalesce(1).write.csv("file:///mnt/hgfs/project_data/count_salary", header=True, mode='overwrite')

    # 停止spark会话
    spark.stop()

# 含参数，用于直接向前端返回结果
def get_count_salary(keyword:str):

    # 初始化spark会话
    spark = SparkSession.builder.appName("count_salary").getOrCreate()

    # 读取文件
    df = spark.read.csv(path, header=True, multiLine=True)

    # 先筛选出对应列，减少运行时间
    df = df.filter((df["keyword"] == keyword))

    # 统计同一个keyword下，不同experience的数量
    salary_count = df.groupBy("keyword", "salary").count()

    #把salary转为数值型
    salary_count = salary_count.withColumn("salary", col("salary").cast("int"))

    # 清除格式不对的薪资
    filter_data = salary_count.filter((salary_count['salary'] <= 100) & (salary_count["keyword"] == keyword))

    # 排序
    sort_data = filter_data.sort(asc('salary'))

    # 转json文件
    pd_data = sort_data.toPandas()
    json_data = pd_data.to_json(force_ascii=False)

    # 停止spark会话
    spark.stop()
    return json_data

