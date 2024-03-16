######################################
######## IPORTING LIBRARIES ##########
######################################

import os
import subprocess
from libqtile import bar, extension, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget import StatusNotifier
import colors
from libqtile.utils import guess_terminal
from qtile_extras.widget.decorations import PowerLineDecoration

##########################################
############## AUTO START ################
##########################################

# wallpaper settings

from libqtile import hook
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(["nitrogen","--restore"])

@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(['~/Downloads/notifyDT.sh',"$HOME/abhis-expiriment/notify.log"])


@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(["dunst"])
    subprocess.Popen(["pulseaudio --start"])


import os
import subprocess

from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

########################################################
#################### KEY BINDINGS ######################
########################################################

mod = "mod4"
terminal = guess_terminal()


keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Key([mod,"shift"],"Escape", lazy.spawn("rofi -show launcher -modi launcher:~/.config/rofi/launchers/type-6/launcher.sh: ")),

    # my keys
    Key([mod],"e", lazy.spawn("emacs")),
    Key([mod],"f", lazy.spawn("firefox")),
    Key([mod],"v", lazy.spawn("vivaldi-snapshot")),

i
    ##########################################

    Key([mod],"d", lazy.spawn("sh -c ~/.config/rofi/launchers/type-6/launcher.sh")),
    Key([mod, "control"],"y", lazy.spawn("sh -c ~/.config/rofi/powermenu/type-3/powermenu.sh")),

    Key([mod, "shift"],"Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
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
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_width=3,
        border_focus='#cba6f7',
        border_on_single=True,
        margin=3,
        margin_on_single=1,
        ),
    layout.Floating(
        border_width=1,
        border_focus='#cba6f7',
        ),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                #   widget.CurrentLayout(),
                widget.GroupBox(
                    margin_y = 3,
                    margin_x = 0,
                    padding_y =5,
                    padding_x = 3,
                    borderwidth = 3,
                    this_current_screen_border = '#a6e3a1',
                    highlight_method='line',
                    active='#a6e3a1',
                    ),
                widget.Prompt(),
                widgddigggget.WindowName(
                    foreground='#a6e3a1'
                    ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Clipboard(
                    foreground='#eba0ac',
                    timeout=10,
                    ),
widget.Spacer(length = 12),

widget.TextBox(
    text=" ",
    foreground='#f5c2e7',
    fontsize=15,
    decorations=[
                        BorderDecoration(
                            colour = '#f5c2e7',
                            border_width = [0, 0, 2, 0],
                            )
                        ]

    ),


                widget.OpenWeather(
                    location='Ponkunnam',
                    foreground='#f5c2e7',
                    decorations=[
                        BorderDecoration(
                            colour = '#f5c2e7',
                            border_width = [0, 0, 2, 0],
                            )
                        ]

                    ),
widget.Spacer(length = 12),


iwidget.TextBox(
    text="󰘚 ",
    foreground='#74c7ec',
    fontsize=15,
    decorations=[
                        BorderDecoration(
                            colour = '#74c7ec',
                            border_width = [0, 0, 2, 0],
                            )
                        ]

    ),
                widget.Memory(
                    foreground='#74c7ec',
                    decorations=[
                        BorderDecoration(
                            colour = '#74c7ec',
                            border_width = [0, 0, 2, 0],
                            )
                        ]
                    ),
widget.Spacer(length = 12),

widget.TextBox(
        text="󰤨 ",
        foreground='#fff6b3',
        fontsize=15,
        decorations=[
                        BorderDecoration(
                            colour = '#fff6b3',
                            border_width = [0, 0, 2, 0],
                            )
                        ]

        ),
                widget.Net(
                    format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                    foreground='#fff6b3',
                    decorations=[
                        BorderDecoration(
                            colour = '#fff6b3',
                            border_width = [0, 0, 2, 0],
                            )
                        ]

                    ),

                widget.NetGraph(
                        type='line',
                        line_width=1,
                        bandwidth_type='down',
                        border_color = '#000000',
                        graph_color='#fff6b3',
                        decorations=[
                        BorderDecoration(
                            colour = '#fff6b3',
                            border_width = [0, 0, 2, 0],
                            )
                        ]

                        ),


widget.Spacer(length = 12),

widget.TextBox(
    text="󱑂 ",
    foreground='#cba6f7',

    fontsize=15,
    decorations=[
                        BorderDecoration(
                            colour = '#cba6f7',
                            border_width = [0, 0, 2, 0],
                            )
                        ]

    ),

widget.Clock(format="%A,  %B %d - %I:%M %p",
                             foreground='#cba6f7',
                             decorations=[
                        BorderDecoration(
                            colour = '#cba6f7',
                            border_width = [0, 0, 2, 0],
                            )
                        ]

                             ),
                widget.Spacer(length = 12),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

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

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "Qtile"
