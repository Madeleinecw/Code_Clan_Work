import pdb 
from models.tasks import Task
from models.user import User
import repositories.user_repository as user_repository
import repositories.task_repository as task_repository

# task_repository.delete_all()

# task_1 = Task("Walk Dog", "Jack Jarvis", 60)
# print(task_1.__dict__)
# task_repository.save(task_1)

# task_2 = Task("Feed Cat", "Victor McDade", 5)
# task_repository.save(task_2)

# # res = task_repository.select_all()
# # for task in res:
# #     print(task.__dict__)

# found_task = task_repository.select(1).__dict__

# task_1.mark_complete()
# task_repository.update()
task_repository.delete_all()
user_repository.delete_all()

user_2 = User('Halle', 'Berry')
user_repository.save(user_2)
user_1 = User('Maddie', 'Wood')
user_repository.save(user_1)
user_repository.select_all()
user_repository.update(user_2)
user_repository.select_all()

task = Task("Walk Dog", user_2, 10)
task_repository.save(task)

pdb.set_trace()
