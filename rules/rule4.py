import  csv
f1=open('output3.csv','r',encoding='utf-8')
reader1=csv.reader(f1)
w=open('output4.csv','w',encoding='utf-8',newline="")
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
ct=0
total_dict={}
fd={}
f1=open('output3.csv','r',encoding='utf-8')
reader1=csv.reader(f1)
tp=0
for i in reader1:
    if len(i)<1:
        continue

    if i[-1] in total_n:
        if i[-1] not in total_dict:
            total_dict[i[-1]]=0
            fd[i[-1]]=[]
        else:
            if i[0]=='Total':
                total_dict[i[-1]]=total_dict[i[-1]] + 1
                tp=9
            if tp==8 and (('S' in i[0]) or ('It' in i[0])):
                tp=0
            if tp > 0 and ('ash' in i[0] or 'ASH' in i[0]):
                tp = 0
                # print(i)

            if tp>0 and (i[0].isdigit()==True ) and len(i[0])<=6:
                fd[i[-1]].append(i[0])
                tp=tp-1

            if tp>0 and ('.' in i[0] ) and len(i[0])<=6:

                tpi=list(i[0])
                for tpii in range(len(tpi)):
                    if tpi[tpii]=='.':
                        tpi.pop(tpii)
                        break
                tpi="".join(tpi)
                if tpi.isdigit():
                    fd[i[-1]].append(i[0])
            if tp > 0:
                tp=tp-1





# print(total_dict)
# print(fd)

for i in fd.keys():
    if len(fd[i])>2 and len(fd[i])<5:
        fd[i]=fd[i][:2]
    if len(fd[i])>=5:
        fd[i] = [fd[i][-1]]
# print(fd)
#
f1=open('output3.csv','r',encoding='utf-8')
reader1=csv.reader(f1)

for i in reader1:
    if len(i)<1:
        writer.writerow([])
        continue
    if i[-1] in fd.keys():
        if len(fd[i[-1]])>0:
            for j in range(len(fd[i[-1]])):
                 if i[0]==fd[i[-1]][j]:
                      i[1]='S-TOTAL'
                      fd[i[-1]].pop(j)
                      break
    writer.writerow(i)

#
#
#
