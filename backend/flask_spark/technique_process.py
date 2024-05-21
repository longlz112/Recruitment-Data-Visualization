from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, explode, desc, when
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number
import pandas as pd

# 本地读取路径
path = "file:///mnt/hgfs/project_data/merge_all.csv"
# 将technique列内容展开，！注意，运行时间较长
def Count_skill():

    # 初始化Spark会话
    spark = SparkSession.builder.appName("SkillFrequency").getOrCreate()

    # 读取CSV文件
    df = spark.read.csv(path, header=True, inferSchema=True)

    # 分割technique列，并展开为单独的行，处理格式不对的数据
    df_exploded = df.withColumn("skill", explode(split(col("technique"), "/")))
    df_exploded2 = df_exploded.withColumn('skill', when(col('skill') == 'c#', 'C#')
                                          .when(col('skill') == 'c++', 'C++')
                                          .when(col('skill') == 'C语言', 'C')
                                          .when(col('skill') == 'python', 'Python')
                                          .when(col('skill') == 'java', 'Java')
                                          .when(col('skill') == 'vue', 'Vue')
                                          .when(col('skill') == 'HTML5', 'HTML')
                                          .when(col('skill') == 'html', 'HTML')
                                          .when(col('skill') == 'css', 'CSS')
                                          .when(col('skill') == 'javascript', 'Javascript')
                                          .when(col('skill') == 'php', 'PHP')
                                          .when(col('skill') == 'spark', 'Spark')
                                          .when(col('skill') == 'mysql', 'MySQL')
                                          .when(col('skill') == 'sql', 'SQL')
                                          .otherwise(col('skill')))

    # 对keyword和skill进行分组，并计算每种技能的出现次数
    skill_frequency = df_exploded2.groupBy("keyword", "skill").count()

    skill_frequency_2 = skill_frequency.orderBy("keyword", desc("count"))

    # 用于保存前20的数据
    # # 定义窗口规格，按keyword分组，按count降序排序
    # windowSpec = Window.partitionBy("keyword").orderBy(desc("count"))
    #
    # # 使用窗口函数分配行号
    # ranked_skills = skill_frequency_2.withColumn("rank", row_number().over(windowSpec))
    #
    # # 过滤出每个keyword组内排名前20的记录
    # top_20_skills = ranked_skills.filter(col("rank") <= 20)

    # 显示结果
    skill_frequency_2.show()

    skill_frequency_2.coalesce(1).write.csv("file:///mnt/hgfs/project_data/count_skill", header=True, mode='overwrite')

    # 停止Spark会话
    spark.stop()


# 在展开technique前先进行筛选，减少运行时间
def count_by_keyword(keyword: str):

    # 初始化Spark会话
    spark = SparkSession.builder.appName("SkillFrequency").getOrCreate()

    # 读取CSV文件
    df = spark.read.csv(path, header=True, inferSchema=True)

    # 筛选
    df_filter = df.filter(df['keyword'] == keyword)

    # 分割technique列，并展开为单独的行，处理格式不对的数据
    df_exploded = df_filter.withColumn("skill", explode(split(col("technique"), "/")))
    df_exploded2 = df_exploded.withColumn('skill', when(col('skill') == 'c#', 'C#')
                                          .when(col('skill') == 'c++', 'C++')
                                          .when(col('skill') == 'C语言', 'C')
                                          .when(col('skill') == 'python', 'Python')
                                          .when(col('skill') == 'java', 'Java')
                                          .when(col('skill') == 'vue', 'Vue')
                                          .when(col('skill') == 'HTML5', 'HTML')
                                          .when(col('skill') == 'html', 'HTML')
                                          .when(col('skill') == 'css', 'CSS')
                                          .when(col('skill') == 'javascript', 'Javascript')
                                          .when(col('skill') == 'php', 'PHP')
                                          .when(col('skill') == 'spark', 'Spark')
                                          .when(col('skill') == 'mysql', 'MySQL')
                                          .when(col('skill') == 'sql', 'SQL')
                                          .otherwise(col('skill')))

    # 对keyword和skill进行分组，并计算每种技能的出现次数
    skill_frequency = df_exploded2.groupBy("keyword", "skill").count()

    skill_frequency_2 = skill_frequency.orderBy("keyword", desc("count"))

    # 选出前20的数据
    select_data = skill_frequency_2.limit(20)

    # 转json文件
    pd_data = select_data.toPandas()
    json_data = pd_data.to_json(force_ascii=False)

    # 停止Spark会话
    spark.stop()
    return json_data
