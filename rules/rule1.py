import  csv
f1=open('output.csv','r',encoding='utf-8')
reader1=csv.reader(f1)
w=open('output1.csv','w',encoding='utf-8',newline="")
writer = csv.writer(w)

# dict_files={}
# dict_len={}
# ct=0
# for i in reader1:
#     if len(i)<1:
#         ct=ct+1
#         continue
#     if i[-1] not in dict_files:
#         dict_files[i[-1]]=[]
#         dict_files[i[-1]].append(ct)
#         dict_len[i[-1]]=1
#     else:
#         dict_len[i[-1]]=dict_len[i[-1]]+1
#         dict_files[i[-1]]=dict_files[i[-1]][:1]
#         dict_files[i[-1]].append(ct)
#     ct=ct+1
# print(dict_files)

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

total_r=[]
for i in dict_total.keys():
    if len(dict_total[i])>1:
        if len(dict_total[i])==2 and dict_total[i][1]-dict_total[i][0]==1:
            continue
        total_r.append(dict_total[i])

print(total_r)

f1=open('output.csv','r',encoding='utf-8')
reader1=csv.reader(f1)
ct=0
r=0
pre=""
for i in reader1:
    if len(i)<1:
        ct=ct+1
        writer.writerow([])
        continue
    if ct == total_r[r][0]:
        pre=i[0]
    # if ct == total_r[r][0]
    if ct in total_r[r][1:] and i[0]==pre:
        i[1]='O'
    if ct>total_r[r][-1]:
        if r<len(total_r)-1:
            r=r+1
        pre==""
    # print(i)
    writer.writerow(i)
    ct=ct+1
# print(dict_total)
