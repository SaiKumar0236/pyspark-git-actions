from pyspark.sql import SparkSession

 spark = SparkSession.builder.appName("GitHubActionsTest").getOrCreate()
 data = [("Sai", 1), ("Kumar", 2)]
 df = spark.createDataFrame(data, ["name", "id"])
 df.show()
 spark.stop()
