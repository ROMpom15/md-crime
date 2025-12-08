import os
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    LongType,
    FloatType
)
from functools import reduce
from pyspark.sql.functions import col, when, lit

# ============================================================
# SPARK SESSION
# ============================================================
spark = SparkSession.builder \
    .appName("CampusSafetyLoad") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9000") \
    .config("spark.driver.extraJavaOptions", "-Dsun.net.resolve.tag_cache.lifetime=0") \
    .config("spark.executor.extraJavaOptions", "-Dsun.net.resolve.tag_cache.lifetime=0") \
    .config("dfs.client.socket-timeout", "300000") \
    .getOrCreate()

# ============================================================
# PATH SETUP
# ============================================================
# 1. Get the absolute path to your LOCAL CSV files
script_dir = os.path.dirname(os.path.abspath(__file__))
# Navigate: src/preproc/ -> src/ -> md-crime/ -> data/datasets_csv/
local_csv_path = os.path.abspath(os.path.join(script_dir, "../../data/datasets_csv"))

# 2. Define Read Paths (Use file:// for local disk)
base_181920 = f"file://{local_csv_path}/"
base_212223 = f"file://{local_csv_path}/"

# 3. Define Write Path (Use hdfs:// for Hadoop)
hdfs_write_root = "hdfs://localhost:9000/data/merged"

print(f"DEBUG: Reading from Local: {base_181920}")
print(f"DEBUG: Writing to HDFS:  {hdfs_write_root}")

# ============================================================
# SCHEMA INFERENCE AND LOAD HELPERS
# ============================================================
def load_csv_and_show_schema(spark, path, name):
    """
    Loads a CSV file by inferring the schema, prints the schema, 
    and shows the first 5 rows.
    """
    # Use inferSchema=True to automatically detect column data types.
    # Note: Many count columns might still be inferred as StringType if they contain empty strings/missing data.
    df = spark.read.option("header", True).option("inferSchema", True).csv(path)
    print(f"\n--- Loaded DataFrame: {name} ---")
    df.printSchema()
    print("First 5 rows:")
    df.show(5, truncate=False)
    return df

# ============================================================
# DATA LOADING (Capitalized filenames)
# ============================================================

# --- 181920 ---
oncampuscrime181920_df = load_csv_and_show_schema(spark, base_181920 + "Oncampuscrime181920.csv", "oncampuscrime181920_df")
oncampushate181920_df = load_csv_and_show_schema(spark, base_181920 + "Oncampushate181920.csv", "oncampushate181920_df")
oncampusvawa181920_df = load_csv_and_show_schema(spark, base_181920 + "Oncampusvawa181920.csv", "oncampusvawa181920_df")

residencehallcrime181920_df = load_csv_and_show_schema(spark, base_181920 + "Residencehallcrime181920.csv", "residencehallcrime181920_df")
residencehalldiscipline181920_df = load_csv_and_show_schema(spark, base_181920 + "Residencehalldiscipline181920.csv", "residencehalldiscipline181920_df")
residencehallhate181920_df = load_csv_and_show_schema(spark, base_181920 + "Residencehallhate181920.csv", "residencehallhate181920_df")
residencehallvawa181920_df = load_csv_and_show_schema(spark, base_181920 + "Residencehallvawa181920.csv", "residencehallvawa181920_df")

publicpropertycrime181920_df = load_csv_and_show_schema(spark, base_181920 + "Publicpropertycrime181920.csv", "publicpropertycrime181920_df")
publicpropertydiscipline181920_df = load_csv_and_show_schema(spark, base_181920 + "Publicpropertydiscipline181920.csv", "publicpropertydiscipline181920_df")
publicpropertyhate181920_df = load_csv_and_show_schema(spark, base_181920 + "Publicpropertyhate181920.csv", "publicpropertyhate181920_df")
publicpropertyvawa181920_df = load_csv_and_show_schema(spark, base_181920 + "Publicpropertyvawa181920.csv", "publicpropertyvawa181920_df")

reportedcrime181920_df = load_csv_and_show_schema(spark, base_181920 + "Reportedcrime181920.csv", "reportedcrime181920_df")
reporteddiscipline181920_df = load_csv_and_show_schema(spark, base_181920 + "Reporteddiscipline181920.csv", "reporteddiscipline181920_df")
reportedhate181920_df = load_csv_and_show_schema(spark, base_181920 + "Reportedhate181920.csv", "reportedhate181920_df")
reportedvawa181920_df = load_csv_and_show_schema(spark, base_181920 + "Reportedvawa181920.csv", "reportedvawa181920_df")

# --- 212223 ---
oncampuscrime212223_df = load_csv_and_show_schema(spark, base_212223 + "Oncampuscrime212223.csv", "oncampuscrime212223_df")
oncampushate212223_df = load_csv_and_show_schema(spark, base_212223 + "Oncampushate212223.csv", "oncampushate212223_df")
oncampusvawa212223_df = load_csv_and_show_schema(spark, base_212223 + "Oncampusvawa212223.csv", "oncampusvawa212223_df")

residencehallcrime212223_df = load_csv_and_show_schema(spark, base_212223 + "Residencehallcrime212223.csv", "residencehallcrime212223_df")
residencehalldiscipline212223_df = load_csv_and_show_schema(spark, base_212223 + "Residencehalldiscipline212223.csv", "residencehalldiscipline212223_df")
residencehallhate212223_df = load_csv_and_show_schema(spark, base_212223 + "Residencehallhate212223.csv", "residencehallhate212223_df")
residencehallvawa212223_df = load_csv_and_show_schema(spark, base_212223 + "Residencehallvawa212223.csv", "residencehallvawa212223_df")

publicpropertycrime212223_df = load_csv_and_show_schema(spark, base_212223 + "Publicpropertycrime212223.csv", "publicpropertycrime212223_df")
publicpropertydiscipline212223_df = load_csv_and_show_schema(spark, base_212223 + "Publicpropertydiscipline212223.csv", "publicpropertydiscipline212223_df")
publicpropertyhate212223_df = load_csv_and_show_schema(spark, base_212223 + "Publicpropertyhate212223.csv", "publicpropertyhate212223_df")
publicpropertyvawa212223_df = load_csv_and_show_schema(spark, base_212223 + "Publicpropertyvawa212223.csv", "publicpropertyvawa212223_df")

reportedcrime212223_df = load_csv_and_show_schema(spark, base_212223 + "Reportedcrime212223.csv", "reportedcrime212223_df")
reporteddiscipline212223_df = load_csv_and_show_schema(spark, base_212223 + "Reporteddiscipline212223.csv", "reporteddiscipline212223_df")
reportedhate212223_df = load_csv_and_show_schema(spark, base_212223 + "Reportedhate212223.csv", "reportedhate212223_df")
reportedvawa212223_df = load_csv_and_show_schema(spark, base_212223 + "Reportedvawa212223.csv", "reportedvawa212223_df")

# ============================================================
# UTILITY FUNCTIONS
# ============================================================
def get_count_columns(df):
    """
    Identifies count columns based on a pattern (ends with two digits for the year)
    and excludes institution-related fields.
    """
    institution_fields = ["UNITID_P", "INSTNM", "OPEID", "BRANCH", "Address", "City", "State", "ZIP", "sector_cd", "Sector_desc", "men_total", "women_total", "Total"]
    return [c for c in df.columns if c not in institution_fields and c[-2:].isdigit()]

def clean_and_fill(df):
    """
    Casts all identified count columns to LongType and fills resulting nulls with 0.
    This handles cases where original string columns were read as null/empty string.
    """
    count_cols = get_count_columns(df)
    
    for c in count_cols:
        # Cast the column to LongType. If casting fails (e.g., non-numeric data), it will result in NULL.
        # This is a safe way to prepare for fillna.
        df = df.withColumn(c, col(c).cast(LongType()))
    
    # Fill NA/NULL values in the specified numeric columns with 0
    fill_dict = {c: 0 for c in count_cols}
    df = df.fillna(fill_dict)
    
    return df

# ============================================================
# UNIONS AND WRITES TO HDFS
# ============================================================

def union_and_show(dataframes, name, hdfs_path):
    """
    Performs a unionByName, cleans the resulting DataFrame, 
    prints the final schema, shows the first 5 rows, and writes to HDFS.
    """
    print(f"\n====================================================")
    print(f"Processing UNION and CLEANING for: {name}")
    
    # 1. Union DataFrames
    union_df = reduce(lambda df1, df2: df1.unionByName(df2, allowMissingColumns=True), dataframes)
    
    print(f"--- Schema of Unified DataFrame before Cleaning: {name} ---")
    union_df.printSchema()
    
    # 2. Clean and Fill (Cast to Long and fill nulls with 0)
    final_df = clean_and_fill(union_df)
    
    print(f"--- Schema of Unified DataFrame AFTER Cleaning/Filling: {name} ---")
    final_df.printSchema()
    print("First 5 rows of Unified DataFrame (Nulls should be 0 in count columns):")
    final_df.show(5, truncate=False)
    
    # 3. Write to HDFS
    final_df.write.mode("overwrite").parquet(hdfs_path)
    print(f"SUCCESS: {name} saved to HDFS at {hdfs_path}")
    return final_df

# 1. VAWA
vawa_dfs = [
    reportedvawa181920_df, reportedvawa212223_df,
    publicpropertyvawa181920_df, publicpropertyvawa212223_df,
    residencehallvawa181920_df, residencehallvawa212223_df,
    oncampusvawa181920_df, oncampusvawa212223_df
]
vawa = union_and_show(vawa_dfs, "VAWA", f"{hdfs_write_root}/vawa.parquet")

# 2. Crime
crime_dfs = [
    reportedcrime181920_df, reportedcrime212223_df,
    publicpropertycrime181920_df, publicpropertycrime212223_df,
    residencehallcrime181920_df, residencehallcrime212223_df,
    oncampuscrime181920_df, oncampuscrime212223_df
]
crime = union_and_show(crime_dfs, "Crime", f"{hdfs_write_root}/crime.parquet")

# 3. Discipline (Excluding non-existent oncampus discipline DFs)
discipline_dfs = [
    reporteddiscipline181920_df, reporteddiscipline212223_df,
    publicpropertydiscipline181920_df, publicpropertydiscipline212223_df,
    residencehalldiscipline181920_df, residencehalldiscipline212223_df
]
discipline = union_and_show(discipline_dfs, "Discipline", f"{hdfs_write_root}/discipline.parquet")

# 4. Hate
hate_dfs = [
    reportedhate181920_df, reportedhate212223_df,
    publicpropertyhate181920_df, publicpropertyhate212223_df,
    residencehallhate181920_df, residencehallhate212223_df,
    oncampushate181920_df, oncampushate212223_df
]
hate = union_and_show(hate_dfs, "Hate Crimes", f"{hdfs_write_root}/hate.parquet")

print("\nDone! All files saved to HDFS.")
spark.stop()