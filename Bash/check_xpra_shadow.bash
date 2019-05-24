#!/bin/bash

PATH=$PATH:$(sed -n '/PATH=/s/^.*=// ; s/\"//gp' '/etc/environment')


if [[ "$(xpra list)" != 'LIVE session at :0' ]]
then
	xpra shadow :0 --html=off --file-transfer=no --printing=no --pulseaudio=no --notifications=no --system-tray=no --cursors=no --bell=no --remote-logging=no --speaker=disabled --microphone=disabled --av-sync=no --encodings=rgb --encoding=rgb --compression_level=1
	return 1
fi

if [[ "$(pgrep firefox)" == '' ]]
then
	firefox >/dev/null 2>/dev/null &
	return 1
fi

return 0
