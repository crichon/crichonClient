#!/bin/sh
python2.7 ~/bin/todo.py -f title dmenu|dmenu -l 100 |xargs echo 'python2.7 /home/chris/bin/todo.py -d'|`xargs`
