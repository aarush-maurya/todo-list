import os
from time import sleep
from classes.todo_list import TodoList
from classes.task import Task


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_task(todo: TodoList):

    task_id = input(f"Enter the task ID: ")
    try:
        task_id = int(task_id)
        if task_id > 0 and task_id <= len(todo):
            return task_id
        else:
            print(f"The Task ID must be from 1 to {len(todo)}")
            return None
    except ValueError:
        print(f"The Task ID must be an integer")
        return None


def main():
    todo = TodoList()
    while True:
        clear_screen()
        sleep(0.1)
        print(todo)
        print("\n[1] Add Task  [2] View Details  [3] Update  [4] Delete  [5] Exit")
        choice = input(f"Enter the choice (1-5): ").strip()

        if choice == "1":
            try:
                title = input(f"Enter the title of the task: ")
                desc = input(f"Enter the desscription (default - 'N/A'): ")
                if not desc:
                    desc = "N/A"
                # status = input(f"Enter the status [pending(default)/in progress/completed]: ")
                priority = input(f"Enter the priority [low/mid(default)/high]: ").lower()
                if not priority:
                    priority = "mid"

                task = Task(title, desc, priority=priority)
                todo.add(task)
                print(f"Task added successfully!")
                

            except (ValueError, IndexError) as e:
                print(f"ERROR: {e}")
                
            finally:
                sleep(1)

        elif choice == "2":
            try:
                index = get_task(todo) - 1
                clear_screen()
                sleep(0.1)
                print(todo.display(todo[index]))
                input("\npress Enter to exit view...")
            except (TypeError, ValueError) as e:
                print(f"ERROR: {e}")
                sleep(1)

        elif choice == "3":
            valid_attr = ["desc", "status", "priority"]
            try:
                index = get_task(todo) - 1
                attr = input(
                    f"Enter the attribute to change (desc, status, priority): "
                )
                if attr not in valid_attr:
                    raise ValueError(f"The 'attr' must be from {valid_attr}")
                value = input(f"Enter the new value: ")
                if attr == "priority" and value not in Task.valid_priority:
                    raise ValueError(f"'priority' must be from {Task.valid_priority}")
                if attr == "status" and value not in Task.valid_status:
                    raise ValueError(f"'status' must be from {Task.valid_status}")
                if attr == "desc" and not value:
                    value = "N/A"
                    
                todo.update(todo[index], attr, value)
            except (TypeError, ValueError) as e:
                print(f"ERROR: {e}")
                sleep(1)

        elif choice == "4":
            try:
                index = get_task(todo) - 1
                confirm = input(f"Are you sure to delete task '{todo[index]["title"]}'?(y/N): ")
                if confirm.strip().lower() == 'y':
                    todo.delete(todo[index])
            except (TypeError, ValueError) as e:
                print(f"ERROR: {e}")
                sleep(1)
            
        elif choice == "5":
            return 'q'
        
        else:
            print(f"Choose from 1 to 5.")
            sleep(1)
        
        

if __name__ == "__main__":
        if main() == 'q':
            exit()
