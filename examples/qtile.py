
from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [
    Key([mod], "F9", lazy.spawn("audiospread toggle")),
    Key([mod, "shift"], "F9", lazy.spawn("audiospread status")),
]
