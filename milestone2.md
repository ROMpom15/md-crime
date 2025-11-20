# System Architecture Document
## Big Data Computing - Group Project

**Team Number:** 7  
**Project Title:** Crime on College Campuses  
**Date:** [Submission Date]  

---

## Executive Summary

[2-3 paragraphs providing a high-level overview of your system, its purpose, key technical decisions, and current implementation status]



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

We chose this architectural pattern for maximum efficiency and because of our knowledge working with CSVs, Spark, HDFS, and Jupyter. 

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

**Technologies:** HDFS

**Data Organization:**
- **Storage Format:** CSV
- **Partitioning Strategy:** [How data is partitioned - by date, by key, etc.]
- **Replication Factor:** [If applicable]
- **Estimated Size:** [Current and projected]

**Schema Design:**
```
[Show your data schema/table structures]
Example:
Table: user_events
- user_id: String
- event_type: String
- timestamp: Timestamp
- properties: Map<String, String>
```

**Optimization Techniques:**
- [Technique 1]: [Description]
- [Technique 2]: [Description]

---

### 2.3 Data Processing Layer

**Purpose:** [What this layer does]

**Technologies:** Spark (PySpark)

**Processing Pipeline:**

```
Stage 1: Data Cleaning
    ↓
Stage 2: Transformation
    ↓
Stage 3: Aggregation/Analysis
    ↓
Stage 4: Results Storage
```

**Key Transformations:**
1. **[Transformation 1]:** [Description]
   - Input: [Format]
   - Output: [Format]

2. **[Transformation 2]:** [Description]

**Code Snippet:**
```python
# Core processing logic
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Example showing your key transformation
```

**Parallelization Strategy:**
- **Number of Partitions:** [e.g., 100 partitions]
- **Partition Key:** [What you partition by]
- **Shuffle Operations:** [Where they occur and why]

---

### 2.5 Visualization/Presentation Layer

**Purpose:** [How results are presented]

**Technologies:** Jupyter

**Visualization Types:**
- [Viz 1]: [e.g., Time series plot of events]
- [Viz 2]: [e.g., Heatmap of user activity]
- [Viz 3]: [e.g., Dashboard with key metrics]

**Interactive Elements:**
- [Element 1]: [Description]

---

## 3. Technology Stack Justification

| Technology | Purpose | Why Chosen | Alternatives Considered |
|------------|---------|------------|------------------------|
| Apache Spark | Data processing | High performance, in-memory computing | Hadoop MapReduce (too slow) |
| Kafka | Streaming ingestion | High throughput, fault-tolerant | AWS Kinesis (cost), RabbitMQ (scale) |
| Cassandra | NoSQL storage | Write-heavy, horizontally scalable | MongoDB (less scalable), HBase |

---

## 4. Scalability Analysis

### 4.1 Current Scale
- **Data Volume:** [Current size]
- **Processing Time:** [Time to process full dataset]
- **Cluster Configuration:** [Nodes, cores, memory]

### 4.2 Scalability Testing Plan

**Experiment 1: Vertical Scaling**
- Vary: [e.g., Executor memory: 2GB, 4GB, 8GB]
- Measure: [e.g., Processing time, throughput]
- Expected: [Your hypothesis]

**Experiment 2: Horizontal Scaling**
- Vary: [e.g., Number of workers: 2, 4, 8]
- Measure: [e.g., Speedup, efficiency]
- Expected: [Your hypothesis]

### 4.3 Projected Scale
- **Can handle:** [e.g., 100GB data, 10M records/hour]
- **Limitations:** [What would break the system?]

---

## 5. Implementation Status

### 5.1 Completed Components
- [x] Data ingestion pipeline
- [x] Basic Spark processing
- [x] Storage layer setup
- [ ] Machine learning model (in progress)
- [ ] Visualization dashboard (not started)

### 5.2 Code Repository

**Repository URL:** (if applicable)[GitHub/GitLab link]

**Directory Structure:**
```
project/
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

**Current Code Statistics:**
- Lines of Code: [Approximate]
- Number of Scripts: [Count]
- Test Coverage: [If applicable]

---

## 6. Demonstration Plan

### 6.1 Live Demo Flow (5 minutes)
1. **Show input data** (30 seconds)
2. **Run processing pipeline** (2 minutes)
3. **Display results** (1.5 minutes)
4. **Highlight scalability** (1 minute)

### 6.2 Backup Plan
[What if live demo fails? Screenshots, video recording, etc.]

---

## 6. Remaining Work (Milestone 3)

### 6.1 Critical Path Items
1. **[Task 1]:** [Description] - Assigned to: [Name]
2. **[Task 2]:** [Description] - Assigned to: [Name]
3. **[Task 3]:** [Description] - Assigned to: [Name]

### 6.2 Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Plan] |
| [Risk 2] | High/Med/Low | High/Med/Low | [Plan] |

### 6.3 Timeline for Final Week (01DEC)

**Day 1-2:** [Tasks]

**Day 3-4:** [Tasks]

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
