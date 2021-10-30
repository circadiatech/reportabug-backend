from project import db
from models.project import Project, project_schema, projects_schema


def fetch_all_projects():
    projects = Project.query.all()
    return projects_schema.dump(projects)
