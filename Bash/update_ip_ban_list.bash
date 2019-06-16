#!/bin/bash


PS4='$LINENO: '
PATH=$PATH:$(sed -n '/PATH=/s/^.*=// ; s/\"//gp' '/etc/environment')


# Test if internet connection present and abort if not
if ! '/bin/bash' '/home/svn/xjdhdr-random-code/Bash/test_connection.bash'
then
	sDateTime=$(date -u +"%d %b %Y %H:%M")
	printf 'test_connection.bash:\n%s UTC\n-  No internet connection detected\n\n' "$sDateTime" \
		>> '/home/error_reports_to_email.txt'
	exit 1
fi

{
	# Download list of IP ranges belonging to Asutralia and China (Google Cloud charges for traffic to these locations)
	CommandExitCode=$(wget -q -O "$HOME/ip_list.txt" -t 10 -c \
		'https://ip.ludost.net/cgi/process?country=1&country_list=au+cn&format_template=prefix&format_name=&format_target=&format_default=')$?
	if [ "$CommandExitCode" -eq 0 ]
	then
		# Delete blank lines and ones containing only spaces and tabs
		sed -i '/^\s*$/d' "$HOME/ip_list.txt"

		# Delete lines starting with a #
		sed -i '/^#/d' "$HOME/ip_list.txt"

		# Test if IP Tables rules exist and delete if they do
		if [[ $(iptables -nvL INPUT 2>/dev/null) =~ 'match-set aus-and-china-ip-range src' ]]
		then
			iptables -D INPUT -m set --match-set aus-and-china-ip-range src -j DROP
		fi
		if [[ $(iptables -nvL OUTPUT 2>/dev/null) =~ 'match-set aus-and-china-ip-range src' ]]
		then
			iptables -D OUTPUT -m set --match-set aus-and-china-ip-range src -j REJECT
		fi

		# Test if IP Set exists and delete it if it does
		if [[ $(ipset -t list aus-and-china-ip-range 2>&1) != *"The set with the given name does not exist"* ]]
		then
			ipset destroy aus-and-china-ip-range
		fi

		# Create IP Set and fill it with IP ranges from downloaded list
		ipset create aus-and-china-ip-range hash:net
		while IFS= read -r sLineContents
		do
			ipset -! add aus-and-china-ip-range "$sLineContents"
		done < "$HOME/ip_list.txt"
		rm -f "$HOME/ip_list.txt"

		# Create rules to block traffic to and from those IPs
		iptables -I INPUT -m set --match-set aus-and-china-ip-range src -j DROP
		iptables -I OUTPUT -m set --match-set aus-and-china-ip-range src -j REJECT
	fi
} 2> '/tmp/stderr-contents-update_ip_ban_list.txt'

if [ -f '/tmp/stderr-contents-update_ip_ban_list.txt' ]
then
	errors+=$(cat '/tmp/stderr-contents-update_ip_ban_list.txt')
	rm -f '/tmp/stderr-contents-update_ip_ban_list.txt'
fi


if [ -n "$errors" ]
then
	sDateTime=$(date -u +"%d %b %Y %H:%M")
	printf 'update_ip_ban_list.bash:\n%s UTC\n'"$errors"'\n\n' "$sDateTime" >> '/home/error_reports_to_email.txt'
fi
