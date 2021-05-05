import csv
import random
list=random.sample(range(1, 1200), 100)

list1=[0 for i in range(100)]
scen="scen"
for i in range(100):
    list1[i]=scen+str(list[i])
print(list1)


with open('solar_scenarios_1200.csv', newline='') as  inp, open('solar_scenarios_100_1.csv','w', newline='') as out:
    writer = csv.writer(out, delimiter = ',')
    #writer = csv.writer(out)
    reader = csv.reader(inp)
    i=1
    for row in reader:
        #print(row[0])
        if row[1]=='t1':
            writer.writerow(row)
        if row[0] in list1:
            row[0]=scen+str(i)
            writer.writerow(row)
            i=i+1


#Für nächstes Sample den Dateinamen ändern (add a number at the end)
#with open('solar_scenarios_1200.csv', newline='') as  inp, open('solar_scenarios_100_20.csv','w', newline='') as out:
#    writer = csv.writer(out, delimiter = ',')
    #writer = csv.writer(out)
#    reader = csv.reader(inp)
#    for row in reader:
        #print(row[0])
#        if row[0] in list1:
#            writer.writerow(row)

