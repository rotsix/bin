#!/usr/bin/env python

import sys
from time import sleep

# https://github.com/sindresorhus/cli-spinners/blob/master/spinners.json

styles = [
        "/-\\|",
        "⠉⠘⠰⠤⠆⠃",
        [
            "✶",
	    "✸",
	    "✹",
	    "✺",
	    "✹",
            "✷"
        ],
        [
	    "┤",
	    "┘",
	    "┴",
	    "└",
	    "├",
	    "┌",
	    "┬",
	    "┐"
        ]
]

def wait(style, cond):
    while cond:
        for i in range(len(styles[style])):
            print(f"{styles[style][i]}", flush=True, end='')
            for j in range(len(styles[style][i])):
                print("\b", flush=True, end='')
            sleep(0.1)

def main(args):
    wait(3, lambda : True)

if __name__ == "__main__":
    main(sys.argv)
