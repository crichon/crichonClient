#!/bin/sh
## script pour gérer les différentes tâches à  faire avec dmenu.
## sources: <http://thuban.toile-libre.org/index.php/2011/01/22/un-pense-bete-avec-dmenu/>
# variables utilisées pour dmenu
SB="#7D7D7D"
SF="#222222"
NB="#222222"
NF="#7D7D7D"
FN="-*-fixed-*-*-*-*-10-70-*-*-*-*-*-*"

PROMPT="write:add | select:del > "
 
ACTION="python2.7 todo.py -f title dmenu | dmenu -p '$PROMPT:' "
CMD=$(eval $ACTION)
while [ -n "$CMD" ]; do
	echo $CMD
	if [ $? = 0 ]; then
		python2.7 todo.py -d $CMD
	else
		echo "blop"
		echo " "| dmenu -p "Content ?" |xargs echo "python2.7 todo.py -p $CMD" | `xargs`
	fi
 
	CMD=$(eval $ACTION)

done
exit 0
