import os, random
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')

@app.route('/hello/',methods=['POST'])
def hello(name=None):
    user = request.form.get('username')
    return render_template('hello.html', name=user)

@app.context_processor
def gerador():
    foo = ['If debugging is the process of removing software bugs, then programming must be the process of putting them in. - Edsger Dijkstra',
    'One of my most productive days was throwing away 1000 lines of code - Ken Thompson', 
    'Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler', 
    'When debugging, novices insert corrective code; experts remove defective code. - Richard Pattis', 
    'Programming is like sex. One mistake and you have to support it for the rest of your life. - Michael Sinz'
    ]
    return dict(vicks=random.choice(foo))


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)