# bin

Here is some small scripts I use.

## todo
Small todo list in python 3.6+ (f-strings).

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
Without argument, `todu -r` is used.

## stm
Small tasks manager in bash.

**Adapted for** `systemd` **!**

##### Install
Just copy in your `$PATH`.

##### Config
You can directly modify the script to adapt to your uses.

##### Usage
```
stm backlight|bl +|-|up|down|get [value]
stm vol|volume|v +|-|up|toggle|down [value]
stm bluetooth|bt start|up|stop|kill|restart|on|off|down
stm mysql|sql|sqld|mysqld start|up|stop|kill|restart|on|stop|off
stm http|httpd start|up|stop|kill|restart|on|stop|off
stm lamp|LAMP start|up|stop|kill|restart|on|stop|off
```

## popup
Little script to display pop-ups using lemonboy's bar.

##### Depends
This script depends on lemonboy's bar (since it's a little wrapper).
You can use the xft-fork for xft fonts.

##### Install
Just copy in your `$PATH`.

##### Config
You can directly modify the script to adapt to your uses.

##### Usage
```
popup [-h|-t duration|-g geometry|-p position|-B bgcolor|-F fgcolor|-f font] <thing to display>"
```

There is some defaults : 

```
duration = 5
geometry = 100x40+20+20
position = center
bgcolor = '#202020'
fgcolor = '#C6C6C6'
font = mono-8
font2 = FontAwesome-10 # useful for icons
```

## brainfuck
Minimal brainfuck interpreter.

##### Depends
This script is using python3.6.

##### Install
Just copy in your `$PATH`.

##### Usage
```
brainfuck -f|--file <file>
brainfuck -e|--exp <expression>
brainfuck -h|--help
```


