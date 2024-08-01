#!/bin/sh

echo "######### Base tools installation #########"

echo "starting !"

yay -Syu lxsession nwg-look wlr-randr firewalld thunar gvfs tumbler ffmpegthumbnailer flatpak wofi nm-applet gnome-keyring gnome-disk-utility ntfs-3g pavucontrol linux-zen-headers alacrittygrimshot

echo "######### Network configuration #########"

nmcli con mod "Connexion filaire 1" ipv4.ignore-auto-dns yes
nmcli con mod "Connexion filaire 1" ipv4.dns "45.90.28.250 45.90.30.250 9.9.9.9 149.112.112.112 1.1.1.1"

systemctl enable firewalld
systemctl start firewalld
firewall-cmd --set-default-zone=block

echo "######### qtile configurations files intall #########"

sudo rm -rf ~/.config/qtile/
git clone https://github.com/TheCyberArcher/qtile-wayland.git ~/.qtile-dotfiles
sudo mv ~/.qtile-dotfiles/autostart.sh ~/.config/qtile/
sudo mv ~/.qtile-dotfiles/config.py ~/.config/qtile/
sudo mv ~/.qtile-dotfiles/assets/ ~/.config/qtile/
rm -rf ~/.qtile-dotfiles/

echo "######### Theme Installation #########"

git clone https://github.com/cbrnix/Flatery.git ~/.Flatery
cd ~/.Flatery
bash ./install.sh
rm -rf ~/.Flatery

sleep 3

echo "done ! ... restarting"
