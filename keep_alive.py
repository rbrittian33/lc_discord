import os
from threading import Thread

from flask import Flask

app = Flask('')

@app.route('/')
def home():
	return "I'm alive"

def run():
	app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
	t = Thread(target=run)
	t.start()