from project import db
from models.task import Task, task_schema, tasks_schema


def fetch_task(id):
    task = Task.query.filter_by(id=id).first_or_404()
    return task_schema.dump(task)
