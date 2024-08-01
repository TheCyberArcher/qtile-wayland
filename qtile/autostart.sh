#!/bin/sh
#Application Startup Script - Qtile 

wlr-randr --output DP-3 --mode 3440x1440@144 $
exec lxsession $
nm-applet $
protonmail-bridge --no-window &
