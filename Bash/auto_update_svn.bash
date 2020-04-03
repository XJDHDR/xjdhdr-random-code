#!/bin/bash


PS4='$LINENO: '
PATH=$PATH:$(sed -n '/PATH=/s/^.*=// ; s/\"//gp' '/etc/environment')


if ! '/bin/bash' '/home/zz_repositories/xjdhdr-random-code/Bash/test_connection.bash'
then
	sDateTime=$(date -u +"%d %b %Y %H:%M")
	printf 'test_connection.bash:\n%s UTC\n-  No internet connection detected\n\n' "$sDateTime" \
		>> '/home/error_reports_to_email.txt'
	exit 1
fi

sVersion=$(date -u +"%Y%m%d%H%M")
sDateTime=$(date -u +"%d %b %Y %H:%M")
{
	svn update --accept theirs-full --force '/home/zz_repositories/xjdhdr-random-code/Adblock/'
	svn update --accept theirs-full --force '/home/zz_repositories/xjdhdr-random-code/Bash/'
	svn update --accept theirs-full --force '/home/zz_repositories/xjdhdr-random-code/torrent-mega-blocklist/'

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
					grep -iFf '/home/zz_repositories/xjdhdr-random-code/Bash/google_ad_keywords.txt' \
						"$HOME/working_folder/easylist.txt"
					grep -iFf '/home/zz_repositories/xjdhdr-random-code/Bash/google_ad_keywords.txt' \
						"$HOME/working_folder/easyprivacy.txt"
					grep -iFf '/home/zz_repositories/xjdhdr-random-code/Bash/google_ad_keywords.txt' \
						"$HOME/working_folder/fanboy-annoyance.txt"
				} > '/home/zz_repositories/xjdhdr-random-code/Adblock/Google-Filters.txt'
				sed -i '/@gmail\.com/d' '/home/zz_repositories/xjdhdr-random-code/Adblock/Google-Filters.txt'
				# Delete duplicate lines except comments
				awk '/^!/ || !a[$0]++' '/home/zz_repositories/xjdhdr-random-code/Adblock/Google-Filters.txt' \
					> '/home/zz_repositories/xjdhdr-random-code/Adblock/Google-Filters-cleaned.txt'
				mv -f '/home/zz_repositories/xjdhdr-random-code/Adblock/Google-Filters-cleaned.txt' \
					'/home/zz_repositories/xjdhdr-random-code/Adblock/Google-Filters.txt'
				recode -f ..utf8 '/home/zz_repositories/xjdhdr-random-code/Adblock/Google-Filters.txt'
				python '/home/addChecksum.py' < '/home/zz_repositories/xjdhdr-random-code/Adblock/Google-Filters.txt' \
					> '/home/zz_repositories/xjdhdr-random-code/Adblock/Google-Filters-checked.txt'
				mv -f '/home/zz_repositories/xjdhdr-random-code/Adblock/Google-Filters-checked.txt' \
					'/home/zz_repositories/xjdhdr-random-code/Adblock/Google-Filters.txt'
				CommandExitCode=$(python '/home/validateChecksum.py' < \
					'/home/zz_repositories/xjdhdr-random-code/Adblock/Google-Filters.txt')$?
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
			printf '! Title: Acceptable Ads - Third Party Tracking permitted - no Google\n'
			printf '! Last modified: %s UTC\n' "$sDateTime"
			printf '! Expires: 1 days\n'
			printf '! Homepage: https://github.com/XJDHDR/xjdhdr-random-code/\n'
			printf '!\n'
			printf '! This filter list is not associated with the Acceptable Ads Committee or it'"'"'s filter list\n'
			printf '! Rather, this is an unofficial modification to their list.\n'
			printf '!\n'
			printf '! You may report issues with this filter list by creating a ticket on GitHub, GitLab, Bitbucket or SourceForge\n'
			printf '! You may report issues with the original Acceptable Ads list here: support@adblockplus.org\n'
			printf '! To figure out which avenue to report on, please follow the troubleshooting steps below:\n'
			printf '!\n'
			printf '! If you are seeing Google ads with this list enabled, please disable this filter list then reload the webpage.\n'
			printf '! If those adverts disappear, the issue is in my list and please report this issue to me.\n'
			printf '! If the ads does not disappear, please report this to Easylist or whatever ad blocking list you are using.\n'
			printf '!\n'
			printf '! If an ad that does not meet the Acceptable Ads criteria is not blocked, please disable this filter list then reload the webpage.\n'
			printf '! If that ad does not disappear, please report this to Easylist or whatever ad blocking list you are using.\n'
			printf '! If it does disappear, please temporarily enable the regular Acceptable Ads filter list then reload the webpage.\n'
			printf '! If the ad reappears, please report it at the email address above. If not, please create a ticket.\n'
			printf '!\n'
			printf '!\n'
			grep -viFf '/home/zz_repositories/xjdhdr-random-code/Bash/google_ad_keywords.txt' \
				"$HOME/working_folder/exceptionrules.txt"
		} > '/home/zz_repositories/xjdhdr-random-code/Adblock/Acceptable_Ads_-_Third_Party_Tracking_permitted_-_no_Google.txt'

		{
			printf '[Adblock Plus 2.0]\n'
			printf '! Version: %s\n' "$sVersion"
			printf '! Title: Acceptable Ads - Third Party Tracking permitted - no Taboola\n'
			printf '! Last modified: %s UTC\n' "$sDateTime"
			printf '! Expires: 1 days\n'
			printf '! Homepage: https://github.com/XJDHDR/xjdhdr-random-code/\n'
			printf '!\n'
			printf '! This filter list is not associated with the Acceptable Ads Committee or it'"'"'s filter list\n'
			printf '! Rather, this is an unofficial modification to their list.\n'
			printf '!\n'
			printf '! You may report issues with this filter list by creating a ticket on GitHub, GitLab, Bitbucket or SourceForge\n'
			printf '! You may report issues with the original Acceptable Ads list here: support@adblockplus.org\n'
			printf '! To figure out which avenue to report on, please follow the troubleshooting steps below:\n'
			printf '!\n'
			printf '! If you are seeing Taboola ads with this list enabled, please disable this filter list then reload the webpage.\n'
			printf '! If those adverts disappear, the issue is in my list and please report this issue to me.\n'
			printf '! If the ads does not disappear, please report this to Easylist or whatever ad blocking list you are using.\n'
			printf '!\n'
			printf '! If an ad that does not meet the Acceptable Ads criteria is not blocked, please disable this filter list then reload the webpage.\n'
			printf '! If that ad does not disappear, please report this to Easylist or whatever ad blocking list you are using.\n'
			printf '! If it does disappear, please temporarily enable the regular Acceptable Ads filter list then reload the webpage.\n'
			printf '! If the ad reappears, please report it at the email address above. If not, please create a ticket.\n'
			printf '!\n'
			printf '!\n'
			grep -viFe 'taboola' "$HOME/working_folder/exceptionrules.txt"
		} > '/home/zz_repositories/xjdhdr-random-code/Adblock/Acceptable_Ads_-_Third_Party_Tracking_permitted_-_no_Taboola.txt'

		{
			printf '[Adblock Plus 2.0]\n'
			printf '! Version: %s\n' "$sVersion"
			printf '! Title: Acceptable Ads - Third Party Tracking permitted - no Google or Taboola\n'
			printf '! Last modified: %s UTC\n' "$sDateTime"
			printf '! Expires: 1 days\n'
			printf '! Homepage: https://github.com/XJDHDR/xjdhdr-random-code/\n'
			printf '!\n'
			printf '! This filter list is not associated with the Acceptable Ads Committee or it'"'"'s filter list\n'
			printf '! Rather, this is an unofficial modification to their list.\n'
			printf '!\n'
			printf '! You may report issues with this filter list by creating a ticket on GitHub, GitLab, Bitbucket or SourceForge\n'
			printf '! You may report issues with the original Acceptable Ads list here: support@adblockplus.org\n'
			printf '! To figure out which avenue to report on, please follow the troubleshooting steps below:\n'
			printf '!\n'
			printf '! If you are seeing Google or Taboola ads with this list enabled, please disable this filter list then reload the webpage.\n'
			printf '! If those adverts disappear, the issue is in my list and please report this issue to me.\n'
			printf '! If the ads does not disappear, please report this to Easylist or whatever ad blocking list you are using.\n'
			printf '!\n'
			printf '! If an ad that does not meet the Acceptable Ads criteria is not blocked, please disable this filter list then reload the webpage.\n'
			printf '! If that ad does not disappear, please report this to Easylist or whatever ad blocking list you are using.\n'
			printf '! If it does disappear, please temporarily enable the regular Acceptable Ads filter list then reload the webpage.\n'
			printf '! If the ad reappears, please report it at the email address above. If not, please create a ticket.\n'
			printf '!\n'
			printf '!\n'
			grep -viFe 'taboola' -f '/home/zz_repositories/xjdhdr-random-code/Bash/google_ad_keywords.txt' \
				"$HOME/working_folder/exceptionrules.txt"
		} > '/home/zz_repositories/xjdhdr-random-code/Adblock/Acceptable_Ads_-_Third_Party_Tracking_permitted_-_no_Google_or_Taboola.txt'

		for file in /home/zz_repositories/xjdhdr-random-code/Adblock/Acceptable_Ads_-_Third_Party_Tracking_permitted_-_*
		do
			# Delete duplicate lines except comments
			awk '/^!/ || !a[$0]++' "$file" > "$file-cleaned.txt"
			mv -f "$file-cleaned.txt" "$file"
			recode -f ..utf8 "$file"
			python '/home/addChecksum.py' < "$file" > "$file-checked.txt"
			mv -f "$file-checked.txt" "$file"
			CommandExitCode=$(python '/home/validateChecksum.py' < "$file")$?
			if [ "$CommandExitCode" != 'Checksum is valid0' ]
			then
				errors+='Errors encountered during checksum validation of '"$file"':'
				errors+=' Error:'"$CommandExitCode"'\n'
			fi
			CommandExitCode=0
		done
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
			printf '! Title: Acceptable Ads - no Third Party Tracking - no Google\n'
			printf '! Last modified: %s UTC\n' "$sDateTime"
			printf '! Expires: 1 days\n'
			printf '! Homepage: https://github.com/XJDHDR/xjdhdr-random-code/\n'
			printf '!\n'
			printf '! This filter list is not associated with the Acceptable Ads Committee or it'"'"'s filter list\n'
			printf '! Rather, this is an unofficial modification to their list.\n'
			printf '!\n'
			printf '! You may report issues with this filter list by creating a ticket on GitHub, GitLab, Bitbucket or SourceForge\n'
			printf '! You may report issues with the original Acceptable Ads list here: support@adblockplus.org\n'
			printf '! To figure out which avenue to report on, please follow the troubleshooting steps below:\n'
			printf '!\n'
			printf '! If you are seeing Google ads with this list enabled, please disable this filter list then reload the webpage.\n'
			printf '! If those adverts disappear, the issue is in my list and please report this issue to me.\n'
			printf '! If the ads does not disappear, please report this to Easylist or whatever ad blocking list you are using.\n'
			printf '!\n'
			printf '! If an ad that does not meet the Acceptable Ads criteria is not blocked, please disable this filter list then reload the webpage.\n'
			printf '! If that ad does not disappear, please report this to Easylist or whatever ad blocking list you are using.\n'
			printf '! If it does disappear, please temporarily enable the regular Acceptable Ads filter list then reload the webpage.\n'
			printf '! If the ad reappears, please report it at the email address above. If not, please create a ticket.\n'
			printf '!\n'
			printf '!\n'
			grep -viFf '/home/zz_repositories/xjdhdr-random-code/Bash/google_ad_keywords.txt' \
				"$HOME//working_folder/exceptionrules-privacy-friendly.txt"
		} > '/home/zz_repositories/xjdhdr-random-code/Adblock/Acceptable_Ads_-_no_Third_Party_Tracking_-_no_Google.txt'

		{
			printf '[Adblock Plus 2.0]\n'
			printf '! Version: %s\n' "$sVersion"
			printf '! Title: Acceptable Ads - no Third Party Tracking - no Taboola\n'
			printf '! Last modified: %s UTC\n' "$sDateTime"
			printf '! Expires: 1 days\n'
			printf '! Homepage: https://github.com/XJDHDR/xjdhdr-random-code/\n'
			printf '!\n'
			printf '! This filter list is not associated with the Acceptable Ads Committee or it'"'"'s filter list\n'
			printf '! Rather, this is an unofficial modification to their list.\n'
			printf '!\n'
			printf '! You may report issues with this filter list by creating a ticket on GitHub, GitLab, Bitbucket or SourceForge\n'
			printf '! You may report issues with the original Acceptable Ads list here: support@adblockplus.org\n'
			printf '! To figure out which avenue to report on, please follow the troubleshooting steps below:\n'
			printf '!\n'
			printf '! If you are seeing Taboola ads with this list enabled, please disable this filter list then reload the webpage.\n'
			printf '! If those adverts disappear, the issue is in my list and please report this issue to me.\n'
			printf '! If the ads does not disappear, please report this to Easylist or whatever ad blocking list you are using.\n'
			printf '!\n'
			printf '! If an ad that does not meet the Acceptable Ads criteria is not blocked, please disable this filter list then reload the webpage.\n'
			printf '! If that ad does not disappear, please report this to Easylist or whatever ad blocking list you are using.\n'
			printf '! If it does disappear, please temporarily enable the regular Acceptable Ads filter list then reload the webpage.\n'
			printf '! If the ad reappears, please report it at the email address above. If not, please create a ticket.\n'
			printf '!\n'
			printf '!\n'
			grep -viFe 'taboola' "$HOME//working_folder/exceptionrules-privacy-friendly.txt"
		} > '/home/zz_repositories/xjdhdr-random-code/Adblock/Acceptable_Ads_-_no_Third_Party_Tracking_-_no_Taboola.txt'

		{
			printf '[Adblock Plus 2.0]\n'
			printf '! Version: %s\n' "$sVersion"
			printf '! Title: Acceptable Ads - no Third Party Tracking - no Google or Taboola\n'
			printf '! Last modified: %s UTC\n' "$sDateTime"
			printf '! Expires: 1 days\n'
			printf '! Homepage: https://github.com/XJDHDR/xjdhdr-random-code/\n'
			printf '!\n'
			printf '! This filter list is not associated with the Acceptable Ads Committee or it'"'"'s filter list\n'
			printf '! Rather, this is an unofficial modification to their list.\n'
			printf '!\n'
			printf '! You may report issues with this filter list by creating a ticket on GitHub, GitLab, Bitbucket or SourceForge\n'
			printf '! You may report issues with the original Acceptable Ads list here: support@adblockplus.org\n'
			printf '! To figure out which avenue to report on, please follow the troubleshooting steps below:\n'
			printf '!\n'
			printf '! If you are seeing Google or Taboola ads with this list enabled, please disable this filter list then reload the webpage.\n'
			printf '! If those adverts disappear, the issue is in my list and please report this issue to me.\n'
			printf '! If the ads does not disappear, please report this to Easylist or whatever ad blocking list you are using.\n'
			printf '!\n'
			printf '! If an ad that does not meet the Acceptable Ads criteria is not blocked, please disable this filter list then reload the webpage.\n'
			printf '! If that ad does not disappear, please report this to Easylist or whatever ad blocking list you are using.\n'
			printf '! If it does disappear, please temporarily enable the regular Acceptable Ads filter list then reload the webpage.\n'
			printf '! If the ad reappears, please report it at the email address above. If not, please create a ticket.\n'
			printf '!\n'
			printf '!\n'
			grep -viFe 'taboola' -f '/home/zz_repositories/xjdhdr-random-code/Bash/google_ad_keywords.txt' \
				"$HOME//working_folder/exceptionrules-privacy-friendly.txt"
		} > '/home/zz_repositories/xjdhdr-random-code/Adblock/Acceptable_Ads_-_no_Third_Party_Tracking_-_no_Google_or_Taboola.txt'

		for file in /home/zz_repositories/xjdhdr-random-code/Adblock/Acceptable_Ads_-_no_Third_Party_Tracking_-_*
		do
			# Delete duplicate lines except comments
			awk '/^!/ || !a[$0]++' "$file" > "$file-cleaned.txt"
			mv -f "$file-cleaned.txt" "$file"
			recode -f ..utf8 "$file"
			python '/home/addChecksum.py' < "$file" > "$file-checked.txt"
			mv -f "$file-checked.txt" "$file"
			CommandExitCode=$(python '/home/validateChecksum.py' < "$file")$?
			if [ "$CommandExitCode" != 'Checksum is valid0' ]
			then
				errors+='Errors encountered during checksum validation of '"$file"':'
				errors+=' Error:'"$CommandExitCode"'\n'
			fi
			CommandExitCode=0
		done
		CommandExitCode=0
		rm -f "$HOME/working_folder/exceptionrules-privacy-friendly.txt"
	else
		errors+='Could not download exceptionrules.txt: Error:'"$CommandExitCode"'\n'
	fi


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
	mv -f -- "$HOME/working_folder/blocklist.txt.gz" "/home/zz_repositories/xjdhdr-random-code/torrent-mega-blocklist/blocklist.p2p.gz"


	# Commit changes
	#   SourceForge
	sshpass -f "$HOME/sourceforge_password.txt" rsync -qcruz -e ssh --exclude=.svn '/home/zz_repositories/xjdhdr-random-code/' \
		'xjdhdr@frs.sourceforge.net:/home/frs/project/xjdhdr-random-code/'

	#   GitHub, GitLab and Bitbucket
	sNewFiles=$(svn status '/home/zz_repositories/xjdhdr-random-code/' | awk '{if ($1 == "?") print $2 }')
	if [[ $sNewFiles != "" ]]
	then
		printf '%s' "$sNewFiles" | xargs svn add
	fi
	sshpass -f "$HOME/github_password.txt" svn commit --username=XJDHDR --no-auth-cache --force-interactive \
		-m 'Automatic update of Adblock, Bash + blocklist files' '/home/zz_repositories/xjdhdr-random-code'
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

