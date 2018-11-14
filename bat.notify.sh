#!/bin/bash

while true; do
	actual="$(cat /sys/class/power_supply/BAT0/capacity)"
	if [ "$actual" -le "25" ] && [ "$(cat /sys/class/power_supply/BAT0/status)" = "Discharging" ]
	then
		notify-send --urgency=critical "Low battery!" "Battery: $actual%"
	fi

	sleep 2m
done
