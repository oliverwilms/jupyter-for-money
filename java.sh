#!/bin/bash

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
export JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
export CLASSPATH=.:/usr/irissys/dev/java/lib/1.8/*

echo "Building..."
cd /opt/irisapp
javac -classpath $CLASSPATH -d . /usr/irissys/mgr/java/IRISNative.java
echo "Executing..."
java IRISNative /usr/irissys/mgr/excel/money.xls
