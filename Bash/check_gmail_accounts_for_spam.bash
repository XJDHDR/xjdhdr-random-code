#!/bin/bash

if ! '/bin/bash' '/home/svn/xjdhdr-random-code/Bash/test_connection.bash'
then
	sDateTime=$(date -u +"%d %b %Y %H:%M")
	printf 'check_gmail_accounts_for_spam.bash:\n%s UTC\n-  No internet connection detected\n\n' "$sDateTime" \
		>> '/home/error_reports_to_email.txt'
	exit 1
fi

while read -r sAddress sPassword
do
	if [ "$sAddress" != "" ] && [ "$sPassword" != "" ]
	then
		sCurlOutput=$(sshpass -p "$sPassword" curl --url 'imaps://imap.gmail.com' --user "$sAddress" -X 'STATUS [Gmail]/Spam (MESSAGES)')
		sCurlOutputCopy=$sCurlOutput
		sCurlOutput=${sCurlOutput#'* STATUS "[Gmail]/Spam" ('}
		sCurlOutput=${sCurlOutput#')'}
		if [ "$sCurlOutput" != "MESSAGES 0" ]
		then
			sDateTime=$(date -u +"%d %b %Y %H:%M")
			if [[ $sCurlOutput == "MESSAGES "* ]]
			then
				printf 'check_gmail_accounts_for_spam.bash:\n%s UTC\n-  Spam detected while checking %s: %s\n\n' "$sDateTime" "$sAddress" "$sCurlOutputCopy"
			else
				printf 'check_gmail_accounts_for_spam.bash:\n%s UTC\n-  Error occured while checking %s: %s\n\n' "$sDateTime" "$sAddress" "$sCurlOutputCopy"
			fi
		fi
	fi
done < "$HOME/gmail_details.txt" >> '/home/error_reports_to_email.txt'

