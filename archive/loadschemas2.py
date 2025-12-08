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
from pyspark.sql.functions import col

# ============================================================
# SPARK SESSION
# ============================================================
spark = SparkSession.builder \
    .appName("CampusSafetyLoad") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9000") \
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
# SCHEMAS
# ============================================================
institution_fields = [
    StructField("UNITID_P", LongType(), True),
    StructField("INSTNM", StringType(), True),
    StructField("OPEID", StringType(), True),
    StructField("BRANCH", StringType(), True),
    StructField("Address", StringType(), True),
    StructField("City", StringType(), True),
    StructField("State", StringType(), True),
    StructField("ZIP", StringType(), True),
    StructField("sector_cd", IntegerType(), True),
    StructField("Sector_desc", StringType(), True),
    StructField("men_total", FloatType(), True),
    StructField("women_total", FloatType(), True),
    StructField("Total", FloatType(), True),
]

# --- FIX: REMOVED ALL FILTER FIELDS FROM SCHEMAS ---

def make_crime_schema(years):
    offense_codes = ["MURD", "NEG_M", "RAPE", "FONDL", "INCES", "STATR", "ROBBE", "AGG_A", "BURGLA", "VEHIC", "ARSON"]
    fields = []
    
    for y in years:
        for code in offense_codes:
            fields.append(StructField(f"{code}{y}", StringType(), True))
        # REMOVED: FILTER{y}
    
    return StructType(institution_fields + fields)

def make_discipline_schema(years):
    fields = []
    
    for y in years:
        for code in ["WEAPON", "DRUG", "LIQUOR"]:
            fields.append(StructField(f"{code}{y}", StringType(), True))
        # REMOVED: FILTER{y}
        
    return StructType(institution_fields + fields)

def make_vawa_schema(years):
    fields = []
    
    for y in years:
        for code in ["DOMEST", "DATING", "STALK"]:
            fields.append(StructField(f"{code}{y}", StringType(), True))
        # REMOVED: FILTER{y}
        
    return StructType(institution_fields + fields)

def make_hate_schema(years):
    offenses = ["MURD", "RAPE", "FOND", "INCE", "STAT", "ROBBE", "AGG_A", "BURGLA", "VEHIC", "ARSON", "SIM_A", "LAR_T", "INTIM", "VANDAL"]
    suffixes = ["", "_RAC", "_REL", "_SEX", "_GEN", "_GID", "_DIS", "_ET", "_NAT"]
    fields = []
    
    for y in years:
        for off in offenses:
            for suf in suffixes:
                fields.append(StructField(f"{off}{suf}{y}", StringType(), True))
        # REMOVED: FILTER{y}
        
    return StructType(institution_fields + fields)

years_181920 = ["18", "19", "20"]
years_212223 = ["21", "22", "23"]

crime_schema_181920 = make_crime_schema(years_181920)
discipline_schema_181920 = make_discipline_schema(years_181920)
vawa_schema_181920 = make_vawa_schema(years_181920)
hate_schema_181920 = make_hate_schema(years_181920)

crime_schema_212223 = make_crime_schema(years_212223)
discipline_schema_212223 = make_discipline_schema(years_212223)
vawa_schema_212223 = make_vawa_schema(years_212223)
hate_schema_212223 = make_hate_schema(years_212223)

# ============================================================
# LOAD HELPERS
# ============================================================
def load_csv(spark, path, schema):
    return spark.read.option("header", True).schema(schema).csv(path)

# ============================================================
# DATA LOADING (Capitalized filenames)
# ============================================================

# --- 181920 ---
oncampuscrime181920_df = load_csv(spark, base_181920 + "Oncampuscrime181920.csv", crime_schema_181920)
# oncampusdiscipline181920_df = load_csv(spark, base_181920 + "Oncampusdiscipline181920.csv", discipline_schema_181920) THESE DONT EXIST!@!@!@@@@
oncampushate181920_df = load_csv(spark, base_181920 + "Oncampushate181920.csv", hate_schema_181920)
oncampusvawa181920_df = load_csv(spark, base_181920 + "Oncampusvawa181920.csv", vawa_schema_181920)

residencehallcrime181920_df = load_csv(spark, base_181920 + "Residencehallcrime181920.csv", crime_schema_181920)
residencehalldiscipline181920_df = load_csv(spark, base_181920 + "Residencehalldiscipline181920.csv", discipline_schema_181920)
residencehallhate181920_df = load_csv(spark, base_181920 + "Residencehallhate181920.csv", hate_schema_181920)
residencehallvawa181920_df = load_csv(spark, base_181920 + "Residencehallvawa181920.csv", vawa_schema_181920)

publicpropertycrime181920_df = load_csv(spark, base_181920 + "Publicpropertycrime181920.csv", crime_schema_181920)
publicpropertydiscipline181920_df = load_csv(spark, base_181920 + "Publicpropertydiscipline181920.csv", discipline_schema_181920)
publicpropertyhate181920_df = load_csv(spark, base_181920 + "Publicpropertyhate181920.csv", hate_schema_181920)
publicpropertyvawa181920_df = load_csv(spark, base_181920 + "Publicpropertyvawa181920.csv", vawa_schema_181920)

reportedcrime181920_df = load_csv(spark, base_181920 + "Reportedcrime181920.csv", crime_schema_181920)
reporteddiscipline181920_df = load_csv(spark, base_181920 + "Reporteddiscipline181920.csv", discipline_schema_181920)
reportedhate181920_df = load_csv(spark, base_181920 + "Reportedhate181920.csv", hate_schema_181920)
reportedvawa181920_df = load_csv(spark, base_181920 + "Reportedvawa181920.csv", vawa_schema_181920)

# --- 212223 ---
oncampuscrime212223_df = load_csv(spark, base_212223 + "Oncampuscrime212223.csv", crime_schema_212223)
# oncampusdiscipline212223_df = load_csv(spark, base_212223 + "Oncampusdiscipline212223.csv", discipline_schema_212223) THESE DONT EXIST!@!@!@@@@
oncampushate212223_df = load_csv(spark, base_212223 + "Oncampushate212223.csv", hate_schema_212223)
oncampusvawa212223_df = load_csv(spark, base_212223 + "Oncampusvawa212223.csv", vawa_schema_212223)

residencehallcrime212223_df = load_csv(spark, base_212223 + "Residencehallcrime212223.csv", crime_schema_212223)
residencehalldiscipline212223_df = load_csv(spark, base_212223 + "Residencehalldiscipline212223.csv", discipline_schema_212223)
residencehallhate212223_df = load_csv(spark, base_212223 + "Residencehallhate212223.csv", hate_schema_212223)
residencehallvawa212223_df = load_csv(spark, base_212223 + "Residencehallvawa212223.csv", vawa_schema_212223)

publicpropertycrime212223_df = load_csv(spark, base_212223 + "Publicpropertycrime212223.csv", crime_schema_212223)
publicpropertydiscipline212223_df = load_csv(spark, base_212223 + "Publicpropertydiscipline212223.csv", discipline_schema_212223)
publicpropertyhate212223_df = load_csv(spark, base_212223 + "Publicpropertyhate212223.csv", hate_schema_212223)
publicpropertyvawa212223_df = load_csv(spark, base_212223 + "Publicpropertyvawa212223.csv", vawa_schema_212223)

reportedcrime212223_df = load_csv(spark, base_212223 + "Reportedcrime212223.csv", crime_schema_212223)
reporteddiscipline212223_df = load_csv(spark, base_212223 + "Reporteddiscipline212223.csv", discipline_schema_212223)
reportedhate212223_df = load_csv(spark, base_212223 + "Reportedhate212223.csv", hate_schema_212223)
reportedvawa212223_df = load_csv(spark, base_212223 + "Reportedvawa212223.csv", vawa_schema_212223)

# ============================================================
# UNIONS AND WRITES TO HDFS
# ============================================================

# 1. VAWA
print("Processing VAWA...")
vawa = reportedvawa181920_df \
    .unionByName(reportedvawa212223_df, allowMissingColumns=True) \
    .unionByName(publicpropertyvawa181920_df, allowMissingColumns=True) \
    .unionByName(publicpropertyvawa212223_df, allowMissingColumns=True) \
    .unionByName(residencehallvawa181920_df, allowMissingColumns=True) \
    .unionByName(residencehallvawa212223_df, allowMissingColumns=True) \
    .unionByName(oncampusvawa181920_df, allowMissingColumns=True) \
    .unionByName(oncampusvawa212223_df, allowMissingColumns=True)

vawa.write.mode("overwrite").parquet(f"{hdfs_write_root}/vawa.parquet")

# 2. Crime
print("Processing Crime...")
crime = reportedcrime181920_df \
    .unionByName(reportedcrime212223_df, allowMissingColumns=True) \
    .unionByName(publicpropertycrime181920_df, allowMissingColumns=True) \
    .unionByName(publicpropertycrime212223_df, allowMissingColumns=True) \
    .unionByName(residencehallcrime181920_df, allowMissingColumns=True) \
    .unionByName(residencehallcrime212223_df, allowMissingColumns=True) \
    .unionByName(oncampuscrime181920_df, allowMissingColumns=True) \
    .unionByName(oncampuscrime212223_df, allowMissingColumns=True)

crime.write.mode("overwrite").parquet(f"{hdfs_write_root}/crime.parquet")

# 3. Discipline (FIX: Including previously missed oncampus DataFrames)
print("Processing Discipline...")
discipline = reporteddiscipline181920_df \
    .unionByName(reporteddiscipline212223_df, allowMissingColumns=True) \
    .unionByName(publicpropertydiscipline181920_df, allowMissingColumns=True) \
    .unionByName(publicpropertydiscipline212223_df, allowMissingColumns=True) \
    .unionByName(residencehalldiscipline181920_df, allowMissingColumns=True) \
    .unionByName(residencehalldiscipline212223_df, allowMissingColumns=True) \
    # .unionByName(oncampusdiscipline181920_df, allowMissingColumns=True) \THESE DONT EXIST!@!@!@@@@ 
    # .unionByName(oncampusdiscipline212223_df, allowMissingColumns=True) THESE DONT EXIST!@!@!@@@@

discipline.write.mode("overwrite").parquet(f"{hdfs_write_root}/discipline.parquet")

# 4. Hate
print("Processing Hate Crimes...")
hate = reportedhate181920_df \
    .unionByName(reportedhate212223_df, allowMissingColumns=True) \
    .unionByName(publicpropertyhate181920_df, allowMissingColumns=True) \
    .unionByName(publicpropertyhate212223_df, allowMissingColumns=True) \
    .unionByName(residencehallhate181920_df, allowMissingColumns=True) \
    .unionByName(residencehallhate212223_df, allowMissingColumns=True) \
    .unionByName(oncampushate181920_df, allowMissingColumns=True) \
    .unionByName(oncampushate212223_df, allowMissingColumns=True)

hate.write.mode("overwrite").parquet(f"{hdfs_write_root}/hate.parquet")

print("Done! Files saved to HDFS.")