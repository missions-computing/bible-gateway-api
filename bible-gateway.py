from flask import Flask, render_template

from bg_api import BGAPI

app = Flask(__name__)
bg_api = BGAPI()

@app.route('/')
def list_translations():
    return render_template('translation-list.html', translations=bg_api.list_translations())


@app.route('/bible/<xlation>')
def get_translation_info(xlation):
    return render_template('translation-detail.html', translation=bg_api.get_translation(xlation))


@app.route('/bible/<xlation>/book/<book_osis>')
def get_book_info(xlation, book_osis):
    return render_template('book-detail.html', book=bg_api.get_book_info(xlation, book_osis), translation=xlation)


@app.route('/bible/<xlation>/passage/<passage_osis>')
def get_passage(xlation, passage_osis):
    return render_template('passage.html', verse=bg_api.get_passage(xlation, passage_osis))


if __name__ == '__main__':
    app.run(debug=True)
