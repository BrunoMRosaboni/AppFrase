import os, random
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World</hi>"

@app.route('/vicks')
def vicks():
    return 'vicks page!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.context_processor
def example():
    return dict(myexample='This is an example')

@app.context_processor
def gerador():
    foo = ['If debugging is the process of removing software bugs, then programming must be the process of putting them in. - Edsger Dijkstra',
    'One of my most productive days was throwing away 1000 lines of code - Ken Thompson', 
    'Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler', 
    'When debugging, novices insert corrective code; experts remove defective code. - Richard Pattis', 
    'Programming is like sex. One mistake and you have to support it for the rest of your life. - Michael Sinz'
    ]
    return dict(vicks=random.choice(foo))


if __name__ == '__main__':
	app.run()