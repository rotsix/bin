# bin

Here are some small scripts I use.

## todo
Small todo list in python 3.6+.

##### Install
Just copy in your `$PATH`.

##### Config
You can directly modify the script to adapt to your uses.

##### Usage
```
todo [-r | --read]
todo [-a | --add] <note>
todo [-d | --delete] <number>
```
Without argument, `todo -r` is used.

## stm
Small tasks manager in bash.

**Suitable for `systemd` only!**

##### Install
Just copy in your `$PATH`.

##### Config
You can directly modify the script to adapt to your uses.

##### Usage
```
stm backlight|bl +|-|up|down|get [value]
stm vol|volume|v +|-|up|toggle|down [value]
stm mic|micro|microphone|m toggle
stm bluetooth|bt start|up|stop|kill|restart|on|off|down
stm mysql|sql|sqld|mysqld start|up|stop|kill|restart|on|stop|off
stm http|httpd start|up|stop|kill|restart|on|off
stm lamp|LAMP start|up|stop|kill|restart|on|off
```

## brainfuck
Minimal brainfuck interpreter.

##### Depends
This script is using Python 3.6+.

##### Install
Just copy in your `$PATH`.

##### Usage
```
brainfuck -f|--file <file>
brainfuck -e|--exp <expression>
brainfuck -h|--help
```

## themer
Ultra-simple theme manager and switcher.

##### Install
Just copy in your `$PATH`

##### Config
You can directly modify the script to adapt to your uses.

##### Usage
```
themer <theme name>
```

## =
Calculator for use with rofi/dmenu(2).

Stolen from [here](https://github.com/onespaceman/menu-calc).

##### Install
Just copy in your `$PATH`.

##### Usage
Use rofi/dmenu(2), and type `= <equation>`.

Example:
```
= 4+3
7
```

## get-window-criteria
Get windows' criteria.

##### Install
Just copy in your `$PATH`

##### Usage
Run this script, then click on a window.
Output is in the format: `[<name>=<value> <name2>=<value2> ...]`.

> Note: wayland is not supported.

Example:
```
./get-window-criteria
Clicking on this terminal, and returns this:
[class="Termite" id=44040195 instance="termite" title="nvim README.md"]
```

## memo
Want some small memos ? Use it.

##### Install
Just copy in your `$PATH`

##### Usage
```
memo list|show|l|s	    	simple `tree $memo_dir`
memo add|a <item>	    	create the selected item (and directories if needed)
memo edit|e <item>	    	edit the selected item
memo delete|d <item|dir>	delete the selected item (directory requires -r option)
memo git|g <git-command>	uses git directly, so uses ~/.gitconfig
memo help|h|?		    	display this message
```

## post
Create a new post on my blog

##### Install
Just copy in your `$PATH`

##### Usage
```
post <my title>
```

It creates `YYYY-MM-DD-my-title.md` and fill the header.
