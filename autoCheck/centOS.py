import subprocess
import os
import datetime

dt = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
file_name = './autostart.log'
chkProcess = os.popen("docker ps |grep water_group_service |grep -v 'grep' |wc -l").read()
chkProcessArray = chkProcess.split("\n")
chkProcessInfo = [ x for x in chkProcessArray if x != '']
chkStatus = os.popen("docker inspect --format '{{.State.Running}}' water_group_service").read()
chkStatusArray = chkStatus.split("\n")
chkStatusInfo = [ i for i in chkStatusArray if i != '']
chkPing = os.popen("ping 10.11.0.20 -c 4 -w 3 |grep 'packet loss' |grep -v 'grep' |awk -F ',' '{print $3}' |awk -F '%' '{print $1}'").read()
chkPingArray = chkPing.split("\n")
chkPingInfo = [ n for n in chkPingArray if n != '']
chkTelnet = os.popen("(sleep 1;) |telnet 10.11.0.20 8899 > ./telnet_result.txt").read()
chkTelnets = os.popen("cat /home/autoCheck/telnet_result.txt |grep -B 1 \] |grep [0-9] |awk -F ' ' '{print $1}'").read()
chkTelnetsArray = chkTelnets.split("\n")
chkTelnetsInfo = [ m for m in chkTelnetsArray if m != '']
f = open(file_name, mode='a', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
if len(chkProcessInfo) >= 1 and len(chkStatusInfo) >= 1:
    if chkProcessInfo[0] == '0' or chkStatusInfo[0] == 'false':
        f.write(dt+"系统检测到 water_group_service 服务异常 \n")
    else:
        f.write(dt+"系统检测到 water_group_service 正在运行中 \n")
else:
    f.write(dt+"Error: No such object: water_group_service")

if chkPingInfo[0].lstrip() != '100' or chkTelnetsInfo[0].lstrip() == 'connected':
    f.write(dt+"系统检测到 Ping 10.11.0.20 or Telnet 10.11.0.20 8899 服务正常")
else:
    f.write(dt+"系统检测到 Ping 10.11.0.20 or Telnet 10.11.0.20 8899 服务异常")
