#!/usr/bin/env python

# SENUM version 1 Rev 0
# Written By: Viet Luu
# WEB: www.ring0lab.com


##########################################################################
# SENUM                                                                  #
#                                                                        #
# Copyright 2013 Viet Luu                                                #
#                                                                        #
# This file is part of www.redc0re.com, www.ofx7.com .                   #
#                                                                        #
# SENUM is free software; you can redistribute it and/or modify          #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation version 3 of the License.                 #
#                                                                        #
##########################################################################

import os
import signal
import commands

def message():
    print """\033[1;32m
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
  ___ ___ _  _ _   _ __  __
 / __| __| \| | | | |  \/  |
 \__ \ _|| .` | |_| | |\/| |
 |___/___|_|\_|\___/|_|  |_| V.1 Rev 0
######################################
-> www.ring0lab.com
                            \033[1;41m--Viet Luu\033[1;m
\033[1;m"""

def clear():
    os.system('clear')


def ctrl(signum, frm):
    print "\n\033[1;32m[!]Type 'exit' to quit the program.\033[1;m"

signal.signal(signal.SIGINT, ctrl)


def cleansll():
    os.system('cp /tmp/SENUM/SSL/etter.conf /etc/')
    os.system('iptables --flush'), os.system('iptables --table nat --flush'), os.system('iptables --delete-chain'), os.system('iptables --table nat --delete-chain')
    os.system('pkill sslstrip'), os.system('pkill ettercap'), os.system('pkill tail'), os.system('pkill outssl.sh')



def cleanimgtrack():
    os.system('pkill ettercap')
    os.system('cp /tmp/SENUM/IMGT/etter.conf /etc/')

def cleanimgtrackhalf():
    os.system('pkill driftnet')

def cleanimgtrackfull():
    os.system('pkill driftnet'), os.system('pkill sleep')
    os.system('pkill ettercap'), os.system('pkill sslstrip')
    os.system('cp /tmp/SENUM/IMGT/etter.conf /etc/')
    os.system('iptables --flush'), os.system('iptables --table nat --flush'), os.system('iptables --delete-chain'), os.system('iptables --table nat --delete-chain')

def cleanall():
    os.system('pkill sleep')
    os.system('pkill ettercap')
    os.system('pkill driftnet')
    os.system('cp /tmp/SENUM/SSL/etter.conf /etc/')
    os.system('cp /tmp/SENUM/IMGT/etter.conf /etc/')
    os.system('iptables --flush'), os.system('iptables --table nat --flush'), os.system('iptables --delete-chain'), os.system('iptables --table nat --delete-chain')
    os.system('pkill sslstrip'), os.system('pkill ettercap'), os.system('pkill tail'), os.system('pkill outssl.sh')





