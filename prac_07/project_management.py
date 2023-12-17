import datetime
from project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    filename = "projects.txt"
    projects = []

    print(MENU)
    while True:
        choice = input(">>> ").strip().lower()

        if choice == "l":
            projects = load_projects(filename)
        elif choice == "s":
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            save_projects(filename, projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice.")


def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as in_file:
            in_file.readline()
            for line in in_file:
                parts = line.strip().split('\t')
                name, start_date, priority, cost_estimate, completion_percentage = parts
                project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
                projects.append(project)
    except FileNotFoundError:
        print("File not found. Creating an empty project list.")
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(
                f"{project.name}\t{project.start_date_str}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)

    print("Completed projects:")
    for project in completed_projects:
        print(project)


def filter_projects_by_date(projects):
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        start_after_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.compare_date_with_input_date(start_after_date)]
        for project in filtered_projects:
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_new_project():
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    return project


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project choice: "))

    if 0 <= project_choice < len(projects):
        chosen_project = projects[project_choice]
        new_percentage = input("New Percentage: ")
        if new_percentage != "":
            chosen_project.completion_percentage = int(new_percentage)
        new_priority = input("New Priority: ")
        if new_priority != "":
            chosen_project.priority = int(new_priority)
    else:
        print("Invalid project choice.")


if __name__ == "__main__":
    main()