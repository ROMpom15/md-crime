# Project Proposal Template
## Big Data Computing - Group Project

**Team Number:** Team 7  
**Team Name:** Crime Finders  
**Date:** [Submission Date]

---

## Team Members

| Name | Email | Role | Primary Responsibilities |
|------|-------|------|-------------------------|
| [Conrad Jones] | [m263183@usna.edu] | Project Lead & ML/Analytics Engineer | Coordination, integration, final testing, algorithms, analysis, modeling |
| [Davorah Strober] | [m266156@usna.edu] | Data Engineer | Data pipeline, preprocessing, storage |
| [Anna Gotterup] | [m262418@usna.edu] | Documentation Lead & Analytics Engineer Assistant | Reports, documentation, visualization |

---

## 1. Problem Statement & Motivation

**What problem are you solving?**
[2-3 sentences describing the real-world problem or analytical question]

Our team is looking at college campus crime data to investigate how COVID impacted crime rates across campuses. We are also looking to investigate which campuses were affected the most by crime between 2018 - 2023. 

**Why is this problem important?**
[2-3 sentences explaining the significance and potential impact]

This problem is important because crime prevention on college campuses is an ongoing discussion. Our group wants to understand the risk factors and analyze trends to investigate how a pandemic affects crime rates and implement changes to increase safety. 

**Why does it require big data technologies?**
[Explain the scale, velocity, or complexity that necessitates distributed computing]

Our team is using big data technologies (at a 100s of MB scale) in order to develop a pipeline suitable for scaling to GB or TB dimensions. We seek to design a product that could scale to nation wide query scale to identify larger trends in campus crime. Our project requires big data tools to address volume concerns.

---

## 2. Dataset Description

**Dataset Name:** [U.S. Department of Education Campus Safety & Security]

**Source:** [(https://ope.ed.gov/campussafety/#/datafile/list)]

**Size & Format:**
- Volume: 130MB raw, 30 files averaging 5 MB each
- Format: Excel (transforming to csv)
- Time Period: 2018 - 2023

**Key Features:**
- [Feature 1]: [Institution/Location --> need to know where the school is located and the type of school (private, public, etc.)]
- [Feature 2]: [Crime Statistics --> # of reported incidents and their descriptions (Aggravated Assault, Sexual Assault, etc.)]
- [Feature 3]: [Address --> particular addresses may be more vulnerable than others]

**Data Acquisition Plan:**
- [X] Dataset already downloaded/accessible
- [X] Will download during Week 1
- [X] Will use Department of Ed data 

**Sample Data:** [Include 3-5 example records or describe structure]

UNITID_P	INSTNM	OPEID	BRANCH	Address	City	State	ZIP	sector_cd	Sector_desc	men_total	women_total	Total	MURD21	NEG_M21	RAPE21	FONDL21	INCES21	STATR21	ROBBE21	AGG_A21	BURGLA21	VEHIC21	ARSON21	MURD22	NEG_M22	RAPE22	FONDL22	INCES22	STATR22	ROBBE22	AGG_A22	BURGLA22	VEHIC22	ARSON22	MURD23	NEG_M23	RAPE23	FONDL23	INCES23	STATR23	ROBBE23	AGG_A23	BURGLA23	VEHIC23	ARSON23	FILTER21	FILTER22	FILTER23
100654001	Alabama A & M University	00100200	Main Campus	4900 MERIDIAN ST	NORMAL	AL	35762	1	Public, 4-year or above	2671	3943	6614	0	0	2	1	0	0	1	0	8	0	0	0	0	3	2	0	0	0	0	14	0	0	0	0	6	1	0	0	0	1	25	0	0	1	1	1
100663001	University of Alabama at Birmingham	00105200	Main Campus	ADMINISTRATION BLDG SUITE 1070, 701 20th Street So	BIRMINGHAM	AL	352940110	1	Public, 4-year or above	7803	13357	21160	0	0	6	18	0	0	1	5	21	7	0	0	0	4	18	0	0	0	9	15	21	2	0	0	8	25	0	0	0	9	14	26	0	1	1	1
100663002	University of Alabama at Birmingham	00105200	Huntsville Regional Medical Campus	301 Governors Drive SW	Huntsville	AL	35801	1	Public, 4-year or above	7803	13357	21160	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1
100706001	University of Alabama in Huntsville	00105500	Main Campus	301 SPARKMAN DR	HUNTSVILLE	AL	35899	1	Public, 4-year or above	5178	3565	8743	0	0	0	1	0	0	0	0	1	1	0	0	0	2	1	0	0	0	0	3	2	0	0	0	6	3	0	0	0	0	6	2	0	1	1	1

---

## 3. Proposed Technical Architecture

### Core Technologies:
- **Processing Framework:** [Apache Spark (PySpark)]
- **Storage Layer:** [HDFS]
- **Streaming (if applicable):** [e.g., Kafka, Spark Streaming]
- **Machine Learning:** [e.g., Spark MLlib, custom algorithms]
- **Deployment:** [e.g., AWS EMR, local cluster, Google Colab]

- Spark MLlib for predictive crime patterns model (cluster or classified)
- Spark and HDFS
- ML classification (need to get archtecture first), not necessary just an addition

- get data into HDFS
- use Spark to clean and concat data
- visual of crime over time

### High-Level Architecture:
```
[Draw or describe the data flow]
Raw Data → HDFS → Spark

```

### Scalability Approach:
[How will you demonstrate distributed processing? What scaling experiments will you run?]

In order to demonstrate distributed processing our group will start with a small fraction of data and then scale upward by year, consistently adding more data. We are going to experiment scaling by testing the time each dataset takes to run. Our plan is to perform distributed processing using HDFS. 

---

## 4. Expected Outcomes & Success Metrics

### Primary Deliverables:
1. [Crime Analysis Dashboard]

### Success Metrics:
- **Functional Requirements:** [What must the system do?]
  - [Metric 1: Display metrics of various campus crimes]

- **Performance Requirements:** [How fast must it be?]
  - [Metric 1: End-to-end latency < 20 seconds]

- **Quality Requirements:** [How accurate/reliable?]
  - [Metric 1: Dropped nulls/total data]

- 90% goal

### Evaluation Plan:
[How will you measure and demonstrate these metrics?]

In order to measure and demonstrate our metrics we are going to time each run and compare the runtimes. We are also going to create visualizations that are time-based, geography-based, and a pie chart. 

---

## 5. Anticipated Challenges & Mitigation Strategies

| Challenge | Risk Level | Mitigation Strategy |
|-----------|-----------|---------------------|
| [Lots of different excel files] | Medium | Use sample first, try and combine them |
| [Team coordination] | Low | Routine check-ins through google chat, shared GitHub repo |
| [Null Values] | Medium | Dropping null values |

---

## 6. Work Plan

### Milestone 1:
- [X] Dataset acquisition and exploration
- [X] Environment setup (local/cloud)
- [X] Initial data preprocessing scripts
- [X] GitHub repository creation

### Milestone 2:
- [ ] Core pipeline implementation
- [ ] Basic processing/analysis working
- [ ] Architecture documentation
- [ ] Prepare mid-sprint presentation

### Milestone 3:
- [ ] Performance optimization and scaling tests
- [ ] Final implementation and testing
- [ ] Documentation and report writing
- [ ] Presentation preparation

---

## 7. Innovation & Learning Goals

**What makes this project interesting/unique?**
[What new techniques or approaches will you explore?]

This project is unique because we are using college campus crime data to analyze the effects of COVID on crime rates.

**What do you hope to learn?**
[What skills or technologies do you want to master through this project?]

Through this project, we want to master working with parquet files and working with lots of data in HDFS. 


**Next Steps (what a group after you could add to this):**
- [enhancement 1]
- [enhancement 2]

---

## 8. References & Prior Work

**Similar Projects/Papers:**
1. [Reference 1]
2. [Reference 2]

**Technologies/Libraries to Explore:**
1. [Tool/Library 1]
2. [Tool/Library 2]

---

## Approval Section (For Instructor Use)

**Instructor Feedback:**

[ ] Approved as proposed  
[ ] Approved with modifications (see comments)  
[ ] Needs revision and resubmission

**Comments:**


**Instructor Signature:** _________________ **Date:** _________

---