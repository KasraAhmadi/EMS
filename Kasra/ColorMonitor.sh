#!/bin/bash
until python3 /home/pi/Kasra/rgb.py;do
	echo "'rgb.py' crashed with exit code $?. Restarting ..." >&2
	sleep 1
done
