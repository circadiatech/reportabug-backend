from project import db
from models.note import Note, note_schema, notes_schema


def read_all_notes():
    notes = Note.query.all()
    return notes_schema.dump(notes)


def read_one_note(id):
    note = Note.query.filter_by(id=id).first_or_404()
    return note_schema.dump(note)


def create_note(data):
    note = Note(title=data['title'])
    db.session.add(note)
    db.session.commit()
    return note_schema.dump(note)


def update_note(id, data):
    note = Note.query.filter_by(id=id).first_or_404()
    note.title = data.get('title', note.title)
    if 'completed' in data:
        note.completed = data['completed']
    db.session.commit()
    return note_schema.dump(note)


def delete_note(id):
    note = Note.query.filter_by(id=id).first_or_404()
    db.session.delete(note)
    db.session.commit()
    return {
        'success': 'Data deleted successfully'
    }
