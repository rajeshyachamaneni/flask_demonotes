from flask import Flask, render_template, request, redirect, url_for
from google.cloud import firestore

app = Flask(__name__)
db = firestore.Client()

@app.route('/')
def index():
    notes_ref = db.collection('notes')
    notes = notes_ref.stream()
    notes_list = []
    for note in notes:
        notes_list.append(note.to_dict())
    return render_template('index.html', notes=notes_list)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        note_content = request.form['content']
        if note_content:
            db.collection('notes').add({'content': note_content, 'timestamp': firestore.SERVER_TIMESTAMP})
        return redirect(url_for('index'))
    return render_template('add_note.html')

if __name__ == '__main_':
    app.run(debug=True, host='0.0.0.0', port=8080)