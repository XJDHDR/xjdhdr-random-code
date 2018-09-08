#!/bin/bash

if ! /home/svn/xjdhdr-random-code/trunk/Bash/test_connection.bash
then
	exit 1
fi

CurIPaddr=$(dig TXT +short o-o.myaddr.l.google.com @ns1.google.com | sed -e 's/^"//' -e 's/"$//')
OldIPaddr=$(cat ~/run_DuckDNS_data.txt)

if [ "$CurIPaddr" != "$OldIPaddr" ]
then
	curl -k  "https://www.duckdns.org/update?domains=$1&token=$2&ip="
	echo "$CurIPaddr" > ~/run_DuckDNS_data.txt
fi

exit 0
