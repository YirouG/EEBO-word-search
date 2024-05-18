from flask import Flask, request, render_template
import re
import threading
import webbrowser
import os
import sys
import time

app = Flask(__name__)

class WordPatternSearcher:
    def __init__(self, corpus_file):
        self.corpus_file = corpus_file
        self.words = self.load_words()

    def load_words(self):
        with open(self.corpus_file, 'r', encoding='utf-8') as file:
            text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        return words

    def convert_pattern_to_regex(self, pattern):
        regex_pattern = re.escape(pattern).replace(r'\*', '.*').replace(r'\?', '.')
        return f'^{regex_pattern}$'

    def search(self, pattern):
        regex_pattern = self.convert_pattern_to_regex(pattern)
        regex = re.compile(regex_pattern)
        return [word for word in self.words if regex.search(word)]

# Determine if the script is running as a frozen executable
if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.abspath(os.path.dirname(__file__))

# Create the searcher with the correct path to corpus.txt
searcher = WordPatternSearcher(os.path.join(base_dir, 'corpus.txt'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    pattern = request.form['pattern']
    results = searcher.search(pattern)
    return render_template('index.html', results=results, pattern=pattern)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()  # Open the browser after 1 second
    app.run(port=5000, debug=False, use_reloader=False)  # Ensure the server runs in the main thread
    while True:
        time.sleep(1)  # Keep the main thread running
