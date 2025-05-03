#!/bin/bash

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
export JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
export CLASSPATH=.:/usr/irissys/dev/java/lib/1.8/*

echo "Building..."
cd /opt/irisapp
javac -classpath $CLASSPATH -d . java/IRISNative.java
echo "Executing..."
java IRISNative /opt/irisapp/excel/money.xls
