#!/bin/bash

notify-send "$(date '+%B %d %Y - %R')" "Battery:$(acpi -V | head -n 1 | cut -d ',' -f 2)"
