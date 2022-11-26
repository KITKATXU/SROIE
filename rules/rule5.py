import  csv
f1=open('output4.csv','r',encoding='utf-8')
reader1=csv.reader(f1)
w=open('output5.csv','w',encoding='utf-8',newline="")
writer = csv.writer(w)

dict_total={}
ct=0
for i in reader1:
    if len(i)<1:
        ct=ct+1
        continue
    if i[-1] not in dict_total:
        dict_total[i[-1]] = 0
    if i[-1] in dict_total and i[1]=='S-TOTAL':
        dict_total[i[-1]] = dict_total[i[-1]] + 1

# print(len(dict_total))
total_n=[]
for i in dict_total.keys():
    if dict_total[i]<1:
        # print(i,dict_total[i])
        total_n.append(i)

dict_n={}
print(len(total_n))

def IsFloatNum(str):
    s=str.split('.')
    if len(s)>2:
        return False
    else:
        for si in s:
            if not si.isdigit():
                return False
        return True
f1=open('output4.csv','r',encoding='utf-8')
reader1=csv.reader(f1)

for i in reader1:
    if len(i)<1:
        continue
    if i[-1] in total_n:
        if len(i[0])>6:
            continue
        if len(i[0])>=5 and i[0].isdigit()==True:
            continue
        if i[-1] not in dict_n:
            dict_n[i[-1]] = {}
            if i[0].isdigit() == True:
                dict_n[i[-1]][i[0]] = 1
            if '.' in i[0]:
                if IsFloatNum(i[0]) == True:
                    dict_n[i[-1]][i[0]] = 1
        else:
            if i[0] not in dict_n[i[-1]]:
                if i[0].isdigit() == True:
                    dict_n[i[-1]][i[0]] = 1
                if '.' in i[0]:
                    if IsFloatNum(i[0]) == True:
                        dict_n[i[-1]][i[0]] = 1
            if i[0] in dict_n[i[-1]]:
                if i[0].isdigit() == True:
                    dict_n[i[-1]][i[0]] = dict_n[i[-1]][i[0]] + 1
                if '.' in i[0]:
                    if IsFloatNum(i[0]) == True:
                        dict_n[i[-1]][i[0]] = dict_n[i[-1]][i[0]] + 1

print((dict_n))
dct_gross={}
for i in dict_n.keys():
    dct_gross[i]=[]
    for j in dict_n[i].keys():
        if '.' in j and IsFloatNum(j) and dict_n[i][j]>=2:
            dct_gross[i].append(float(j))
print(dct_gross)

for i in dct_gross.keys():
    if len(dct_gross[i])<1:continue
    tpmx=max(dct_gross[i])
    tpmx=str(tpmx).split('.')
    if len(tpmx[-1])<2:
        tpmx[-1]=tpmx[-1]+'0'
    tpmx='.'.join(tpmx)
    dct_gross[i]=[tpmx]
print(dct_gross)
fd=dct_gross
print(fd)
f1=open('output4.csv','r',encoding='utf-8')
reader1=csv.reader(f1)

for i in reader1:
    if len(i)<1:
        writer.writerow([])
        continue
    if i[-1] in fd.keys():
        if len(fd[i[-1]])>0:
            for j in range(len(fd[i[-1]])):
                 if i[0]==str(fd[i[-1]][j]):
                      i[1]='S-TOTAL'
                      fd[i[-1]].pop(j)
                      # print("here")
                      break
    writer.writerow(i)
