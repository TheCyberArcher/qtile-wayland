#!/bin/sh

echo "qtile base wayland install"

yay -Syu qtile qtile-extras python-pywlroots wlroots python-dbus-next xdg-desktop-portal-wlr xdg-desktop-portal xdg-desktop-portal-gtk xorg-xwayland sddm cava dunst

sudo systemctl enable sddm.service

sleep 3

echo "done ! ... restarting"

reboot
