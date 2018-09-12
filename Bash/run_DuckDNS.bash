#!/bin/bash

if ! '/bin/bash' '/home/svn/xjdhdr-random-code/Bash/test_connection.bash'
then
	exit 1
fi

CurIPaddr=$(dig TXT +short o-o.myaddr.l.google.com @ns1.google.com | sed -e 's/^"//' -e 's/"$//')
if [ -f "$HOME/run_DuckDNS_data.txt" ]
then
	OldIPaddr=$(cat "$HOME/run_DuckDNS_data.txt")
fi

if [ "$CurIPaddr" != "$OldIPaddr" ]
then
	sDomain=$(cat "$HOME/$1.txt")
	sToken=$(cat "$HOME/$2.txt")
	curl -k  "https://www.duckdns.org/update?domains=$sDomain&token=$sToken&ip=" 2>'/tmp/stderr-contents-run_DuckDNS.txt'
	echo "$CurIPaddr" > ~/run_DuckDNS_data.txt
fi

if [ -f '/tmp/stderr-contents-run_DuckDNS.txt' ]
then
	errors+=$(cat '/tmp/stderr-contents-run_DuckDNS.txt')
	rm -f '/tmp/stderr-contents-run_DuckDNS.txt'
fi
if [ -n "$errors" ]
then
        printf 'run_DuckDNS.bash:\n%s UTC\n'"$errors"'\n\n' "$sDateTime" >> '/home/error_reports_to_email.txt'
fi

exit 0
