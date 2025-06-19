from pyspark.sql import SparkSession

def word_count(input_data):
    spark = SparkSession.builder.appName("WordCount").getOrCreate()
    rdd = spark.sparkContext.parallelize(input_data)
    counts = rdd.flatMap(lambda line: line.split(" ")) \
                .map(lambda word: (word, 1)) \
                .reduceByKey(lambda a, b: a + b)
    return counts.collect()

if __name__ == "__main__":
    sample_data = ["hello world", "hello PySpark"]
    result = word_count(sample_data)
    print(result)
