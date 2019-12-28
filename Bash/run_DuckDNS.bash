#!/bin/bash

PATH=$PATH:$(sed -n '/PATH=/s/^.*=// ; s/\"//gp' '/etc/environment')


if ! '/bin/bash' '/home/zz_repositories/xjdhdr-random-code/Bash/test_connection.bash'
then
	exit 1
fi

# Check and update DuckDNS's IPv4 address record.
sHostIPaddr=$(dig +short myip.opendns.com A @resolver1.opendns.com)
sDuckDnsIPaddr=$(dig +short xjdhdr-google-cloud.duckdns.org A @resolver1.opendns.com)
if [ "$sHostIPaddr" != "$sDuckDnsIPaddr" ]
then
	sDomain=$(cat "$HOME/$1")
	sToken=$(cat "$HOME/$2")
	curl -k "https://www.duckdns.org/update?domains=$sDomain&token=$sToken&ip=$sHostIPaddr" 2>'/tmp/stderr-contents-run_DuckDNS.txt'
fi

# Check and update DuckDNS's IPv6 address record.
sHostIPaddr=$(dig +short myip.opendns.com AAAA @resolver1.opendns.com)
if [ "$sHostIPaddr" != "" ]
then
	sDuckDnsIPaddr=$(dig +short xjdhdr-google-cloud.duckdns.org AAAA @resolver1.opendns.com)
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
	sDateTime=$(date -u +"%d %b %Y %H:%M")
        printf 'run_DuckDNS.bash:\n%s UTC\n'"$errors"'\n\n' "$sDateTime" >> '/home/error_reports_to_email.txt'
fi

exit 0
