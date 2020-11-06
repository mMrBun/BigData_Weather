from pyhive import hive
import re


stand_id = []
stand_temp = []
cursor = hive.connect(host="0.0.0.0", database="weatherData").cursor()
cursor.execute("select cityid,temp from detail")
test=cursor.fetchall()
for data in test:
    data=list(data)[0]
    stand_id.append(data)
for item in test:
    item=list(item)[1]
    stand_temp.append(item)
target_data=zip(stand_id,stand_temp)
final=dict(target_data)
print(final)


