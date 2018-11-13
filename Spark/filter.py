import csv
import itertools
from pyspark import SparkContext, SparkConf
from time import sleep

f = open('criteria.csv', 'r')
rdr = csv.reader(f)

inputs = ["moderate", "humid", "no", "no", "sunny", "windy", "mask", "dusty"]
check_criteria = [0, 0, 0, 0, 0, 0, 0, 0]

for line in rdr:
    for i in range(0, 24, 3):
        if inputs[i//3] == line[i]:
            check_criteria[i//3] = (line[i+1], line[i+2])

print(check_criteria)
sc = SparkContext("local", "text")
weather_RDD0 = sc.textFile("/user/cloudera/weather/part-m-*")

#temperature
weather_RDD1 = weather_RDD0.filter(lambda x: float(x.split(",")[1]) >= float(check_criteria[0][0]) 
and float(x.split(",")[1]) < float(check_criteria[0][1]))

#humidity
weather_RDD2 = weather_RDD1.filter(lambda x: float(x.split(",")[6]) >= float(check_criteria[1][0]) 
and float(x.split(",")[6]) < float(check_criteria[1][1]))

#snow
weather_RDD3 = weather_RDD2.filter(lambda x: float(x.split(",")[3]) >= float(check_criteria[2][0])
and float(x.split(",")[3]) < float(check_criteria[2][1]))

if inputs[2] == "no":
	#rain
	weather_RDD3 = weather_RDD3.filter(lambda x: float(x.split(",")[2]) >= float(check_criteria[3][0])
	and float(x.split(",")[2]) < float(check_criteria[3][1]))
else:
	pass

#cloud
weather_RDD5 = weather_RDD3.filter(lambda x: float(x.split(",")[7]) >= float(check_criteria[4][0])
and float(x.split(",")[7]) < float(check_criteria[4][1]))

#wind
weather_RDD6 = weather_RDD5.filter(lambda x: x.split(",")[4] >= float(check_criteria[5][0])
and float(x.split(",")[4]) < float(check_criteria[5][1]))

#finedust
weather_RDD7 = weather_RDD6.filter(lambda x: x.split(",")[9] >= float(check_criteria[6][0])
and float(x.split(",")[9]) < float(check_criteria[6][1]))\

#dust
weather_RDD8 = weather_RDD7.filter(lambda x: float(x.split(",")[8]) >= float(check_criteria[7][0])
and float(x.split(",")[8]) < float(check_criteria[7][1]))

#for a in weather_RDD8.take(weather_RDD8.count()):
#	print a
#sleep(5)

date_RDD0 = weather_RDD8.map(lambda x : x.split(",")[0])

date = []
for a in date_RDD0.take(date_RDD0.count()):
    date.append(str(a))

food_RDD0 = sc.textFile("/user/cloudera/food/part-m-*")
food_RDD1 = food_RDD0.filter(lambda x : str(x.split(",")[3]) in date)

food_category = {}
for a in food_RDD1.take(food_RDD1.count()):
    a = a.encode('utf-8')
    if str(a.split(",")[4]) in list(food_category.keys()):
        food_category[str(a.split(",")[4])] += 1
    else:
        food_category[str(a.split(",")[4])] = 1
food_category2 = sorted(food_category, key=lambda k : food_category[k], reverse=True)[0:3]

food_RDD1 = food_RDD0.filter(lambda x:str(x.encode('utf-8').split(",")[4]) in food_category2)
f2 = open('result.txt', 'w')
for a in food_RDD1.take(food_RDD1.count()):
    f2.write(str(a.encode('utf-8'))+"\n")

f.close()
f2.close()
