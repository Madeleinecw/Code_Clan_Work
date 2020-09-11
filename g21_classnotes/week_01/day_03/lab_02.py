

# def find_user_by_ID(list, user_id):
#     found_user = None
#     for user in list:
#         if user["user_id"] == user_id:
#             found_user = user
#     return found_user

# print(find_user_by_ID)


tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def status_of_tasks(list, status):
    found_status = []
    for task in list:
        if task["completed"] == status:
            found_status.append(task["description"])
    return found_status


# print(status_of_tasks(tasks, False))

# print(status_of_tasks(tasks, True))

def list_of_task_descriptions(list):
    list_of_descriptions = []
    for task in list:
        list_of_descriptions.append(task["description"])
    return list_of_descriptions

# print(list_of_task_descriptions(tasks))

def overall_time_taken(list, set_time):
    list_of_descriptions = []
    for task in list:
        if task["time_taken"] >= set_time:
            list_of_descriptions.append(task["description"])
    return list_of_descriptions

# print(overall_time_taken(tasks, 15)) 

def print_task(list, description):
    index_counter = 0
    for task in list:
        if task["description"] == description:
            return tasks[index_counter]
        else:
            index_counter += 1

# print(print_task(tasks, "Feed Cat"))

def mark_as_complete(list, description):
    index_counter = 0
    for task in list:
        if task["description"] != description:
            index_counter += 1
        elif task["description"] == description and task["completed"] == False:
            task["completed"] = True
            return tasks[index_counter]

# print(mark_as_complete(tasks, "Clean Windows"))

def add_task(list):
    descrip = input("Describe task ")
    complete = input("Is it completed, True or False ? ")
    time = input("How much time does it take ? ")
    new_task = {}
    new_task["description"] = descrip
    new_task["completed"] = complete
    new_task["time_taken"]= time
    list.append(new_task)
    return list


# print(add_task(tasks))

def print_all_tasks(list):
    print(list)

# print(print_all_tasks(tasks))

def display_menu(list):
    userinput = None
    while userinput == None:
        print("Menu:")
        print("1: Display All Tasks")
        print("2: Display Uncompleted Tasks")
        print("3: Display Completed Tasks")
        print("4: Mark Task as Complete")
        print("5: Get Tasks Which Take Longer Than a Given Time")
        print("6: Find Task by Description")
        print("7: Add a new Task to list")
        print("M or m: Display this menu")
        print("Q or q: Quit")
        userinput = input("please select from menu... ")
    if userinput == "1":
        print(tasks)
    elif userinput == "2":
        print(status_of_tasks(tasks, False))
    elif userinput == "3":
        print(status_of_tasks(tasks, True))
    elif userinput == "4":
        ask_user = input("What task would you like to set as complete? ")
        print(mark_as_complete(tasks, ask_user))
    elif userinput == "5":
        ask_user = input("How much time would you like? ")
        print(overall_time_taken(tasks, int(ask_user)))
    elif userinput == "6":
        ask_user = input("Describe your required task ")
        print(print_task(tasks, ask_user))
    elif userinput == "7":
        print(add_task(tasks))
    elif userinput == 'M' or userinput == 'm':
        print(display_menu(tasks))
    elif userinput == 'Q' or userinput == 'q':
        print("Bye")
    

display_menu(tasks)
