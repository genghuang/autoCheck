#!/bin/bash
LOG_FILE="/home/autostart.log"
#检测water_group_service
curtime=$(date "+%Y-%m-%d %H:%M:%S")
chkwaterService=`docker ps | grep water_group_service | grep -v "grep" | wc -l`
if [ $chkwaterService -eq 0 ]; then
        echo "$curtime 系统检测到water_group_service,已挂掉,启动中...." >> autostart.log;
else
        echo "$curtime 系统检测到water_group_service运行正常" >> autostart.log;
fi

#检测socket
chkSocket=`docker ps | grep socket | grep -v "grep" | wc -l`
if [ $chkSocket -eq 0 ]; then
        echo "$curtime 系统检测到socket,已挂掉,启动中...." >> autostart.log;
else
        echo "$curtime 系统检测到socket运行正常" >> autostart.log;
fi
