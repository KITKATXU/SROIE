

import  csv
# reader0=open('test_predictions.txt','r',encoding='utf-8').readlines()
reader=open('op_test.txt','r',encoding='utf-8').readlines()
writer=open('test.txt','w',encoding='utf-8')

ct=0
for i in reader:
    # i = i.decode("utf-8", "ignore")
    # i=i.encode('gbk', 'ignore').decode("gbk")
    i=i.strip('\n')
    i=i.split('\t')
    # print(i)
    if len(i)<2:
        writer.write('\n')
        # ct=ct+1
        continue

    if len(i)==2:
        print("here")
        i=':'+'\t'+i[0]
        break
    else:
        # print("here")
        # break
        tp=0
        while i[tp+1]!='O':
            tp=tp+1
        if tp>0:
            i = " ".join(i[:tp + 1])
            i=i+"\t"+'O'
        else:
            i = "\t".join(i[:tp+2])
    writer.write(i+"\n")


writer.close()