def task():
    tasks = [] #empty list
    print("---Welcome to the task management app-----")
    total_task = int(input("enter total no. of  task :"))#No. of tasks
    # starts from 1 to total_task
    for i in range(1,total_task+1):
        task_name = input(f"enter task {i} =")
        tasks.append(task_name)
    print(f"today's tasks are\n{tasks}")

    while True:
        operation = int(input("enter \n1.add\n2update\n3-delete\n4-view\n5-exit\stop!"))
        # add the task to list
        if operation == 1:
            add = input("enter the task you want to add:")
            tasks.append(add)
            print(f"your task ({add}) is added successfully")
        # update the task in the list
        elif operation == 2:
            up_var = input("enter the task name you want to add:")
            if up_var in tasks :
                up = input("enter new task :")
                mun = tasks.index(up_var)# find the taskname with index and update it
                up = tasks[mun]
                print(f"your task ({up}) is successfully updated")
        elif operation == 3:
            del_var = input("enter the task you want to delete :")
            if del_var in tasks :
                mun = tasks.index(del_var)#del the taskname with index and delete it
                del tasks[mun]
                print(f"your task ({del_var}) is successfully deleted")
        elif operation == 4:
            print(f"total tasks = {tasks}")
        elif operation == 5:
            print("program is closing.......")
            break
        else:
            print("Invalid Input (error)")
task()

