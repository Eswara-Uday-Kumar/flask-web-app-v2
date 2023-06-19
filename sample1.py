
import time

js = {
    'id' : 'lafnskjnksjd',
    'activities': [
        {
            'activityid': 'kshfusf',
            'activityname': 'taxonomy governor',
            'activitystatus': 'succeeded'
        },
        {
            'activityid': 'kjasdfhishfncv',
            'activityname': 'Access Orchestration',
            'activitystatus': 'succeeded'
        }
    ] 
}


"""
for k,v in js.items():
    if k == 'activities':
        print(k,v)
"""
resultset = {k:v for k,v in js.items() if k=='activities'}

print(resultset)
act_len = len(resultset['activities'])

for i in range(act_len):
    if resultset['activities'][i]['activityname'] == 'taxonomy governor':
        print(resultset['activities'][i]['activitystatus'])
        js['activities'][i]['activitystatus'] = 'queued'
    time.sleep(2)
    if resultset['activities'][i]['activityname'] == 'Access Orchestration':
        print(resultset['activities'][i]['activitystatus'])
        js['activities'][i]['activitystatus'] = 'queued'


print(js)

acti_len = len(js['activities'])
#print(acti_len)
for i in range(acti_len):
    if js['activities'][i]['activityname'] == 'taxonomy governor':
        print(js['activities'][i]['activityname'])
        print(js['activities'][i]['activitystatus'])
        js['activities'][i]['activitystatus'] = 'queued'
    time.sleep(5)
    if js['activities'][i]['activityname'] == 'Access Orchestration':
        print(js['activities'][i]['activityname'])
        print(js['activities'][i]['activitystatus'])
        js['activities'][i]['activitystatus'] = 'queued'