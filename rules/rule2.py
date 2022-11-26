import  csv
f1=open('output1.csv','r',encoding='utf-8')
reader1=csv.reader(f1)
w=open('output2.csv','w',encoding='utf-8',newline="")
writer = csv.writer(w)

dict_total={}
ct=0
for i in reader1:
    if len(i)<1:
        ct=ct+1
        continue
    if i[1]=='S-TOTAL':
        if i[-1] not in dict_total:
            dict_total[i[-1]] = []
            dict_total[i[-1]].append(ct)

        else:
            dict_total[i[-1]].append(ct)
    ct=ct+1
print(dict_total)
dict_s=[]
for i in list(dict_total.values()):
    dict_s.append(i[-1])
print(dict_s)

f1=open('output1.csv','r',encoding='utf-8')
reader1=csv.reader(f1)
ct=0
r=0
pre=0
for i in reader1:
    if len(i)<1:
        writer.writerow([])
        ct=ct+1
        continue
    if pre!=0:
        if pre!=i[0]:
            if i[0].isdigit()==True:
                i[1]='S-TOTAL'
        pre=0
    if ct in dict_s:
        pre=i[0]

    ct=ct+1
    writer.writerow(i)
