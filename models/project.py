from project import db, ma


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text, nullable=True)
    api_key = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"Project: {self.title}"


class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project
        fields = ("id", "title", "description", "api_key", "is_active")


project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)