# Nodes and Structure #
In order to simulate a large distributed data system, we decided to use docker to create "nodes." We based our initial layout from the fourth lab of this semester and worked from there. Gemini was used 

# Commands (Docker Specific) #
docker ps -> find nodes 
docker compose up -d -> spin up local cluster
docker run -it <container> bash

docker cp <lcl_filepath> <node>:/opt/hadoop<filename> -> copies files into hadoop folder of container
docker stop <container>
docker rm -f <container-name>



# Commands (HDFS, in Docker) #
docker exec -it <namenode> bash -> open a shell inside the name node container
hdfs dfs -mkdir -p <directory> -> mkdir
hdfs dfs -ls -> ls
hdfs dfs - copyFromLocal <file>
hdfs dfs -cp <words.txt> <words2.txt> -> cp within hdfs
hdfs dfs -copyToLocal <words2.txt>


# Steps to load data into docker HDFS system #
Gemini was used to clarify and troubleshoot. All commands were developed and typed by hand.
1. 



# Citations
https://courses.cs.usna.edu/SD411/calendar.php?type=lab&event=3
    SD411 Lab03
    Developed by Brett Gentile
https://courses.cs.usna.edu/SD411/calendar.php?type=lab&event=4
    SD411 Lab04
    Developed by Brett Gentile
Gemini 3.0 Pro