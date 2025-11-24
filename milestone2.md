# System Architecture Document
## Big Data Computing - Group Project

**Team Number:** 7  
**Project Title:** Crime on College Campuses  
**Date:** 24 NOV 2025      

---

## Executive Summary

[2-3 paragraphs providing a high-level overview of your system, its purpose, key technical decisions, and current implementation status]

Our system is collecting data and metrics regarding crime in the United States in order to determine patterns of crime. Our only technical decision was storing data using HDFS. HDFS was unable to process excel files so we converted the 30 excel files into CSVs. We then processed them using HDFS. All of the files have been converted, they just need to be run. 

---

## 1. System Architecture Overview

### 1.1 Architecture Diagram

```
[Insert your detailed architecture diagram here]
Include:
- Data sources
- Ingestion layer
- Processing layer
- Storage layer
- Presentation layer
- All technologies used at each layer
- Data flow directions

Data Sources → XLS/XLSX (Department of Education), CSV

Ingestion Layer → Direct File Upload

Processing Layer → Spark (PySpark)

Storage Layer → HDFS

Presentation Layer → Jupyter

```

**Diagram Tools:** Use draw.io, Lucidchart, or similar. Export as PNG/PDF.

### 1.2 Architecture Pattern

**Pattern Used:** Batch Processing

**Justification:**
[Explain why you chose this architectural pattern. What are its benefits for your use case?]

We chose this architectural pattern for maximum efficiency and because of our knowledge working with CSVs, Spark, HDFS, and Jupyter. In our case, the benefits include cheap storage and scalability. 

---

## 2. Detailed Component Design

### 2.1 Data Ingestion Layer

**Purpose:** [What this layer does]

The purpose of the Data Ingestion Layer is to collect and cleanse the data from the Department of Education.

**Technologies:** Direct File Upload

**Implementation Details:**
- **Data Source:** Department of Education
- **Ingestion Method:** Batch
- **Data Format:** XLS → CSV
- **Frequency:** Real-time
- **Volume:** Records/second

**Code Snippet:**
```python
# Example of your ingestion code
# Show key logic, not everything
```

**Challenges & Solutions:**
- Alter Schemas: Use the given tables from the DoE to create more accurate schemas. 

---

### 2.2 Data Storage Layer

**Purpose:** [What this layer does]

The Data Storage Layer stores, organizes, and prepares data for use. HDFS specifically stores large files by distributing their contents over multiple clusters.

**Technologies:** HDFS

**Data Organization:**
- **Storage Format:** CSV
- **Partitioning Strategy:** By university
- **Estimated Size:** 135.1 MB

**Schema Design:**
vawa = reportedvawa181920_df \
    .unionByName(reportedvawa212223_df) \
    .unionByName(publicpropertyvawa181920_df) \
    .unionByName(publicpropertyvawa212223_df) \
    .unionByName(residencehallvawa181920_df) \
    .unionByName(residencehallvawa212223_df) \
    .unionByName(oncampusvawa181920_df) \
    .unionByName(oncampusvawa212223_df)

crime = reportedcrime181920_df \
    .unionByName(reportedcrime212223_df) \
    .unionByName(publicpropertycrime181920_df) \
    .unionByName(publicpropertycrime212223_df) \
    .unionByName(residencehallcrime181920_df) \
    .unionByName(residencehallcrime212223_df) \
    .unionByName(oncampuscrime181920_df) \
    .unionByName(oncampuscrime212223_df)

discipline = reporteddiscipline181920_df \
    .unionByName(reporteddiscipline212223_df) \
    .unionByName(publicpropertydiscipline181920_df) \
    .unionByName(publicpropertydiscipline212223_df) \
    .unionByName(residencehalldiscipline181920_df) \
    .unionByName(residencehalldiscipline212223_df) \
    .unionByName(oncampusdiscipline181920_df) \
    .unionByName(oncampusdiscipline212223_df)

hate = reportedhate181920_df \
    .unionByName(reportedhate212223_df) \
    .unionByName(publicpropertyhate181920_df) \
    .unionByName(publicpropertyhate212223_df) \
    .unionByName(residencehallhate181920_df) \
    .unionByName(residencehallhate212223_df) \
    .unionByName(oncampushate181920_df) \
    .unionByName(oncampushate212223_df)

**Optimization Techniques:**
- [Technique 1]: [Description]
- [Technique 2]: [Description]

---

### 2.3 Data Processing Layer

**Purpose:** [What this layer does]

The purpose of the Data Processing Layer is to transform the data into a clean, usable version that can be used for analysis and visualization.

**Technologies:** Spark (PySpark)

**Processing Pipeline:**

```
Stage 2: Transformation (Excel --> CSV, CSV --> Parquet)
    ↓
Stage 3: Aggregation/Analysis
    ↓
Stage 4: Results Storage
```

**Key Transformations:**
1. **[Transformation 1]:** 30 Excel files to 30 CSV files
   - Input: 30 Excel
   - Output: 30 CSV

2. **[Transformation 2]:** 30 CSV to 1 Parquet
   - Input: 30 CSV
   - Output: 1 Parquet

**Code Snippet:**
```python
# Core processing logic
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Example showing your key transformation
```
---

### 2.5 Visualization/Presentation Layer

**Purpose:** [How results are presented]

The purpose of the Visualization/Presentation Layer is to transform and display the data to be easily readable and understandable using graphs, charts, and other visualization methods.

**Technologies:** Jupyter

**Visualization Types:**
- [Viz 1]: Heat map of the United States (more opaque at crime hotspots)
- [Viz 2]: Bar chart displaying highest top 20 crime rates by institution
- [Viz 3]: Bar chart displaying lowest top 20 crime rates by institution

---

## 3. Technology Stack Justification

| Technology | Purpose | Why Chosen | Alternatives Considered |
|------------|---------|------------|------------------------|
| Apache Spark | Data processing | High performance, in-memory computing | Hadoop MapReduce (too slow) |
| Jupyter | NoSQL storage | Iterative, integrated environment, Matplotlib | Tableau |

---

## 4. Scalability Analysis

### 4.1 Current Scale
- **Data Volume:** 135.1 MB
- **Processing Time:** ~ 1 minute
- **Cluster Configuration:** Memory

---

## 5. Implementation Status

### 5.1 Completed Components
- [x] Data ingestion pipeline
- [x] Basic Spark processing
- [x] Storage layer setup
- [ ] Visualization dashboard (not started)

### 5.2 Code Repository

**Repository URL:** (https://github.com/ROMpom15/md-crime)

**Directory Structure:**
```
md-crime/
├── src/
│   ├── ingestion/
│   ├── processing/
│   ├── ml_models/
│   └── utils/
├── configs/
├── notebooks/
├── data/
└── tests/


```
---

## 6. Demonstration Plan

### 6.1 Live Demo Flow 

Our group is going to demonstrate what it looks like to load our data into HDFS then run the code reading from HDFS. From there, we will generate a graphic. 

### 6.2 Backup Plan
[What if live demo fails? Screenshots, video recording, etc.]

If the live demo fails, we will produce a video recording of a successful attempt.

---

### 6.3 Timeline for Final Week (04DEC)

**Day 1-2:** Have everything loaded in by 25NOV. By 01DEC, join the CSVs into one large parquet. 

**Day 3-4:** By 02DEC, we will complete all visualizations. By 03DEC, add finishing touches and complete Jupyter notebook.

---

## 7. Lessons Learned So Far

### 7.1 Technical Insights
- **What worked well:** [e.g., Using Parquet significantly reduced storage]
- **What was challenging:** [e.g., Debugging distributed shuffle operations]
- **Key learning:** [e.g., Importance of partitioning strategy]

### 7.2 Team Process
- **Effective practices:** [e.g., Daily standups kept everyone aligned]
- **Improvements needed:** [e.g., Earlier integration testing]

---

## 8. References

1. [Reference to documentation used]
2. [Reference to tutorials or papers]
3. [Reference to similar projects]

---

**Submit by: Tuesday 25NOV25 @ 0730**
