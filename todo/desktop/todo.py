"""
Simple script which interact with the todo webservice
todo: implement token auth
"""
import argparse
import requests
import json
from config import base_url, username, password 
user = (username, password)

def get_tags():
    pass


def get_id(title):
    todos = get_todo()
    for item in todos['todos']:
        if item['title'] == title:
                print item['id']
                return str(item['id'])
    return "nop"


def delete(id):
    if not id.isdigit():
        id = get_id(id)
    response = requests.delete(base_url + 'todo/' + id, auth=user)
    if response.status_code == 400 or  response.status_code == 405:
        print "todo not found, plz provide a correct id or existing title"
        return
    print response.status_code


def post(title, content):
    item = json.dumps({u'title': title, u'content': content, u'done': False})
    response = requests.post(base_url + 'todo', data=item,
            headers={'content-type': 'application/json'}, auth=user)
    print response.json()


def get_todo():
    #request = prepare_request(base_url + 'todo')
    response = requests.get(base_url + 'todo', auth=user)
    if response.status_code == 200 and response.headers['content-type'] == 'application/json':
       return response.json()
    else:
        # raise error
        pass


def display_todo(args=[]):
    todos = get_todo()
    dmenu = False
    for item in todos['todos']:
        if 'nice' in args:
            print '%s, id: %i, done: %s\n %s' % (item['title'], item['id'], item['done'], item['content'])
            print ""
            continue 
        elif 'dmenu' in args:
            dmenu = True
            args.remove('dmenu')
        for x in args:
            print item[x]
        if not dmenu:
            print ""


def handle_args(args):
    if args.delete and args.post:
        print "you can't use both post and delete at the same time"
        return
    elif args.delete:
        delete(args.delete)
    elif args.post:
        post(*args.post)
    else:
        display_todo(args.fields)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "todo clients for crichon_backend, \
            if invoke without args retrieve todo and diplay them nicely")

    parser.add_argument("-f", "--fields", type=str,nargs='*', choices=["title", "id", "done", "content", "nice", "dmenu"],
            default=['nice'], metavar="XXX",
            help="field to include in output do nothing if used with delete or post, special output: nice and dmenu")

    parser.add_argument("-o", "--output", type=str,metavar='o', help="print to ouptut file instead of stdout")

    parser.add_argument("-d", "--delete", type=str, metavar='y', help="delete the todo with y id or title")
    parser.add_argument("-p", "--post", nargs=2, type=str, metavar=('x', 'z'), help="post a new todo, title: x, content: z")

    args = parser.parse_args()
    if args.output:
        import sys
        with open(args.output, 'w') as f:
            sys.stdout = f
            handle_args(args)
    else:
        handle_args(args)

