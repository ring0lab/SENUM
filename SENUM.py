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



from modules.man import enumssl
from packages import main
from packages import helper
from modules.man import injection
from modules.man import imgtrack







# Global variables

signal = ''
helpsignal = ''
x = ''
y = ''




main.ctrl(x, y)
main.clear()
main.message()


while signal.upper() != 'EXIT':
    signal = str(raw_input('\033[1;32m[!]senum> \033[1;m'))
    if signal.split().__contains__('use') == 1 and signal.split()[0] == 'use':
        if (signal.split().__contains__('--man') == 1 or signal.split().__contains__('-M') == 1) and (signal.split().__contains__('--ssl') == 1 or signal.split().__contains__('-s') == 1) and (len(signal.split()) == 3):
            enumssl.ssl()
        elif (signal.split().__contains__('--man') == 1 or signal.split().__contains__('-M') == 1) and (signal.split().__contains__('-imgT') == 1) and (len(signal.split()) == 3):
            imgtrack.imgtrack()
        elif (signal.upper().split().__contains__('--MAN') == 1 or signal.upper().split().__contains__('-M') == 1) and (len(signal.split()) == 3):
            if len(signal) == 10:
                injection.main(signal[9])
            else:
                print '\033[1;32mUnknown command "%s" | type "show use" for more help.\033[1;m' % signal
        else:
            print '\033[1;32mUnknown command "%s" | type "show use" for more help.\033[1;m' % signal
    elif signal.upper().split().__contains__('SHOW') == 1:
        if len(signal.split()) == 2:
            helper.main(signal.upper())
        else:
            print '\033[1;32mUnknown command "%s" | type "show help" for a list of commands.\033[1;m' % signal.lower()
    elif signal.upper() == '' or signal.upper() == 'EXIT':
        pass
    else:
        print '\033[1;32mUnknown command "%s" | type "show help" for a list of commands.\033[1;m' % signal.lower()
main.clear()
main.cleansll()



