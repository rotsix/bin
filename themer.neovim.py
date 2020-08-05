#!/usr/bin/python
#
# rotsix - (c) wtfpl 2017
# reload all neovim sessions

from neovim import attach
from glob import glob

for p in glob("/tmp/nvim*/0"):
    try:
        nvim = attach("socket", path=p)
        nvim.command("source ~/.config/nvim/init.vim")
    except ConnectionRefusedError:
        pass
