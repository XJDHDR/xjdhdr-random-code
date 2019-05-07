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

{
	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' fetch --prune-tags >'/dev/null'
	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' diff master origin/master --name-only >'/home/git_user/github_wiki_changes.txt'
	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' pull --no-edit --no-log --strategy-option=theirs >'/dev/null'

	git -C '/home/git/gitlab_wiki/' --git-dir='/home/git/gitlab_wiki/.git' fetch --prune-tags >'/dev/null'
	git -C '/home/git/gitlab_wiki/' --git-dir='/home/git/gitlab_wiki/.git' diff master origin/master --name-only >'/home/git_user/gitlab_wiki_changes.txt'
	git -C '/home/git/gitlab_wiki/' --git-dir='/home/git/gitlab_wiki/.git' pull --no-edit --no-log --strategy-option=theirs >'/dev/null'

	unison -silent -batch -times -ignore "Name .git" '/home/git/github_wiki' '/home/git/gitlab_wiki'

	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' add --all
	git -C '/home/git/gitlab_wiki/' --git-dir='/home/git/gitlab_wiki/.git' add --all
	if ! git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' diff-index --quiet HEAD --
	then
		git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' commit --all --message='Automated sync with GitLab wiki' --quiet
		sshpass -f "$HOME/github_password.txt" -P "nter passphrase for key" git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' push origin/master master
	fi
	if ! git -C '/home/git/github_wiki/' --git-dir='/home/git/gitlab_wiki/.git' diff-index --quiet HEAD --
	then
		git -C '/home/git/gitlab_wiki/' --git-dir='/home/git/gitlab_wiki/.git' commit --all --message='Automated sync with GitHub wiki' --quiet
		sshpass -f "$HOME/gitlab_password.txt" -P "nter passphrase for key" git -C '/home/git/gitlab_wiki/' --git-dir='/home/git/gitlab_wiki/.git' push origin/master master
	fi

	sFilesEdited_GitHub_wiki=$(cat '/home/git_user/github_wiki_changes.txt')
	sFilesEdited_GitLab_wiki=$(cat '/home/git_user/gitlab_wiki_changes.txt')

	grep --fixed-strings --line-regexp -f '/home/git_user/github_wiki_changes.txt' '/home/git_user/gitlab_wiki_changes.txt' >'/home/git_user/matching_lines.txt'
	if [ -f '/home/git_user/matching_lines.txt' ]
	then
		sMergeConflicts+=$(cat '/home/git_user/matching_lines.txt')
		rm -f '/home/git_user/matching_lines.txt'
	fi

	rm -f '/home/git_user/github_wiki_changes.txt'
	rm -f '/home/git_user/gitlab_wiki_changes.txt'
} 2> '/tmp/stderr-contents-sync_git_repositories.txt'

if [ -f '/tmp/stderr-contents-sync_git_repositories.txt' ]
then
	sErrors+=$(cat '/tmp/stderr-contents-auto_update_svn.txt')
	rm -f '/tmp/stderr-contents-sync_git_repositories.txt'
fi

if [ "$(du -bs /home/git/github_wiki | cut -f1)" -gt 2147483648 ]	# If more than 2GB
then
	sErrors+=$(printf '/home/git/github_wiki is more than 2GB in size')
fi
if [ "$(du -bs /home/git/gitlab_wiki | cut -f1)" -gt 2147483648 ]	# If more than 2GB
then
	sErrors+=$(printf '/home/git/gitlab_wiki is more than 2GB in size')
fi

if [[ -n "$sErrors" ]] || [[ -n "$sMergeConflicts" ]] || [[ -n "$sFilesEdited_GitHub_wiki" ]] || [[ -n "$sFilesEdited_GitLab_wiki" ]]
then
	sDateTime=$(date -u +"%d %b %Y %H:%M")
	printf 'sync_git_repositories.bash:\n%s UTC\n' "$sDateTime" >> '/home/error_reports_to_email.txt'
fi

if [[ -n "$sErrors" ]]
then
	printf 'Errors reported by script:\n%s\n\n' "$sErrors" >> '/home/error_reports_to_email.txt'
fi

if [[ -n "$sMergeConflicts" ]]
then
	printf 'The following merge conflicts were found:\n%s\n\n' "$sMergeConflicts" >> '/home/error_reports_to_email.txt'
fi

if [[ -n "$sFilesEdited_GitHub_wiki" ]]
then
	printf 'The following pages were edited on the GitHub wiki:\n%s\n\n' "$sFilesEdited_GitHub_wiki" >> '/home/error_reports_to_email.txt'
fi

if [[ -n "$sFilesEdited_GitLab_wiki" ]]
then
	printf 'The following pages were edited on the GitLab wiki:\n%s\n\n' "$sFilesEdited_GitLab_wiki" >> '/home/error_reports_to_email.txt'
fi

exit 0
