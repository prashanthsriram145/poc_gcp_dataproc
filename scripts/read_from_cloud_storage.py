from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.master('local').appName('read_from_bigquery_write_to_bigquery').getOrCreate()

schema = StructType([
    StructField('ID', IntegerType(), True),
    StructField('ATTR1', StringType(), True)
])

# Create data frame
json_file_path = 'gs://spk-spikey-df-store/data/input_data.txt'
df = spark.read.json(json_file_path, schema=schema, multiLine=True)
print(df.schema)
df.show()
