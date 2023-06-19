print("Testing Github commit")

dates, max_temp, min_temp, avg_temp, conditions =  ([] for i in range(5))
print(dates)

js = {'source': 'msx', 'entity': 'dbo_mssales', 'version': 'v1'}
print(type(js))
string = ""
for k,v in js.items():
    string += '"' + k + '" = ' + "'" + v + "'" + "\n"

print(string)


filename = "Unknown Facts @ green  shorts   YT shorts.mp4"
names = filename.split(" ")
lst = [name for name in names if name.isalpha()]
title = '_'.join(lst)
print(names)
print(lst)
print(title)