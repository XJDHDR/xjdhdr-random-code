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
	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' fetch --prune-tags github-fetch master >'/dev/null'
	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' diff --name-only master github-fetch/master >'/home/git_user/github_wiki_changes.txt'

	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' fetch --prune-tags bitbucket-fetch master >'/dev/null'
	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' diff --name-only master bitbucket-fetch/master >'/home/git_user/bitbucket_wiki_changes.txt'

	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' fetch --prune-tags gitlab-fetch master >'/dev/null'
	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' diff --name-only master gitlab-fetch/master >'/home/git_user/gitlab_wiki_changes.txt'

	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' merge --no-edit --no-log master github-fetch/master >'/dev/null'
	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' merge --no-edit --no-log master bitbucket-fetch/master >'/dev/null'
	git -C '/home/git/gitlab_wiki/' --git-dir='/home/git/gitlab_wiki/.git' merge --no-edit --no-log master gitlab-fetch/master >'/dev/null'

#	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' add --all
	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' push github master
	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' push bitbucket master
	git -C '/home/git/github_wiki/' --git-dir='/home/git/github_wiki/.git' push gitlab master

	sFilesEdited_GitHub_wiki=$(cat '/home/git_user/github_wiki_changes.txt')
	sFilesEdited_Bitbucket_wiki=$(cat '/home/git_user/bitbucket_wiki_changes.txt')
	sFilesEdited_GitLab_wiki=$(cat '/home/git_user/gitlab_wiki_changes.txt')

	grep --fixed-strings --line-regexp -f '/home/git_user/github_wiki_changes.txt' '/home/git_user/bitbucket_wiki_changes.txt' >'/home/git_user/matching_lines.txt'
	grep --fixed-strings --line-regexp -f '/home/git_user/github_wiki_changes.txt' '/home/git_user/gitlab_wiki_changes.txt' >'/home/git_user/matching_lines.txt'
	grep --fixed-strings --line-regexp -f '/home/git_user/bitbucket_wiki_changes.txt' '/home/git_user/gitlab_wiki_changes.txt' >'/home/git_user/matching_lines.txt'
	if [ -f '/home/git_user/matching_lines.txt' ]
	then
		sMergeConflicts+=$(cat '/home/git_user/matching_lines.txt')
		rm -f '/home/git_user/matching_lines.txt'
	fi

	rm -f '/home/git_user/github_wiki_changes.txt'
	rm -f '/home/git_user/bitbucket_wiki_changes.txt'
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
	printf 'The following files were edited in two or more wikis simultaneously. Check for merge conflicts:\n%s\n\n' "$sMergeConflicts" >> '/home/error_reports_to_email.txt'
fi

if [[ -n "$sFilesEdited_GitHub_wiki" ]]
then
	printf 'The following pages were edited on the GitHub wiki:\n%s\n\n' "$sFilesEdited_GitHub_wiki" >> '/home/error_reports_to_email.txt'
fi

if [[ -n "$sFilesEdited_Bitbucket_wiki" ]]
then
	printf 'The following pages were edited on the Bitbucket wiki:\n%s\n\n' "$sFilesEdited_Bitbucket_wiki" >> '/home/error_reports_to_email.txt'
fi

if [[ -n "$sFilesEdited_GitLab_wiki" ]]
then
	printf 'The following pages were edited on the GitLab wiki:\n%s\n\n' "$sFilesEdited_GitLab_wiki" >> '/home/error_reports_to_email.txt'
fi

exit 0
