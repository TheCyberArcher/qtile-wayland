###############################################################################################################################################
##                                                                                                                                           ##
## ,--------.,--.  ,--.,------.     ,-----.,--.   ,--.,-----.  ,------.,------.       ,---.  ,------.  ,-----.,--.  ,--.,------.,------.     ##
## '--.  .--'|  '--'  ||  .---'    '  .--./ \  `.'  / |  |) /_ |  .---'|  .--. '     /  O  \ |  .--. ''  .--./|  '--'  ||  .---'|  .--. '    ##
##    |  |   |  .--.  ||  `--,     |  |      '.    /  |  .-.  \|  `--, |  '--'.'    |  .-.  ||  '--'.'|  |    |  .--.  ||  `--, |  '--'.'    ##
##    |  |   |  |  |  ||  `---.    '  '--'\    |  |   |  '--' /|  `---.|  |\  \     |  | |  ||  |\  \ '  '--'\|  |  |  ||  `---.|  |\  \     ##
##    `--'   `--'  `--'`------'     `-----'    `--'   `------' `------'`--' '--'    `--' `--'`--' '--' `-----'`--'  `--'`------'`--' '--'    ##
##                                                                                                                                           ##
###############################################################################################################################################                                                                                          
                
#░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░       $$$$$$\    $$\     $$\ $$\  
#░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░      $$  __$$\   $$ |    \__|$$ |
#░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌      $$ /  $$ |$$$$$$\   $$\ $$ | $$$$$$\
#░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░      $$ |  $$ |\_$$  _|  $$ |$$ |$$  __$$\ 
#░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░      $$ |  $$ |  $$ |    $$ |$$ |$$$$$$$$ |
#▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░      $$ $$\$$ |  $$ |$$\ $$ |$$ |$$   ____|
#▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░      \$$$$$$ /   \$$$$  |$$ |$$ |\$$$$$$$\
#░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄       \___$$$\    \____/ \__|\__| \_______|      --- Ma super Ultra configuration Script pour Le Archlinux BTW ---
#░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒           \___|
#▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒     

                                                
######################################
# Python lib
######################################


from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
from qtile_extras import widget as extrawidgets
import subprocess
import os


qtile.core.cmd_set_keymap(layout="fr") ### comment this line for X11 and use setxkbmap

######################################
# Master key
######################################


mod = "mod4"
terminal = guess_terminal()


######################################
# Global Layout
######################################


layouts = [
    layout.Columns(border_focus=["#8A2BE2", "8A2BE2", "#8A2BE2", "8A2BE2"], border_width=6, num_columns=2, margin=8),
    layout.Max(),
    ]


######################################
# Setup Widget Defaults
######################################


widget_defaults = dict(
    font="sans bold",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()


######################################
# Top-bar
######################################


screens = [
    Screen(

),
]


######################################
# Base Keyboard shortcut
######################################


keys = [


    Key([mod], "LEFT", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "RIGHT", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "DOWN", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "UP", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),


    Key([mod, "shift"], "LEFT", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "RIGHT", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "DOWN", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "UP", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "LEFT", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "RIGHT", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "DOWN", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "UP", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod, "mod1"], "LEFT", lazy.layout.swap_column_left(),desc="Move column to the left"),
    Key([mod, "mod1"], "RIGHT", lazy.layout.swap_column_right(),desc="Move column to the right"),

    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
 


######################################
# Custom Keyboard shortcut
######################################


    Key([mod], "r", lazy.spawn("wofi --show drun"), desc="wofi"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("ddcutil --bus=6 setvcp 10 - 10")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("ddcutil --bus=6 setvcp 10 + 10")),
    Key([mod], "i", lazy.spawn("grimshot --notify copy area"), desc="screenshot"),
    Key([mod], "z", lazy.screen.next_group()),
    Key([mod], "a", lazy.screen.prev_group()),

]

######################################
# Mouse
######################################


mouse = [

    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),

    ### uncomment to control workspace switch with mouse scrolling ###

    #Click([mod], "Button4", lazy.screen.next_group()), 
    #Click([mod], "Button5", lazy.screen.prev_group()), 

]


######################################
# Autostart scripts
######################################


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

######################################
# OTHER
######################################



dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)



auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None


wmname = "Qtile-wayland"


######################################
# Groups
######################################


groups = [

    Group(name="1", screen_affinity=0),
    Group(name="2", screen_affinity=0),
    Group(name="3", screen_affinity=0),
    Group(name="4", screen_affinity=0),

    

### Uncomment for secondary vertical  screen usage : 

# VERTICAL SCREEN WORKSPACE :  Group(name="q", screen_affinity=1, layouts=[layout.VerticalTile(border_focus=["#8A2BE2", "000000", "#8A2BE2", "000000"], border_width=6, margin=10),]),

]


for i in groups :
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
          
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )
