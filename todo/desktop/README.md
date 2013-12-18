todo.py
----------

usage: todo.py [-h] [-f [XXX [XXX ...]]] [-o o] [-d y] [-p x z]

todo clients for crichon_backend, if invoke without args retrieve todo and
diplay them nicely

    optional arguments:
      -h, --help            show this help message and exit
      -f [XXX [XXX ...]], --fields [XXX [XXX ...]]
                            field to include in output do nothing if used with
                            delete or post, special output: nice and dmenu
      -o o, --output o      print to ouptut file instead of stdout
      -d y, --delete y      delete the todo with y id or title
      -p x z, --post x z    post a new todo, title: x, content: z

todo
------

a shell script which rely on dmenu for user input
can either select and delete a todo or add a new item

user can may also use dmenu_add and dmenu_dell

boot_todo
-------------

to start server and conky in background
you may need to install conky

when conky is started, it will ask every 5 secondes the todo list by calling todo.py -o todo.list
to edit this behaviour (update intervall, display or file options) edit todo.conkyrc 
item are written to a file which will be read by conky every 3 secondes

todo.conkyrc
-----------------
conky config file with the execi call
please refer to conky documentation for more info

RoadMap:
-------------
 - try to factorise this code
 - implement patch and filter
 - implement token auth
