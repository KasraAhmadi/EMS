#!/bin/bash
until python3 /home/pi/Kasra/AiClient.py ;do
	echo "'AIClient.py' crashed with exit code $?. Restarting ..." >&2
	sleep 1
done
