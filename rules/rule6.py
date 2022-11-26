import  csv
f1=open('output5.csv','r',encoding='utf-8')
reader1=csv.reader(f1)
w=open('output6.csv','w',encoding='utf-8',newline="")
writer = csv.writer(w)


dict_total={}
ct=0
for i in reader1:
    if len(i)<1:
        ct=ct+1
        continue
    if i[-1] not in dict_total:
        dict_total[i[-1]] = 0
    if i[-1] in dict_total and i[1]=='S-DATE':
        dict_total[i[-1]] = dict_total[i[-1]] + 1

# print(dict_total)
total_n=[]
for i in dict_total.keys():
    if dict_total[i]<1:
        print(i,dict_total[i])
        total_n.append(i)

dict_n={}
print(len(total_n))

def IsFloatNum(str):
    s=str.split('/')
    for si in s:
        if not si.isdigit():
            return False
    return True

def IsFloatNum2(str):
    s=str.split('-')
    for si in s:
        if not si.isdigit():
            return False
        if int(si)>2200:
            return False
    return True


Date_dct={}

f1=open('output5.csv','r',encoding='utf-8')
reader1=csv.reader(f1)
for i in reader1:
    if len(i) < 1:
        continue
    if i[-1] in total_n:
        if i[-1] not in Date_dct:
            Date_dct[i[-1]] = []
        else:
            if '2018' == i[0]:
                Date_dct[i[-1]].append(i[0])
            if i[0] in ['Mar','May','Jun','Jul']:
                Date_dct[i[-1]].append(i[0])
            if '-18' in i[0]:
                Date_dct[i[-1]].append(i[0])
            if '/' in i[0] and IsFloatNum(i[0]):
                Date_dct[i[-1]].append(i[0])
            if '-' in i[0] and IsFloatNum2(i[0]):
                Date_dct[i[-1]].append(i[0])


print(Date_dct)

fd=Date_dct
f1=open('output5.csv','r',encoding='utf-8')
reader1=csv.reader(f1)

for i in reader1:
    if len(i)<1:
        writer.writerow([])
        continue
    if i[-1] in fd.keys():
        if len(fd[i[-1]])>0:
            for j in range(len(fd[i[-1]])):
                 if i[0]==str(fd[i[-1]][j]):
                      i[1]='S-DATE'
                      fd[i[-1]].pop(j)
                      # print("here")
                      break
    writer.writerow(i)