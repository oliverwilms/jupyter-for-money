# jupyter-for-money

Lately I reviewed many apps dealing with AI and I came across workshop-llm. I got inspired so that I wanted to create a Jupyter Notebook for analyzing personal financial data. I saw that I needed a CSV input file. My data is in Excel workbook with many sheets. I am not aware of any tool to export multiple sheets into a CSV file.

## excel-java-iris

excel-java-iris contains a java routine to read data from Excel 95, 97, 2000, XP, and 2003 workbooks and write the data into IRIS globals using Java Native API library.
Executing IRISNative.java imports data from an xls file with multiple sheets into a single IRIS global (^excel).
There is a class method to transform data from ^excel into a persistent class.
New otw.iris.excel class imports data from ^excel global into dc.iris.transact table.
I added code to export to CSV

## From workshop-llm to jupyter-for-money

I modeled the GitHub repo after workshop-llm.

I added zpm "install excel-java-iris" to iris.script.

This provided a sample excel data file:
/usr/irissys/mgr/excel/money.xls

I updated the module.xml in excel-java-iris to also copy java files.
I also added a dependency so that code from iris-globals-contest is included.

## iris-globals-contest

iris-globals-contest provides persistent class

Class dc.iris.transact Extends %Persistent [ StorageStrategy = NewStorage1 ]

<Global>^GLOBAL</Global>

I updated the iris Dockerfile in jupyter-for-money to copy java.sh script which builds (compiles) java code and executes it.
I realized that I also needed jar in lib folder.

## Prerequisites
Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker desktop](https://www.docker.com/products/docker-desktop) installed.

## Installation: Docker
Clone/git pull the repo into any local directory

```
$ git clone https://github.com/oliverwilms/jupyter-for-money.git
```

Open the terminal in this directory and run:

```
$ docker-compose up -d
```

## Stage the data
A sample file is included.
```
$ docker exec -it iris bash
irisowner@184619d1c385:/opt/irisapp$ cd /usr/irissys/mgr/excel/
irisowner@184619d1c385:/usr/irissys/mgr/excel$ ls -ltr
total 28
-rwxr-xr-x. 1 irisowner irisowner 26112 May  4 15:52 money.xls
```
## Execute java

java.sh script executes IRISNative java code with parameter "/usr/irissys/mgr/excel/money.xls" as the excel input file.
```
irisowner@12f8c54b639f:/opt/irisapp$ ./java.sh
Building...
Executing...
```
IRISNative.java populates ^excel in USER namespace. 

![screenshot](https://github.com/oliverwilms/bilder/blob/main/Money_xls.PNG)

## IRIS session

```
$ docker-compose exec -it iris iris session iris
```

## See data from Excel workbook in IRIS global

```
USER>zw ^excel
^excel(0,0,0)="Date"
^excel(0,0,1)="Check"
^excel(0,0,2)="Merchant"
^excel(0,0,3)="Category"
^excel(0,0,4)="SubCategory"
^excel(0,0,5)="Memo"
^excel(0,0,6)="Credit"
^excel(0,0,7)="Debit"
^excel(0,0,8)="Account"
^excel(0,0,9)="Status"
^excel(0,1,0)="27-Nov"
^excel(0,1,1)=101
^excel(0,1,2)="Landlord"
^excel(0,1,3)="Business Expense"
^excel(0,1,4)="Rent"
^excel(0,1,5)="December"
^excel(0,1,7)=250
^excel(0,1,8)="Checking"
^excel(0,2,0)="27-Nov"
^excel(0,2,2)="Aldi"
^excel(0,2,3)="Groceries"
^excel(0,2,5)=16
^excel(0,2,7)=54.35
^excel(0,2,8)="Checking"
```

## Import Excel data from IRIS global into IRIS persistent class

Since I started this project with files copied from workshop-llm, zpm installed excel-java-iris into LLMRAG namespace.

I added a global mapping in Installer class so that I can use the same ^excel global in USER.

```
LLMRAG>w ##class(otw.iris.excel).importExcel(-1)
1
```

I added -1 above because I want to start importing with sheet 0. In my personal Excel workbook, I want to skip the first five workbooks.

## See data from Excel workbook in IRIS SQL table

![screenshot](https://github.com/oliverwilms/bilder/blob/main/Capture_SQL.JPG)

Select * from dc_iris.transact

## CSV file

If you do not provide a file parameter, the following command will produce /opt/irisapp/dc_iris-transact.csv.
```
w ##class(otw.excel.iris).exportToCSV(file)
```

