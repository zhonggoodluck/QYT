department1 = 'zhonggoodluck'
department2 = 'python'
depart1_m = 'Zhong'
depart2_m = 'lucky'
COUSE_FEES_zh = 525529.212313
COUSE_FEES_lucky = 79306.23212


line1 = "department1 name:%-16sManger:%-10sCOUSE_FEES  %-12.2fthe end!" % (department1,depart1_m,COUSE_FEES_zh)
line2 = "department2 name:%-16sManger:%-10sCOUSE_FEES  %-12.2fthe end!" % (department2,depart2_m,COUSE_FEES_lucky)
length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)


line1 = 'department1 name:{0:16}Manger:{1:10}COUSE_FEES  {2:<12.2f}the end!'.format(department1,depart1_m,COUSE_FEES_zh)
line2 = 'department2 name:{0:16}Manger:{1:10}COUSE_FEES  {2:<12.2f}the end!'.format(department2,depart2_m,COUSE_FEES_lucky)
length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)


line1 = f'department1 name:{department1:16}Manger:{depart1_m:10}COUSE_FEES  {COUSE_FEES_zh:<12.2f}the end!'
line2 = f'department2 name:{department2:16}Manger:{depart2_m:10}COUSE_FEES  {COUSE_FEES_lucky:<12.2f}the end!'

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)
