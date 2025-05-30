from model.validator import *



class Task :

    def __init__(self,id,title,description,star_time,end_time,assignee):
        self.id = id
        self.title = title
        self.description = description
        self.star_time = star_time
        self.end_time = end_time
        self.assignee = assignee

    def validate(self):
        return task_validator(self)

    def to_tuple(self):
        return (self.id, self.title, self.description, self.star_time, self.end_time, self.assignee)



