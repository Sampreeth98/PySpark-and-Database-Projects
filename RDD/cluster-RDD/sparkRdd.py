'''
    This is spark program to read the data from hdfs and write the output to the HDFS directory
    The program reads an input data and constructs a rdd.
    Transformations and actions are applied to genreate the output back to HDFS.
'''

import pyspark
import time
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('RDD_program').master('local[2]').getOrCreate()
sc = spark.sparkContext
#rdd2 = sc.textFile('/home/jayantm/Spark/rdd_datasets/temp_data.txt') # This is local file system
text_file = sc.textFile("hdfs://nn.insofe.edu.in/user/insofe/input.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
                  .map(lambda word: (word, 1)) \
                  .reduceByKey(lambda a, b: a + b)
#print(counts.take(4))
time.sleep(120)
counts.saveAsTextFile("hdfs://nn.insofe.edu.in/user/insofe/B97/rddoutput")