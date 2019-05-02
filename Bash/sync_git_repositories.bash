#!/bin/bash


PS4='$LINENO: '
PATH=$PATH:$(sed -n '/PATH=/s/^.*=// ; s/\"//gp' '/etc/environment')



