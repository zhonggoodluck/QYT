import re
str1 = '166    54a2.74f7.0326    DYNAMIC    Gi1/0/11'
result = re.match(r'(\d{1,4})\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(\w+)\s+(\w\S+\d)',str1.strip()).groups()
print(result)
print('%-10s : %s' % ('VLAN ID', result[0]))
print('%-10s : %s' % ('MAC', result[1]))
print('%-10s : %s' % ('Type', result[2]))
print('%-10s : %s' % ('Interface', result[3]))