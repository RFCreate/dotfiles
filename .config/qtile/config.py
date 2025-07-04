# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os, random, re, subprocess
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

alt = "mod1"
mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Shuffle/Move focused window
    Key([mod, "shift"], "h", lazy.window.move_floating(dx=-10, dy=0).when(when_floating=True),
        lazy.layout.shuffle_left().when(when_floating=False), desc="Move window left"),
    Key([mod, "shift"], "l", lazy.window.move_floating(dx=10, dy=0).when(when_floating=True),
        lazy.layout.shuffle_right().when(when_floating=False), desc="Move window right"),
    Key([mod, "shift"], "j", lazy.window.move_floating(dx=0, dy=10).when(when_floating=True),
        lazy.layout.shuffle_down().when(when_floating=False), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.window.move_floating(dx=0, dy=-10).when(when_floating=True),
        lazy.layout.shuffle_up().when(when_floating=False), desc="Move window up"),
    # Grow/Resize focused window
    Key([mod, "control"], "h", lazy.window.resize_floating(dw=-10, dh=0).when(when_floating=True),
        lazy.layout.grow_left().when(when_floating=False), desc="Grow window left"),
    Key([mod, "control"], "l", lazy.window.resize_floating(dw=20, dh=0).when(when_floating=True),
        lazy.layout.grow_right().when(when_floating=False), desc="Grow window right"),
    Key([mod, "control"], "j", lazy.window.resize_floating(dw=0, dh=30).when(when_floating=True),
        lazy.layout.grow_down().when(when_floating=False), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.window.resize_floating(dw=0, dh=-10).when(when_floating=True),
        lazy.layout.grow_up().when(when_floating=False), desc="Grow window up"),
    # Change window in focus
    Key([alt], "Tab", lazy.group.next_window(), desc="Focus next window"),
    Key([alt, "shift"], "Tab", lazy.group.prev_window(), desc="Focus previous window"),
    # Change group in focus
    Key([mod], "Tab", lazy.screen.next_group(skip_empty=True, skip_managed=False), desc="Switch to next group"),
    Key([mod, "shift"], "Tab", lazy.screen.prev_group(skip_empty=True, skip_managed=False), desc="Switch to previous group"),
    Key([mod], "0", lazy.screen.toggle_group(), desc="Switch to last group"),
    Key([mod], "Escape", lazy.screen.toggle_group(), desc="Switch to last group"),
    # Change window state
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle window fullscreen"),
    Key([mod], "Up", lazy.window.toggle_floating(), desc="Toggle window floating"),
    Key([mod], "Down", lazy.window.toggle_minimize(), desc="Toggle window minimize"),
    # Close active window
    Key([alt], "F4", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "w", lazy.window.kill(), desc="Kill focused window"),
    # Toggle between different layouts
    Key([mod], "space", lazy.next_layout(), desc="Toggle next layout"),
    Key([mod, "shift"], "space", lazy.prev_layout(), desc="Toggle previous layout"),
    # Grow or shrink tiled windows
    Key([mod], "plus", lazy.layout.grow()),
    Key([mod], "minus", lazy.layout.shrink()),
    Key([mod, "shift"], "plus", lazy.layout.grow_main()),
    Key([mod, "shift"], "minus", lazy.layout.shrink_main()),
    # Change tiled window state
    Key([mod, "shift"], "m", lazy.layout.maximize(), desc="Grow tiled window to max size"),
    Key([mod, "shift"], "n", lazy.layout.normalize(), desc="Reset secondary window sizes"),
    Key([mod, "shift"], "r", lazy.layout.reset(), desc="Reset all window sizes"),
    Key([mod, "shift"], "f", lazy.layout.flip(), desc="Flip main window position"),
    Key([mod, "shift"], "s", lazy.layout.swap_main(), desc="Send window to main"),
    # Open guessed terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between split and unsplit sides of the stack
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle split sides of stack"),
    # Change qtile state
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

keys.extend([
    # Brightness commands
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightness-notify up"), desc="Raise brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightness-notify down"), desc="Lower brightness"),
    # Volume commands
    Key([], "XF86AudioRaiseVolume", lazy.spawn("volume-notify up"), desc="Raise volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("volume-notify down"), desc="Lower volume"),
    Key([], "XF86AudioMute", lazy.spawn("volume-notify mute"), desc="Mute/unmute volume"),
    # Screenshot commands
    Key([], "Print", lazy.spawn("maimpick Select"), desc="Save screenshot of selection"),
    Key(["shift"], "Print", lazy.spawn("maimpick Window"), desc="Save screenshot of window"),
    Key([alt], "Print", lazy.spawn("maimpick Screen"), desc="Save screenshot of screen"),
    Key(["control"], "Print", lazy.spawn("maimpick Copy_Select"), desc="Copy screenshot of selection"),
    Key(["control", "shift"], "Print", lazy.spawn("maimpick Copy_Window"), desc="Copy screenshot of window"),
    Key(["control", alt], "Print", lazy.spawn("maimpick Copy_Screen"), desc="Copy screenshot of screen"),
    # Application commands
    Key(["control", "shift"], "Escape", lazy.spawn("lxterminal -e btop"), desc="Open task manager"),
    Key([mod], "e", lazy.spawn("pcmanfm"), desc="Open file manager"),
    Key([mod], "t", lazy.spawn("lxterminal"), desc="Open terminal"),
    Key([mod], "q", lazy.spawn("rofi -show drun"), desc="Open program launcher"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Open command launcher"),
    Key([mod], "w", lazy.spawn("rofi -show window"), desc="Open window switcher"),
    Key([mod], "v", lazy.spawn("rofi -modi ':greenclip print' -show  -no-show-icons"), desc="Open clipboard history"),
])

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"], f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

# Define workspaces
groups = [
    Group("1", label="󰈹", matches=[Match(wm_class="firefox")]),
    Group("2", label="", matches=[Match(wm_class="lxterminal")]),
    Group("3", label="󰨞", matches=[Match(wm_class=re.compile("code(-oss)?$|codium$"))]),
    Group("4", label="", matches=[Match(wm_class="pcmanfm")]),
    Group("5", label="󰋩", matches=[Match(wm_class=re.compile("imv$|gimp"))]),
    Group("6", label="󰿎", matches=[Match(wm_class=re.compile("mpv$|Shotcut$"))]),
    Group("7", label="󰈙", matches=[Match(wm_class="org.pwmt.zathura")]),
    Group("8", label="", matches=[Match(wm_class="KeePassXC")]),
    Group("9", label="󰏆", matches=[Match(wm_class=re.compile(".*office"))]),
]

# Keys to navigate workspaces
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle=True),
            desc="Switch to group {}".format(i.name)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        Key([mod, alt], i.name, lazy.window.togroup(i.name),
            desc="Move focused window to group {}".format(i.name)),
    ])

layouts = [
    # layout.Columns(),
    layout.Max(),
    # layout.Stack(),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(),
    layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Default values for all widgets
widget_defaults = dict(
    font="monospace",
    fontsize=18,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Default values for bars and specific widgets
bar_defaults = dict(
    size=32,
    background="#2b2b2b",
    border_color="#ffffff",
)
sep_defaults = dict(
    foreground="#bbbbbb",
    padding=18,
)

screens = [
    Screen(
        top=bar.Bar(
            widgets=[
                widget.GroupBox(
                    active="#00ffff",
                    block_highlight_text_color="#ffffff",
                    borderwidth=5,
                    highlight_color="#555555",
                    highlight_method="line",
                    inactive="#888888",
                    this_current_screen_border="#ffdd66",
                    this_screen_border="#ffdd66",
                    fontsize=26,
                ),
                widget.Sep(**sep_defaults),
                widget.TaskList(
                    border="#005577",
                    highlight_method="block",
                    theme_mode="fallback",
                    unfocused_border="#444444",
                    parse_text=lambda window_name: "",
                ),
                widget.Systray(padding=8),
                widget.Sep(**sep_defaults),
                widget.Volume(
                    unmute_format="<big>󰕾</big> {volume}%",
                    mute_format="<big>󰝟</big> {volume}%",
                    mute_foreground="#888888",
                    foreground="#bbbbff",
                    volume_app="lxterminal -e pulsemixer",
                ),
                widget.Sep(**sep_defaults),
                widget.Memory(
                    fmt="<big></big> {}",
                    format="{MemPercent:.0f}% 󰪍 {SwapPercent:.0f}%",
                    foreground="#ddbbdd",
                ),
                widget.Sep(**sep_defaults),
                widget.CPU(
                    fmt="<big></big> {}",
                    format="{load_percent:.0f}%",
                    foreground="#ffbbbb",
                ),
                widget.Sep(**sep_defaults),
                widget.Battery(
                    fmt="<big>󰁹</big> {}",
                    format="{percent:2.0%} {char}",
                    foreground="#99dd99",
                    full_char="",
                    charge_char="󰁞",
                    discharge_char="󰁆",
                    empty_char="",
                    show_short_text=False,
                ),
                widget.Sep(**sep_defaults),
                widget.Clock(
                    fmt="<big></big> {}",
                    format="%H:%M:%S",
                    foreground="#ffdd66",
                ),
                widget.Sep(**sep_defaults),
                widget.CurrentLayout(icon_first=True, scale=0.74),
            ],
            border_width=[0, 0, 1, 0],
            **bar_defaults
        ),
    ),
]

# Mouse functions to drag and resize
mouse = [
    Click([mod], "Button1", lazy.window.bring_to_front()),
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Click([mod, "shift"], "Button1", lazy.window.bring_to_front()),
    Drag([mod, "shift"], "Button1", lazy.window.set_size_floating(), start=lazy.window.get_size()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = "click_or_drag_only"
bring_front_click = "floating_only"
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus="#ff0000", border_normal="#000000", border_width=1,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="galculator"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
try:
    from libqtile.backend.wayland import InputConfig
    wl_input_rules = {
        "type:keyboard": InputConfig(
            kb_layout="latam",
            kb_variant="deadtilde",
        ),
        "type:touchpad": InputConfig(
            natural_scroll=True,
            pointer_accel=0.25,
            tap=True,
        ),
    }
except ImportError:
    pass

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# Move to group where window spawn
@hook.subscribe.client_managed
def client_managed(client):
    if not hasattr(client, "group") or client.group is None:
        return
    client.group.toscreen()

# Move to previous group if has windows or to next group with windows
# when group where window lived is on screen and has no windows
@hook.subscribe.client_killed
def client_killed(client):
    if not hasattr(client, "group") or client.group is None:
        return
    group, screen = client.group, client.group.screen
    # Compare greater than one since window is still atached to group
    if not screen or len(group.windows) > 1:
        return
    previous_group = screen.previous_group
    if previous_group and previous_group.windows:
        screen.set_group(previous_group)
    else:
        screen.next_group(skip_empty=True, skip_managed=False)

# Set wallpaper on every start
@hook.subscribe.startup_once
def change_wallpaper():
    try:
        path = os.path.expanduser("~/.config/wallpapers")
        wallpaper = os.path.join(path, random.choice(os.listdir(path)))
        assert os.path.isfile(wallpaper)
    except:
        return
    [screen.set_wallpaper(path=wallpaper, mode="fill") for screen in screens]

# Autostart programs
@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/autostart.sh")
    if os.access(script, os.X_OK):
        subprocess.run([script])
