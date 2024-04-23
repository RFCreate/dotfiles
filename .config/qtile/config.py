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
from libqtile import bar, layout, qtile, widget
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
    Key([mod], "Tab",lazy.screen.next_group(skip_empty=True) , desc="Focus next group"),
    Key([mod, "shift"], "Tab",lazy.screen.prev_group(skip_empty=True) , desc="Focus previous group"),
    # Change window state
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle window fullscreen"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc="Toggle window floating"),
    Key([mod], "Up", lazy.window.toggle_floating(), desc="Toggle window floating"),
    Key([mod], "Down", lazy.window.toggle_minimize(), desc="Toggle window minimize"),
    # Move floating window
    Key([mod, "shift"], "Left", lazy.window.eval('if self.info()["floating"] is True: self.move_floating(dx=-10, dy=0)')),
    Key([mod, "shift"], "Right", lazy.window.eval('if self.info()["floating"] is True: self.move_floating(dx=10, dy=0)')),
    Key([mod, "shift"], "Down", lazy.window.eval('if self.info()["floating"] is True: self.move_floating(dx=0, dy=10)')),
    Key([mod, "shift"], "Up", lazy.window.eval('if self.info()["floating"] is True: self.move_floating(dx=0, dy=-10)')),
    # Resize floating window (Numbers don't seem to be normalized)
    Key([mod, "control"], "Left", lazy.window.eval('if self.info()["floating"] is True: self.resize_floating(dw=-10, dh=0)')),
    Key([mod, "control"], "Right", lazy.window.eval('if self.info()["floating"] is True: self.resize_floating(dw=20, dh=0)')),
    Key([mod, "control"], "Down", lazy.window.eval('if self.info()["floating"] is True: self.resize_floating(dw=0, dh=30)')),
    Key([mod, "control"], "Up", lazy.window.eval('if self.info()["floating"] is True: self.resize_floating(dw=0, dh=-10)')),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle split sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.spawn(expanduser("~/.config/qtile/reload.sh")), desc="Reload config"),
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

groups = [Group(i) for i in "123456789"]
# groups = [Group(i) for i in "󰈹󰨞󰏆6789"]

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen(toggle=True),
                desc="Switch to group {}".format(i.name)),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name)),
            Key([mod, alt], i.name, lazy.window.togroup(i.name),
                desc="Move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Max(),
    layout.Columns(),
    # layout.Stack(),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(border_width=0)

widget_defaults = dict(
    font="sans",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            widgets=[
                widget.CurrentLayoutIcon(scale=0.75),
                widget.CurrentLayout(fmt="<b>{}</b>", foreground="#ffff00"),
                widget.Sep(foreground="#ffffff", padding=6),
                widget.TaskList(theme_mode="fallback", unfocused_border="#111111"),
            ],
            size=28,
            border_width=[1, 0, 0, 0],
            border_color="#ffffff",
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
