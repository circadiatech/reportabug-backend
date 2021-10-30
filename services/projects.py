from project import db
from models.project import Project, project_schema
from utilities.common_utils import get_true_random_string


def create_project(data):
    project = Project(title=data['title'],
                      description=data.get('description', ''),
                      api_key=get_true_random_string(16))
    db.session.add(project)
    db.session.commit()
    return project_schema.dump(project)
