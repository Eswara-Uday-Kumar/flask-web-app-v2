import datetime

WindowStart = "20190701_000000"
WindowEnd = "20191001_000000"
#fullyqualifiedname = "usp_gdcprogress(@fromDate datetime)"
fullyqualifiedname = "usp_gdcprogress(@fromDate datetime,@toDate datetime)"
#fullyqualifiedname = "usp_gdcprogress"
loadtype = "delta"

print(loadtype)
index1 = fullyqualifiedname.find("(")
index2 = fullyqualifiedname.find(" ")
index3 = fullyqualifiedname.find(",")

QStart = datetime.datetime.strptime(WindowStart.replace('_', ''), '%Y%m%d%H%M%S')
QStart = datetime.datetime.strftime(QStart, '%Y-%m-%d %H:%M:%S.%f')
QStart = QStart[:-3]

subQuery = ""
query = ""

if loadtype.lower() == "delta":
    subQuery += fullyqualifiedname[index1+1:index2] + " = '" + QStart + "',"

else:
    QStart = "1900-01-01 00:00:00:000"
    subQuery += fullyqualifiedname[index1+1:index2] + " = '" + QStart + "',"

if loadtype.lower() == "delta" and "," in fullyqualifiedname:
    QEnd = datetime.datetime.strptime(WindowEnd.replace('_', ''), '%Y%m%d%H%M%S')
    QEnd = datetime.datetime.strftime(QEnd, '%Y-%m-%d %H:%M:%S.%f')
    QEnd = QEnd[:-3]
    subQuery += fullyqualifiedname[index3+1:index3+8] + " = '" + QEnd + "'"

query = fullyqualifiedname[4:index1] + " " + subQuery

print(query)