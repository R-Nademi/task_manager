import re
from datetime import datetime


def id_validator(id):
    return type(id)== int  and id > 0

def title_validator(title):
    return type(title)== str and re.match( r"^[a-zA-Z\s]{3,30}$", title)

def description_validator(description):
    return type(description)== str and re.match( r"^[a-zA-Z\s]{3,30}$", description)

def star_time_validator(star_time):
    try:
        if type(star_time) == str:
            datetime.strptime(star_time, '%Y-%m-%d').time()
        elif type(star_time) == datetime:
            pass
        else:
            raise TypeError()
        return True
    except ValueError:
        return False

def end_time_validator(end_time):
    try:
        if type(end_time) == str:
            datetime.strptime(end_time, '%Y-%m-%d').time()
        elif type(end_time) == datetime:
            pass
        else:
            raise TypeError()
        return True
    except ValueError:
        return False

def assignee_validator(assignee):
    return type(assignee) == str and re.match(r"^[a-zA-Z\s]{3,15}$", assignee)


def task_validator(task):
    errors = []
    if not id_validator(task.id):
        errors.append("task id must be an integer > 0")

    if not title_validator(task.title):
        errors.append("task title is invalid")

    if not description_validator(task.description):
        errors.append("task description is invalid")

    if not star_time_validator(task.star_time):
        task.star_time = datetime.strptime(task.star_time, '%Y-%m-%d').time()
        errors.append("task star time is invalid")



    if not end_time_validator(task.end_time):
        task.end_time = datetime.strptime(task.end_time, '%Y-%m-%d').time()
        errors.append("task end time is invalid")


    return errors



