#!/bin/bash

PATH=$PATH:$(sed -n '/PATH=/s/^.*=// ; s/\"//gp' '/etc/environment')


if ! '/bin/bash' '/home/svn/xjdhdr-random-code/Bash/test_connection.bash'
then
	sDateTime=$(date -u +"%d %b %Y %H:%M")
	printf 'check_gmail_accounts_for_spam.bash:\n%s UTC\n-  No internet connection detected\n\n' "$sDateTime" \
		>> '/home/error_reports_to_email.txt'
	exit 1
fi

bSpamDetected=0
while read -r sAddress sPassword
do
	if [[ $sAddress != "" ]] && [[ $sPassword != "" ]]
	then
		sCurlOutput=$(curl -s --url 'imaps://imap.gmail.com' --user "$sAddress":"$sPassword" -X 'STATUS [Gmail]/Spam (MESSAGES)')
		sCurlOutputCopy=$sCurlOutput
		sCurlOutput=${sCurlOutput#'* STATUS "[Gmail]/Spam" ('}
		sCurlOutput=${sCurlOutput/)/}
		if [[ $sCurlOutput != "MESSAGES 0"* ]]
		then
			if [[ $bSpamDetected == 0 ]]
			then
				bSpamDetected=1
				sDateTime=$(date -u +"%d %b %Y %H:%M")
				printf 'check_gmail_accounts_for_spam.bash:\n%s UTC\n' "$sDateTime"
			fi
			if [[ $sCurlOutput == "MESSAGES "* ]]
			then
				printf '%s Spam detected while checking %s: %s\n' "-" "$sAddress" "$sCurlOutput"
			else
				printf '%s Error occured while checking %s: %s\n' "-" "$sAddress" "$sCurlOutputCopy"
			fi
		fi
	fi
done < "$HOME/gmail_details.txt" >> '/home/error_reports_to_email.txt'
