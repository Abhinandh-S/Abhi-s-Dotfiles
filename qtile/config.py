##########################################
################ IMPORT ##################
##########################################

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import subprocess
from libqtile import hook
import subprocess
import os
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration


##########################################
############## AUTO START ################
##########################################

@hook.subscribe.startup_once
def autostart():
    #  subprocess.Popen(["nitrogen","--restore"])
    subprocess.Popen(['~/Downloads/notifyDT.sh',"$HOME/abhis-expiriment/notify.log"])
    subprocess.Popen(["dunst"])
    subprocess.Popen(["pulseaudio --start"])
    subprocess.Popen(["emacs --daemon"])

    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

##########################################
############# KEY BINDINGS ###############
##########################################

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
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window",),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    ####################################################
    ################# MY KEYBINDINGS ###################
    ####################################################   
    Key([mod],"a", lazy.window.keep_above()),
    Key([mod],"b", lazy.window.keep_below()),
    Key([mod],"m", lazy.spawn("telegram-desktop")),
    Key([mod],"e", lazy.spawn("emacs")),
    Key([mod],"f", lazy.spawn("firefox")),
    Key([mod],"v", lazy.spawn("vivaldi-snapshot")),
    Key([mod],"d", lazy.spawn("sh -c ~/.config/rofi/launchers/type-6/launcher.sh")),
    Key([mod, "control"],"y", lazy.spawn("sh -c ~/.config/rofi/powermenu/type-3/powermenu.sh")),
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
        layout.MonadTall(
         border_width=2,
         border_focus='#666666',
         ),

    layout.Columns(
        border_width=2,
        border_focus='#666666',
        ),
    #layout.Max(),
    #Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
     #layout.Matrix(),
          #layout.MonadWide(),
     layout.RatioTile(),
     #layout.Tile(),
     #layout.TreeTab(),
     #layout.VerticalTile(),
     # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono-Medium",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
##############################################
############# Qtile Extras ##################
##############################################

w = "#ffffff"
bg = "background"

powerline = {
    "decorations": [
        PowerLineDecoration(
            path='forward_slash',
            )
    ]
}

decoration_group = {
    "decorations": [
        RectDecoration(colour="#707070", radius=10, filled=True, padding_y=4, group= False,)
    ],
    "padding":10,
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    margin_y = 3,
                    margin_x = 0,
                    padding_y =5,
                    padding_x = 3,
                    borderwidth = 3,
                    this_current_screen_border = w,
                    highlight_method='line',
                    active=w,
                    ),
                widget.TextBox(
        text=" ",
                    background='#000000',
                    **powerline,
                    ),

                widget.Systray(
                        **powerline,
                        background='#292929',
                        icon_size=13,
                         ),

                widget.Prompt(
                    ),
                widget.WindowName(
                    max_chars=80,
                    ),
                widget.Chord(
                    chords_colors={"launch": ("#ff0000", "#ffffff"), }, 
                    name_transform=lambda name: name.upper(), ),
                                widget.Spacer(
                    length=800,
                    ),
                                widget.Spacer(length = 12),

                widget.TextBox(
                    text="󰤨 ",
                    foreground=w,
                    fontsize=15,
                                      ),
                widget.Net(
                    format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                    foreground=w,
                                    ),

                widget.NetGraph(
                        type='line',
                        line_width=1,
                        bandwidth_type='down',
                        border_color = '#000000',
                        graph_color=w,
                       
                        ),
 widget.Spacer(length = 6),

widget.Sep(
        linewidth=1,
        ),

    widget.Memory(),
    widget.Spacer(length = 6),

    widget.Sep(
            linewidth=1,
            ),

widget.Spacer(length = 6),

widget.Clock(format="%Y-%m-%d %a %I:%M %p",),
widget.Spacer(length = 6),

widget.Sep(
        linewidth=1,
        ),
widget.Spacer(length = 6),

widget.TextBox(
        text="Volume:",
                    foreground=w,
                    fontsize=13,
                                        ),

widget.PulseVolume(
        emoji_list=['󰝟', '󰕿', '󰖀', '󰕾'],
        ),
widget.Spacer(length = 6),
widget.Sep(
        linewidth=1,
        ),
widget.Spacer(length = 12),

widget.WidgetBox(
        close_button_location='right',
        text_open='',
        text_closed='',
        fontsize=18,
        widgets=[
            widget.WidgetBox(
        close_button_location='right',
        text_open='' ,
        text_closed='' ,
        fontsize=15,
        widgets=[
widget.Wallpaper(
        directory='~/Pictures/wallpaper/',
        random_selection=True,
        wallpaper_command=['feh', '--bg-fill'],
               ),
    ]
),


    ]
),
widget.Spacer(length = 12),




    widget.QuickExit(default_text='', countdown_format='[{}]',background='#000000',),
widget.Spacer(length = 12),
            ],
            28,
        ),
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
# focus, should we respect this or not?
auto_minimize = True
wl_input_rules = None
wmname = "Qtile"
