from project import db, ma


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.LargeBinary)
    status_id = db.Column(db.Integer)
    created_by = db.Column(db.String(100))
    update_by = db.Column(db.String(100))
    project_id = db.Column(db.Integer)

    def __repr__(self):
        return f"Task: {self.title}"


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "title", "description", "image", "status_id", "created_by", "update_by", "project_id")


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
