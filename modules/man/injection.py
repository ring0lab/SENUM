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

import os
import commands



def main(module):
    signal = module
    rip = ''
    gate = commands.getoutput("netstat -nr | awk 'FNR == 3 { print $2}'")
    interface = commands.getoutput("netstat -nr | awk 'FNR == 3 { print $8'}")
    img = ''
    status = '0'
    if signal == 'D':
        while signal.upper() != 'EXIT':
            signal = str(raw_input("[*]senum/DLOADER> "))
    elif signal == 'P':
        while signal.upper() != 'EXIT':
            signal = str(raw_input("[*]senum/IMG> "))
            if signal.upper().split().__contains__('SHOW') == 1 and signal.upper().split().__contains__('CONFIG') == 1 and len(signal.split()) == 2:
                print '\n[*] - SENUM > Modules > Man > Injection > Image:'
                print '''
  ----------------------------------------------------------------
 |  DESCRIPTION             NAME                SETTING           |
  ----------------------------------------------------------------
  REMOTE IP ADDRESS         RHOST               %s
  LOCAL GATEWAY ADDRESS     GATEWAY             %s
  NETWORK ADAPTER           INTERFACE           %s
  IMAGINE TO INJECT         IMAGE               %s
  ''' % (rip, gate, interface, img)
            elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('RHOST') == 1 and len(signal.split()) == 2:
                pass
            elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('RHOST') == 1 and len(signal.split()) == 3:
                rip = signal.split()[2]
            elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('GATEWAY') == 1 and len(signal.split()) == 2:
                pass
            elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('GATEWAY') == 1 and len(signal.split()) == 3:
                gate = signal.split()[2]
            elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('INTERFACE') == 1 and len(signal.split()) == 2:
                pass
            elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('INTERFACE') == 1 and len(signal.split()) == 3:
                interface = signal.split()[2]
            elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('IMAGE') == 1 and len(signal.split()) == 2:
                pass
            elif signal.upper().split().__contains__('SET') == 1 and signal.upper().split().__contains__('IMAGE') == 1 and len(signal.split()) == 3:
                img = signal.split()[2]
            elif signal.upper().split().__contains__('RUN') == 1 and len(signal.split()) == 1:
                if rip == "":
                    print "[*]Can't start exploit. Check your remote host setting. "
                elif gate == "":
                    print "[*]Can't start exploit. Check your gateway setting. "
                elif interface == "":
                    print "[*]Can't start exploit. Check your interface setting."
                elif img == "":
                    print "[*]Can't start exploit. Check your image setting."
                elif status == '1':
                    x = '[*]Please stop the current exploit.'
                    i = 0
                    while i < 5:
                        print x
                        i += 1
                else:
                    status = '1'
                    os.system('mkdir -p /tmp/SENUM/IMAGE'), os.system('cp /etc/etter.conf /tmp/SENUM/SSL'), os.system("sed -i 's/65534/0/g' /etc/etter.conf")
            elif signal.upper() == '' or signal.upper() == 'EXIT':
                pass
            else:
                print 'Unknown command "%s" | type "show help" for more help.' % signal.lower()
    else:
        print 'Unknown command "use -m -i%s" | type "show help" for a list of commands.' % signal.lower()


