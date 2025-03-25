#!/bin/sh

# Application Startup

wlr-randr --output DP-1 --mode 3840x2160@238 --scale 1.0 --adaptive-sync disabled &
exec lxsession $
protonmail-bridge --no-window &
exec wpaperd -d &

# Discord screensharing patch

export XDG_CURRENT_DESKTOP=qtile &
export XDG_SESSION_TYPE=wayland &
dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=qtile &
systemctl --user stop pipewire wireplumber xdg-desktop-portal xdg-desktop-portal-wlr &
sleep 1
systemctl --user start wireplumber pipewire &
