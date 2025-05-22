import re
from datetime import datetime


def task_validator(task):
    errors = []

    if not (type(task[1]) == int and task[1]>0):
        errors.append('task ID must be an integer > 0')

    if not (type(task[2]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", task[2])):
        errors.append('task title is Invalid')


    if not (type(task[3]) == str and re.match(r"^[a-zA-Z\s]{3,50}$", task[3])):
        errors.append('task description is Invalid')

    try:
        datetime.strptime(task[4], '%Y-%m-%d')
    except:
        errors.append('task start time is Invalid')

    try:
        datetime.strptime(task[5], '%Y-%m-%d')
    except:
        errors.append('task end time is Invalid')

    if not (type(task[6]) == str and re.match(r"^[a-zA-Z\s]{3,15}$", task[6])):
        errors.append('task assignee must be an integer > 0')






    return errors


