#!/bin/sh
title=`echo " " | dmenu -p "title: "`
content=`echo " " |dmenu -p "content"`

python2.7 ~/bin/todo.py -p $title "$content"
