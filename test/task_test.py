from model.task import Task

task = (1 , "services", "green space", '8:30  am',  '5:30 pm', 'engineer ahmadi')


task = Task(*task)


print(Task.validate(task))

print(Task.to_tuple(task))








