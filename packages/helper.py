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



def main(module):
    signal = module
    if signal.upper() == 'SHOW HELP':
        print """\033[1;32m
Type 'show <command>' for more detailed help on a command.
 Commands:
    modules        - Display available modules
    use            - use <module-name>
    exit           - exits the program
    version        - Display framework version. - no help available
    show help      - prints this screen, or help on 'command'
\033[1;m"""
    elif signal.upper() == 'SHOW USE':
        print """\033[1;32m
Usage: use <module-name> <command>
ex:
    use -M -ssl    <-  For SSL Stripping
    use -M -imgT   <-  For Imagine Injection
\033[1;m"""
    elif signal.upper() == 'SHOW MODULES':
        print """\033[1;32m
Usage: Type 'show use'
modules:
    [m - Man in the Middle]

    -M    --man
        commands
        -s    --ssl           - SSL Stripping
        -imgT                 - Image Tracking
\033[1;m"""
    elif signal.upper() == 'SHOW EXIT':
        print '\033[1;32mExits the program\033[1;m'
    elif signal.upper() == 'SHOW VERSION':
        print '\033[1;32mversion 1.0 Rev 0\033[1;m'
    elif signal.upper() == '' or signal.upper() == 'EXIT':
        pass
    else:
        print 'Unknown command "{0:s}" | type "show help" for a list of commands'.format(signal).lower()


def ssl():
    print """\033[1;32m

Usage: show config                ||  Display current settings
Usage: set <NAME> <SETTING>       ||  Config settings
Usage: run                        ||  To run exploit
Usage: stop                       ||  To stop exploit
Usage: save                       ||  To save log
Usage: exit                       ||  To exit the current exploit

                          RHOST   ||  Remote IP Address or Target IP Address
                                      Example: set rhost 192.168.1.2

                        INTERFACE ||  Network Card Interface
                                      Ex: eth0, Wlan0
                                      Example: set interface eth0

                            LPORT ||  Local Port.  * Don't use port 80, 443
                                      Example: set lport 8080

                          GATEWAY ||  Your Network Gateway Address
                                      Usually, this address is the router IP
                                      Example: set gateway 192.168.1.1
    \033[1;m"""
