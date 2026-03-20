from classes.task import Task
import json
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = self.read_json()  # this will return a list of dictionaries

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, tasks: list):
        temp_list = []
        if isinstance(tasks, list):
            for task in tasks:
                if isinstance(task, dict):
                    temp_list.append(task)
                else:
                    raise TypeError("Each task must be a dictionary")
            self._tasks = temp_list
            self.write_json()
        else:
            raise TypeError("'tasks' must be a list")

    def add(self, task: Task):
        if any(t["title"] == task.title for t in self.tasks):
            raise ValueError("The task already exists.")
        time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        task = self.task_to_dict(task)
        task.update({"time": time})
        self.tasks.append(task)
        self.write_json()

    def update(self, task: dict, attr, value):
        if task["title"] in [t["title"] for t in self.tasks]:
            task[attr] = value
            self.write_json()
        else:
            raise ValueError("Task not found")

    def delete(self, task: dict):
        if task["title"] in [t["title"] for t in self.tasks]:
            self.tasks.remove(task)
            self.write_json()
        else:
            raise ValueError("Task not found")

    def task_to_dict(self, task: Task):
        task_dict = {
            "title": task.title,
            "desc": task.desc,
            "status": task.status,
            "priority": task.priority,
        }
        return task_dict

    def read_json(self):
        try:
            with open("todo_list.json", "r") as f:
                data = json.load(f)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def write_json(self):
        json_list = []
        for task in self.tasks:
            json_list.append(task)
        with open("todo_list.json", "w") as f:
            data = json.dumps(json_list, indent=4)
            f.write(data)

    def display(self, task: dict):
        string = f"{'-'*54}\n"
        string += f"TITLE: {task['title']}\n"
        string += f"{'-'*54}\n"
        string += f"STATUS: {task['status'].capitalize()} | PRIORITY: {task['priority'].capitalize()}\n"
        string += f"ADDED: {task['time']}\n"
        string += f"{'-'*54}\n"
        string += f"DESCRIPTION:\n{task['desc']}"

        return string

    def __str__(self):
        task_completed = 0
        task_in_progress = 0
        task_pending = 0
        digit_width = len(str(len(self.tasks)))
        titles = [t["title"] for t in self.tasks]
        try:
            max_width = max(list(map(lambda x: len(x), titles)))
        except ValueError:
            max_width = 23
        title_width = max_width if max_width > 23 else 23
        string = f"==================== MY TODO LIST ====================\n"
        string += f"{'ID':<{digit_width}}  Stat  {'Task Title':<{title_width}}Priority   Added\n"
        string += f"{'-'*digit_width}  ----  ----------              --------   -----\n"
        for index, task in enumerate(self.tasks, start=1):
            string += f"{index:0>{digit_width}}  "
            if task["status"] == "in progress":
                string += f" [-] "
                task_in_progress += 1
            elif task["status"] == "completed":
                string += f" [X] "
                task_completed += 1
            else:
                string += f" [ ] "
                task_pending += 1
            string += f" {task["title"]:<{title_width}}"
            string += f" {task["priority"].capitalize():<8}  "
            string += f" {task["time"][:5]}\n"
        string += "======================================================\n"
        string += f"Summary: {len(self.tasks)} Tasks | {task_completed} Done | {task_in_progress} Working | {task_pending} To-Do"
        return string

    def __len__(self):
        return len(self.tasks)
    
    def __getitem__(self, index):
        return self.tasks[index]