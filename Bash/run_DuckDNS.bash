#!/bin/bash

PATH=$PATH:$(sed -n '/PATH=/s/^.*=// ; s/\"//gp' '/etc/environment')


if ! '/bin/bash' '/home/zz_repositories/xjdhdr-random-code/Bash/test_connection.bash'
then
	exit 1
fi

# Check and update DuckDNS's IPv4 address record.
sHostIPaddr=$(dig -4 TXT +short o-o.myaddr.l.google.com @ns1.google.com | sed -e 's/^"//' -e 's/"$//')
sDuckDnsIPaddr=$(dig -4 +short xjdhdr-google-cloud.duckdns.org)
if [ "$sHostIPaddr" != "$sDuckDnsIPaddr" ]
then
	sDomain=$(cat "$HOME/$1")
	sToken=$(cat "$HOME/$2")
	curl -k "https://www.duckdns.org/update?domains=$sDomain&token=$sToken&ip=$sHostIPaddr" 2>'/tmp/stderr-contents-run_DuckDNS.txt'
fi

# Check and update DuckDNS's IPv6 address record.
sHostIPaddr=$(dig -6 TXT +short o-o.myaddr.l.google.com @ns1.google.com 2>'/dev/null' | sed -e 's/^"//' -e 's/"$//')
iDigExitCode=$?
if [ "$iDigExitCode" == 0 ]
then
	sDuckDnsIPaddr=$(dig -6 +short xjdhdr-google-cloud.duckdns.org)
	if [ "$sHostIPaddr" != "$sDuckDnsIPaddr" ]
	then
		sDomain=$(cat "$HOME/$1")
		sToken=$(cat "$HOME/$2")
		curl -k "https://www.duckdns.org/update?domains=$sDomain&token=$sToken&ipv6=$sHostIPaddr" \
			2>'/tmp/stderr-contents-run_DuckDNS.txt'
	fi
fi

# Add any errors that occured during the update process to the error log.
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
