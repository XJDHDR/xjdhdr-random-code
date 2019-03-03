#!/bin/bash

PATH=$PATH:$(sed -n '/PATH=/s/^.*=// ; s/\"//gp' '/etc/environment')


if wget -q --spider --max-redirect 0 --no-cookies http://www.google.com/
then
	exit 0
else
	exit 1
fi
