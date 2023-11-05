"""CP1404 Practical - Project Management
Estimated: 60 minutes
Actual:  minutes
Current time: 1650
Finish time:
"""
from datetime import datetime
from project import Project

FILENAME = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Main function to run the project management program."""
    projects = load_projects(FILENAME)
    is_running = True
    while is_running:
        print(MENU)
        choice = input(">>> ").lower()
        if choice == 'l':
            projects = load_projects(FILENAME)
        elif choice == 's':
            save_projects(projects, FILENAME)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects(projects)
        elif choice == 'a':
            projects.append(add_new_project())
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            print("Thank you for using custom-built project management software.")
            is_running = False


def load_projects(filename):
    """Load the projects from a given filename and return them as a list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Skip header line
        for line in lines:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = datetime.strptime(parts[1], '%d/%m/%Y').date()  # Convert string to datetime.date object
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(filename, projects):
    """Saves projects to a given file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display the projects, separating incomplete and complete projects."""
    print("Incomplete projects: ")
    for project in projects:
        if project.completion_percentage < 100:
            print(f"  {project}")
    print("Completed projects: ")
    for project in projects:
        if project.completion_percentage == 100:
            print(f"  {project}")


def filter_projects(projects):
    """Filter and display projects that start after a given date."""
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    after_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    for project in projects:
        if project.start_date > after_date:
            print(f"  {project}")


def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = datetime.datetime.strptime(input("Start date (dd/mm/yy): "), "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """Update a project."""
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    project_choice = int(input("Project choice: "))
    chosen_project = projects[project_choice]
    print(chosen_project)
    new_percentage = input("New Percentage: ")
    if new_percentage:
        chosen_project.completion_percentage = int(new_percentage)
    new_priority = input("New Priority: ")
    if new_priority:
        chosen_project.priority = int(new_priority)


if __name__ == "__main__":
    main()

main()
