from datetime import datetime


def delete_element_in_list(name, list):
    for index, element in enumerate(list):
            if(element.name == name):
                new_list = list.pop(index)
                return new_list


class ProjectManager():
    def __init__(self):
        self.projects = []

    def delete_project(self, project_name):
        self.projects = delete_element_in_list(project_name, self.projects)

    def create_project(self):
        project_name = input("Enter name of the project")
        project_description = input("Describe project")
        project = Project(project_name, project_description)
        self.projects.append(project)
    
    def add_task_to_project(self):
        project_name = input("Enter project name")
        project_found = False
        for project in self.projects:
            if(project.name == project_name):
                task_name = input("Enter task name")
                task_description = input("Enter task description")
                task_deadline = input("Please enter a deadline in foramt (YYYY-MM-DD): ")
                date_object = datetime.strptime(task_deadline, "%Y-%m-%d")
                executor = input("Enter task executor name")
                role = input("Enter task executor role")
                new_task = Task(task_name, task_description, date_object, {"name": executor, "role": role})
                project.tasks.append(new_task)
                project_found = True
                break
        if( not project_found):
            print("There is no any project with such name")



    def delete_task_from_project(self):
        project_name = input("Enter project name")
        for project in self.projects:
            if(project.name == project_name):
                task_name = input("Enter task name")
                project.tasks = delete_element_in_list(task_name, project.tasks)
                print("Task was deleted succesfuly")
                



                

        



class Task():
    def __init__(self, task_name, task_description, task_due_date, task_executor):
        self.name = task_name
        self.task_description = task_description
        self.due_date = task_due_date
        self.task_executor = {"name": task_executor.name, "role": task_executor.role}
        self.status = 'In progress'



class Project():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.tasks = []
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")



