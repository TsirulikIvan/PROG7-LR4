from flask import Flask, url_for
from flask import render_template, request
import json


app = Flask(__name__)
rules = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
APP_NAME = 'LR4 - example by TI'
data = None
with open('messages.json', 'r') as json_file:
	data = json.load(json_file)


@app.route('/')
def index():
	return render_template('index.html', appname=APP_NAME, content=rules )


@app.route('/command/<id>')
def command(id):
	return f'running command with {id}'


app.add_url_rule('/command/<id>', 'command', command)


@app.route('/add/message', methods=['POST'])
def add_message():
	data[request.form['username']] = request.form['msgtxt']
	with open("messages.json", "w") as write_file:
		json.dump(data, write_file)
	return render_template('index.html', appname=APP_NAME, content=rules)


if __name__ == '__main__':
	app.run()

