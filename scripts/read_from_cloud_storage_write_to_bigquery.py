from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.master('local').appName('read_from_bigquery_write_to_bigquery').getOrCreate()

schema = StructType([
    StructField('ID', IntegerType(), True),
    StructField('ATTR1', StringType(), True)
])


# Load data from BigQuery.
# words = spark.read.format('bigquery') \
#   .option('table', 'bigquery-public-data:samples.shakespeare') \
#   .load()

bucket = "spk_tempbucket"
spark.conf.set('temporaryGcsBucket', bucket)

# json path to read from local machine
# json_file_path = '../data/input_data.txt'

json_file_path = 'gs://spk-spikey-df-store/data/input_data.txt'
df = spark.read.json(json_file_path, schema=schema, multiLine=True)
print(df.schema)
df.show()

df.write.format('bigquery').option('table', 'spikey-developers-377712:sample.output_data').save()
