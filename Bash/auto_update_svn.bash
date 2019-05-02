#!/bin/bash


PS4='$LINENO: '
PATH=$PATH:$(sed -n '/PATH=/s/^.*=// ; s/\"//gp' '/etc/environment')


if ! '/bin/bash' '/home/svn/xjdhdr-random-code/Bash/test_connection.bash'
then
	sDateTime=$(date -u +"%d %b %Y %H:%M")
	printf 'test_connection.bash:\n%s UTC\n-  No internet connection detected\n\n' "$sDateTime" \
		>> '/home/error_reports_to_email.txt'
	exit 1
fi

sVersion=$(date -u +"%Y%m%d%H%M")
sDateTime=$(date -u +"%d %b %Y %H:%M")
{
	svn update --accept theirs-full --force '/home/svn/xjdhdr-random-code/Adblock/'
	svn update --accept theirs-full --force '/home/svn/xjdhdr-random-code/Bash/'
	svn update --accept theirs-full --force '/home/svn/xjdhdr-random-code/torrent-mega-blocklist/'

	rm -rdf -- "$HOME/working_folder/*"

	CommandExitCode=$(wget -q -O "$HOME/working_folder/easylist.txt" -t 10 \
		-c 'https://easylist.to/easylist/easylist.txt')$?
	if [ "$CommandExitCode" -eq 0 ]
	then
		CommandExitCode=$(wget -q -O "$HOME/working_folder/easyprivacy.txt" -t 10 \
			-c 'https://easylist.to/easylist/easyprivacy.txt')$?
		if [ "$CommandExitCode" -eq 0 ]
		then
			CommandExitCode=$(wget -q -O "$HOME/working_folder/fanboy-annoyance.txt" -t 10 \
				-c 'https://easylist.to/easylist/fanboy-annoyance.txt')$?
			if [ "$CommandExitCode" -eq 0 ]
			then
				recode -f ..utf8 "$HOME/working_folder/easylist.txt"
				recode -f ..utf8 "$HOME/working_folder/easyprivacy.txt"
				recode -f ..utf8 "$HOME/working_folder/fanboy-annoyance.txt"
				{
					printf '[Adblock Plus 2.0]\n'
					printf '! Version: %s\n' "$sVersion"
					printf '! Title: Block Google'"'"'s adverts and tracking only\n'
					printf '! Last modified: %s UTC\n' "$sDateTime"
					printf '! Expires: 4 days\n'
					printf '! Homepage: https://github.com/XJDHDR/xjdhdr-random-code/\n'
					printf '! Licence: https://easylist-downloads.adblockplus.org/COPYING\n'
					printf '!\n'
					printf '! Filters were extracted from the Easylist, EasyPrivacy and Fanboy'"'"'s '
					printf 'Annoyances filter lists to block only Google'"'"'s adverts and tracking\n'
					printf '! Please use the License link to find licensing information\n'
					printf '! My thanks go to those listed here under "Credits" for these filters:'
					printf ' https://easylist.adblockplus.org/en/about\n'
					printf '!\n'
					printf '! Please report any issues by creating a ticket on GitHub or SourceForge\n'
					printf '!\n'
					printf '!\n'
					grep -iFf '/home/svn/xjdhdr-random-code/Bash/google_ad_keywords.txt' \
						"$HOME/working_folder/easylist.txt"
					grep -iFf '/home/svn/xjdhdr-random-code/Bash/google_ad_keywords.txt' \
						"$HOME/working_folder/easyprivacy.txt"
					grep -iFf '/home/svn/xjdhdr-random-code/Bash/google_ad_keywords.txt' \
						"$HOME/working_folder/fanboy-annoyance.txt"
				} > '/home/svn/xjdhdr-random-code/Adblock/Google-Filters.txt'
				sed -i '/@gmail\.com/d' '/home/svn/xjdhdr-random-code/Adblock/Google-Filters.txt'
				# Delete duplicate lines except comments
				awk '/^!/ || !a[$0]++' '/home/svn/xjdhdr-random-code/Adblock/Google-Filters.txt' \
					> '/home/svn/xjdhdr-random-code/Adblock/Google-Filters-cleaned.txt'
				mv -f '/home/svn/xjdhdr-random-code/Adblock/Google-Filters-cleaned.txt' \
					'/home/svn/xjdhdr-random-code/Adblock/Google-Filters.txt'
				recode -f ..utf8 '/home/svn/xjdhdr-random-code/Adblock/Google-Filters.txt'
				python '/home/addChecksum.py' < '/home/svn/xjdhdr-random-code/Adblock/Google-Filters.txt' \
					> '/home/svn/xjdhdr-random-code/Adblock/Google-Filters-checked.txt'
				mv -f '/home/svn/xjdhdr-random-code/Adblock/Google-Filters-checked.txt' \
					'/home/svn/xjdhdr-random-code/Adblock/Google-Filters.txt'
				CommandExitCode=$(python '/home/validateChecksum.py' < \
					'/home/svn/xjdhdr-random-code/Adblock/Google-Filters.txt')$?
				if [ "$CommandExitCode" != 'Checksum is valid0' ]
				then
					errors+='Errors encountered during checksum validation of Google-Filters.txt:'
					errors+=' Error:'"$CommandExitCode"'\n'
				fi
				CommandExitCode=0
				rm -f "$HOME/working_folder/fanboy-annoyance.txt"
			else
				errors+='Could not download fanboy-annoyance.txt: Error:'"$CommandExitCode"'\n'
			fi
			rm -f "$HOME/working_folder/easyprivacy.txt"
		else
			errors+='Could not download easyprivacy.txt: Error:'"$CommandExitCode"'\n'
		fi
		rm -f "$HOME/working_folder/easylist.txt"
	else
		errors+='Could not download easylist.txt: Error:'"$CommandExitCode"'\n'
	fi


	CommandExitCode=$(wget -q -O "$HOME/working_folder/exceptionrules.txt" -t 10 \
		-c 'https://easylist-downloads.adblockplus.org/exceptionrules.txt')$?
	if [ "$CommandExitCode" -eq 0 ]
	then
		recode -f ..utf8 "$HOME/working_folder/exceptionrules.txt"
		sed -i '/\[Adblock Plus 2\.0\]/d' "$HOME/working_folder/exceptionrules.txt"
		sed -i '/! Checksum: /d' "$HOME/working_folder/exceptionrules.txt"
		sed -i '/! Version: /d' "$HOME/working_folder/exceptionrules.txt"
		sed -i '/! Title: /d' "$HOME/working_folder/exceptionrules.txt"
		sed -i '/! Expires: /d' "$HOME/working_folder/exceptionrules.txt"
		sed -i '/! Homepage: /d' "$HOME/working_folder/exceptionrules.txt"
		{
			printf '[Adblock Plus 2.0]\n'
			printf '! Version: %s\n' "$sVersion"
			printf '! Title: AdBlock Plus'"'"' Acceptable Ads list without Google related filters\n'
			printf '! Last modified: %s UTC\n' "$sDateTime"
			printf '! Expires: 1 days\n'
			printf '! Homepage: https://github.com/XJDHDR/xjdhdr-random-code/\n'
			printf '!\n'
			printf '! Please report any issues by creating a ticket on GitHub or SourceForge\n'
			printf '!\n'
			printf '!\n'
			grep -viFf '/home/svn/xjdhdr-random-code/Bash/google_ad_keywords.txt' \
				"$HOME/working_folder/exceptionrules.txt"
		} > '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google.txt'
		# Delete duplicate lines except comments
		awk '/^!/ || !a[$0]++' '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google.txt' \
			> '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-cleaned.txt'
		mv -f '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-cleaned.txt' \
			'/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google.txt'
		recode -f ..utf8 '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google.txt'
		python '/home/addChecksum.py' < '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google.txt' \
			> '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-checked.txt'
		mv -f '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-checked.txt' \
			'/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google.txt'
		CommandExitCode=$(python '/home/validateChecksum.py' < \
			'/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google.txt')$?
		if [ "$CommandExitCode" != 'Checksum is valid0' ]
		then
			errors+='Errors encountered during checksum validation of Acceptable-ads-without-Google.txt:'
			errors+=' Error:'"$CommandExitCode"'\n'
		fi
		CommandExitCode=0
		rm -f "$HOME/working_folder/exceptionrules.txt"
	else
		errors+='Could not download exceptionrules.txt: Error:'"$CommandExitCode"'\n'
	fi


	CommandExitCode=$(wget -q -O "$HOME/working_folder/exceptionrules-privacy-friendly.txt" -t 10 -c \
		'https://easylist-downloads.adblockplus.org/exceptionrules-privacy-friendly.txt')$?
	if [ "$CommandExitCode" -eq 0 ]
	then
		recode -f ..utf8 "$HOME/working_folder/exceptionrules-privacy-friendly.txt"
		sed -i '/\[Adblock Plus 2\.0\]/d' "$HOME/working_folder/exceptionrules-privacy-friendly.txt"
		sed -i '/! Checksum: /d' "$HOME/working_folder/exceptionrules-privacy-friendly.txt"
		sed -i '/! Version: /d' "$HOME/working_folder/exceptionrules-privacy-friendly.txt"
		sed -i '/! Title: /d' "$HOME/working_folder/exceptionrules-privacy-friendly.txt"
		sed -i '/! Expires: /d' "$HOME/working_folder/exceptionrules-privacy-friendly.txt"
		sed -i '/! Homepage: /d' "$HOME/working_folder/exceptionrules-privacy-friendly.txt"
		{
			printf '[Adblock Plus 2.0]\n'
			printf '! Version: %s\n' "$sVersion"
			printf '! Title: AdBlock Plus'"'"' Acceptable Ads list without Google related filters or third-party tracking\n'
			printf '! Last modified: %s UTC\n' "$sDateTime"
			printf '! Expires: 1 days\n'
			printf '! Homepage: https://github.com/XJDHDR/xjdhdr-random-code/\n'
			printf '!\n'
			printf '! Please report any issues by creating a ticket on GitHub or SourceForge\n'
			printf '!\n'
			printf '!\n'
			grep -viFf '/home/svn/xjdhdr-random-code/Bash/google_ad_keywords.txt' \
				"$HOME//working_folder/exceptionrules-privacy-friendly.txt"
		} > '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-or-Third-party-Tracking.txt'
		# Delete duplicate lines except comments
		awk '/^!/ || !a[$0]++' \
			'/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-or-Third-party-Tracking.txt' \
			> '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-or-Third-party-Tracking-cleaned.txt'
		mv -f '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-or-Third-party-Tracking-cleaned.txt' \
			'/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-or-Third-party-Tracking.txt'
		recode -f ..utf8 '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-or-Third-party-Tracking.txt'
		python '/home/addChecksum.py' < \
			'/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-or-Third-party-Tracking.txt' \
			> '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-or-Third-party-Tracking-checked.txt'
		mv -f '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-or-Third-party-Tracking-checked.txt' \
			'/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-or-Third-party-Tracking.txt'
		CommandExitCode=$(python '/home/validateChecksum.py' \
			< '/home/svn/xjdhdr-random-code/Adblock/Acceptable-ads-without-Google-or-Third-party-Tracking.txt')$?
		if [ "$CommandExitCode" != 'Checksum is valid0' ]
		then
			errors+='Errors encountered during checksum validation of Acceptable-ads-without-Google'
			errors+='-or-Third-party-Tracking.txt: Error:'"$CommandExitCode"'\n'
		fi
		CommandExitCode=0
		rm -f "$HOME/working_folder/exceptionrules-privacy-friendly.txt"
	else
		errors+='Could not download exceptionrules.txt: Error:'"$CommandExitCode"'\n'
	fi


	declare -a HPHostsDownloadList=("emd" "exp" "fsa" "grm" "hfs" "hjk" "mmt" "pha" "psh" "pup" "wrz")
	for HPHostsDownloadItem in "${HPHostsDownloadList[@]}"
	do
		CommandExitCode=$(wget -q -O "$HOME/working_folder/hphosts-$HPHostsDownloadItem.txt" -t 10 \
			-c "https://hosts-file.net/$HPHostsDownloadItem.txt")$?
		if [ "$CommandExitCode" -eq 0 ]
		then
			dos2unix --quiet "$HOME/working_folder/hphosts-$HPHostsDownloadItem.txt"
			recode -f ..utf8 "$HOME/working_folder/hphosts-$HPHostsDownloadItem.txt"
			sed -i '/ localhost /d' "$HOME/working_folder/hphosts-$HPHostsDownloadItem.txt"
			sed -i 's/#/!/g' "$HOME/working_folder/hphosts-$HPHostsDownloadItem.txt"
			sed -i 's/[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\t/||/g' \
				"$HOME/working_folder/hphosts-$HPHostsDownloadItem.txt"
			sed -i '/!/!s/$/\^/g' "$HOME/working_folder/hphosts-$HPHostsDownloadItem.txt"
			{
				printf '[Adblock Plus 2.0]\n'
				printf '! Version: %s\n' "$sVersion"
				printf "! Title: HP Hosts %s list\n" "$HPHostsDownloadItem"
				printf '! Last modified: %s UTC\n' "$sDateTime"
				printf '! Expires: 4 days\n'
				printf '! Homepage: https://github.com/XJDHDR/xjdhdr-random-code/\n'
				printf '!\n'
				printf '! These filters were derived from the Hosts files that are provided by hpHosts\n'
				printf '! The original files can be found here: http://hosts-file.net/?s=Download\n'
				printf '! The 3 letter code at the end of this file'"'"'s name indicates the classification given to\n'
				printf '! all of the domains listed here by hpHosts. The definitions of those codes can be found here:\n'
				printf '! http://hosts-file.net/?s=classifications\n'
				printf '!\n'
				printf '! Please report any issues by creating a ticket on GitHub or SourceForge\n'
				printf '!\n'
				printf '!\n'
				cat "$HOME/working_folder/hphosts-$HPHostsDownloadItem.txt"
			} > "/home/svn/xjdhdr-random-code/Adblock/hphosts-$HPHostsDownloadItem.txt"
			# Delete duplicate lines except comments
			awk '/^!/ || !a[$0]++' "/home/svn/xjdhdr-random-code/Adblock/hphosts-$HPHostsDownloadItem.txt" \
				> "/home/svn/xjdhdr-random-code/Adblock/hphosts-$HPHostsDownloadItem-cleaned.txt"
			mv -f "/home/svn/xjdhdr-random-code/Adblock/hphosts-$HPHostsDownloadItem-cleaned.txt" \
				"/home/svn/xjdhdr-random-code/Adblock/hphosts-$HPHostsDownloadItem.txt"
			recode -f ..utf8 "/home/svn/xjdhdr-random-code/Adblock/hphosts-$HPHostsDownloadItem.txt"
			python '/home/addChecksum.py' < "/home/svn/xjdhdr-random-code/Adblock/hphosts-$HPHostsDownloadItem.txt" \
				> "/home/svn/xjdhdr-random-code/Adblock/hphosts-$HPHostsDownloadItem-checked.txt"
			mv -f "/home/svn/xjdhdr-random-code/Adblock/hphosts-$HPHostsDownloadItem-checked.txt" \
				"/home/svn/xjdhdr-random-code/Adblock/hphosts-$HPHostsDownloadItem.txt"
			CommandExitCode=$(python '/home/validateChecksum.py' < \
				"/home/svn/xjdhdr-random-code/Adblock/hphosts-$HPHostsDownloadItem.txt")$?
			if [ "$CommandExitCode" != 'Checksum is valid0' ]
			then
				errors+="Errors encountered during checksum validation of "
				errors+="hphosts-$HPHostsDownloadItem.txt: Error: $CommandExitCode\n"
			fi
			CommandExitCode=0
			rm -f "$HOME/working_folder/hphosts-$HPHostsDownloadItem.txt"
		else
			errors+="Could not download hphosts-$HPHostsDownloadItem.txt: Error:$CommandExitCode\n"
		fi
	done


	rm -f "$HOME/working_folder/blocklist.txt"
	CommandExitCode=$(wget -q -O "$HOME/working_folder/level_1.gz" -t 10 -c \
		'http://list.iblocklist.com/?list=ydxerpxkpcfqjaybcssw&fileformat=p2p&archiveformat=gz')$?
	if [ "$CommandExitCode" -eq 0 ]
	then
		gzip -cdf -- "$HOME/working_folder/level_1.gz" >> "$HOME/working_folder/blocklist.txt"
		rm -f "$HOME/working_folder/level_1.gz"
	else
		errors+="Could not download level_1.gz: Error:$CommandExitCode\n"
	fi
	CommandExitCode=$(wget -q -O "$HOME/working_folder/level_2.gz" -t 10 -c \
		'http://list.iblocklist.com/?list=gyisgnzbhppbvsphucsw&fileformat=p2p&archiveformat=gz')$?
	if [ "$CommandExitCode" -eq 0 ]
	then
		gzip -cdf -- "$HOME/working_folder/level_2.gz" >> "$HOME/working_folder/blocklist.txt"
		rm -f "$HOME/working_folder/level_2.gz"
	else
		errors+="Could not download level_2.gz: Error:$CommandExitCode\n"
	fi
	CommandExitCode=$(wget -q -O "$HOME/working_folder/rangetest.gz" -t 10 -c \
		'http://list.iblocklist.com/?list=plkehquoahljmyxjixpu&fileformat=p2p&archiveformat=gz')$?
	if [ "$CommandExitCode" -eq 0 ]
	then
		gzip -cdf -- "$HOME/working_folder/rangetest.gz" >> "$HOME/working_folder/blocklist.txt"
		rm -f "$HOME/working_folder/rangetest.gz"
	else
		errors+="Could not download rangetest.gz: Error:$CommandExitCode\n"
	fi
	CommandExitCode=$(wget -q -O "$HOME/working_folder/bogon.gz" -t 10 -c \
		'http://list.iblocklist.com/?list=gihxqmhyunbxhbmgqrla&fileformat=p2p&archiveformat=gz')$?
	if [ "$CommandExitCode" -eq 0 ]
	then
		gzip -cdf -- "$HOME/working_folder/bogon.gz" >> "$HOME/working_folder/blocklist.txt"
		rm -f "$HOME/working_folder/bogon.gz"
	else
		errors+="Could not download bogon.gz: Error:$CommandExitCode\n"
	fi
	CommandExitCode=$(wget -q -O "$HOME/working_folder/proxy.gz" -t 10 -c \
		'http://list.iblocklist.com/?list=xoebmbyexwuiogmbyprb&fileformat=p2p&archiveformat=gz')$?
	if [ "$CommandExitCode" -eq 0 ]
	then
		gzip -cdf -- "$HOME/working_folder/proxy.gz" >> "$HOME/working_folder/blocklist.txt"
		rm -f "$HOME/working_folder/proxy.gz"
	else
		errors+="Could not download proxy.gz: Error:$CommandExitCode\n"
	fi
	CommandExitCode=$(wget -q -O "$HOME/working_folder/microsoft.gz" -t 10 -c \
		'http://list.iblocklist.com/?list=xshktygkujudfnjfioro&fileformat=p2p&archiveformat=gz')$?
	if [ "$CommandExitCode" -eq 0 ]
	then
		gzip -cdf -- "$HOME/working_folder/microsoft.gz" >> "$HOME/working_folder/blocklist.txt"
		rm -f "$HOME/working_folder/microsoft.gz"
	else
		errors+="Could not download microsoft.gz: Error:$CommandExitCode\n"
	fi
	CommandExitCode=$(wget -q -O "$HOME/working_folder/iana-reserved.gz" -t 10 -c \
		'http://list.iblocklist.com/?list=bcoepfyewziejvcqyhqo&fileformat=p2p&archiveformat=gz')$?
	if [ "$CommandExitCode" -eq 0 ]
	then
		gzip -cdf -- "$HOME/working_folder/iana-reserved.gz" >> "$HOME/working_folder/blocklist.txt"
		rm -f "$HOME/working_folder/iana-reserved.gz"
	else
		errors+="Could not download iana-reserved.gz: Error:$CommandExitCode\n"
	fi
	CommandExitCode=$(wget -q -O "$HOME/working_folder/iana-multicast.gz" -t 10 -c \
		'http://list.iblocklist.com/?list=pwqnlynprfgtjbgqoizj&fileformat=p2p&archiveformat=gz')$?
	if [ "$CommandExitCode" -eq 0 ]
	then
		gzip -cdf -- "$HOME/working_folder/iana-multicast.gz" >> "$HOME/working_folder/blocklist.txt"
		rm -f "$HOME/working_folder/iana-multicast.gz"
	else
		errors+="Could not download iana-multicast.gz: Error:$CommandExitCode\n"
	fi
	# Delete duplicate lines
	awk '!a[$0]++' "$HOME/working_folder/blocklist.txt" > "$HOME/working_folder/blocklist-cleaned.txt"
	mv -f "$HOME/working_folder/blocklist-cleaned.txt" "$HOME/working_folder/blocklist.txt"
	gzip -f9 -- "$HOME/working_folder/blocklist.txt"
	mv -f -- "$HOME/working_folder/blocklist.txt.gz" "/home/svn/xjdhdr-random-code/torrent-mega-blocklist/blocklist.p2p.gz"


	# Commit changes
	#   SourceForge
	sshpass -f "$HOME/sourceforge_password.txt" rsync -qcruz -e ssh --exclude=.svn '/home/svn/xjdhdr-random-code/' \
		'xjdhdr@frs.sourceforge.net:/home/frs/project/xjdhdr-random-code/'

	#   GitHub
#	svn status '/home/svn/xjdhdr-random-code/' | grep ^\? | cut -c2- | while IFS='' read -r sFile
#	do
#		svn add "$sFile"
#	done
	svn status '/home/svn/xjdhdr-random-code/' | awk '{if ($1 == "?") print $2 }' | xargs svn add
	sshpass -f "$HOME/github_password.txt" svn commit --username=XJDHDR --no-auth-cache --force-interactive \
		-m 'Automatic update of Adblock, Bash + blocklist files' '/home/svn/xjdhdr-random-code'
} 2> '/tmp/stderr-contents-auto_update_svn.txt'

if [ -f '/tmp/stderr-contents-auto_update_svn.txt' ]
then
	errors+=$(cat '/tmp/stderr-contents-auto_update_svn.txt')
	rm -f '/tmp/stderr-contents-auto_update_svn.txt'
fi


if [ -n "$errors" ]
then
	printf 'auto_update_svn.bash:\n%s UTC\n'"$errors"'\n\n' "$sDateTime" >> '/home/error_reports_to_email.txt'
fi
