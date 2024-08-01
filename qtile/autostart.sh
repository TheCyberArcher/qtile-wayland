#!/bin/sh
#Application Startup Script - Qtile 

wlr-randr --output DP-3 --mode 3440x1440@144 $
exec lxsession $
nm-applet $
signal-desktop --use-tray-icon --start-in-tray --no-sandbox %U &
flatpak run --branch=stable --arch=x86_64 --command=whatsapp-desktop-linux io.github.mimbrero.WhatsAppDesktop --start-hidden &
webcord --start-minimized $
protonmail-bridge --no-window &
steam -silent &