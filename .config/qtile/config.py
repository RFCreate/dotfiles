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

from os.path import expanduser
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

alt = "mod1"
mod = "mod4"
terminal = guess_terminal()

keys = [
    # Change window in focus
    Key([alt], "Tab", lazy.group.next_window(), desc="Focus next window"),
    Key([alt, "shift"], "Tab", lazy.group.prev_window(), desc="Focus previous window"),
    # Change group in focus
    Key([mod], "Tab", lazy.screen.next_group(skip_empty=True) , desc="Switch to next group"),
    Key([mod, "shift"], "Tab", lazy.screen.prev_group(skip_empty=True) , desc="Switch to previous group"),
    Key([mod], "0", lazy.screen.toggle_group() , desc="Switch to last group"),
    # Change window state
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle window fullscreen"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle window floating"),
    Key([mod], "Up", lazy.window.toggle_floating(), desc="Toggle window floating"),
    Key([mod], "Down", lazy.window.toggle_minimize(), desc="Toggle window minimize"),
    # Close active window
    Key([alt], "F4", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "w", lazy.window.kill(), desc="Kill focused window"),
    # Toggle between different layouts
    Key([mod], "space", lazy.next_layout(), desc="Toggle next layout"),
    Key([mod, "shift"], "space", lazy.prev_layout(), desc="Toggle previous layout"),
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
    # Grow or shrink tiled windows
    Key([mod], "plus", lazy.layout.grow()),
    Key([mod], "minus", lazy.layout.shrink()),
    Key([mod, "shift"], "plus", lazy.layout.grow_main()),
    Key([mod, "shift"], "minus", lazy.layout.shrink_main()),
    # Change tiled window state
    Key([mod, "control"], "plus", lazy.layout.maximize(), desc="Grow tiled window to max size"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset secondary window sizes"),
    Key([mod, "shift"], "n", lazy.layout.reset(), desc="Reset all window sizes"),
    Key([mod, alt], "f", lazy.layout.flip()),
    # Toggle between split and unsplit sides of the stack
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle split sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Change qtile state
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

mouse = [
    # Drag window in focus
    Click([mod], "Button1", lazy.window.bring_to_front()),
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    # Resize window in focus
    Click([mod, "shift"], "Button1", lazy.window.bring_to_front()),
    Drag([mod, "shift"], "Button1", lazy.window.set_size_floating(), start=lazy.window.get_size()),
]

# Application keys
keys.extend([
    # Screenshot commands
    Key([], "Print", lazy.spawn("maimpick Select"), desc="Save screenshot of selection"),
    Key(["shift"], "Print", lazy.spawn("maimpick Window"), desc="Save screenshot of window"),
    Key([alt], "Print", lazy.spawn("maimpick Screen"), desc="Save screenshot of screen"),
    Key(["control"], "Print", lazy.spawn("maimpick Copy Select"), desc="Copy screenshot of selection"),
    Key(["control", "shift"], "Print", lazy.spawn("maimpick Copy Window"), desc="Copy screenshot of window"),
    Key(["control", alt], "Print", lazy.spawn("maimpick Copy Screen"), desc="Copy screenshot of screen"),
    # Brightness commands
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -q set +5%"),
        lazy.spawn("brightness-notify"), desc="Raise brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -q set 5%-"),
        lazy.spawn("brightness-notify"), desc="Lower brightness"),
    # Volume commands
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
        lazy.spawn("volume-notify"), desc="Raise volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
        lazy.spawn("volume-notify"), desc="Lower volume"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        lazy.spawn("volume-notify"), desc="Mute/unmute volume"),
    # Application programs
    Key([mod], "q", lazy.spawn("rofi -show drun"), desc="Open program launcher"),
    Key([mod], "w", lazy.spawn("rofi -show window"), desc="Open window switcher"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Open command launcher"),
    Key([mod], "v", lazy.spawn("clipcat-menu"), desc="Open clipboard history"),
    Key([mod], "e", lazy.spawn("pcmanfm"), desc="Open file manager"),
    Key([mod], "t", lazy.spawn("lxterminal"), desc="Open terminal"),
    Key(["control", "shift"], "Escape", lazy.spawn("lxtask"), desc="Open task manager"),
])

# Define workspaces
groups = [
    Group("1", label="󰈹", matches=[Match(wm_class="firefox")]),
    Group("2", label="", matches=[Match(wm_class="lxterminal")]),
    Group("3", label="󰨞", matches=[Match(wm_class="vscodium")]),
    Group("4", label="", matches=[Match(wm_class="pcmanfm")]),
    Group("5", label="", matches=[Match(wm_class="l3afpad")]),
    Group("6", label="󰋩", matches=[Match(wm_class="imv")]),
    Group("7", label="󰕧", matches=[Match(wm_class="mpv")]),
    Group("8", label="󰿎", matches=[Match(wm_class="shotcut")]),
    Group("9", label="󰏆", matches=[Match(wm_class="DesktopEditors")]),
]

# Move to group where window spawn
@hook.subscribe.group_window_add
def group_window_add(group, window):
    group.toscreen()

for i in groups:
    keys.extend([
        # Keys to navigate workspaces
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle=True),
            desc="Switch to group {}".format(i.name)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        Key([mod, alt], i.name, lazy.window.togroup(i.name),
            desc="Move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Max(),
    # layout.Columns(),
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

# Floating window attributes
floating_layout = layout.Floating(
    border_focus="#888888", border_normal="#ff0000", border_width=1,
)

# Default values for widgets and bars
widget_defaults = dict(
    font="sans",
    fontsize=16,
    padding=3,
)
bar_defaults = dict(
    size=30,
    border_color="#ffffff",
    background="#2b2b2b",
)
top_bar_sep = dict(
    foreground="#bbbbbb",
    padding=18,
)
top_bar_text = dict(
    font="mesloLGSNF",
    foreground="#f0d080",
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
                    this_current_screen_border="#f0d040",
                    this_screen_border="#f0d040",
                    padding=4,
                    fontsize=18,
                ),
                widget.Spacer(),
                widget.Systray(padding=8),
                widget.Sep(**top_bar_sep),
                widget.TextBox("VOL", **top_bar_text),
                widget.Volume(mute_format="muted {volume}%", mute_foreground="#888888"),
                widget.Sep(**top_bar_sep),
                widget.TextBox("CPU", **top_bar_text),
                widget.CPU(format="{load_percent:.0f}%"),
                widget.Sep(**top_bar_sep),
                widget.TextBox("RAM", **top_bar_text),
                widget.Memory(format="{MemPercent:.0f}%"),
                widget.Sep(**top_bar_sep),
                widget.TextBox("SWAP", **top_bar_text),
                widget.Memory(format="{SwapPercent:.0f}%"),
                widget.Sep(**top_bar_sep),
                widget.TextBox("BAT", **top_bar_text),
                widget.Battery(
                    format="{percent:2.0%} {char}",
                    full_char="",
                    charge_char="",
                    discharge_char="",
                    empty_char="",
                    low_percentage=0.25,
                    show_short_text=False,
                    notify_below=25,
                ),
                widget.Sep(**top_bar_sep),
                widget.Clock(format="%d/%m/%Y %I:%M:%S %p", **top_bar_text),
            ],
            border_width=[0, 0, 1, 0],
            **bar_defaults
        ),
        bottom=bar.Bar(
            widgets=[
                widget.CurrentLayoutIcon(scale=0.75),
                widget.CurrentLayout(fmt="<b>{}</b>", foreground="#ffff00"),
                widget.Sep(foreground="#ffffff", padding=6),
                widget.TaskList(
                    border="#005577",
                    highlight_method="block",
                    theme_mode="fallback",
                    unfocused_border="#444444",
                ),
            ],
            border_width=[1, 0, 0, 0],
            **bar_defaults
        ),
    ),
]

bring_front_click = "floating_only"
follow_mouse_focus = False

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
