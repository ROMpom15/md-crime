#!/bin/bash
# generated with gemini
# https://stackoverflow.com/questions/21732524/how-to-know-what-script-header-to-use-and-why-it-matters
# Create environment with ONLY Java
# mamba create -n hdfs_env openjdk=17 -c conda-forge -y
# mamba install fastparquet
mamba activate hdfs_env

# generate key
# ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
# cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
# chmod 0600 ~/.ssh/authorized_keys

# test: ssh localhost
# 1. Set Hadoop Home to the folder we just unzipped
export HADOOP_HOME=~/hadoop

# 2. Point Hadoop to the Mamba Java environment
# (This command dynamically finds the java path inside your active conda env)
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))

# 3. Add Hadoop to your path so you can type 'hdfs' instead of full paths
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# 4. Configure Hadoop's internal config folder location
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME

