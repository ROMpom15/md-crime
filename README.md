# md-crime
This is a core skill for any Big Data project. The pipeline from **Raw Data $\rightarrow$ HDFS $\rightarrow$ Spark** forms the essential **Extract, Load, Transform (ELT)** foundation.

Here is a step-by-step walkthrough using Python/Pandas for the initial E/L phase and PySpark for the T phase.

-----

## Phase 1: E $\rightarrow$ L (Extract Raw Data & Load to HDFS as Parquet)

The goal here is to get your proprietary `.xls` and `.sav` files into the optimal, distributed format (**Parquet**) and store them in the primary data lake (**HDFS**).

### 1\. Extract from Proprietary Files (Local Processing)

Since Spark cannot natively read formats like `.sav`, you must first convert them into a pandas DataFrame locally on an edge node or a machine with the required libraries.

| Format | Library & Code |
| :--- | :--- |
| **SPSS (.sav)** | You need **`pyreadstat`**. `pandas.read_spss()` also uses this library behind the scenes. |
| **Excel (.xls)** | You need **`openpyxl`**. `pandas.read_excel()` uses this engine. |

```python
import pandas as pd
# You may need: pip install pyreadstat openpyxl pyarrow

def read_and_clean_data(file_path):
    # Determine file type
    if file_path.endswith('.sav'):
        # Read SPSS file, applying value labels for categorical data
        df, meta = pd.read_spss(file_path, convert_categoricals=True, usecols=None, read_data_only=False)
    elif file_path.endswith('.xls') or file_path.endswith('.xlsx'):
        # Read Excel file
        df = pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file type for {file_path}")

    # Standardize Column Names (e.g., lowercase and replace spaces with underscores)
    df.columns = df.columns.str.lower().str.replace(' ', '_', regex=False)

    # Convert all string-like columns to the 'string' dtype for better Parquet handling
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('string')

    return df

# Example Execution (run this for each raw file)
try:
    campus_crime_df = read_and_clean_data('path/to/raw/md_campus_crime.sav')
    # If the combined data is over ~1GB, this step MUST be distributed using Spark's Pandas UDFs
    # or performed on a distributed engine (e.g., Dask, or specialized tools).
    # Since you start with local files, pandas is the most straightforward method.

except Exception as e:
    print(f"Error during extraction/local cleaning: {e}")
```

### 2\. Load to HDFS (Intermediate Step: Local Parquet $\rightarrow$ HDFS)

You cannot write a pandas DataFrame directly into the **distributed** structure of HDFS. The simplest method is to use a low-level HDFS client or command line tools to upload the converted Parquet file.

```python
# 1. Convert the Pandas DataFrame to a Local Parquet file
local_parquet_path = '/tmp/campus_crime_data.parquet'
campus_crime_df.to_parquet(local_parquet_path, engine='pyarrow', compression='snappy')
print(f"Pandas DataFrame written to local Parquet file: {local_parquet_path}")

# 2. Upload the Parquet file to HDFS using command-line (or a Python HDFS client)
# Assuming your HDFS is configured and accessible via the 'hdfs' command:
hdfs_path = '/user/YOUR_USER/campus_safety/raw_data/'

# Execute HDFS command to put the local file into the distributed file system
import subprocess
try:
    subprocess.run(['hdfs', 'dfs', '-put', '-f', local_parquet_path, hdfs_path], check=True)
    print(f"Successfully loaded Parquet file to HDFS at: {hdfs_path}")
except subprocess.CalledProcessError as e:
    print(f"HDFS upload failed. Ensure 'hdfs' command is available and permissions are set. Error: {e}")
```

-----

## Phase 2: T (Spark Processing on HDFS Data)

Now that your data is in **Parquet format** on **HDFS**, it's ready for high-performance, distributed processing with Spark.

### 3\. Read Parquet from HDFS into Spark DataFrame

You must first initialize a Spark Session, then you can use the built-in `read.parquet()` function. Spark is intelligent enough to read Parquet directly from the HDFS location.

```python
from pyspark.sql import SparkSession

# 1. Initialize Spark Session (Mandatory Component)
spark = SparkSession.builder \
    .appName("CampusCrimeETL") \
    .getOrCreate()

# The HDFS path to your Parquet file(s)
hdfs_input_path = 'hdfs:///user/YOUR_USER/campus_safety/raw_data/'

# 2. Read the Parquet data into a Spark DataFrame
# Spark automatically infers the schema and uses columnar storage (Parquet) efficiently.
spark_df = spark.read.parquet(hdfs_input_path)

# Display the schema and some data for verification
print("--- Spark DataFrame Schema ---")
spark_df.printSchema()
print("--- Spark DataFrame Sample ---")
spark_df.show(5)
```

### 4\. Distributed Transformation (Spark ETL/ML)

This is where you execute your Big Data logic on the distributed data.

```python
from pyspark.sql.functions import col, year, month, dayofweek

# Example Transformations (Data Cleansing and Feature Engineering)

# 1. Filter out null or incomplete records
cleaned_df = spark_df.na.drop(subset=["reported_date", "crime_type", "campus_id"])

# 2. Derive temporal features (good for predictive model)
transformed_df = cleaned_df.withColumn("report_year", year(col("reported_date"))) \
                           .withColumn("report_month", month(col("reported_date"))) \
                           .withColumn("day_of_week", dayofweek(col("reported_date")))

# 3. Aggregation (Count crimes by university and year)
analysis_df = transformed_df.groupBy("campus_id", "report_year", "crime_type") \
                            .count() \
                            .orderBy("count", ascending=False)

print("--- Analysis DataFrame Sample (Top Crime Counts) ---")
analysis_df.show(5)
```

### 5\. Write Final Results to a Serving Layer

For your project, the final results will go to **Cassandra** for the dashboard or back to HDFS/Hive for further batch analytics.

```python
# --- Option A: Write back to HDFS as Parquet (for re-use or Hive tables) ---
hdfs_output_path_parquet = 'hdfs:///user/YOUR_USER/campus_safety/cleaned_data/'

# Partition the data by a key like 'report_year' for optimized future querying
analysis_df.write \
    .mode("overwrite") \
    .partitionBy("report_year") \
    .parquet(hdfs_output_path_parquet)

print(f"Final Parquet data written to HDFS: {hdfs_output_path_parquet}")

# --- Option B: Write to Cassandra (for the predictive dashboard) ---
# Requires spark-cassandra-connector JAR installed in your environment
# analysis_df.write \
#     .format("org.apache.spark.sql.cassandra") \
#     .mode("append") \
#     .option("keyspace", "campus_keyspace") \
#     .option("table", "crime_counts") \
#     .save()
```

This pipeline provides a robust and scalable foundation for your project, moving the data from a fragile legacy format to a distributed, analysis-ready state.