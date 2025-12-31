tasks = []
def add_task(task):
    if not task:
        print('Empty task not allowed')
        return
    tasks.append(task)
    print("task added:", task)