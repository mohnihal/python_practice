'''SPark MNM Count'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import count
import sys

if len(sys.argv) !=2:
    print ("error:")
    sys.exit(-1)
spark = SparkSession.builder.appName("PythonMnMCount").getOrCreate()
mnm_file = sys.argv[1]
mnmdf = spark.read.format("csv").option("header","true").option("inferSchema","true").load(mnm_file)

mnm_df_filter = mnmdf.select("State","Color","Count").groupBy("State","Color").agg(count("Count").alias("Total")).orderBy("Total",ascending=False)

mnm_df_filter.show(60,truncate=False)

mnm_df_ca = mnmdf.select("State","Color","Count").where(mnmdf.State=="CA").groupBy("State","Color").agg(count("Count").alias("Total")).orderBy("Total",ascending=False)

mnm_df_ca.show(10,truncate=False)
mnm_df_ca.stop()