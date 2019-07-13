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
	git -C '/home/git/git_wikis/' --git-dir='/home/git/git_wikis/.git' fetch --prune-tags github-fetch master >'/tmp/stdout_collection.txt' 2>&1 \
		|| cat '/tmp/stdout_collection.txt' 1>&2
	rm '/tmp/stdout_collection.txt'
	git -C '/home/git/git_wikis/' --git-dir='/home/git/git_wikis/.git' fetch --prune-tags bitbucket-fetch master >'/tmp/stdout_collection.txt' 2>&1 \
		|| cat '/tmp/stdout_collection.txt' 1>&2
	rm '/tmp/stdout_collection.txt'
	git -C '/home/git/git_wikis/' --git-dir='/home/git/git_wikis/.git' fetch --prune-tags gitlab-fetch master >'/tmp/stdout_collection.txt' 2>&1 \
		|| cat '/tmp/stdout_collection.txt' 1>&2
	rm '/tmp/stdout_collection.txt'

	git -C '/home/git/git_wikis/' --git-dir='/home/git/git_wikis/.git' diff --name-only master github/master >"$HOME/github_wiki_changes.txt"
	git -C '/home/git/git_wikis/' --git-dir='/home/git/git_wikis/.git' diff --name-only master bitbucket/master >"$HOME/bitbucket_wiki_changes.txt"
	git -C '/home/git/git_wikis/' --git-dir='/home/git/git_wikis/.git' diff --name-only master gitlab/master >"$HOME/gitlab_wiki_changes.txt"

	git -C '/home/git/git_wikis/' --git-dir='/home/git/git_wikis/.git' merge --no-edit --no-log master github/master >'/dev/null'
	git -C '/home/git/git_wikis/' --git-dir='/home/git/git_wikis/.git' merge --no-edit --no-log master bitbucket/master >'/dev/null'
	git -C '/home/git/git_wikis/' --git-dir='/home/git/git_wikis/.git' merge --no-edit --no-log master gitlab/master >'/dev/null'

	sshpass -f "$HOME/github_password.txt" -P "$HOME/.ssh/github_ed25519" \
		git -C '/home/git/git_wikis/' --git-dir='/home/git/git_wikis/.git' push github master >'/tmp/stdout_collection.txt' 2>&1 \
			|| cat '/tmp/stdout_collection.txt' 1>&2
	rm '/tmp/stdout_collection.txt'
	sshpass -f "$HOME/bitbucket_password.txt" -P "$HOME/.ssh/bitbucket_ed25519" \
		git -C '/home/git/git_wikis/' --git-dir='/home/git/git_wikis/.git' push bitbucket master >'/tmp/stdout_collection.txt' 2>&1 \
			|| cat '/tmp/stdout_collection.txt' 1>&2
	rm '/tmp/stdout_collection.txt'
	sshpass -f "$HOME/gitlab_password.txt" -P "$HOME/.ssh/gitlab_ed25519" \
		git -C '/home/git/git_wikis/' --git-dir='/home/git/git_wikis/.git' push gitlab master >'/tmp/stdout_collection.txt' 2>&1 \
			|| cat '/tmp/stdout_collection.txt' 1>&2
	rm '/tmp/stdout_collection.txt'

	sFilesEdited_GitHub_wiki=$(cat "$HOME/github_wiki_changes.txt")
	sFilesEdited_Bitbucket_wiki=$(cat "$HOME/bitbucket_wiki_changes.txt")
	sFilesEdited_GitLab_wiki=$(cat "$HOME/gitlab_wiki_changes.txt")

	grep --fixed-strings --line-regexp -f "$HOME/github_wiki_changes.txt" "$HOME/bitbucket_wiki_changes.txt" >"$HOME/matching_lines.txt"
	grep --fixed-strings --line-regexp -f "$HOME/github_wiki_changes.txt" "$HOME/gitlab_wiki_changes.txt" >>"$HOME/matching_lines.txt"
	grep --fixed-strings --line-regexp -f "$HOME/bitbucket_wiki_changes.txt" "$HOME/gitlab_wiki_changes.txt" >>"$HOME/matching_lines.txt"
	if [ -f "$HOME/matching_lines.txt" ]
	then
		sMergeConflicts+=$(cat "$HOME/matching_lines.txt")
		rm -f "$HOME/matching_lines.txt"
	fi

	rm -f "$HOME/github_wiki_changes.txt"
	rm -f "$HOME/bitbucket_wiki_changes.txt"
	rm -f "$HOME/gitlab_wiki_changes.txt"
} 2> '/tmp/stderr-contents-sync_git_repositories.txt'

if [ -f '/tmp/stderr-contents-sync_git_repositories.txt' ]
then
	sErrors+=$(cat '/tmp/stderr-contents-sync_git_repositories.txt')
	rm -f '/tmp/stderr-contents-sync_git_repositories.txt'
fi

if [ "$(du -bs /home/git/git_wikis | cut -f1)" -gt 1932735283 ]       # If more than 1.8GB
then
	sErrors+=$(printf '/home/git/git_wikis is more than 1.8GB in size')
fi


# If something will be added to email file, add the date.
if [[ -n "$sErrors" ]] || [[ -n "$sMergeConflicts" ]] || [[ -n "$sFilesEdited_GitHub_wiki" ]] || [[ -n "$sFilesEdited_GitLab_wiki" ]] || [[ -n "$sFilesEdited_Bitbucket_wiki" ]]
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
