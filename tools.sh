#!/bin/sh

echo "######### Base tools installation #########"

echo "starting !"

yay -Syu lxsession nwg-look wlr-randr thunar gvfs tumbler ffmpegthumbnailer flatpak wofi gnome-keyring gnome-disk-utility ntfs-3g pavucontrol linux-zen-headers alacritty grimshot wpaperd

echo "######### qtile configurations files intall #########"

sudo rm -rf ~/.config/qtile/

git clone https://github.com/TheCyberArcher/qtile-wayland.git ~/.qtile-dotfiles
sudo mv ~/.qtile-dotfiles/autostart.sh ~/.config/qtile/
sudo mv ~/.qtile-dotfiles/config.py ~/.config/qtile/
sudo mv ~/.qtile-dotfiles/assets/ ~/.config/qtile/
sudo mv ~/.qtile-dotfiles/wofi/  ~/.config/wofi/

rm -rf ~/.qtile-dotfiles/

echo "######### Theme Installation #########"

git clone https://github.com/cbrnix/Flatery.git ~/.Flatery
cd ~/.Flatery
bash ./install.sh
rm -rf ~/.Flatery

sleep 3

echo "done ! ... restarting"
