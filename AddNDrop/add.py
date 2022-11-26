

import  csv
# reader0=open('test_predictions.txt','r',encoding='utf-8').readlines()
reader=open('op_test.txt','r',encoding='utf-8').readlines()
reader0=open('test_predictions (12).txt','r',encoding='utf-8').readlines()
w=open('new_predictions_1123.csv','w',encoding='utf-8',newline="")
writer = csv.writer(w)
ct=0
saves=[]
for i in reader:
    # i = i.decode("utf-8", "ignore")
    # i=i.encode('utf-8', 'ignore').decode("utf-8")
    i=i.strip('\n')
    i=i.split('\t')
    # print(i)
    if len(i)<3:
        # writer.write('\n')
        writer.writerow([])
        ct=ct+1
        # ct=ct+2
        continue
    reader0[ct]=reader0[ct].strip('\n')
    reader0[ct]=reader0[ct].split()
    print(i,reader0[ct])
    if reader0[ct][1] not in ['O','S-COMPANY','S-ADDRESS',\
                              'S-DATE','S-TOTAL']:
        print("here",reader0[ct])
        break
    print(reader0[ct])
    print(reader0[ct][1])
    # break
    if reader0[ct][0] in i[0] or i[0] in reader0[ct][0]:
        i[1]=reader0[ct][1]
        ct=ct+1
    else:
        print("here2",reader0[ct],i)
        break


    writer.writerow(i)
    # if len(reader0[ct+1])>1:
    #     ct=ct+1


# writer.close()

