#!/bin/bash
# generated with gemini
# https://stackoverflow.com/questions/21732524/how-to-know-what-script-header-to-use-and-why-it-matters
# Create environment with ONLY Java
mamba create -n hdfs_env openjdk=11 -c conda-forge -y
mamba activate hdfs_env

# generate key
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys

# test: ssh localhost