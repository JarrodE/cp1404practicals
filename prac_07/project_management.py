"""CP1404 Practical - Project Management
Estimated: 60 minutes
Actual:  minutes
Current time: 1650
Finish time:
"""

from project import Project

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """
    Main function to run the project management program.
    """
    projects = load_projects("projects.txt")
    is_running = True
    while is_running:
        print(MENU)
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yy): ")
            date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date_obj)
        elif choice == 'a':
            projects.append(add_new_project())
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            print("Thank you for using custom-built project management software.")
            is_running = False


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]
        for line in lines:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")


if __name__ == "__main__":
    main()

main()
