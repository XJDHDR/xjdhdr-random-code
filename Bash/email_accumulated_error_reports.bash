#!/bin/bash

PATH=$PATH:$(sed -n '/PATH=/s/^.*=// ; s/\"//gp' '/etc/environment')


if ! '/bin/bash' '/home/svn/xjdhdr-random-code/Bash/test_connection.bash'
then
	sDateTime=$(date -u +"%d %b %Y %H:%M")
	printf 'email_accumulated_error_reports.bash:\n%s UTC\n-  No internet connection detected\n\n' "$sDateTime" \
		>> '/home/error_reports_to_email.txt'
	exit 1
fi

if [ -s '/home/error_reports_to_email.txt' ]
then
	sErrorReportsFileContents=$(cat '/home/error_reports_to_email.txt')
	read -r sReceiver sSender < "$HOME/email_addresses.txt"
	printf 'To: %s\nFrom: %s\nSubject: Errors reported by Google server\n\n%s' \
		"$sReceiver" "$sSender" "$sErrorReportsFileContents" | msmtp -a default "$sReceiver"
	printf "" > '/home/error_reports_to_email.txt'
fi

exit 0

