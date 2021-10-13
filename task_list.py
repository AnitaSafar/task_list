tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def uncompleted_tasks():
     for task in tasks:
        if task["completed"] == False:
            print(task)

uncompleted_tasks()

print("")

def completed_tasks():
     for task in tasks:
        if task["completed"] == True:
            print(task)

completed_tasks()

print("")

def task_descriptions():
     for task in tasks:
        print(task["description"])

task_descriptions()

print("")

def task_time():
    time = int(input("Enter time?"))
    for task in tasks:
        if task["time_taken"] >= time:  
            print(task)

task_time()

def given_task():
    task_name = input("Enter task?")
    for task in tasks:
        if task["description"] == task_name:  
            print(task)

given_task()