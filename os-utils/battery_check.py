# -*- coding: utf-8 -*-
''' Battery check
    21/10/2015 (felix) Script to check battery status and launch a sound warning
    22/06/2021 (felix) Last modified, setting the volume param
    
    At the crontab set:
    
        */5 * * * * python3.7 /path/of/the/battery_check.py
'''
import os, subprocess

dir_sounds = "/usr/share/sounds/gnome/default/alerts/"
file_sound = os.path.join(dir_sounds, 'glass.ogg')
acpi_tool = subprocess.check_output('/usr/bin/acpitool -b', shell=True)
mplayer_cmd = '/usr/bin/mplayer -vo fbdev2 -volume 120'

if acpi_tool:
    acpi_result = str(acpi_tool).split(',')
    percent = int(acpi_result[1].strip().split('.')[0])
    status = acpi_result[0].strip()
    if percent <= 15 and 'Discharging' in status:
        for i in range(0, 12):
            os.system('%s %s' % (mplayer_cmd, file_sound))
