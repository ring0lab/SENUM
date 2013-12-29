#!/bin/sh


tail -f /tmp/SENUM/SSL/log.txt | while read line; do echo "$line" | awk '/USER/ { print "\033[1;32m[!]WEB ADDRESS: \033[1;m" substr($10,8,16) "\n\033[1;32m[!]SERVER IP  : \033[1;m" $3 "\n\033[1;32m[!]USERNAME   : \033[1;m" $6 "\n\033[1;32m[!]PASSWORD   : \033[1;m" $8 "\n\n\033[1;32m-----------------------------------\033[1;m"}'; done
