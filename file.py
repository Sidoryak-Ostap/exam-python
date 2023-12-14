from datetime import datetime

def delete_element_in_list(name, my_list):
    return [element for element in my_list if element.name != name]

class ProjectManager:
    def __init__(self):
        self.projects = []

    def delete_project(self, project_name):
        try:
            project_name = input("Enter project name: ")
            self.projects = delete_element_in_list(project_name, self.projects)
        except Exception as e:
            print(f"An error occurred: {e}")

    def create_project(self):
        try:
            project_name = input("Enter name of the project: ")
            project_description = input("Describe project: ")
            project = Project(project_name, project_description)
            self.projects.append(project)
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_task_to_project(self):
        try:
            project_name = input("Enter project name: ")
            project_found = False
            for project in self.projects:
                if project.name == project_name:
                    task_name = input("Enter task name: ")
                    task_description = input("Enter task description: ")
                    task_deadline = input("Please enter a deadline in format (YYYY-MM-DD): ")
                    date_object = datetime.strptime(task_deadline, "%Y-%m-%d")
                    executor = input("Enter task executor name: ")
                    role = input("Enter task executor role: ")
                    new_task = Task(task_name, task_description, date_object, {"name": executor, "role": role})
                    project.tasks.append(new_task)
                    project_found = True
                    break
            if not project_found:
                print("There is no any project with such name")
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_task_from_project(self):
        try:
            project_name = input("Enter project name: ")
            for project in self.projects:
                if project.name == project_name:
                    task_name = input("Enter task name: ")
                    project.delete_task_by_name(task_name)
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_project_info_by_name(self):
        try:
            project_name = input("Enter name of the project: ")
            for project in self.projects:
                if project.name == project_name:
                    project.display_project_info()
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_team_member_from_project(self):
        try:
            project_name = input("Enter project name: ")
            for project in self.projects:
                if project.name == project_name:
                    project.delete_member_from_team()
        except Exception as e:
            print(f"An error occurred: {e}")

    def change_task_executor(self):
        try:
            project_name = input("Enter project name: ")
            for project in self.projects:
                if project.name == project_name:
                    task_name = input("Enter task name: ")
                    for task in project.tasks:
                        if task.name == task_name:
                            task.change_task_executor()
        except Exception as e:
            print(f"An error occurred: {e}")

class Info:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Task(Info):
    def __init__(self, task_name, task_description, task_due_date, task_executor):
        super().__init__(task_name, task_description)
        self.due_date = task_due_date
        self.task_executor = {"name": task_executor["name"], "role": task_executor["role"]}
        self.status = 'In progress'
    
    def change_task_executor(self):
        old_task_executor = input("Enter task executor who you want to replace: ")
        new_task_executor = input("Enter new task executor: ")
        self.task_executor[old_task_executor] = new_task_executor

class Project(Info):
    def __init__(self, name, description, team=None):
        super().__init__(name, description)
        self.team = team or []
        self.tasks = []
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def delete_task_by_name(self, name):
        self.tasks = delete_element_in_list(name, self.tasks)

    def display_project_info(self):
        print(f"Project name: {self.name}")
        print(f"Project description: {self.description}")
        for name, role in self.team:
            print(f"Name: {name}, role: {role}")

        for index, task in enumerate(self.tasks):
            print(f"Task number - {index + 1}")
            print(f"Task name - {task.name}")
            print(f"Task description - {task.description}")
            print(f"Task status - {task.status}")
            print(f"Task executor: {task.task_executor['name']}")
            print(f"Executor role: {task.task_executor['role']}")

    def add_new_member_of_team(self):
        member_name = input("Enter member name: ")
        member_role = input("Enter member role: ")
        self.team.append((member_name, member_role))

    def delete_member_from_team(self):
        member_name = input("Enter member name: ")
        self.team = [(name, role) for name, role in self.team if name != member_name]

# Example usage:
manager = ProjectManager()

while True:
    try:
        print("Choose one of the operations: ")
        print("1. Create project")
        print("2. Delete project")
        print("3. Add task to project")
        print("4. Delete task from project")
        print("5. Display project information")
        print("6. Delete team member from project")
        print("7. Change task executor")

        action = int(input())

        match action:
            case 1:
                manager.create_project()
            case 2:
                manager.delete_project()
            case 3:
                manager.add_task_to_project()
            case 4:
                manager.delete_task_from_project()
            case 5:
                manager.display_project_info_by_name()
            case 6:
                manager.delete_team_member_from_project()
            case 7:
                manager.change_task_executor()

    except ValueError:
        print("Incorrect value")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
