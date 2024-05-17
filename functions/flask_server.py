import os
from flask import Flask, request, render_template
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

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

searcher = WordPatternSearcher(os.path.join(os.path.dirname(__file__), 'corpus.txt'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    pattern = request.form['pattern']
    results = searcher.search(pattern)
    return render_template('index.html', results=results, pattern=pattern)

if __name__ == "__main__":
    app.run(debug=True)
