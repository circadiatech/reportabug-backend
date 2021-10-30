from project import db
from models.project import Project, project_schema, projects_schema
from utilities.common_utils import get_true_random_string


def create_project(data):
    project = Project(title=data['title'],
                      description=data.get('description', ''),
                      api_key=get_true_random_string(16))
    db.session.add(project)
    db.session.commit()
    return project_schema.dump(project)


def fetch_all_projects():
    projects = Project.query.all()
    return projects_schema.dump(projects)


def fetch_project(id):
    project = Project.query.filter_by(id=id).first_or_404()
    return project_schema.dump(project)


def delete_project(id):
    project = Project.query.filter_by(id=id).first_or_404()
    db.session.delete(project)
    db.session.commit()
    return {
        'success': 'Data deleted successfully'
    }