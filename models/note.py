from project import db, ma

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    completed = db.Column(db.Boolean(), default=False, nullable=False)

    def __repr__(self):
        return '<Post %s>' % self.title

class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)
