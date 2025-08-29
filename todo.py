# todo.py

# Step 1: Start with an empty list to hold tasks
tasks = []
compList = []

# Step 2: Add a task
def addTask(task):
    tasks.append(task)

# Step 3: View tasks
def viewTasks():
    print(f"Tasks: {tasks}")
# Step 4: Delete a task
def delTasks(task):
    tasks.pop(task)
    print(f"Task {task} deleted")
# Step 5: Mark task complete
def markComplete(task):
    complete = tasks.pop(task)
    compList.append(complete)
def viewComplete():
    print(f"Completed Tasks: {compList}")
# Step 6: Save/load tasks (extra stretch for today)
def saveTasks():
    with open("todo.txt", "w") as file:
        file.write(str(tasks))
        file.write("\n")
        file.write(str(compList))
    print("Tasks saved successfully")
def loadTasks():
    toggle = 0
    with open("todo.txt", "r") as file:
        for line in file:
            print(line)
            if toggle == 0:
                tasks = line
                print(f"Tasks={tasks}")
                toggle += 1
            else:
                compList = line
                print(f"compList={compList}")
    print("New tasks loaded successfully")
# Demo flow (you can run this file directly: python todo.py)
if __name__ == "__main__":
    addTask("Write code")
    addTask("Finish Cyber 201 assignment")
    addTask("Push code to GitHub")
    addTask("Buy Silksong")
    delTasks(1)
    markComplete(0)
    loadTasks()
    viewTasks()
    viewComplete()