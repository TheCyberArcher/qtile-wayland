# Qtile-Wayland

<br />

> This setup is an adaptation to run the qtile windows manager under wayland and get a full desktop experience. It is a variation of my original setup in the qtile-x11 folder here. Some packages are needed to run older applications with the wayland compositor, with partial support. Minor bugs are present for now, but the desktop is fully usable in daily use.

> The bar used is the original qtile one, reworked to be more aesthetic and to integrate well into the modern theme. The file manager is thunar and the application launcher is wofi.

### Base packages 

- [qtile](https://archlinux.org/packages/extra/x86_64/qtile/) (base package for Qtile TWM)
- [qtile-extras](https://aur.archlinux.org/packages/qtile-extras) (add more features and widget)
- [python-wlroots](https://archlinux.org/packages/extra/x86_64/python-pywlroots/) (python wayland)
- [wlroots](https://archlinux.org/packages/extra/x86_64/wlroots/) (wayland compositor library)
- [python-dbus-next](https://archlinux.org/packages/extra/any/python-dbus-next/) (Python library for DBus)
- [xdg-desktop-portal-wlr](https://archlinux.org/packages/extra/x86_64/xdg-desktop-portal-wlr/) (xdg-desktop-portal backend for wlroots)
- [xdg-desktop-portal](https://archlinux.org/packages/extra/x86_64/xdg-desktop-portal/) (exposes D-Bus interfaces for file access, opening URIs, printing and more)
- [xdg-desktop-portal-gtk](https://archlinux.org/packages/extra/x86_64/xdg-desktop-portal-gtk/) (xdg-desktop backward compatibility)
- [xorg-xwayland](https://archlinux.org/packages/extra/x86_64/xorg-xwayland/) (run X clients under wayland, X11 app compatibility)
- [sddm](https://archlinux.org/packages/extra/x86_64/sddm/) (graphical login program and session manager)
- [cava](https://aur.archlinux.org/packages/cava) (Console-based Audio Visualizer for Alsa)
- [wofi](https://archlinux.org/packages/extra/x86_64/wofi/) (rofi inspired application launcher for wlroots compositors)

### Required tools

- [lxsession](https://archlinux.org/packages/extra/x86_64/lxsession-gtk3/) (provide polkit agent and user session)
- [nwg-look](https://archlinux.org/packages/extra/x86_64/nwg-look/) (wayland apparence editor)
- [wlr-randr](https://archlinux.org/packages/extra/x86_64/wlr-randr/) (xrandr equivalent for wayland - to set the screen resolution)
- [firewalld](https://archlinux.org/packages/extra/any/firewalld/) (best firewall for linux)
- [thunar](https://archlinux.org/packages/extra/x86_64/thunar/) (filemanager)
- [gvfs](https://archlinux.org/packages/extra/x86_64/gvfs/) (required by thunar)
- [tumbler](https://archlinux.org/packages/extra/x86_64/tumbler/) (required by thunar)
- [ffmpegthumbnailer](https://archlinux.org/packages/extra/x86_64/ffmpegthumbnailer/) (required by thunar)
- [flatpak](https://archlinux.org/packages/extra/x86_64/flatpak/) (flatpak application support)
- [nm-applet](https://man.archlinux.org/man/nm-applet.1.en) (networkmanager tray support - required for some apps)
- [gnome-keyring](https://archlinux.org/packages/extra/x86_64/gnome-keyring/) (keyring support - required for some apps)
- [gnome-disk-utility](https://archlinux.org/packages/extra/x86_64/gnome-disk-utility/) (drive management GUI)
- [ntfs-3g](https://archlinux.org/packages/extra/x86_64/ntfs-3g/) (ntfs support for gnome-disk)
- [pavucontrol](https://archlinux.org/packages/extra/x86_64/pavucontrol/) (volume Mixer - require pipewire-pulse)
- [linux-zen-headers](https://archlinux.org/packages/extra/x86_64/linux-zen-headers/) (headers for zen-kernel - required for some apps)
- [alacritty](https://archlinux.org/packages/extra/x86_64/alacritty/) (terminal emulator)
