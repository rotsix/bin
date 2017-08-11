#!/usr/bin/env python
#
# rotsix - (c) wtfpl 2017
# reload all neovim sessions

import os
from neovim import attach

try:
    from neovim import attach
    from glob import glob
    neovimInstances = glob('/tmp/nvim*/0')
    for p in neovimInstances:
        nvim = attach('socket', path=p)
        nvim.command('source ~/.config/nvim/init.vim', async=True)
except ConnectionRefusedError:
    pass
