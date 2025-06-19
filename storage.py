def load_tasks(filename):
    tasks = []
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file]
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks, filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
