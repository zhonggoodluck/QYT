import os
import re

ifconfig_result = os.popen('ifconfig ' + 'ens33').read()
print(ifconfig_result)

#正则表达式查找IP，掩码，广播和mac地址
ipv4_address = re.findall(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
netmask = re.findall(r'netmask (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
broadcast = re.findall(r'broadcast (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
mac_address = re.findall(r'ether ([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})',
                         ifconfig_result)[0]

#格式化字符串
format_string = '{0:15}{1}{2}'

#打印结果
print(format_string.format('ipv4_address',': ',ipv4_address))
print(format_string.format('netmask',': ',netmask))
print(format_string.format('broadcast',': ',broadcast))
print(format_string.format('mac_address',': ',mac_address))

#产生网关的IP地址
ipv4_list = ipv4_address.split('.')
ipv4_list[3]='1'
gateway = '.'.join(ipv4_list)

#打印网关的IP地址
print('\n我们假设网关地址为最后一位为1，因此网关IP地址为：' + gateway +'\n')

#ping网关
ping_result = os.popen('ping ' + gateway + ' -c 5').read()


re_ping = re.findall(r'5 received',ping_result)

if re_ping:
    print('网关可达！')
else:
    print('网关不可达！')


