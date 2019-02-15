#!/bin/bash
until python2 /home/pi/Aminiok/Main.py ;do
	echo "'Main.py' crashed with exit code $?. Restarting ..." >&2
	sleep 1
done
