import  csv
f1=open('output2.csv','r',encoding='utf-8')
reader1=csv.reader(f1)
w=open('output3.csv','w',encoding='utf-8',newline="")
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
f1=open('output2.csv','r',encoding='utf-8')
reader1=csv.reader(f1)
dict_n={}
print(len(total_n))
#
# # 输入参数 str 需要判断的字符串
# # 返回值   True：该字符串为浮点数；False：该字符串不是浮点数。
def IsFloatNum(str):
    s=str.split('.')
    if len(s)>2:
        return False
    else:
        for si in s:
            if not si.isdigit():
                return False
        return True
#
#
# for i in reader1:
#     if len(i)<1:
#         continue
#     if i[-1] in total_n:
#         if len(i[0])>6:
#             continue
#         if len(i[0])>=5 and i[0].isdigit()==True:
#             continue
#         if i[-1] not in dict_n:
#             dict_n[i[-1]] = {}
#             if i[0].isdigit() == True:
#                 dict_n[i[-1]][i[0]] = 1
#             if '.' in i[0]:
#                 if IsFloatNum(i[0]) == True:
#                     dict_n[i[-1]][i[0]] = 1
#         else:
#             if i[0] not in dict_n[i[-1]]:
#                 if i[0].isdigit() == True:
#                     dict_n[i[-1]][i[0]] = 1
#                 if '.' in i[0]:
#                     if IsFloatNum(i[0]) == True:
#                         dict_n[i[-1]][i[0]] = 1
#             if i[0] in dict_n[i[-1]]:
#                 if i[0].isdigit() == True:
#                     dict_n[i[-1]][i[0]] = dict_n[i[-1]][i[0]] + 1
#                 if '.' in i[0]:
#                     if IsFloatNum(i[0]) == True:
#                         dict_n[i[-1]][i[0]] = dict_n[i[-1]][i[0]] + 1
#
# print((dict_n))
# # for i in dict_n.keys():
#
#

# for i in total_n:
ct=0
cash_dict={}
fd={}
prepre=""
pre=""
for i in reader1:
    if len(i)<1:
        continue

    if i[-1] in total_n:
        if i[-1] not in cash_dict:
            cash_dict[i[-1]]=0
            fd[i[-1]]=[]
        else:
            if i[0]=='CASH':
                if len(prepre)<=6 and (prepre.isdigit()==True or IsFloatNum(prepre)==True):
                    fd[i[-1]].append(prepre)
                if len(pre)<=6 and (pre.isdigit()==True or IsFloatNum(pre)==True):
                    fd[i[-1]].append(pre)
                cash_dict[i[-1]]=cash_dict[i[-1]] + 1
    pre=prepre
    prepre=i[0]

print(cash_dict)
print(fd)


f1=open('output2.csv','r',encoding='utf-8')
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




